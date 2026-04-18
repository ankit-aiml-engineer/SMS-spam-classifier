import streamlit as st
import pickle

model = pickle.load(open("models/spam_pipeline.pkl", "rb"))

def predict_sms(text):
    result = model.predict([text])[0]
    return "Spam" if result == 1 else "Ham"

st.title("SMS Spam Classifier")

msg = st.text_area("Enter message")

if st.button("Check"):
    if msg.strip() == "":
        st.warning("Enter message")
    else:
        result = predict_sms(msg)
        if result == "Spam":
            st.error("Spam Message")
        else:
            st.success("Normal Message")