from __future__ import annotations

import html

import streamlit as st

from db import DatabaseUnavailable, is_configured, save_consultation, save_feedback
from figures import FIGURES, all_figures, get_fact, get_source
from llm import generate_advice
from styles import apply_styles


st.set_page_config(
    page_title="もしもし相談室 〜歴史の有名人に聞いてみた！〜",
    page_icon="☎️",
    layout="centered",
    initial_sidebar_state="collapsed",
)
apply_styles()


for key, default in {
    "selected_figure": None,
    "answer": None,
    "consultation_id": None,
    "feedback_sent": False,
    "last_concern": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = default


def reset_answer() -> None:
    st.session_state.answer = None
    st.session_state.consultation_id = None
    st.session_state.feedback_sent = False
    st.session_state.last_concern = ""


def select_figure(name: str) -> None:
    st.session_state.selected_figure = name
    reset_answer()


def back_to_figures() -> None:
    st.session_state.selected_figure = None
    reset_answer()


def render_header() -> None:
    st.markdown(
        """
        <div class="hero-wrap">
          <div class="kicker">HISTORICAL DECISIONS × MODERN ADVICE</div>
          <h1 class="hero-title">もしもし相談室</h1>
          <div class="hero-subtitle">〜歴史の有名人に聞いてみた！〜</div>
          <div class="hero-copy">昔の決断から、いまの一手を。</div>
          <div class="hero-description">
            歴史上の人物が実際に行った決断や行動を手がかりに、いまの悩みを一緒に考えます。<br>
            本人の名言を再現するのではなく、確認できる史実と、そこから整理した判断傾向を現代へ応用します。
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_figure_card(figure: dict, column) -> None:
    chips = "".join(
        f'<span class="chip">{html.escape(topic)}</span>'
        for topic in figure["consultation_topics"][:4]
    )
    card = f"""
    <div class="figure-card">
      <div class="figure-head">
        <div class="seal">{html.escape(figure['seal'])}</div>
        <div>
          <div class="figure-name">{html.escape(figure['name'])}</div>
          <div class="figure-meta">{html.escape(figure['reading'])} ｜ {html.escape(figure['era'])}</div>
        </div>
      </div>
      <div class="figure-desc">{html.escape(figure['short_description'])}</div>
      <div class="chips">{chips}</div>
      <div class="fact-badge">史実をもとに回答</div>
    </div>
    """
    with column:
        st.markdown(card, unsafe_allow_html=True)
        if st.button(
            f"{figure['name']}に相談する",
            key=f"select_{figure['name']}",
            use_container_width=True,
        ):
            select_figure(figure["name"])
            st.rerun()


def render_selection() -> None:
    st.markdown('<div class="section-label">誰に相談しますか？</div>', unsafe_allow_html=True)
    figures = all_figures()
    for i in range(0, len(figures), 2):
        cols = st.columns(2, gap="medium")
        render_figure_card(figures[i], cols[0])
        if i + 1 < len(figures):
            render_figure_card(figures[i + 1], cols[1])
        st.write("")


def render_selected_figure(figure: dict) -> None:
    col1, col2 = st.columns([1, 5], vertical_alignment="center")
    with col1:
        st.markdown(f'<div class="seal">{html.escape(figure["seal"])}</div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f"### {figure['name']}に相談")
        st.caption(f"{figure['reading']} ｜ {figure['era']} ｜ 史実をもとに回答")
        st.write(figure["short_description"])


def render_fact_sources(figure: dict, fact_ids: list[str]) -> None:
    displayed_source_ids: set[str] = set()
    for fact_id in fact_ids:
        fact = get_fact(figure, fact_id)
        if not fact:
            continue
        confidence_label = "" if fact["confidence"] == "high" else "（確定度に注意）"
        st.markdown(
            f"""
            <div class="source-box">
              <strong>{html.escape(fact['title'])}{confidence_label}</strong><br>
              {html.escape(fact['statement'])}
            </div>
            """,
            unsafe_allow_html=True,
        )
        displayed_source_ids.update(fact.get("source_ids", []))

    if displayed_source_ids:
        with st.expander("出典を確認"):
            for source_id in displayed_source_ids:
                source = get_source(figure, source_id)
                if not source:
                    continue
                st.markdown(
                    f"""**{source['organization']}**  \n[{source['title']}]({source['url']})  \n{source.get('note', '')}"""
                )


def render_answer(figure: dict, answer: dict) -> None:
    st.markdown(f"## {figure['name']}さんからの回答")
    st.caption("以下は史実上の本人の発言ではなく、登録済み史実をもとにAIが現代向けに構成した助言です。")

    st.markdown(
        f'<div class="answer-card"><h3>ひと言</h3><p>{html.escape(answer["one_liner"])}</p></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="answer-card"><h3>史実の手がかり</h3></div>', unsafe_allow_html=True)
    render_fact_sources(figure, answer.get("fact_ids", []))

    st.markdown(
        f'<div class="answer-card"><h3>この人物の史実から考えると</h3><p>{html.escape(answer["analysis"])}</p></div>',
        unsafe_allow_html=True,
    )

    steps_html = "".join(f"<li>{html.escape(step)}</li>" for step in answer.get("next_steps", []))
    st.markdown(
        f'<div class="answer-card"><h3>次の一手</h3><ol>{steps_html}</ol></div>',
        unsafe_allow_html=True,
    )

    if answer.get("safety_note"):
        st.warning(answer["safety_note"])

    st.markdown("### この回答は役に立ちましたか？")
    if st.session_state.feedback_sent:
        st.success("フィードバックを受け付けました。")
    else:
        c1, c2 = st.columns(2)
        with c1:
            helpful_clicked = st.button("役に立った", use_container_width=True)
        with c2:
            not_helpful_clicked = st.button("いまひとつ", use_container_width=True)

        if helpful_clicked or not_helpful_clicked:
            if not is_configured():
                st.info("Supabase未設定のため、フィードバックは保存されません。READMEの手順で設定すると保存できます。")
            else:
                try:
                    save_feedback(
                        helpful=helpful_clicked,
                        consultation_id=st.session_state.consultation_id,
                    )
                    st.session_state.feedback_sent = True
                    st.rerun()
                except Exception as exc:
                    st.error(f"フィードバックを保存できませんでした: {exc}")


def render_consultation() -> None:
    figure = FIGURES[st.session_state.selected_figure]

    if st.button("← 相談相手を選び直す"):
        back_to_figures()
        st.rerun()

    render_selected_figure(figure)
    st.divider()
    st.markdown("### もしもし。今日は、どんなご相談ですか？")
    st.caption("氏名・住所・勤務先・電話番号など、個人を特定できる情報は入力しないでください。")

    with st.form("consultation_form", clear_on_submit=False):
        concern = st.text_area(
            "相談内容",
            value=st.session_state.last_concern,
            height=180,
            max_chars=1200,
            placeholder="新しい仕事を任されました。挑戦したい気持ちはありますが、失敗して周囲に迷惑をかけるのが不安です。どう考えればよいでしょうか。",
            label_visibility="collapsed",
        )
        save_allowed = st.checkbox(
            "相談内容と回答を、サービス改善のため保存してよい",
            value=False,
            help="初期値はOFFです。OFFの場合、相談内容と回答はSupabaseへ保存しません。",
        )
        submitted = st.form_submit_button(
            "この人に聞いてみる",
            type="primary",
            use_container_width=True,
        )

    if submitted:
        if not concern.strip():
            st.error("相談内容を入力してください。")
        else:
            reset_answer()
            st.session_state.last_concern = concern
            try:
                with st.spinner(f"{figure['name']}が史実をたどりながら考えています……"):
                    answer = generate_advice(figure["name"], concern)
                st.session_state.answer = answer

                if save_allowed:
                    if not is_configured():
                        st.warning("回答は生成できましたが、Supabase未設定のため相談内容と回答は保存されていません。")
                    else:
                        try:
                            st.session_state.consultation_id = save_consultation(
                                figure_name=figure["name"],
                                concern=concern,
                                answer=answer,
                            )
                        except DatabaseUnavailable:
                            st.warning("回答は生成できましたが、Supabase設定がないため保存されていません。")
                        except Exception as exc:
                            st.warning(f"回答は生成できましたが、保存に失敗しました: {exc}")
            except Exception as exc:
                st.error(f"回答を生成できませんでした。{exc}")

    if st.session_state.answer:
        st.divider()
        render_answer(figure, st.session_state.answer)
        if st.button("同じ人物に別の相談をする", use_container_width=True):
            reset_answer()
            st.rerun()


def render_footer() -> None:
    st.markdown(
        """
        <div class="disclaimer">
          このサービスの回答は、史実上の本人の発言ではありません。公開されている史実や人物の意思決定を参考に、AIが現代向けに構成した助言です。<br>
          歴史上の人物については諸説存在する場合があります。医療・法律・金融・自傷・他害・犯罪・緊急性の高い相談では、必要に応じて専門家や公的な相談先を利用してください。
        </div>
        """,
        unsafe_allow_html=True,
    )


render_header()
if st.session_state.selected_figure is None:
    render_selection()
else:
    render_consultation()
render_footer()
