import streamlit as st

def main():
    st.set_page_config(
        page_title="Gujarati POS Morph Analyzer",
        page_icon="✨",
        layout='wide'
    )

if __name__ == "__main__":
    main()

st.title("Gujarati POS & Morph Analyzer")
st.markdown("---")
st.subheader("About")
st.markdown(
    "This application allows you to perform part-of-speech tagging and morphological analysis "
    "of Gujarati language text using different models."
)
st.markdown(
    "You can select the desired model from the navigation below to get started. Each model serves "
    "a specific purpose based on your requirements."
)
st.subheader("Models Available:")
st.markdown("- GUJ POS MORPH: Model for predicting POS and morphological features.")
# st.markdown("- GUJ MORPH BY POS SUPPORT : Model for predicting morphological features with POS support.")
# st.markdown("- GUJ ONLY POS: Model for predicting only POS of Gujarati words.")

st.markdown("#### Research 🔬 Design & Training by : ")
st.markdown("* Prof. Brijesh Bhatt")
st.markdown("* Prof. Jatayu Baxi")
st.markdown("* Om Ashishkumar Soni")

