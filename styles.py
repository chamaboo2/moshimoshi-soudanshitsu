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
  padding-top: 1.5rem;
  padding-bottom: 4rem;
}

h1, h2, h3, h4, p, div, span, label, button, textarea {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Noto Sans JP", "Hiragino Sans", "Yu Gothic", sans-serif;
}

.hero-wrap {
  padding: 1.2rem 0 .6rem 0;
}

.kicker {
  color: var(--vermillion);
  font-size: .86rem;
  font-weight: 700;
  letter-spacing: .1em;
  margin-bottom: .35rem;
}

.hero-title {
  color: var(--navy);
  font-size: clamp(2rem, 7vw, 3.25rem);
  line-height: 1.05;
  font-weight: 800;
  letter-spacing: .02em;
  margin: 0;
}

.hero-subtitle {
  color: var(--navy-2);
  font-size: clamp(1rem, 4vw, 1.35rem);
  margin-top: .45rem;
  font-weight: 700;
}

.hero-copy {
  color: var(--vermillion);
  font-size: 1.05rem;
  font-weight: 700;
  margin-top: 1.2rem;
}

.hero-description {
  color: var(--ink);
  line-height: 1.8;
  max-width: 720px;
  margin-top: .4rem;
}

.section-label {
  color: var(--navy);
  font-size: 1.35rem;
  font-weight: 800;
  margin-top: .4rem;
  margin-bottom: .8rem;
}

.figure-card {
  border: 1px solid var(--line);
  background: rgba(255,255,255,.66);
  border-radius: 18px;
  padding: 1rem 1rem .55rem 1rem;
  min-height: 265px;
  box-shadow: 0 5px 18px rgba(48,45,39,.035);
}

.figure-head {
  display: flex;
  align-items: center;
  gap: .8rem;
  margin-bottom: .7rem;
}

.seal {
  width: 52px;
  height: 52px;
  min-width: 52px;
  border: 2px solid var(--vermillion);
  color: var(--vermillion);
  border-radius: 50%;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  font-weight: 800;
  background: #fffaf2;
}

.figure-name {
  color: var(--navy);
  font-size: 1.22rem;
  font-weight: 800;
  margin: 0;
}

.figure-meta {
  color: var(--muted);
  font-size: .83rem;
  margin-top: .05rem;
}

.figure-desc {
  color: var(--ink);
  line-height: 1.65;
  margin: .4rem 0 .65rem 0;
}

.chips {
  display: flex;
  flex-wrap: wrap;
  gap: .35rem;
  margin: .4rem 0 .6rem 0;
}

.chip {
  font-size: .76rem;
  color: var(--navy);
  border: 1px solid #c9d3da;
  background: #f5f8fa;
  padding: .24rem .5rem;
  border-radius: 999px;
}

.fact-badge {
  color: var(--vermillion);
  font-size: .8rem;
  font-weight: 700;
}

.answer-card {
  border: 1px solid var(--line);
  background: rgba(255,255,255,.78);
  border-radius: 18px;
  padding: 1rem 1.05rem;
  margin: .65rem 0;
}

.answer-card h3 {
  color: var(--navy);
  font-size: 1rem;
  margin: 0 0 .55rem 0;
}

.answer-card p, .answer-card li {
  line-height: 1.8;
}

.source-box {
  border-left: 3px solid var(--vermillion);
  background: rgba(255,250,242,.95);
  padding: .75rem .85rem;
  margin: .65rem 0;
  border-radius: 0 10px 10px 0;
}

.disclaimer {
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid var(--line);
  color: var(--muted);
  font-size: .82rem;
  line-height: 1.7;
}

div.stButton > button {
  border-radius: 12px;
  min-height: 45px;
  font-weight: 700;
}

div.stButton > button[kind="primary"] {
  background: var(--navy);
  border-color: var(--navy);
}

div.stButton > button[kind="primary"]:hover {
  background: var(--navy-2);
  border-color: var(--navy-2);
}

textarea {
  line-height: 1.65 !important;
}

[data-testid="stAlert"] {
  border-radius: 14px;
}

@media (max-width: 640px) {
  .block-container {
    padding: 1rem .85rem 3rem .85rem;
  }
  .figure-card {
    min-height: auto;
  }
  .hero-wrap {
    padding-top: .55rem;
  }
}
</style>
"""


def apply_styles() -> None:
    st.markdown(CSS, unsafe_allow_html=True)
