import streamlit as st
import random

# App Configuration
st.set_page_config(page_title="Upcycle App", page_icon="♻️", layout="centered")

# Upcycling Ideas with Difficulty
upcycle_ideas = {
    "Plastic Bottle": [
        {"text": "make a self-watering plant pot", "difficulty": "Easy"},
        {"text": "create a bird feeder", "difficulty": "Medium"},
        {"text": "turn into a pencil holder", "difficulty": "Easy"},
        {"text": "use as a mini greenhouse for seedlings", "difficulty": "Medium"},
        {"text": "make a hanging herb garden", "difficulty": "Hard"}
    ],
    "Old Jeans": [
        {"text": "sew a denim tote bag", "difficulty": "Medium"},
        {"text": "cut into coasters", "difficulty": "Easy"},
        {"text": "make a braided dog toy", "difficulty": "Medium"},
        {"text": "create patchwork quilts", "difficulty": "Hard"},
        {"text": "turn into chair cushion covers", "difficulty": "Medium"}
    ],
    "Glass Jar": [
        {"text": "use as a candle holder", "difficulty": "Easy"},
        {"text": "make a herb planter", "difficulty": "Easy"},
        {"text": "store spices or buttons", "difficulty": "Easy"},
        {"text": "create a DIY snow globe", "difficulty": "Medium"},
        {"text": "paint and use as a flower vase", "difficulty": "Medium"}
    ],
    "Cardboard": [
        {"text": "build a phone stand", "difficulty": "Easy"},
        {"text": "make drawer dividers", "difficulty": "Easy"},
        {"text": "create a puppet theater", "difficulty": "Medium"},
        {"text": "design an art canvas", "difficulty": "Medium"},
        {"text": "make seed starter pots", "difficulty": "Easy"}
    ],
    "Old T-Shirts": [
        {"text": "make a tote bag with no sewing", "difficulty": "Easy"},
        {"text": "turn into cleaning cloths", "difficulty": "Easy"},
        {"text": "weave into a rug", "difficulty": "Medium"},
        {"text": "create braided bracelets", "difficulty": "Easy"},
        {"text": "turn into pillow covers", "difficulty": "Medium"}
    ],
    "Magazines or Paper": [
        {"text": "create paper beads for jewelry", "difficulty": "Medium"},
        {"text": "make a vision board or collage", "difficulty": "Easy"},
        {"text": "fold into origami", "difficulty": "Medium"},
        {"text": "make DIY envelopes", "difficulty": "Easy"},
        {"text": "create paper mâché crafts", "difficulty": "Hard"}
    ],
    "Single Socks": [
        {"text": "make a rice-filled hand warmer", "difficulty": "Easy"},
        {"text": "create a sock puppet", "difficulty": "Easy"},
        {"text": "turn into a coin purse", "difficulty": "Medium"},
        {"text": "stuff and turn into a door draft stopper", "difficulty": "Medium"},
        {"text": "use for shoe polishing", "difficulty": "Easy"}
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
    col1, col2, col3 = st.columns([2, 2, 1])

    with col1:
        selected_material = st.selectbox("Choose a material:", list(upcycle_ideas.keys()))
    with col2:
        difficulty_level = st.selectbox("Choose difficulty:", ["All", "Easy", "Medium", "Hard"])
    with col3:
        if st.button("🎲 Random Idea"):
            all_ideas = [(k, i) for k, v in upcycle_ideas.items() for i in v]
            material, idea = random.choice(all_ideas)
            st.success(f"**{material}** → {idea['text'].capitalize()} _(Difficulty: {idea['difficulty']})_")

    st.markdown(f"### 💡 Ideas for {selected_material} ({difficulty_level})")
    filtered = [
        idea for idea in upcycle_ideas[selected_material]
        if difficulty_level == "All" or idea["difficulty"] == difficulty_level
    ]

    if filtered:
        for idea in filtered:
            st.markdown(f"- {idea['text'].capitalize()} _(Difficulty: {idea['difficulty']})_")
    else:
        st.info("No ideas found for that difficulty level.")

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
