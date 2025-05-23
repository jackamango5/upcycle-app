import streamlit as st
import random

st.set_page_config(page_title="♻️ Upcycle Ideas Generator", page_icon="♻️", layout="centered")

# --- Data with difficulty only ---
upcycle_ideas = {
    "Plastic Bottle": [
        {"idea": "Cut into a self-watering plant pot", "difficulty": "Easy"},
        {"idea": "Use as a pencil holder", "difficulty": "Easy"},
        {"idea": "Turn into a bird feeder", "difficulty": "Medium"},
    ],
    "Old Jeans": [
        {"idea": "Make a denim tote bag", "difficulty": "Medium"},
        {"idea": "Turn into patchwork for jackets", "difficulty": "Hard"},
        {"idea": "Create a dog toy with braiding", "difficulty": "Easy"},
    ],
    "Glass Jar": [
        {"idea": "Use as a spice container", "difficulty": "Easy"},
        {"idea": "Make a DIY lantern with candles", "difficulty": "Medium"},
        {"idea": "Create a mini indoor herb planter", "difficulty": "Easy"},
    ],
    "Cardboard": [
        {"idea": "Make a custom phone stand", "difficulty": "Medium"},
        {"idea": "Build a small storage box", "difficulty": "Hard"},
    ],
}

# --- Page title with color and emoji ---
st.markdown("<h1 style='color:green; text-align:center;'>♻️ Upcycle Ideas Generator</h1>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar: Filters and user input
st.sidebar.header("Customize Your Experience")

# Select item
selected_item = st.sidebar.selectbox("Choose your material:", list(upcycle_ideas.keys()))

# Difficulty filter
difficulty_filter = st.sidebar.selectbox("Select difficulty:", ["All", "Easy", "Medium", "Hard"])

# User idea input
st.sidebar.markdown("### 💡 Add Your Own Idea")
user_idea = st.sidebar.text_area("Describe your upcycling idea:")

if st.sidebar.button("Submit Idea"):
    if user_idea.strip():
        st.sidebar.success("Thanks for sharing your idea!")
        st.sidebar.write(f"💡 Your idea: {user_idea}")
    else:
        st.sidebar.error("Please enter an idea before submitting.")

st.sidebar.markdown("---")

# Main app content
st.subheader(f"Creative ways to upcycle **{selected_item}**:")

# Filter and display ideas
ideas_to_show = upcycle_ideas[selected_item]
if difficulty_filter != "All":
    ideas_to_show = [i for i in ideas_to_show if i["difficulty"] == difficulty_filter]

for idx, idea_data in enumerate(ideas_to_show, 1):
    st.markdown(f"### {idx}. {idea_data['idea']}  ")
    st.markdown(f"**Difficulty:** {idea_data['difficulty']}")
    st.markdown("---")

# Random idea generator
if st.button("🎲 Give me a random upcycling idea!"):
    random_item = random.choice(list(upcycle_ideas.keys()))
    random_idea = random.choice(upcycle_ideas[random_item])
    st.info(f"Try upcycling a **{random_item}** by: {random_idea['idea']} (Difficulty: {random_idea['difficulty']})")

# Footer
st.markdown(
    """
    <footer style='text-align:center; color:gray; margin-top:30px;'>
    Developed with ♻️ to inspire creativity and sustainability!
    </footer>
    """,
    unsafe_allow_html=True,
)
