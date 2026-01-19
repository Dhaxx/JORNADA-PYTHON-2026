# Titulo
# input do chat (campo de mensagem)
# a cada mensagem que o usuário enviar:
    # mostrar a mensagem na tela
    # enviar a pergunta para a IA
    # mostrar resposta da IA na tela

# Streamlit -> Apenas com python criar frontend e backend
# IA utilizada: OpenAI

import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyAaMoYE6KBna9imXnO1D3ETmVw5pYBqTGs")
modelo_ia = genai.GenerativeModel("gemini-2.5-flash")

st.title("Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state['lista_mensagens'] = []

input_usuario = st.chat_input("Digite sua mensagem:")

def formata_para_gemini(chat_history):
    mensagens_gemini = []
    for mensagem in chat_history:
        role = mensagem["role"]
        # Gemini API uses 'model' for its responses, not 'assistant'
        if role == "assistant":
            role = "model"
        mensagens_gemini.append({
            "role": role,
            "parts": [{"text": mensagem["content"]}]
        })
    return mensagens_gemini

chat_iniciado = False
if not chat_iniciado:
    chat = modelo_ia.start_chat(history=formata_para_gemini(st.session_state['lista_mensagens']))
    chat_iniciado = True

if input_usuario:
    mensagem_usuario = {
        "role": "user",
        "content": input_usuario
    }
    st.session_state['lista_mensagens'].append(mensagem_usuario)

    # Resposta da IA
    resposta_ia = chat.send_message(input_usuario)
    print(resposta_ia.text)

    output_ia = {
        "role": "assistant",
        "content": resposta_ia.text
    }
    st.session_state['lista_mensagens'].append(output_ia)

for mensagem in st.session_state['lista_mensagens']:
    st.chat_message(mensagem['role']).write(mensagem['content'])