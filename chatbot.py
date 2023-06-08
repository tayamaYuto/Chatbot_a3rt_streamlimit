import streamlit as st
import requests

apikey = "DZZLGgsZbWHeXS39vl8VRFQ7FpbP9oyr"

chat_logs = []

st.title("Chatbot with streamlit")
st.subheader("メッセージを入力してから送信ボタンを押してくだい")

message = st.text_input("メッセージ")


def send_pya3rt(endpoint, apikey, text, callback):
    params = {'apikey' : apikey,
              'query' : text
             }
    if callback is not None:
        params['callbacl'] = callback
    
    response = requests.post(endpoint, params)

    return response.json()

def generate_response():
    ans_json = send_pya3rt('https://api.a3rt.recruit.co.jp/talk/v1/smalltalk',
                       apikey, message, None)
    ans = ans_json['results'][0]['reply']
    chat_logs.append('you: ' + message)
    chat_logs.append('AI: ' + ans)
    for chat_log in chat_logs:
        st.write(chat_log)

if st.button("送信"):
    generate_response()
