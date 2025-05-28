import streamlit as st
import random

# App Configuration
st.set_page_config(page_title="Upcycle App", page_icon="♻️", layout="centered")

# Expanded Upcycling Ideas
upcycle_ideas = {
    "Plastic Bottle": [
        "make a self-watering plant pot",
        "create a bird feeder",
        "turn into a pencil holder",
        "use as a mini greenhouse for seedlings",
        "make a hanging herb garden"
    ],
    "Old Jeans": [
        "sew a denim tote bag",
        "cut into coasters",
        "make a braided dog toy",
        "create patchwork quilts",
        "turn into chair cushion covers"
    ],
    "Glass Jar": [
        "use as a candle holder",
        "make a herb planter",
        "store spices or buttons",
        "create a DIY snow globe",
        "paint and use as a flower vase"
    ],
    "Cardboard": [
        "build a phone stand",
        "make drawer dividers",
        "create a puppet theater",
        "design an art canvas",
        "make seed starter pots"
    ],
    "Old T-Shirts": [
        "make a tote bag with no sewing",
        "turn into cleaning cloths",
        "weave into a rug",
        "create braided bracelets",
        "turn into pillow covers"
    ],
    "Magazines or Paper": [
        "create paper beads for jewelry",
        "make a vision board or collage",
        "fold into origami",
        "make DIY envelopes",
        "create paper mâché crafts"
    ],
    "Single Socks": [
        "make a rice-filled hand warmer",
        "create a sock puppet",
        "turn into a coin purse",
        "stuff and turn into a door draft stopper",
        "use for shoe polishing"
    ]
}

# Session State
if "user_ideas" not in st.session_state:
    st.session_state.user_ideas = []

# Sidebar Navigation
st.sidebar.title("📱 Upcycle App")
page = st.sidebar.radio("Go to", [
    "🏠 Browse Ideas",
    "💡 Submit Idea",
    "📒 My Saved Ideas",
    "ℹ️ About"
])

# App Header
st.markdown(
    "<h1 style='text-align: center; color: #2e7d32;'>♻️ Upcycle Idea Generator</h1>",
    unsafe_allow_html=True
)
st.markdown("<p style='text-align: center;'>Inspire and be inspired to upcycle creatively.</p>", unsafe_allow_html=True)
st.markdown("---")

# Page 1: Browse Ideas
if page == "🏠 Browse Ideas":
    st.subheader("🔍 Browse Creative Ideas")
    col1, col2 = st.columns([2, 1])

    with col1:
        selected = st.selectbox("Choose a material:", list(upcycle_ideas.keys()))
    with col2:
        if st.button("🎲 Random Idea"):
            random_item = random.choice(list(upcycle_ideas.keys()))
            random_idea = random.choice(upcycle_ideas[random_item])
            st.success(f"**{random_item}** → {random_idea.capitalize()}")

    st.markdown(f"### 💡 Ideas for {selected}")
    for idea in upcycle_ideas[selected]:
        st.markdown(f"- {idea.capitalize()}")

# Page 2: Submit an Idea
elif page == "💡 Submit Idea":
    st.subheader("💬 Submit Your Own Upcycling Idea")
    user_idea = st.text_input("Your idea:")
    if st.button("Submit"):
        if user_idea.strip():
            st.session_state.user_ideas.append(user_idea.strip())
            st.success("✅ Idea added to your saved list!")
        else:
            st.error("Please enter a valid idea.")

# Page 3: My Saved Ideas
elif page == "📒 My Saved Ideas":
    st.subheader("📋 My Saved Ideas")
    if st.session_state.user_ideas:
        for i, idea in enumerate(st.session_state.user_ideas, 1):
            st.markdown(f"{i}. {idea}")
    else:
        st.info("You haven't added any ideas yet!")

# Page 4: About
elif page == "ℹ️ About":
    st.subheader("ℹ️ About This App")
    st.write("""
    This app was created to explore the question:  
    **“How can I design something that encourages people to start upcycling in creative ways?”**

    ♻️ **Purpose:**  
    The goal of this app is to spark ideas and curiosity. By organizing creative reuse projects by material, users can instantly find ways to turn old or unused items into useful, fun, or artistic creations.

    💡 **How It Encourages Upcycling:**
    - It lowers the barrier to entry: you just pick a material you already have.
    - It inspires creativity through diverse, easy-to-understand ideas.
    - It lets users share their own upcycling projects — making it feel more like a community.
    - It keeps the experience simple, engaging, and focused on action — helping users go from idea to project quickly.

    🌱 Whether you're a beginner or already into DIY, this app encourages everyone to take small steps toward reducing waste and making something meaningful.
    """)

