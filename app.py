import streamlit as st

# --- Streamlit Page Config ---
st.set_page_config(
    page_title="Student Study Dashboard",
    page_icon=":books:",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    body, .stApp { 
        background-color: var(--background-color); 
    }
    .main { 
        background-color: var(--background-color);
    }
    </style>
    """, unsafe_allow_html=True
)

# --- LIGHT/DARK MODE Toggle ---
# Streamlit uses system theme, users can switch in the settings menu

# --- DASHBOARD ---
st.title("Student Study Dashboard")
st.subheader("Dashboard Overview")
col1, col2 = st.columns(2)
with col1:
    st.metric("Upcoming Assignment", "Math HW - Due Monday")
    st.progress(7/10, text="7/10 Study Sessions Complete")
with col2:
    st.metric("Mood", "😊 Motivated")
    st.caption("Tip: Take a short break after every 2 study hours!")

# --- CENTRAL CHATBOT (Simple demo, no API) ---
st.header("AI Chatbot Helper")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_query = st.text_input("Ask the chatbot something:")
if user_query:
    # Example simple logic: echo, with some canned prompts
    if "hello" in user_query.lower():
        reply = "Hello! How can I help you in your studies?"
    elif "flashcard" in user_query.lower():
        reply = "Go ahead and try adding a new flashcard below."
    elif "assignment" in user_query.lower():
        reply = "Your next assignment is Math HW due Monday."
    elif "progress" in user_query.lower():
        reply = "You are doing well! 7 out of 10 study sessions completed."
    else:
        reply = f"I am a simple study bot. You said: '{user_query}'"
    st.session_state.chat_history.append(("You", user_query))
    st.session_state.chat_history.append(("Bot", reply))

# Display chat history
for speaker, msg in st.session_state.chat_history:
    if speaker == "You":
        st.chat_message("user").write(msg)
    else:
        st.chat_message("assistant").write(msg)

st.divider()

# --- FLASHCARDS FEATURE ---
st.header("Flashcards")

if "flashcards" not in st.session_state:
    st.session_state.flashcards = [
        {"question": "What is Python?", "answer": "A popular programming language for versatile applications."},
        {"question": "Streamlit purpose?", "answer": "It is a Python framework for easy data web apps."}
    ]
    st.session_state.flashcard_idx = 0
    st.session_state.flashcard_flip = False

# Navigation buttons
col_prev, col_flip, col_next = st.columns([1,1,1])
with col_prev:
    if st.button("Previous"):
        st.session_state.flashcard_idx = (st.session_state.flashcard_idx - 1) % len(st.session_state.flashcards)
        st.session_state.flashcard_flip = False
with col_flip:
    if st.button("Flip"):
        st.session_state.flashcard_flip = not st.session_state.flashcard_flip
with col_next:
    if st.button("Next"):
        st.session_state.flashcard_idx = (st.session_state.flashcard_idx + 1) % len(st.session_state.flashcards)
        st.session_state.flashcard_flip = False

card = st.session_state.flashcards[st.session_state.flashcard_idx]
if st.session_state.flashcard_flip:
    st.success(card["answer"])
else:
    st.info(card["question"])

# Add new flashcard form
with st.form("new_flashcard", clear_on_submit=True):
    q = st.text_input("New flashcard question")
    a = st.text_input("New flashcard answer")
    submitted = st.form_submit_button("Add Flashcard")
    if submitted and q and a:
        st.session_state.flashcards.append({"question": q, "answer": a})
        st.success("Flashcard added!")

# --- THEME INFO ---
st.divider()
st.caption("To switch between dark and light mode, use the 'Settings' menu in the Streamlit sidebar. Blue/black colors follow your OS or Streamlit preferences.")

# CATa
