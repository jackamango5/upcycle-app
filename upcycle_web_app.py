import streamlit as st
import random

st.set_page_config(page_title="Upcycle Idea App", page_icon="♻️", layout="centered")

# --- Data ---
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

# --- Header ---
st.title("♻️ Upcycle Idea Generator")
st.subheader("Design something that encourages people to upcycle creatively")

# --- Tabs for Layout ---
tab1, tab2, tab3 = st.tabs(["🔍 Browse Ideas", "💡 Submit Your Idea", "📒 My Saved Ideas"])

# --- TAB 1: Browse Ideas ---
with tab1:
    st.header("Find Upcycling Ideas")

    selected_item = st.selectbox("Choose a material:", list(upcycle_ideas.keys()))
    if selected_item:
        st.markdown(f"### ♻️ Ideas for {selected_item}")
        for idea in upcycle_ideas[selected_item]:
            st.markdown(f"- {idea}")

    if st.button("🎲 Show me a random idea!"):
        item = random.choice(list(upcycle_ideas.keys()))
        idea = random.choice(upcycle_ideas[item])
        st.success(f"**{item}** → {idea}")

# --- TAB 2: Submit Idea ---
with tab2:
    st.header("Share Your Own Idea 💬")
    new_idea = st.text_input("Type your upcycling idea:")
    if st.button("Submit Idea"):
        if new_idea.strip():
            st.session_state.user_ideas.append(new_idea.strip())
            st.success("Thanks! Your idea was saved.")
        else:
            st.error("Please type something before submitting.")

# --- TAB 3: View Saved Ideas ---
with tab3:
    st.header("Your Saved Ideas")
    if st.session_state.user_ideas:
        for idx, idea in enumerate(st.session_state.user_ideas, start=1):
            st.markdown(f"{idx}. {idea}")
    else:
        st.info("You haven't saved any ideas yet.")

# --- Footer ---
st.markdown("---")
st.caption("✨ Created with creativity and code for a sustainable future.")
