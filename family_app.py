import json
import time
import random
import streamlit as st
import os

VISITS_FILE = "visits.txt"


def get_total_visits():
    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            f.write("0")

    with open(VISITS_FILE, "r") as f:
        visits = int(f.read())

    visits += 1

    with open(VISITS_FILE, "w") as f:
        f.write(str(visits))

    return visits


LEADERBOARD_FILE = "emoji_leaderboard.json"


def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return {}
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)


def save_score(name, score):
    leaderboard = load_leaderboard()

    if name not in leaderboard or score < leaderboard[name]:
        leaderboard[name] = round(score, 3)

        with open(LEADERBOARD_FILE, "w") as f:
            json.dump(leaderboard, f, indent=2)


st.set_page_config(
    page_title="Hakim Family Tree",
    page_icon="🌳",
    layout="centered"
)
total_visits = get_total_visits()


# --- FAMILY COUNTER DATA ---
current_members = {
    "Hakeem", "Mymoona", "Raihana", "Abbas", "Lubaina", "Kaleem", "Momin", "Naziya",
    "Matheen", "Reshma", "Shahina", "Mohsin", "Affan", "Nisha", "Afreena", "Habeeb",
    "Ainy", "Ayaz", "Fathima", "Ahmed", "Lubaid", "Jahan", "Lubaba", "Shahid",
    "Muzna", "Muzayyin", "Mazin", "Mizan", "Mehreen", "Mahir", "Mariyam",
    "Muhammad", "Malhan", "Nafa", "Nazneen", "Haya", "Yahya", "Hannee",
    "Hala", "Eesa", "Rabi", "Huma", "Shanaya", "Noureen"
}

coming_soon = {
    "Lulu Boya's child",
    "Ainy DD's child"
}

total_current = len(current_members)
total_coming = len(coming_soon)

st.title("🌳 Hakim Family Tree")

# ================= FAMILY NEWS + COUNTER =================
with st.sidebar:
    st.header("📰 Hakeem Family News")

    st.markdown("""

    🔵 **Upcoming**
    - Noni Moni Soon!
    
    🟢 **07/02/2026**
    - Muhammad shows off his driving skills! 😎
    
    🟢 **06/02/2026**
    - MeemNoon Family did Umrah!

    🟡 **05/02/2026**
    - The development of this website began!

    """)

    st.divider()

    st.subheader("📊 Family Count")
    st.markdown(f"""
    👨‍👩‍👧‍👦 **Family Members:** {total_current}  
    👶 **Coming Soon:** {total_coming}
    """)

    st.divider()
    st.subheader("👀 Website Visits")
    st.markdown(f"**Total Visits:** {total_visits}")

    st.divider()
    st.caption("Updated by Muzayyin News 👑")
    st.caption("Version: 1.3.0 <-- sooo cooool")

# --- NAME INPUT ---
user_name = st.text_input(
    "Enter your name (Make sure to just add your first name only, I coded it so that it takes just your first name :))")

# Normalize name
user_name = user_name.strip().capitalize()

