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
