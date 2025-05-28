import streamlit as st

st.set_page_config(page_title="Upcycle Ideas", layout="centered")

# Sample upcycling ideas with difficulty
upcycling_ideas = {
    "Old T-Shirts": [
        {"idea": "Turn into a reusable tote bag", "difficulty": "Easy"},
        {"idea": "Cut and braid into a rug", "difficulty": "Medium"},
        {"idea": "Sew into a quilt", "difficulty": "Hard"}
    ],
    "Glass Jars": [
        {"idea": "Use as storage containers", "difficulty": "Easy"},
        {"idea": "Make candle holders with twine", "difficulty": "Medium"},
        {"idea": "Create LED lanterns", "difficulty": "Hard"}
    ],
    "Cardboard Boxes": [
        {"idea": "Make drawer organizers", "difficulty": "Easy"},
        {"idea": "Build a mini shelf", "difficulty": "Medium"},
        {"idea": "Construct a playhouse", "difficulty": "Hard"}
    ]
}

# Initialize session state
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "submissions" not in st.session_state:
    st.session_state.submissions = []

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Add an Idea", "Favorites", "About the App"])

# Home Page
if page == "Home":
    st.title("♻️ Upcycle Idea Generator")
    st.write("Find fun ways to reuse materials and help the planet.")

    material = st.selectbox("Choose a material:", list(upcycling_ideas.keys()))
    difficulty = st.selectbox("Filter by difficulty:", ["All", "Easy", "Medium", "Hard"])

    if material:
        ideas = upcycling_ideas.get(material, [])
        if difficulty != "All":
            ideas = [i for i in ideas if i["difficulty"] == difficulty]

        if ideas:
            for idea in ideas:
                st.markdown(f"- **{idea['idea']}** _(Difficulty: {idea['difficulty']})_")
                if st.button(f"❤️ Save '{idea['idea']}'", key=idea['idea']):
                    if idea not in st.session_state.favorites:
                        st.session_state.favorites.append(idea)
        else:
            st.info("No ideas found for this difficulty.")

# Add an Idea Page
elif page == "Add an Idea":
    st.title("💡 Add Your Upcycling Idea")

    new_material = st.text_input("Material:")
    new_idea = st.text_area("Your idea:")
    new_difficulty = st.selectbox("Select difficulty:", ["Easy", "Medium", "Hard"])

    if st.button("Submit"):
        if new_material and new_idea:
            idea_obj = {"idea": new_idea.strip(), "difficulty": new_difficulty}
            upcycling_ideas.setdefault(new_material.strip(), []).append(idea_obj)
            st.session_state.submissions.append(idea_obj)
            st.success("Thanks for your idea!")
        else:
            st.warning("Please fill out both fields.")

# Favorites Page
elif page == "Favorites":
    st.title("❤️ Saved Ideas")
    if st.session_state.favorites:
        for fav in st.session_state.favorites:
            st.markdown(f"- **{fav['idea']}** _(Difficulty: {fav['difficulty']})_")
    else:
        st.info("No favorites yet.")

# About Page
elif page == "About the App":
    st.title("ℹ️ About the App")
    st.write("""
    This app was designed to answer the question:
    **How can I design something that encourages people to start upcycling in creative ways?**

    By offering fun and practical reuse ideas, the app inspires users to look at waste materials differently.
    It encourages action by making upcycling approachable and interactive.
    """)

