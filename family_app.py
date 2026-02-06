import streamlit as st

st.set_page_config(
    page_title="Family Viewer",
    page_icon="👨‍👩‍👧‍👦",
    layout="centered"
)

st.title("👨‍👩‍👧‍👦 Hakim Family")

# --- NAME INPUT ---
user_name = st.text_input("Enter your name")

# Normalize name: first letter capital
user_name = user_name.strip().capitalize()

# Personalized messages
personal_messages = {
    "Hakeem": "The legend who started this family! May Allah have mercy on him! Ameen!",
    "Mymoona": "AMITOTO TO TO TO TO TO TOLE TO TO! The mother of the family!",
    "Raihana": "Puppi! The first child and the first daughter! Welcome!",
    "Abbas": "Puppa! The man who married the first daughter of HF!",
    "Lubaina": "Small Puppi! Welcome! The second child of HF!",
    "Kaleem": "Uncle! The legend who married the second child of HF! Welcome!",
    "Momin": "Abee!! You are the coolest man alive right now! My father! Welcome!",
    "Naziya": "EMMA! My MOTHER! The best mom ever! Welcome!",
    "Matheen": "Buddy! Buddy! The smallest son of HF! Welcome!",
    "Reshma": "Mami! The first wife of Buddy! Welcome!",
    "Shahina": "Mimi! The second wife of Buddy! Welcome!",
    "Mohsin": "APUN! Another legend! Welcome!",
    "Affan": "Affan Boya! The first grandson in the family! Welcome!",
    "Nisha": "Nisha Babhi! Welcome!",
    "Afreena": "Afreena DD! The big DD of the whole family!",
    "Habeeb": "Jiju! Welcome!",
    "Ainy": "Ainy DD! Welcome!",
    "Ayaz": "Ayaz Giju! Welcome!",
    "Fathima": "Uhm....Wel..welcome...",
    "Ahmed": "Ahmed! Welcome!",
    "Lubaid": "Lulu Boya! Welcome!",
    "Jahan": "Jahan Babhi! Welcome!",
    "Lubaba": "Baba DD! My favorite DD!",
    "Shahid": "Shahid Giju! Welcome!",
    "Muzna": "Ayyyyy! My one and only sister!",
    "Muzayyin": "Really?",
    "Mazin": "Ayyy Mazin!",
    "Mizan": "My smallest brother! I LOVE YOU!",
    "Mehreen": "Welcome!",
    "Noureen": "Loading...",
    "Mahir": "Soldier! Welcome!",
    "Mariyam": "Welcome!",
    "Muhammad": "Welcome!",
    "Malhan": "Welcome!",
    "Nafa": "Welcome!",
    "Nazneen": "Welcome!",
    "Haya": "Welcome!",
    "Yahya": "Welcome!",
    "Hannee": "Welcome!",
    "Hala": "Welcome!",
    "Eesa": "Welcome!",
    "Rabi": "Fan! Fan!",
    "Huma": "Welcome!",
    "Shanaya": "Hide & Seek champion!"
}

# ---- SHOW REST ONLY AFTER NAME IS ENTERED ----
if not user_name:
    st.info("👆 Please enter your name to continue")

else:
    message = personal_messages.get(
        user_name,
        f"Welcome {user_name}! We're happy to have you here 😊"
    )
    st.success(message)

    st.divider()

    family = {
        "Parents": ["Hakeem", "Mymoona"],
        "Children": [
            "Raihana", "Abbas", "Lubaina", "Kaleem",
            "Momin", "Naziya", "Matheen", "Shahina",
            "Reshma", "Mohsin"
        ],
        "Grandchildren": [
            "Affan", "Nisha", "Afreena", "Habeeb", "Ainy",
            "Ayaz", "Fathima", "Ahmed", "Lubaid", "Jahan",
            "Lubaba", "Shahid", "Muzna", "Muzayyin",
            "Mazin", "Mizan", "Mehreen", "Noureen",
            "Mahir", "Mariyam", "Muhammad", "Malhan"
        ],
        "Great-Grandchildren": [
            "Nafa", "Nazneen", "Haya", "Yahya", "Hannee",
            "Hala", "Eesa", "Rabi", "Huma", "Shanaya"
        ]
    }

    group = st.selectbox(
        "Which group do you want to see?",
        list(family.keys())
    )

    st.subheader(group)

    for name in family[group]:
        st.write("•", name)


