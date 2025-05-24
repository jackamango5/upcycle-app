import streamlit as st
import random

# App Config
st.set_page_config(page_title="Upcycle App", page_icon="♻️", layout="centered")

# Expanded Upcycling Ideas
upcycle_ideas = {
    "Plastic Bottle": [
        "Make a self-watering plant pot",
        "Create a bird feeder",
        "Turn into a pencil holder",
        "Use as a mini greenhouse for seedlings",
        "Make a plastic bottle broom",
        "Create decorative flower petals",
        "Use to store small hardware like nails or buttons",
        "Cut and use as funnels",
        "Make a hanging herb garden",
        "Build a vertical wall planter"
    ],
    "Old Jeans": [
        "Sew a denim tote bag",
        "Cut into coasters",
        "Make a braided dog toy",
        "Create a denim pencil roll",
        "Turn into a phone sleeve",
        "Create patchwork quilts",
        "Make a fabric plant holder",
        "Use pockets as wall organizers",
        "Turn into chair cushion covers",
        "Cut and stitch a headband or scrunchie"
    ],
    "Glass Jar": [
        "Use as a candle holder",
        "Make a herb planter",
        "Store spices or buttons",
        "Create a DIY snow globe",
        "Make a hanging lantern",
        "Turn into a bathroom organizer",
        "Store homemade jams or sauces",
        "Paint and use as a flower vase",
        "Use as desk storage for pens",
        "Create layered sand art"
    ],
    "Cardboard": [
        "Build a phone stand",
        "Create drawer dividers",
        "Make an organizer box",
        "Cut into stencils or templates",
        "Create a mini pinball machine",
        "Make a puppet theater",
        "Craft greeting cards",
        "Build a cat house",
        "Design an art canvas",
        "Make seed starter pots"
    ],
    "Old T-Shirts": [
        "Make a tote bag with no sewing",
        "Turn into cleaning cloths",
        "Weave into a rug",
        "Make headbands or wristbands",
        "Create braided bracelets",
        "Make a reusable produce bag",
        "Stuff into a pet bed",
        "Turn into pillow covers",
        "Use strips for gift wrapping",
        "Create wall art from fabric designs"
    ],
    "Magazines or Paper": [
        "Create paper beads for jewelry",
        "Make a vision board or collage",
        "Fold into origami",
        "Make DIY envelopes",
        "Use to wrap gifts artistically",
        "Create paper mâché crafts",
        "Shred for packaging material",
        "Line pet cages",
        "Make bookmarks",
        "Create handmade notebooks"
    ],
    "Single Socks": [
        "Make a rice-filled hand warmer",
        "Create a sock puppet",
        "Turn into a coin purse",
        "Use as a glasses protector",
        "Stuff and turn into a door draft stopper",
        "Make baby leg warmers",
        "Create a dryer ball",
        "Fill with lavender for drawer sachets",
        "Turn into a stress ball",
        "Use for shoe polishing"
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

    st.markdown(f"### 💡 Ideas for {selected}")
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
