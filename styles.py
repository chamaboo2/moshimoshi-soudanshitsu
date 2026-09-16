import streamlit as st


CSS = r"""
<style>
:root {
  --paper: #f6f0e4;
  --paper-2: #fbf8f1;
  --navy: #18324a;
  --navy-2: #24465f;
  --vermillion: #a54835;
  --ink: #2f3439;
  --muted: #6f7275;
  --line: #ddd2bf;
}

.stApp {
  background:
    radial-gradient(circle at 10% 0%, rgba(165,72,53,.05), transparent 30%),
    linear-gradient(180deg, var(--paper-2), var(--paper));
  color: var(--ink);
}

.block-container {
  max-width: 900px;
  padding-top: 1rem;
  padding-bottom: 2.5rem;
}

h1, h2, h3, h4, p, div, span, label, button, textarea {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans JP", "Hiragino Sans", "Yu Gothic", sans-serif;
}

.hero-wrap {
  padding: .7rem 0 .35rem 0;
}

.hero-title {
  color: var(--navy);
  font-size: clamp(2rem, 7vw, 3.15rem);
  line-height: 1.08;
  font-weight: 800;
  letter-spacing: .02em;
  margin: 0;
}

.hero-subtitle {
  color: var(--navy-2);
  font-size: clamp(1rem, 4vw, 1.3rem);
  margin-top: .4rem;
  font-weight: 700;
}

.hero-copy {
  color: var(--vermillion);
  font-size: 1.04rem;
  font-weight: 700;
  margin-top: .95rem;
}

.hero-description {
  color: var(--ink);
  line-height: 1.7;
  max-width: 760px;
  margin-top: .35rem;
}

.compact-brand {
  color: var(--navy);
  font-weight: 800;
  font-size: 1.05rem;
  margin: 0 0 .4rem 0;
}

.section-label {
  color: var(--navy);
  font-size: 1.35rem;
  font-weight: 800;
  margin-top: .7rem;
  margin-bottom: .15rem;
}

.section-note {
  color: var(--muted);
  font-size: .88rem;
  margin-bottom: .8rem;
}

.figure-card {
  border: 1px solid var(--line);
  background: rgba(255,255,255,.72);
  border-radius: 18px;
  padding: .95rem 1rem .8rem 1rem;
  min-height: 245px;
  box-shadow: 0 5px 18px rgba(48,45,39,.035);
}

.figure-head {
  display: flex;
  align-items: center;
  gap: .75rem;
  margin-bottom: .55rem;
}

.seal {
  width: 50px;
  height: 50px;
  min-width: 50px;
  border: 2px solid var(--vermillion);
  color: var(--vermillion);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.18rem;
  font-weight: 800;
  background: #fffaf2;
}

.figure-name {
  color: var(--navy);
  font-size: 1.2rem;
  font-weight: 800;
  margin: 0;
}

.figure-meta {
  color: var(--muted);
  font-size: .82rem;
  margin-top: .05rem;
}

.figure-desc {
  color: var(--ink);
  line-height: 1.58;
  margin: .35rem 0 .55rem 0;
}

.role-label {
  display: inline-block;
  color: var(--vermillion);
  font-size: .78rem;
  font-weight: 800;
  margin-bottom: .4rem;
}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: .32rem;
  margin: .3rem 0 .35rem 0;
}

.chip {
  font-size: .74rem;
  color: var(--navy);
  border: 1px solid #c9d3da;
  background: #f5f8fa;
  padding: .22rem .48rem;
  border-radius: 999px;
}

.selected-figure {
  border: 1px solid var(--line);
  background: rgba(255,255,255,.72);
  border-radius: 16px;
  padding: .8rem .95rem;
  margin: .25rem 0 .55rem 0;
}

.selected-label {
  color: var(--muted);
  font-size: .78rem;
  font-weight: 700;
  margin-bottom: .1rem;
}

.selected-name {
  color: var(--navy);
  font-size: 1.25rem;
  font-weight: 800;
}

.selected-meta {
  color: var(--muted);
  font-size: .82rem;
  margin-top: .05rem;
}

.privacy-note {
  color: #565c61;
  background: rgba(255,255,255,.5);
  border-left: 3px solid #b4a68e;
  border-radius: 0 8px 8px 0;
  padding: .52rem .7rem;
  margin: .2rem 0 .55rem 0;
  font-size: .84rem;
  line-height: 1.55;
}

.demo-badge {
  display: inline-block;
  color: #705b00;
  background: #fff7cf;
  border: 1px solid #eadc91;
  border-radius: 999px;
  padding: .28rem .6rem;
  font-size: .78rem;
  font-weight: 700;
  margin: .1rem 0 .55rem 0;
}

.answer-card {
  border: 1px solid var(--line);
  background: rgba(255,255,255,.8);
  border-radius: 16px;
  padding: .82rem .95rem;
  margin: .48rem 0;
}

.answer-card h3 {
  color: var(--navy);
  font-size: 1rem;
  margin: 0 0 .45rem 0;
}

.answer-card p, .answer-card li {
  line-height: 1.68;
}

.answer-section-title {
  color: var(--navy);
  font-size: 1rem;
  font-weight: 800;
  margin: .72rem 0 .25rem 0;
}

.source-box {
  border-left: 3px solid var(--vermillion);
  background: rgba(255,250,242,.95);
  padding: .7rem .82rem;
  margin: .4rem 0;
  border-radius: 0 10px 10px 0;
  line-height: 1.58;
}

.feedback-note {
  color: var(--muted);
  font-size: .82rem;
  margin-top: .2rem;
}

.disclaimer {
  margin-top: 1.25rem;
  padding: .8rem .9rem;
  border: 1px solid var(--line);
  border-radius: 12px;
  background: rgba(255,255,255,.46);
  color: var(--muted);
  font-size: .78rem;
  line-height: 1.6;
}

div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
  border-radius: 12px;
  min-height: 44px;
  font-weight: 700;
}

div.stButton > button[kind="primary"],
div[data-testid="stFormSubmitButton"] > button[kind="primary"],
button[data-testid="stBaseButton-primary"] {
  background: var(--navy) !important;
  border-color: var(--navy) !important;
  color: white !important;
}

div.stButton > button[kind="primary"]:hover,
div[data-testid="stFormSubmitButton"] > button[kind="primary"]:hover,
button[data-testid="stBaseButton-primary"]:hover {
  background: var(--navy-2) !important;
  border-color: var(--navy-2) !important;
}

textarea {
  line-height: 1.6 !important;
}

[data-testid="stAlert"] {
  border-radius: 12px;
}

[data-testid="stVerticalBlock"] > [style*="flex-direction: column"] {
  gap: .65rem;
}

@media (max-width: 640px) {
  .block-container {
    padding: .75rem .8rem 2.2rem .8rem;
  }
  .figure-card {
    min-height: auto;
  }
  .hero-wrap {
    padding-top: .35rem;
  }
  .hero-description {
    line-height: 1.62;
  }
  .answer-card {
    padding: .75rem .82rem;
  }
  [data-testid="stHorizontalBlock"] {
    flex-direction: column !important;
    gap: .7rem !important;
  }
  [data-testid="column"] {
    width: 100% !important;
    flex: 1 1 100% !important;
  }
}
</style>
"""


def apply_styles() -> None:
    st.markdown(CSS, unsafe_allow_html=True)
