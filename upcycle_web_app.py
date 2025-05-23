import streamlit as st
import random

st.set_page_config(page_title="♻️ Upcycle Ideas Generator", page_icon="♻️", layout="centered")

# --- Data with images, difficulty, and tutorial links ---
upcycle_ideas = {
    "Plastic Bottle": [
        {
            "idea": "Cut into a self-watering plant pot",
            "difficulty": "Easy",
            "image": "https://cdn-icons-png.flaticon.com/512/2907/2907257.png",
            "tutorial": "https://www.youtube.com/watch?v=QFJ3_8_pIMQ"
        },
        {
            "idea": "Use as a pencil holder",
            "difficulty": "Easy",
            "image": "https://cdn-icons-png.flaticon.com/512/2907/2907257.png",
            "tutorial": ""
        },
        {
            "idea": "Turn into a bird feeder",
            "difficulty": "Medium",
            "image": "https://cdn-icons-png.flaticon.com/512/616/616408.png",
            "tutorial": "https://www.youtube.com/watch?v=QjpHZ8gO8xk"
        },
    ],
    "Old Jeans": [
        {
            "idea": "Make a denim tote bag",
            "difficulty": "Medium",
            "image": "https://cdn-icons-png.flaticon.com/512/941/941790.png",
            "tutorial": "https://www.youtube.com/watch?v=gyF1jX_rFK4"
        },
        {
            "idea": "Turn into patchwork for jackets",
            "difficulty": "Hard",
            "image": "https://cdn-icons-png.flaticon.com/512/941/941790.png",
            "tutorial": ""
        },
        {
            "idea": "Create a dog toy with braiding",
            "difficulty": "Easy",
            "image": "https://cdn-icons-png.flaticon.com/512/616/616408.png",
            "tutorial": "https://www.youtube.com/watch?v=7rz8m9zFz44"
        },
    ],
    "Glass Jar": [
        {
            "idea": "Use as a spice container",
            "difficulty": "Easy",
            "image": "https://cdn-icons-png.flaticon.com/512/2942/2942138.png",
            "tutorial": ""
        },
        {
            "idea": "Make a DIY lantern with candles",
            "difficulty": "Medium",
            "image": "https://cdn-icons-png.flaticon.com/512/2942/2942138.png",
            "tutorial": "https://www.youtube.com/watch?v=dY5W8uBebkE"
        },
        {
            "idea": "Create a mini indoor herb planter",
            "difficulty": "Easy",
            "image": "https://cdn-icons-png.flaticon.com/512/415/415733.png",
            "tutorial": ""
        },
    ],
    "Cardboard": [
        {
            "idea": "Make a custom phone stand",
            "difficulty": "Medium",
            "image": "https://cdn-icons-png.flaticon.com/512/1259/1259060.png",
            "tutorial": "https://www.youtube.com/watch?v=QhE5B6QYRM4"
        },
        {
            "idea": "Build a small storage box",
            "difficulty": "Hard",
            "image": "https://cdn-icons-png.flaticon.com/512/1259/1259060.png",
            "tutorial": ""
        },
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
    if idea_data["image"]:
        st.image(idea_data["image"], width=150)
    if idea_data["tutorial"]:
        st.markdown(f"[Watch tutorial here ▶️]({idea_data['tutorial']})")
    st.markdown("---")

# Random idea generator
if st.button("🎲 Give me a random upcycling idea!"):
    random_item = random.choice(list(upcycle_ideas.keys()))
    random_idea = random.choice(upcycle_ideas[random_item])
    st.info(f"Try upcycling a **{random_item}** by: {random_idea['idea']} (Difficulty: {random_idea['difficulty']})")
    if random_idea["tutorial"]:
        st.markdown(f"[Watch tutorial ▶️]({random_idea['tutorial']})")

# Footer
st.markdown(
    """
    <footer style='text-align:center; color:gray; margin-top:30px;'>
    Developed with ♻️ to inspire creativity and sustainability!
    </footer>
    """,
    unsafe_allow_html=True,
)
