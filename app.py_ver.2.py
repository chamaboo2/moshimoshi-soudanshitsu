from __future__ import annotations

import html

import streamlit as st

from db import is_configured, save_consultation, save_feedback
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


ROLE_LABELS = {
    "楠木正成": "難局・戦略・再挑戦",
    "小野篁": "自分の判断・異論・専門性",
    "平重盛": "板挟み・調整・関係性",
    "空海": "学び・成長・仕組み化",
}


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
          <h1 class="hero-title">もしもし相談室</h1>
          <div class="hero-subtitle">〜歴史の有名人に聞いてみた！〜</div>
          <div class="hero-copy">昔の決断から、いまの一手を。</div>
          <div class="hero-description">
            歴史上の人物が実際に行った決断や行動を手がかりに、いまの悩みを一緒に考えます。
            本人の名言を再現するのではなく、確認できる史実と、そこから整理した判断傾向を現代へ応用します。
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_compact_header() -> None:
    st.markdown('<div class="compact-brand">もしもし相談室 <span style="font-weight:500;">〜歴史の有名人に聞いてみた！〜</span></div>', unsafe_allow_html=True)


def render_figure_card(figure: dict, column) -> None:
    chips = "".join(
        f'<span class="chip">{html.escape(topic)}</span>'
        for topic in figure["consultation_topics"][:4]
    )
    role_label = ROLE_LABELS.get(figure["name"], "")
    card = f"""
    <div class="figure-card">
      <div class="figure-head">
        <div class="seal">{html.escape(figure['seal'])}</div>
        <div>
          <div class="figure-name">{html.escape(figure['name'])}</div>
          <div class="figure-meta">{html.escape(figure['reading'])} ｜ {html.escape(figure['era'])}</div>
        </div>
      </div>
      <div class="role-label">{html.escape(role_label)}</div>
      <div class="figure-desc">{html.escape(figure['short_description'])}</div>
      <div class="chips">{chips}</div>
    </div>
    """
    with column:
        st.markdown(card, unsafe_allow_html=True)
        if st.button(
            f"{figure['name']}に相談する",
            key=f"select_{figure['name']}",
            type="primary",
            use_container_width=True,
        ):
            select_figure(figure["name"])
            st.rerun()


def render_selection() -> None:
    st.markdown('<div class="section-label">誰に相談しますか？</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-note">4人とも、登録済みの史実をもとに人物ごとの判断傾向を現代の相談へ応用します。</div>', unsafe_allow_html=True)
    figures = all_figures()
    for i in range(0, len(figures), 2):
        cols = st.columns(2, gap="medium")
        render_figure_card(figures[i], cols[0])
        if i + 1 < len(figures):
            render_figure_card(figures[i + 1], cols[1])
        st.write("")


def render_selected_figure(figure: dict) -> None:
    st.markdown(
        f"""
        <div class="selected-figure">
          <div class="selected-label">相談相手</div>
          <div class="selected-name">{html.escape(figure['name'])}</div>
          <div class="selected-meta">{html.escape(figure['reading'])} ｜ {html.escape(figure['era'])} ｜ {html.escape(ROLE_LABELS.get(figure['name'], ''))}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


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
            for source_id in sorted(displayed_source_ids):
                source = get_source(figure, source_id)
                if not source:
                    continue
                st.markdown(
                    f"""**{source['organization']}**  \n[{source['title']}]({source['url']})  \n{source.get('note', '')}"""
                )


def render_answer(figure: dict, answer: dict) -> None:
    st.markdown(f"## {figure['name']}さんからの回答")
    st.caption("史実上の本人の発言ではなく、登録済み史実と人物の判断傾向をもとに現代向けに構成した助言です。")

    if answer.get("is_demo"):
        st.markdown('<div class="demo-badge">現在は画面確認用のデモ回答です</div>', unsafe_allow_html=True)

    st.markdown(
        f'<div class="answer-card"><h3>ひと言</h3><p>{html.escape(answer["one_liner"])}</p></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="answer-section-title">史実の手がかり</div>', unsafe_allow_html=True)
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
    if not is_configured():
        c1, c2 = st.columns(2)
        with c1:
            st.button("役に立った", use_container_width=True, disabled=True)
        with c2:
            st.button("いまひとつ", use_container_width=True, disabled=True)
        st.markdown('<div class="feedback-note">フィードバック機能は現在準備中です。</div>', unsafe_allow_html=True)
        return

    if st.session_state.feedback_sent:
        st.success("フィードバックを受け付けました。")
        return

    c1, c2 = st.columns(2)
    with c1:
        helpful_clicked = st.button("役に立った", use_container_width=True)
    with c2:
        not_helpful_clicked = st.button("いまひとつ", use_container_width=True)

    if helpful_clicked or not_helpful_clicked:
        try:
            save_feedback(
                helpful=helpful_clicked,
                consultation_id=st.session_state.consultation_id,
            )
            st.session_state.feedback_sent = True
            st.rerun()
        except Exception:
            st.error("フィードバックを保存できませんでした。時間をおいてもう一度お試しください。")


def render_consultation() -> None:
    figure = FIGURES[st.session_state.selected_figure]

    render_compact_header()
    render_selected_figure(figure)
    if st.button("← 相談相手を変える", use_container_width=False):
        back_to_figures()
        st.rerun()

    st.markdown("### もしもし。今日は、どんなご相談ですか？")
    st.markdown(
        '<div class="privacy-note">氏名・住所・勤務先・電話番号など、個人を特定できる情報は入力しないでください。</div>',
        unsafe_allow_html=True,
    )

    with st.form("consultation_form", clear_on_submit=False):
        concern = st.text_area(
            "相談内容",
            value=st.session_state.last_concern,
            height=160,
            max_chars=1200,
            placeholder="新しい仕事を任されました。挑戦したい気持ちはありますが、失敗して周囲に迷惑をかけるのが不安です。どう考えればよいでしょうか。",
            label_visibility="collapsed",
        )
        save_allowed = st.checkbox(
            "相談内容と回答を、サービス改善のために保存してもよい",
            value=False,
            help="初期値はOFFです。OFFの場合、相談内容と回答は保存しません。",
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
                with st.spinner(f"{figure['name']}の史実をたどりながら考えています……"):
                    answer = generate_advice(figure["name"], concern)
                st.session_state.answer = answer

                if save_allowed:
                    if not is_configured():
                        st.warning("現在、相談内容の保存機能は準備中です。今回の相談内容と回答は保存されていません。")
                    else:
                        try:
                            st.session_state.consultation_id = save_consultation(
                                figure_name=figure["name"],
                                concern=concern,
                                answer=answer,
                            )
                        except Exception:
                            st.warning("回答は生成できましたが、相談内容の保存には失敗しました。")
            except Exception:
                st.error("回答を生成できませんでした。設定を確認して、もう一度お試しください。")

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
          このサービスの回答は史実上の本人の発言ではありません。公開されている史実や人物の意思決定を参考に、AIが現代向けに構成した助言です。歴史上の人物については諸説存在する場合があります。<br>
          医療・法律・金融・自傷・他害・犯罪・緊急性の高い相談では、必要に応じて専門家や公的な相談先を利用してください。
        </div>
        """,
        unsafe_allow_html=True,
    )


if st.session_state.selected_figure is None:
    render_header()
    render_selection()
else:
    render_consultation()
render_footer()
