import streamlit as st
import pickle

# Load the saved model
with open('models/fake_news_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit UI
st.set_page_config(page_title="Fake News Detection", layout="centered")
st.title("📰 Fake News Detection App")

st.markdown("""
Enter a news article below, and the model will predict whether it's **Real** or **Fake**.
""")

# Text input
input_text = st.text_area("📝 Enter News Article", height=250)

# Predict button
if st.button("🔍 Predict"):
    if input_text.strip() == "":
        st.warning("Please enter some text to classify.")
    else:
        prediction = model.predict([input_text])[0]
        if prediction == 'FAKE':
            st.error("🛑 This news article is **FAKE**.")
        else:
            st.success("✅ This news article is **REAL**.")
