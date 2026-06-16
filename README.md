# 🧠 Quiz Deep Learning — CNN / RNN / Regularização

50 perguntas difíceis sobre CNN, RNN e Regularização com explicações detalhadas.

## Como rodar

```bash
# 1. Instale as dependências
pip install -r requirements.txt

# 2. Execute o app
streamlit run app.py
```

O quiz abrirá automaticamente em `http://localhost:8501`.

## Estrutura dos arquivos

```
quiz_dl/
├── app.py           # App Streamlit principal (UI, lógica do quiz)
├── questions.py     # Banco de 50 perguntas com opções, respostas e explicações
├── requirements.txt # Dependências
└── README.md        # Este arquivo
```

## Funcionalidades

- ✅ 50 perguntas difíceis organizadas por tema (CNN / RNN / Regularização)
- ✅ Feedback imediato após cada resposta (certo/errado + explicação técnica)
- ✅ Barra de progresso visual
- ✅ Revisão de erros ao final com explicações
- ✅ Placar final com percentual de acerto
- ✅ Botão para reiniciar o quiz
