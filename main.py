
import streamlit as st
import random

# --- Page Configuration ---
st.set_page_config(page_title="AI Assistant", layout="centered")

# --- Title ---
st.markdown("<h1 style='text-align: center; color: #673AB7;'>🤖 AI Agent Assistant</h1>", unsafe_allow_html=True)
st.markdown("### Ask me anything or try a quick task!")

# --- Sidebar with suggestions ---
with st.sidebar:
    st.markdown("## ✨ Try Questions")
    if st.button("What is Python?"):
        st.session_state.user_input = "What is Python?"
    if st.button("Tell me a joke"):
        st.session_state.user_input = "Tell me a joke"
    if st.button("Motivate me"):
        st.session_state.user_input = "Motivate me"

# --- Input Text ---
user_input = st.text_input("💬 Type your question here:", value=st.session_state.get("user_input", ""))

# --- AI Agent Logic (Rule-based) ---
def ai_agent_response(query):
    query = query.lower()
    if "python" in query:
        return "🐍 Python is a powerful programming language used for web development, data science, AI, and more!"
    elif "joke" in query:
        jokes = [
            "Why don't programmers like nature? It has too many bugs. 🐛",
            "Why do Java developers wear glasses? Because they don't see sharp. 🤓"
        ]
        return random.choice(jokes)
    elif "motivate" in query:
        return "Believe in yourself! You're capable of amazing things! 🚀"
    else:
        return "I’m still learning! Ask me about Python, jokes, or motivation."

# --- Display Response ---
if st.button("🧠 Get Response"):
    if user_input.strip():
        response = ai_agent_response(user_input)
        st.markdown(
            f"<div style='background-color: #EDE7F6; padding: 20px; border-radius: 10px;'>"
            f"<h3>AI Agent says:</h3><p>{response}</p>"
            f"</div>",
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter a question or command!")

# --- Footer ---
st.markdown("<hr><center>Developed by Ansiya • Internship AI Project</center>", unsafe_allow_html=True)
