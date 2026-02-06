import streamlit as st

st.set_page_config(
    page_title="Hakim Family Tree",
    page_icon="🌳",
    layout="centered"
)

st.title("🌳 Hakim Family Tree")

# --- NAME INPUT ---
user_name = st.text_input("Enter your name")

# Normalize name
user_name = user_name.strip().capitalize()

# --- PERSONAL MESSAGES ---
personal_messages = {
    "Hakeem": "The legend who started this family! May Allah have mercy on him! Ameen!",
    "Maimoona": "AMITOTO TO TO TO TO TO TOLE TO TO! The mother of the family!",
    "Raihana": "Puppi! The first child and the first daughter! Welcome!",
    "Abbas": "Puppa! The man who married the first daughter of HF!",
    "Lubaina": "Small Puppi! Welcome! The second child of HF!",
    "Kaleem": "Uncle! The legend who married the second child of HF! Welcome!",
    "Momin": "Abee!! You are the coolest man alive right now! My father! Welcome!",
    "Naziya": "EMMA! My MOTHER! The best mom ever! Welcome!",
    "Matheen": "Buddy! Buddy! The busiest son of HF! Welcome!",
    "Reshma": "Mami! The first wife of Buddy! Welcome!",
    "Shahina": "Mimi! The second wife of Buddy! Welcome!",
    "Mohsin": "APUN! Another legend! Welcome!",
    "Affan": "Affan Boya! The first grandson in the family! Welcome!",
    "Nisha": "Nisha Babhi! Welcome!",
    "Afreena": "Afreena DD! The big DD of the whole family!",
    "Habeeb": "Jiju! Welcome!",
    "Ainy": "Ainy DD! Welcome!",
    "Ayaz": "Ayaz Giju! Welcome!",
    "Fathima": "Uhm.... Wel... welcome...",
    "Ahmed": "Ahmed! One of the cool dudes in the family!",
    "Lubaid": "Lulu Boya! Welcome!",
    "Jahan": "Jahan Babhi! Welcome!",
    "Lubaba": "Baba DD! My favorite DD!",
    "Shahid": "Shahid Giju! Welcome!",
    "Muzna": "Ayyyyyyy! My one and only sister!",
    "Muzayyin": "Really?",
    "Mazin": "Ayyy Mazin!",
    "Mizan": "My smallest brother!!!! I LOVE YOU!",
    "Mehreen": "The first daughter of Buddy! Welcome!",
    "Noureen": "Welcome to the family!",
    "Mahir": "Soldier! My defender! Welcome!",
    "Muhammad": "One of the coolest dudes in the family!",
    "Mariyam": "The smallest daughter of Buddy! Welcome!",
    "Nafa": "The daughter of the biggest Pulli in the family!",
    "Nazneen": "The daughter of the biggest grandson of the family!",
    "Haya": "The biggest daughter of Jiju!",
    "Yahya": "The biggest grandson of Puppi!!",
    "Hannee": "The second daughter of Afreena DD!",
    "Hala": "Hala Wallah 3amak Abdullah!",
    "Eesa": "The biggest son of Ayaz Jiju!",
    "Rabi": "Fan! Fan! Only me and Rabi know what that means!",
    "Huma": "Lulu Boya's first daughter and soon to be a big sister!",
    "Shanaya": "Hide & Seek champion! Best seeker and hider!"
}

# --- ACCESS CONTROL ---
allowed_names = set(personal_messages.keys())

if not user_name:
    st.info("👆 Please enter your name to continue")
    st.stop()

if user_name not in allowed_names:
    st.error("🚫 Access denied. This family tree is private.")
    st.warning("Please enter a valid family member name.")
    st.stop()

# --- SHOW PERSONAL MESSAGE ---
st.success(personal_messages[user_name])

st.divider()

# ================= FAMILY TREE =================
st.header("🌳 Family Tree")

with st.expander("👴 Hakeem ❤️ Maimoona", expanded=True):

    st.markdown("### 👩 Raihana ❤️ Abbas")
    st.markdown("- 👦 **Affan** ❤️ Nisha")
    st.markdown("  - 👧 Nafa")
    st.markdown("  - 👧 Nazneen")
    st.markdown("- 👧 **Afreena** ❤️ Habeeb")
    st.markdown("  - 👧 Haya")
    st.markdown("  - 👧 Hannee")
    st.markdown("  - 👧 Hala")
    st.markdown("  - 👦 Yahya")
    st.markdown("- 👧 **Ainy** ❤️ Ayaz")
    st.markdown("  - 👦 Eesa")
    st.markdown("  - 👦 Rabi")

    st.divider()

    st.markdown("### 👩 Lubaina ❤️ Kaleem")
    st.markdown("- 👧 Fathima")
    st.markdown("- 👦 Ahmed")
    st.markdown("- 👦 **Lubaid** ❤️ Jahan")
    st.markdown("  - 👧 Huma")
    st.markdown("- 👧 **Lubaba** ❤️ Shahid")
    st.markdown("  - 👧 Shanaya")

    st.divider()

    st.markdown("### 👨 Momin ❤️ Naziya")
    st.markdown("- 👧 Muzna")
    st.markdown("- 👦 Muzayyin")
    st.markdown("- 👦 Mazin")
    st.markdown("- 👦 Mizan")

    st.divider()

    st.markdown("### 👨 Mohsin")
    st.markdown("- Single")

    st.divider()

    st.markdown("### 👨 Matheen ❤️ Reshma & Shahina")
    st.markdown("- 👧 **Mehreen** ❤️ Noureen")
    st.markdown("- 👦 Mahir")
    st.markdown("- 👦 Muhammad")
    st.markdown("- 👧 Mariyam")

st.divider()

# ================= GROUP VIEW =================
st.header("👨‍👩‍👧‍👦 View by Generation")

family_groups = {
    "Parents": ["Hakeem", "Maimoona"],
    "Children": [
        "Raihana", "Lubaina", "Momin", "Mohsin", "Matheen",
        "Abbas", "Kaleem", "Naziya", "Reshma", "Shahina"
    ],
    "Grandchildren": [
        "Affan", "Afreena", "Ainy", "Fathima", "Ahmed",
        "Lubaid", "Lubaba", "Muzna", "Muzayyin",
        "Mazin", "Mizan", "Mehreen", "Mahir",
        "Muhammad", "Mariyam"
    ],
    "Great-Grandchildren": [
        "Nafa", "Nazneen", "Haya", "Hannee", "Hala",
        "Yahya", "Eesa", "Rabi", "Huma", "Shanaya"
    ]
}

group = st.selectbox("Select a group", family_groups.keys())

for name in family_groups[group]:
    st.write("•", name)
