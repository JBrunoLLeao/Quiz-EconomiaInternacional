import streamlit as st
from questions import QUESTIONS

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Quiz · Economia Internacional (Krugman)",
    layout="centered",
)

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background: #0d0f14;
    color: #e2e8f0;
}

/* hide streamlit default decorations */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 2rem; max-width: 760px; }

/* ── Hero ── */
.hero {
    background: linear-gradient(135deg, #1a1f2e 0%, #0d1321 100%);
    border: 1px solid #2a3550;
    border-radius: 16px;
    padding: 2.4rem 2.8rem;
    margin-bottom: 2rem;
}
.hero h1 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.75rem;
    font-weight: 700;
    color: #7dd3fc;
    margin: 0 0 .4rem 0;
    letter-spacing: -0.5px;
}
.hero p { margin: 0; color: #94a3b8; font-size: .95rem; }

/* ── Progress bar ── */
.progress-wrap {
    background: #1e2533;
    border-radius: 99px;
    height: 6px;
    margin-bottom: 1.6rem;
    overflow: hidden;
}
.progress-fill {
    height: 100%;
    border-radius: 99px;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    transition: width .4s ease;
}

/* ── Question card ── */
.q-card {
    background: #141824;
    border: 1px solid #252d3d;
    border-radius: 14px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.4rem;
}
.q-meta {
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    color: #475569;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: .8rem;
}
.q-tag {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: .68rem;
    font-weight: 600;
    margin-left: 8px;
}
.tag-mp   { background: #1e3a5f; color: #7dd3fc; }
.tag-esc  { background: #2d1f5e; color: #c4b5fd; }
.tag-pol  { background: #1a3d2e; color: #6ee7b7; }
.tag-eco  { background: #4a2e12; color: #fdba74; }
.tag-omc  { background: #4a1942; color: #f9a8d4; }
.q-text {
    font-size: 1.05rem;
    font-weight: 500;
    line-height: 1.65;
    color: #e2e8f0;
}

/* ── Answer feedback ── */
.feedback-correct {
    background: #0f2d1e;
    border: 1px solid #166534;
    border-left: 4px solid #22c55e;
    border-radius: 10px;
    padding: 1.1rem 1.4rem;
    margin-top: .8rem;
}
.feedback-wrong {
    background: #2d1012;
    border: 1px solid #7f1d1d;
    border-left: 4px solid #ef4444;
    border-radius: 10px;
    padding: 1.1rem 1.4rem;
    margin-top: .8rem;
}
.feedback-correct .fb-header { color: #22c55e; font-weight: 700; margin-bottom: .4rem; font-size: .9rem; }
.feedback-wrong  .fb-header { color: #ef4444; font-weight: 700; margin-bottom: .4rem; font-size: .9rem; }
.fb-correct-answer { color: #86efac; font-weight: 600; margin-bottom: .5rem; font-size: .88rem; }
.fb-explanation { color: #cbd5e1; font-size: .9rem; line-height: 1.6; }

/* ── Scoreboard ── */
.score-card {
    background: linear-gradient(135deg, #141e30, #1a1f2e);
    border: 1px solid #2a3550;
    border-radius: 16px;
    padding: 2.8rem;
    text-align: center;
}
.score-card h2 {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.5rem;
    color: #7dd3fc;
    margin-bottom: .3rem;
}
.score-big {
    font-family: 'JetBrains Mono', monospace;
    font-size: 4.5rem;
    font-weight: 700;
    background: linear-gradient(90deg, #38bdf8, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    line-height: 1;
    margin: .8rem 0;
}
.score-label { color: #64748b; font-size: .9rem; margin-bottom: 1.4rem; }
.breakdown {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-top: 1.2rem;
}
.breakdown-item { text-align: center; }
.breakdown-item .val { font-size: 1.5rem; font-weight: 700; font-family: 'JetBrains Mono', monospace; }
.breakdown-item .lbl { font-size: .75rem; color: #64748b; }
.val-correct { color: #22c55e; }
.val-wrong   { color: #ef4444; }

/* ── Buttons ── */
div.stButton > button {
    background: #1e2d45;
    color: #7dd3fc;
    border: 1px solid #2a4a6b;
    border-radius: 8px;
    font-family: 'Inter', sans-serif;
    font-weight: 600;
    font-size: .92rem;
    padding: .55rem 1.4rem;
    transition: all .2s;
}
div.stButton > button:hover {
    background: #253550;
    border-color: #38bdf8;
    color: #bae6fd;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #1d4ed8, #4f46e5);
    border-color: transparent;
    color: #fff;
}
div.stButton > button[kind="primary"]:hover {
    background: linear-gradient(135deg, #2563eb, #6366f1);
}

/* radio overrides */
div[data-testid="stRadio"] label {
    background: #1a2030;
    border: 1px solid #252d3d;
    border-radius: 8px;
    padding: .6rem 1rem;
    margin: .25rem 0;
    display: block;
    cursor: pointer;
    transition: border-color .2s;
    color: #cbd5e1;
    font-size: .95rem;
}
div[data-testid="stRadio"] label:hover { border-color: #38bdf8; }
</style>
""", unsafe_allow_html=True)

# ── Session state init ────────────────────────────────────────────────────────
def init_state():
    if "q_idx" not in st.session_state:
        st.session_state.q_idx = 0
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "answered" not in st.session_state:
        st.session_state.answered = False
    if "selected" not in st.session_state:
        st.session_state.selected = None
    if "finished" not in st.session_state:
        st.session_state.finished = False
    if "wrong_qs" not in st.session_state:
        st.session_state.wrong_qs = []

init_state()

TOTAL = len(QUESTIONS)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>Quiz · Economia Internacional</h1>
  <p>50 perguntas baseadas em Krugman — <strong>Modelo Padrão</strong>, <strong>Economias de Escala</strong>, <strong>Política Comercial</strong>, <strong>Economia Política</strong> e <strong>OMC/Desenvolvimento</strong> — leia com atenção!</p>
</div>
""", unsafe_allow_html=True)

# ── Finished screen ───────────────────────────────────────────────────────────
if st.session_state.finished:
    pct = int(st.session_state.score / TOTAL * 100)
    wrong = TOTAL - st.session_state.score
    emoji = "🏆" if pct >= 80 else ("💪" if pct >= 50 else "📚")
    msg   = "Excelente domínio!" if pct >= 80 else ("Bom progresso — revise os erros." if pct >= 50 else "Continue estudando — não desista!")

    st.markdown(f"""
    <div class="score-card">
      <h2>{emoji} Resultado Final</h2>
      <div class="score-big">{pct}%</div>
      <div class="score-label">{msg}</div>
      <div class="breakdown">
        <div class="breakdown-item">
          <div class="val val-correct">{st.session_state.score}</div>
          <div class="lbl">Certas</div>
        </div>
        <div class="breakdown-item">
          <div class="val val-wrong">{wrong}</div>
          <div class="lbl">Erradas</div>
        </div>
        <div class="breakdown-item">
          <div class="val" style="color:#7dd3fc">{TOTAL}</div>
          <div class="lbl">Total</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.wrong_qs:
        st.markdown("### 📋 Questões que você errou")
        for wq in st.session_state.wrong_qs:
            with st.expander(f"Q{wq['num']} — {wq['topic']}"):
                st.markdown(f"**Pergunta:** {wq['question']}")
                st.markdown(f"**Sua resposta:** {wq['selected']}")
                st.markdown(f"**Resposta correta:** {wq['correct']}")
                st.markdown(f"**Explicação:** {wq['explanation']}")

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Reiniciar Quiz", type="primary"):
        for k in ["q_idx","score","answered","selected","finished","wrong_qs"]:
            del st.session_state[k]
        st.rerun()
    st.stop()

# ── Progress ──────────────────────────────────────────────────────────────────
idx = st.session_state.q_idx
pct_done = idx / TOTAL * 100
st.markdown(f"""
<div style="display:flex;justify-content:space-between;font-size:.8rem;color:#475569;margin-bottom:.4rem;">
  <span>Pergunta {idx+1} de {TOTAL}</span>
  <span>Pontuação: {st.session_state.score}</span>
</div>
<div class="progress-wrap">
  <div class="progress-fill" style="width:{pct_done}%"></div>
</div>
""", unsafe_allow_html=True)

# ── Current question ──────────────────────────────────────────────────────────
q = QUESTIONS[idx]
tag_class = {
    "Modelo Padrão": "tag-mp",
    "Escala e Concorrência": "tag-esc",
    "Política Comercial": "tag-pol",
    "Economia Política": "tag-eco",
    "OMC e Desenvolvimento": "tag-omc",
}.get(q["topic"], "tag-mp")

st.markdown(f"""
<div class="q-card">
  <div class="q-meta">
    Questão {idx+1}
    <span class="q-tag {tag_class}">{q['topic']}</span>
  </div>
  <div class="q-text">{q['question']}</div>
</div>
""", unsafe_allow_html=True)

# ── Radio options (disabled after answer) ────────────────────────────────────
options = q["options"]

if not st.session_state.answered:
    chosen = st.radio("Escolha uma alternativa:", options, key=f"radio_{idx}", index=None)

    if chosen is not None:
        st.session_state.selected = chosen
        st.session_state.answered = True
        correct = q["answer"]
        if chosen == correct:
            st.session_state.score += 1
        else:
            st.session_state.wrong_qs.append({
                "num": idx + 1,
                "topic": q["topic"],
                "question": q["question"],
                "selected": chosen,
                "correct": correct,
                "explanation": q["explanation"],
            })
        st.rerun()
else:
    # show disabled-looking options
    st.radio("Escolha uma alternativa:", options, key=f"radio_{idx}_done",
             index=options.index(st.session_state.selected), disabled=True)

    correct = q["answer"]
    is_right = st.session_state.selected == correct

    if is_right:
        st.markdown(f"""
        <div class="feedback-correct">
          <div class="fb-header">✅ Correto!</div>
          <div class="fb-explanation">{q['explanation']}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="feedback-wrong">
          <div class="fb-header">❌ Incorreto</div>
          <div class="fb-correct-answer">Resposta correta: {correct}</div>
          <div class="fb-explanation">{q['explanation']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    label = "Próxima →" if idx < TOTAL - 1 else "Ver Resultado 🏁"
    if st.button(label, type="primary"):
        if idx < TOTAL - 1:
            st.session_state.q_idx += 1
            st.session_state.answered = False
            st.session_state.selected = None
        else:
            st.session_state.finished = True
        st.rerun()
