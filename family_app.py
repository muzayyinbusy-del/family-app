import streamlit as st

st.set_page_config(
    page_title="Family Viewer",
    page_icon="👨‍👩‍👧‍👦",
    layout="centered"
)

st.title("👨‍👩‍👧‍👦 Hakim Family")

# --- NAME INPUT ---
user_name = st.text_input("Enter your name")

# Normalize name
user_name = user_name.strip().capitalize()

# Personalized messages
personal_messages = {
    "Hakeem": "The legend who started this family! May Allah have mercy on him! Ameen!",
    "Mymoona": "AMITOTO TO TO TO TO TO TOLE TO TO! The mother of the family!",
    "Raihana": "Puppi! The first child and the first daughter!",
    "Abbas": "Puppa! Welcome!",
    "Lubaina": "Small Puppi! Welcome!",
    "Kaleem": "Uncle! Welcome!",
    "Momin": "Abee!! My father! Welcome!",
    "Naziya": "EMMA! My MOTHER!",
    "Matheen": "Buddy! Welcome!",
    "Reshma": "Mami! Welcome!",
    "Shahina": "Mimi! Welcome!",
    "Mohsin": "APUN! Legend!",
    "Affan": "First grandson!",
    "Nisha": "Babhi! Welcome!",
    "Afreena": "Big DD!",
    "Habeeb": "Jiju!",
    "Ainy": "DD!",
    "Ayaz": "Giju!",
    "Fathima": "Welcome!",
    "Ahmed": "Welcome!",
    "Lubaid": "Boya!",
    "Jahan": "Babhi!",
    "Lubaba": "Favorite DD 👀",
    "Shahid": "Giju!",
    "Muzna": "My sister!",
    "Muzayyin": "Really?",
    "Mazin": "Brother!",
    "Mizan": "Smallest brother!",
    "Mehreen": "Welcome!",
    "Noureen": "Loading...",
    "Mahir": "Soldier!",
    "Mariyam": "Welcome!",
    "Muhammad": "Welcome!",
    "Malhan": "Smallest one!",
    "Nafa": "Welcome!",
    "Nazneen": "Welcome!",
    "Haya": "Welcome!",
    "Yahya": "Welcome!",
    "Hannee": "Welcome!",
    "Hala": "Welcome!",
    "Eesa": "Welcome!",
    "Rabi": "Fan!",
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

    # --- GROUP VIEW ---
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

    st.divider()

    # --- FAMILY TREE ---
    st.subheader("🌳 Family Tree")

    tree = """
    digraph family {
        Hakeem -> Mymoona
        Hakeem -> Lubaina
        Hakeem -> Momin
        Hakeem -> Matheen
        Hakeem -> Mohsin

        Raihana -> Affan
        Raihana -> Afreena

        Affan -> Nafa
        Afreena -> Hannee

        Momin -> Muzna
        Momin -> Muzayyin
        Momin -> Mazin
        Momin -> Mizan
    }
    """

    st.graphviz_chart(tree)
