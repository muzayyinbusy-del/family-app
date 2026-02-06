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
    "Hakeem": "The legend who started this family! May Allah have mercy on him. Ameen 🤍",
    "Mymoona": "The heart of the family 💖",
    "Momin": "Abee! The coolest dad ever 😎",
    "Naziya": "Emma! The best mom ever 💕",
    "Muzayyin": "Really? 😏",
}

if not user_name:
    st.info("👆 Please enter your name to continue")
else:
    st.success(
        personal_messages.get(
            user_name,
            f"Welcome {user_name}! We're happy to have you here 😊"
        )
    )

    st.divider()

    # ================= FAMILY TREE =================

    st.header("🌳 Family Tree")

    with st.expander("👴 Hakeem ❤️ Mymoona", expanded=True):

        # --- CHILD 1 ---
        st.markdown("### 👩 Raihana ❤️ Abbas")
        with st.container():
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

        # --- CHILD 2 ---
        st.markdown("### 👩 Lubaina ❤️ Kaleem")
        with st.container():
            st.markdown("- 👧 Fathima")
            st.markdown("- 👦 Ahmed")
            st.markdown("- 👦 **Lubaid** ❤️ Jahan")
            st.markdown("  - 👧 Huma")
            st.markdown("- 👧 **Lubaba** ❤️ Shahid")
            st.markdown("  - 👧 Shanaya")

        st.divider()

        # --- CHILD 3 ---
        st.markdown("### 👨 Momin ❤️ Naziya")
        with st.container():
            st.markdown("- 👧 Muzna")
            st.markdown("- 👦 Muzayyin")
            st.markdown("- 👦 Mazin")
            st.markdown("- 👦 Mizan")

        st.divider()

        # --- CHILD 4 ---
        st.markdown("### 👨 Mohsin")
        st.markdown("- Single")

        st.divider()

        # --- CHILD 5 ---
        st.markdown("### 👨 Matheen ❤️ Reshma & Shahina")
        with st.container():
            st.markdown("- 👧 **Mehreen** ❤️ Noureen")
            st.markdown("- 👦 Mahir")
            st.markdown("- 👦 Mohammad")
            st.markdown("- 👧 Mariyam")

    st.divider()

    # ================= GROUP VIEW =================

    st.header("👨‍👩‍👧‍👦 View by Generation")

    family_groups = {
        "Parents": ["Hakeem", "Mymoona"],
        "Children": [
            "Raihana", "Lubaina", "Momin", "Mohsin", "Matheen",
            "Abbas", "Kaleem", "Naziya", "Reshma", "Shahina"
        ],
        "Grandchildren": [
            "Affan", "Afreena", "Ainy", "Fathima", "Ahmed",
            "Lubaid", "Lubaba", "Muzna", "Muzayyin",
            "Mazin", "Mizan", "Mehreen", "Mahir",
            "Mohammad", "Mariyam"
        ],
        "Great-Grandchildren": [
            "Nafa", "Nazneen", "Haya", "Hannee", "Hala",
            "Yahya", "Eesa", "Rabi", "Huma", "Shanaya"
        ]
    }

    group = st.selectbox("Select a group", family_groups.keys())

    for name in family_groups[group]:
        st.write("•", name)
