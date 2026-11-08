import streamlit as st
from src.predict import predict_news

st.set_page_config(
    page_title="Fake News Detector",
    page_icon="📰",
    layout="centered"
)

st.title("📰 Fake News Detector")
st.write("Enter a news article below to classify it as fake or real.")

news_text = st.text_area(
    "News article",
    height=220,
    placeholder="Paste your news article here..."
)

if st.button("Analyze News"):
    if not news_text.strip():
        st.warning("Please enter some news text.")
    else:
        try:
            result = predict_news(news_text)
            prediction = result["prediction"]
            confidence = result["confidence"]

            if prediction == "fake":
                st.error("⚠️ Prediction: FAKE NEWS")
            else:
                st.success("✅ Prediction: REAL NEWS")

            st.metric("Model confidence", f"{confidence:.1%}")
            st.caption(
                "This is a machine-learning prediction, not a verified fact-check."
            )

        except FileNotFoundError as error:
            st.error(str(error))
        except Exception as error:
            st.error(f"Prediction failed: {error}")
