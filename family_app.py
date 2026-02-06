import streamlit as st

st.set_page_config(
    page_title="Family Viewer",
    page_icon="👨‍👩‍👧‍👦",
    layout="centered"
)

st.title("👨‍👩‍👧‍👦 Hakim Family")

# --- NAME INPUT ---
user_name = st.text_input("Enter your name")

# Personalized messages
personal_messages = {
    "Hakeem": "The legend who started this family! May Allah have mercy on him! Ameen!",
    "Maimoona": "AMITOTO TO TO TO TO TO TOLE TO TO! The mother of the family!",
    "Raihana": "Puppi! The first child and the first daughter! Welcome!",
    "Abbas": "Puppa! The man who married the first daughter of HF!",
    "Lubaina": "Small Puppi! Welcome! The second child of HF!",
    "Kaleem": "Uncle! The legend who married the second child of HF! Welcome!",
    "Momin": "Abee!! You are the coolest man alive right now! My father! The first son of HF! Welcome!",
    "Naziya": "EMMA! My MOTHER! The best mom ever! Welcome to the website! I love you!",
    "Matheen": "Buddy! Buddy! The smallest son and the busiest son of HF! Welcome!",
    "Reshma": "Mami! The first wife of Buddy! Welcome!",
    "Shahina": "Mimi! The second wife of Buddy! Welcome!",
    "Mohsin": "APUN! Another legend! Welcome!",
    "Affan": "Affan Boya! The first grandson in the family! Welcome!",
    "Nisha": "Nisha Babhi! The wife of the first grandson of the family! Welcome!",
    "Afreena": "Afreena DD! The big DD of the whole family!",
    "Habeeb": "Jiju! The man who married the biggest DD of the family! Welcome!",
    "Ainy": "Ainy DD! The second biggest DD of the family! Welcome!",
    "Ayaz": "Ayaz Giju! The man who married the second biggest DD in the family!",
    "Fathima": "Uhm....Wel..welcome... 👀",
    "Ahmed": "Ahmed! One of the cool dudes in the family! Welcome!",
    "Lubaid": "Lulu Boya! The second biggest grandson of the family! Welcome!",
    "Jahan": "Jahan Babhi! The wife of the 2nd biggest grandson! Welcome!",
    "Lubaba": "Baba DD! My favorite DD! (Don’t tell the others 👀)",
    "Shahid": "Shahid Giju! The husband of my favorite DD!",
    "Muzna": "Ayyyyy! My one and only sister! Welcome!",
    "Muzayyin": "Really?",
    "Mazin": "Ayyy Mazin! My only brother! oh wait...",
    "Mizan": "My smallest brother!!!! Mizannnnnn! I LOVE YOU!",
    "Mehreen": "The first daughter of Buddy! Welcome!",
    "Noureen": "Loading...",
    "Mahir": "Soldier! My defender! Welcome!",
    "Mariyam": "The smallest daughter of Buddy! Welcome!",
    "Muhammad": "One of the coolest dudes in the family! Welcome!",
    "Malhan": "The smallest one in the family so far! Welcome!",
    "Nafa": "Nafa! The daughter of the biggest Pulli in the family!",
    "Nazneen": "Nazneen! Welcome!",
    "Haya": "Haya! The biggest daughter of Jiju!",
    "Yahya": "Yahya! The biggest grandson of Puppi!",
    "Hannee": "Hannee! Welcome!",
    "Hala": "Hala Wallah 3amak Abdullah!",
    "Eesa": "Eesa! The biggest son of Ayaz Jiju!",
    "Rabi": "Rabi! Fan! Fan!",
    "Huma": "Huma! Lulu Boya's first daughter!",
    "Shanaya": "Shannu! Hide & Seek champion!"
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

    # --- FAMILY DATA ---
    family = {
        "Parents": [
            "Hakeem",
            "Maimoona"
        ],
        "Children": [
            "Raihana",
            "Abbas",
            "Lubaina",
            "Kaleem",
            "Momin",
            "Naziya",
            "Matheen",
            "Shahina",
            "Reshma",
            "Mohsin",
        ],
        "Grandchildren": [
            "Affan",
            "Nisha",
            "Afreena",
            "Habeeb",
            "Ainy",
            "Ayaz",
            "Fathima",
            "Ahmed",
            "Lubaid",
            "Jahan",
            "Lubaba",
            "Shahid",
            "Muzna",
            "Muzayyin",
            "Mazin",
            "Mizan",
            "Mehreen",
            "Noureen",
            "Mahir",
            "Mariyam",
            "Muhammad",
            "Malhan",
        ],
        "Great-Grandchildren": [
            "Nafa",
            "Nazneen",
            "Haya",
            "Yahya",
            "Hannee",
            "Hala",
            "Eesa",
            "Rabi",
            "Huma",
            "Shanaya",
        ]
    }

    group = st.selectbox(
        "Which group do you want to see?",
        list(family.keys())
    )

    st.subheader(group)

    for name in family[group]:
        st.write("•", name)