# --- PERSONAL MESSAGES ---
personal_messages = {
    "Hakeem": "The legend who started this family! May Allah have mercy on him! Ameen!",
    "Mymoona": "AMITOTO TO TO TO TO TO TOLE TO TO! The mother of the family!",
    "Raihana": "Puppi! The first child and the first daughter! Welcome!",
    "Abbas": "Puppa! The man who married the first daughter of HF!",
    "Lubaina": "Small Puppi! Welcome! The second child of HF!",
    "Kaleem": "Uncle! The legend who married the second child of HF! Welcome!",
    "Momin": "Abee!! You are the coolest man alive right now! My father! The first son of HF! Welcome!",
    "Naziya": "EMMA! My MOTHER! The best mom ever! Welcome to the website! I love you! The women who married the best man alive!",
    "Matheen": "Buddy! Buddy! The youngest son and the busiest son of HF! Welcome!",
    "Reshma": "Mami! The first wife of Buddy! Welcome!",
    "Shahina": "Mimi! The second wife of Buddy! Welcome!",
    "Mohsin": "APUN! Another legend! When people hear his name they run the other way! Welcome!",
    "Affan": "Affan Boya! The first grandson in the family! Welcome!",
    "Nisha": "Nisha Babhi! The wife of the first grandson of the family! Welcome!",
    "Afreena": "Afreena DD! The big DD of the whole family!",
    "Habeeb": "Jiju! Yes Giju with the J! The man who married the biggest DD of the family! Welcome!",
    "Ainy": "Ainy DD! The second eldest DD of the family! Welcome!",
    "Ayaz": "Ayaz Giju! The man who married the second biggest DD in the family!",
    "Fathima": "Uhm....Wel..welcome...the.......jreoihifdgjer",
    "Ahmed": "Ahmed! Cool dude in the family! Welcome!",
    "Lubaid": "Lulu Boya! The second eldest grandson of the family! Welcome!",
    "Jahan": "Jahan Babhi! The wife of the 2nd eldest grandson! Welcome!",
    "Lubaba": "Baba DD! My favorite DD! (Don't say other DDs!) Welcome!",
    "Shahid": "Shahid Gju! The husband of my favorite DD! (Don't tell anyone!) Welcome!",
    "Muzna": "Ayyyyyyy! My one and only sister! Welcome to the board!",
    "Muzayyin": "Really?",
    "Mazin": "Ayyy Mazin! My only brother! oh wait........",
    "Mizan": "My youngest brother!!!! Mizannnnnn! I LOVE YOU!",
    "Mehreen": "The first daughter of Buddy! Welcome!",
    "Noureen": "Loading...",
    "Mahir": "Solider! My defender! Welcome to the website!",
    "Mariyam": "The youngest daughter of buddy! Welcome!",
    "Muhammad": "Muhammad! Cool dude in the family! Welcome!",
    "Malhan": "The youngest one in the family so far! Welcome!",
    "Nafa": "Nafa! The daughter of the eldest Pulli in the family!",
    "Nazneen": "Nazneen! The daughter of the eldest grandson of the family! Welcome!",
    "Haya": "Haya! The eldest daughter of Jiju!",
    "Yahya": "The eldest grandson of Puppi!!",
    "Hannee": "Hannee! The second daughter of Afreena DD! Welcome!",
    "Hala": "Hala Wallah 3amak Abdullah! Welcome!",
    "Eesa": "Eesa! The eldest son of Ayaz Jiju!",
    "Rabi": "Rabi! Fan! Fan! only me and Rabi knows what the code 'Fan' means!",
    "Huma": "Huma! Lulu Boya's first daughter and soon to be a big sister! Welcome!",
    "Shanaya": "Shannu! Hide & Seek champion! Best seeker and best hider!"
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
st.header("🎮 Tap the Tree 🌳")

if "game_started" not in st.session_state:
    st.session_state.game_started = False
    st.session_state.start_time = None
    st.session_state.penalty = 0
    st.session_state.emojis = []


if not st.session_state.game_started:
    if st.button("▶️ Start Game", use_container_width=True):
        st.session_state.game_started = True
        st.session_state.start_time = time.time() + random.uniform(2, 4)
        st.session_state.penalty = 0
        emojis = ["😈", "👀", "💣", "🍌", "🐸", "🌳"]
        random.shuffle(emojis)
        st.session_state.emojis = emojis
        st.rerun()

if st.session_state.game_started:

    now = time.time()

    # Waiting phase
    if now < st.session_state.start_time:
        st.info("⏳ Get ready...")
    else:
        st.write("👇 Tap the 🌳 as fast as you can!")

        emojis = st.session_state.emojis

        cols = st.columns(3)

        for i, emoji in enumerate(emojis):
            with cols[i % 3]:
                if st.button(
                    emoji,
                    key=f"emoji_{i}",
                    use_container_width=True
                ):
                    reaction_time = time.time() - st.session_state.start_time

                    # ❌ Wrong emoji
                    if emoji != "🌳":
                        st.session_state.penalty += 0.5
                        st.warning("❌ Wrong emoji! +0.5s penalty")
                        st.rerun()

                    # ✅ Correct emoji
                    else:
                        final_score = reaction_time + st.session_state.penalty
                        save_score(user_name, final_score)

                        st.success(
                            f"🌳 Nice! Your time: {final_score:.3f} seconds"
                        )

                        st.session_state.game_started = False
                        st.rerun()

st.subheader("🏆 Fastest Fingers Leaderboard")

leaderboard = load_leaderboard()

if leaderboard:
    sorted_scores = sorted(leaderboard.items(), key=lambda x: x[1])[:10]

    for i, (name, score) in enumerate(sorted_scores, start=1):
        if i == 1:
            medal = "🥇"
        elif i == 2:
            medal = "🥈"
        elif i == 3:
            medal = "🥉"
        else:
            medal = "👑"

        st.write(f"{medal} {i}. **{name}** — {score:.3f}s")
else:
    st.info("No scores yet. Be the first to tap the 🌳 😏")


# 🔔 NEWS POPUP (ADD THIS)
st.toast("📰 New Hakeem Family News available! Click the sidebar 👈", icon="👀")
st.info("👈 Don’t miss today’s Hakeem Family News in the sidebar!")

st.divider()

# ================= FAMILY TREE =================
st.header("🌳 Family Tree")

with st.expander("👴 Hakeem ❤️ Mymoona", expanded=True):

    st.markdown("### 👩 Raihana ❤️ Abbas")
    st.markdown("- 👦 **Affan** ❤️ Nisha")
    st.markdown("  - --> 👧 Nafa")
    st.markdown("  - --> 👧 Nazneen")
    st.markdown("- 👧 **Afreena** ❤️ Habeeb")
    st.markdown("  - --> 👧 Haya")
    st.markdown("  - --> 👦 Yahya")
    st.markdown("  - --> 👧 Hannee")
    st.markdown("  - --> 👧 Hala")
    st.markdown("- 👧 **Ainy** ❤️ Ayaz")
    st.markdown("  - --> 👦 Eesa")
    st.markdown("  - --> 👦 Rabi")

    st.divider()

    st.markdown("### 👩 Lubaina ❤️ Kaleem")
    st.markdown("- 👦 **Lubaid** ❤️ Jahan")
    st.markdown("  - --> 👧 Huma")
    st.markdown("- 👧 **Lubaba** ❤️ Shahid")
    st.markdown("  - --> 👧 Shanaya")
    st.markdown("- 👧 Fathima")
    st.markdown("- 👦 Ahmed")

    st.divider()

    st.markdown("### 👨 Momin ❤️ Naziya")
    st.markdown("- 👦 Muzayyin")
    st.markdown("- 👧 Muzna")
    st.markdown("- 👦 Mazin")
    st.markdown("- 👦 Mizan")

    st.divider()

    st.markdown("### 👨 Mohsin")
    st.markdown("- Single")

    st.divider()

    st.markdown("### 👨 Matheen ❤️ Reshma & Shahina")
    st.markdown("- 👧 **Mehreen** ❤️ Noureen")
    st.markdown("- 👧 Mariyam")
    st.markdown("- 👦 Muhammad")
    st.markdown("- 👦 Mahir")


st.divider()

# ================= GROUP VIEW =================
st.header("👨‍👩‍👧‍👦 View by Generation")

family_groups = {
    "Parents": ["Hakeem ❤️ Mymoona "],
    "Children": [
        "Raihana ❤️ Abbas", "Lubaina ❤️ Kaleem", "Momin ❤️ Naziya", "Mohsin", "Matheen ❤️ Reshma & Shahina",

    ],
    "Grandchildren": [
        "Affan ❤️ Nisha", "Afreena ❤️ Habeeb", "Lubaid ❤️ Jahan", "Lubaba ❤️ Shahid",
        "Ainy ❤️ Ayaz", "Muzayyin", "Fathima", "Mehreen ❤️ Noureen",
        "Mariyam", "Muzna", "Muhammad", "Ahmed",
        "Mazin", "Mahir", "Mizan", "Malhan"
    ],
    "Great-Grandchildren": [
        "Haya", "Nafa", "Nazneen",  "Yahya", "Shanaya", "Eesa", "Hannee", "Hala",
        "Rabi", "Huma",
    ]
}

group = st.selectbox("Select a group", family_groups.keys())

for name in family_groups[group]:
    st.write("•", name)
