import streamlit as st
from google import genai

# Load environment variables


# Get Gemini API key
api_key =st.secrets["GEMINI_API_KEY"]

# Create Gemini client
client = genai.Client(api_key=api_key)

# Streamlit page configuration
st.set_page_config(
    page_title="Gemini AI Chatbot",
    layout="centered"
)

# Title
st.title("Gemini AI Chatbot")

st.write("Ask Gemini anything!")

# Prompt input
prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Explain Artificial Intelligence in simple words..."
)

# Generate response
if st.button("Generate Response"):

    if prompt:

        with st.spinner("Gemini is thinking..."):

            response = client.models.generate_content(
                model="gemini-3.5-flash-lite",
                contents=prompt
            )

        st.success("Response generated!")

        st.write(response.text)

    else:

        st.warning("Please enter a prompt.")