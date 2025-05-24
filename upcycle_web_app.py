import streamlit as st
import random

# App Config
st.set_page_config(page_title="Upcycle App", page_icon="♻️", layout="centered")

# Data
upcycle_ideas = {
    "Plastic Bottle": [
        "Make a self-watering plant pot",
        "Create a bird feeder",
        "Turn into a pencil holder"
    ],
    "Old Jeans": [
        "Sew a denim tote bag",
        "Cut into coasters",
        "Make a braided dog toy"
    ],
    "Glass Jar": [
        "Use as a candle holder",
        "Make a herb planter",
        "Store spices or buttons"
    ],
    "Cardboard": [
        "Build a phone stand",
        "Create drawer dividers",
        "Make an organizer box"
    ]
}

# Session state for saved ideas
if "user_ideas" not in st.session_state:
    st.session_state.user_ideas = []

# Sidebar Navigation
st.sidebar.title("📱 Upcycle App")
page = st.sidebar.radio("Go to", ["🏠 Browse Ideas", "💡 Submit Idea", "📒 My Saved Ideas"])

# Header
st.markdown(
    "<h1 style='text-align: center; color: #2e7d32;'>♻️ Upcycle Idea Generator</h1>",
    unsafe_allow_html=True
)
st.markdown("<p style='text-align: center;'>Inspire and be inspired to upcycle creatively.</p>", unsafe_allow_html=True)

st.markdown("---")

# Page: Browse Ideas
if page == "🏠 Browse Ideas":
    st.subheader("🔍 Browse Creative Ideas")

    col1, col2 = st.columns([2, 1])
    with col1:
        selected = st.selectbox("Choose a material:", list(upcycle_ideas.keys()))
    with col2:
        if st.button("🎲 Random Idea"):
            random_item = random.choice(list(upcycle_ideas.keys()))
            random_idea = random.choice(upcycle_ideas[random_item])
            st.success(f"**{random_item}** → {random_idea}")

    st.markdown("### 💡 Ideas for " + selected)
    for idea in upcycle_ideas[selected]:
        st.markdown(f"- {idea}")

# Page: Submit Idea
elif page == "💡 Submit Idea":
    st.subheader("💬 Submit Your Own Idea")

    user_idea = st.text_input("What’s your creative upcycling idea?")
    if st.button("Submit Idea"):
        if user_idea.strip():
            st.session_state.user_ideas.append(user_idea.strip())
            st.success("✅ Your idea was added to your personal board!")
        else:
            st.error("Please type an idea first!")

# Page: My Saved Ideas
elif page == "📒 My Saved Ideas":
    st.subheader("📋 My Saved Ideas")

    if st.session_state.user_ideas:
        for idx, idea in enumerate(st.session_state.user_ideas, start=1):
            st.markdown(f"{idx}. {idea}")
    else:
        st.info("You haven’t saved any ideas yet. Go submit one!")

# Footer
st.markdown("---")
st.caption("Made with passion for a cleaner, more creative world ✨")
