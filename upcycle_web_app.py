import streamlit as st
import random

st.set_page_config(page_title="Creative Upcycling Ideas", layout="wide")

# Upcycling Ideas Data with Difficulty Levels
upcycling_ideas = {
    "Old T-Shirts": [
        {"idea": "Turn into a reusable tote bag", "difficulty": "Easy"},
        {"idea": "Cut and braid into a rug", "difficulty": "Medium"},
        {"idea": "Sew into a quilt", "difficulty": "Hard"}
    ],
    "Glass Jars": [
        {"idea": "Use as storage containers", "difficulty": "Easy"},
        {"idea": "Make candle holders with paint or twine", "difficulty": "Medium"},
        {"idea": "Create decorative lanterns with LED lights", "difficulty": "Hard"}
    ],
    "Cardboard Boxes": [
        {"idea": "Create drawer organizers", "difficulty": "Easy"},
        {"idea": "Build a mini shelf", "difficulty": "Medium"},
        {"idea": "Construct a kid’s playhouse", "difficulty": "Hard"}
    ],
    "Plastic Bottles": [
        {"idea": "Make a bird feeder", "difficulty": "Easy"},
        {"idea": "Create a hanging planter", "difficulty": "Medium"},
        {"idea": "Build a vertical garden wall", "difficulty": "Hard"}
    ],
    "Tin Cans": [
        {"idea": "Use as desk organizers", "difficulty": "Easy"},
        {"idea": "Turn into candle holders with punched designs", "difficulty": "Medium"},
        {"idea": "Build a wind chime with multiple cans", "difficulty": "Hard"}
    ]
}

# Initialize favorites and submissions in session state
if "favorites" not in st.session_state:
    st.session_state.favorites = []
if "submissions" not in st.session_state:
    st.session_state.submissions = []

# Sidebar Navigation
st.sidebar.title("Explore")
page = st.sidebar.radio("Go to", ["Home", "Add Your Idea", "Favorites", "About"])

# Home Page
if page == "Home":
    st.title("♻️ Creative Upcycling Ideas")
    st.write("Find inspiration to reuse everyday materials in fun and creative ways!")

    material = st.selectbox("Choose a material:", list(upcycling_ideas.keys()))
    selected_difficulty = st.selectbox("Filter by Difficulty", ["All", "Easy", "Medium", "Hard"])

    if material:
        ideas = upcycling_ideas.get(material, [])
        if selected_difficulty != "All":
            ideas = [idea for idea in ideas if idea["difficulty"] == selected_difficulty]

        if ideas:
            for idea in ideas:
                st.markdown(f"- **{idea['idea']}** _(Difficulty: {idea['difficulty']})_")
                if st.button(f"❤️ Save: {idea['idea']}", key=idea['idea']):
                    if idea not in st.session_state.favorites:
                        st.session_state.favorites.append(idea)
        else:
            st.info("No ideas match your difficulty filter.")

# Add Your Idea Page
elif page == "Add Your Idea":
    st.title("💡 Share Your Upcycling Idea")
    st.write("Have a creative idea? Add it here!")

    new_material = st.text_input("What material is it for?")
    new_idea = st.text_area("Describe your upcycling idea:")
    new_difficulty = st.selectbox("Select a difficulty level:", ["Easy", "Medium", "Hard"])

    if st.button("Submit Idea"):
        if new_material and new_idea:
            entry = {"idea": new_idea.strip(), "difficulty": new_difficulty}
            upcycling_ideas.setdefault(new_material.strip(), []).append(entry)
            st.session_state.submissions.append(entry)
            st.success("Thank you! Your idea has been added.")
        else:
            st.warning("Please fill in all fields before submitting.")

# Favorites Page
elif page == "Favorites":
    st.title("❤️ Your Favorite Ideas")
    if st.session_state.favorites:
        for fav in st.session_state.favorites:
            st.markdown(f"- **{fav['idea']}** _(Difficulty: {fav['difficulty']})_")
    else:
        st.info("You haven't saved any ideas yet.")

# About Page
elif page == "About":
    st.title("📘 About the App")
    st.write("""
    This app was created as a way to encourage people to explore upcycling in fun and creative ways. 
    By offering practical ideas for reusing everyday materials, it aims to make sustainability feel more accessible and exciting.
    Whether you're new to upcycling or already love DIY projects, this tool helps spark creativity while helping the environment.
    """)

