import streamlit as st

st.set_page_config(
    page_title="Family Viewer",
    page_icon="👨‍👩‍👧‍👦",
    layout="centered"
)

st.title("👨‍👩‍👧‍👦 Our Family")

# --- NAME INPUT ---
user_name = st.text_input("Enter your name")

# Personalized messages
personal_messages = {
    "Ahmed": "Welcome Ahmed! You are always the heart of this family ❤️",
    "Fatima": "Fatima, your kindness keeps us together 🌸",
    "Ali": "Ali! May your days be full of success and joy 🚀"
}

if user_name:
    message = personal_messages.get(
        user_name,
        f"Welcome {user_name}! We're happy to have you here 😊"
    )
    st.success(message)

st.divider()

# --- FAMILY DATA ---
family = {
    "Parents": [
        "Parent 1",
        "Parent 2"
    ],
    "Children": [
        "Child 1",
        "Child 2"
    ],
    "Grandchildren": [
        "Grandchild 1",
        "Grandchild 2"
    ],
    "Great-Grandchildren": [
        "Great-Grandchild 1"
    ]
}

# --- GROUP SELECTION ---
group = st.selectbox(
    "Which group do you want to see?",
    list(family.keys())
)

st.subheader(group)

for name in family[group]:
    st.write("•", name)
