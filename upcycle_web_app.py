import streamlit as st

# Upcycling ideas
upcycle_ideas = {
    "Plastic Bottle": [
        "Cut into a self-watering plant pot",
        "Use as a pencil holder",
        "Turn into a bird feeder"
    ],
    "Old Jeans": [
        "Make a denim tote bag",
        "Turn into patchwork for jackets",
        "Create a dog toy with braiding"
    ],
    "Glass Jar": [
        "Use as a spice container",
        "Make a DIY lantern with candles",
        "Create a mini indoor herb planter"
    ]
}

# App title
st.title("♻️ Upcycle Ideas Generator")

# Dropdown
item = st.selectbox("What item do you have?", list(upcycle_ideas.keys()))

# Show ideas
if item:
    st.subheader(f"Creative ways to upcycle your {item.lower()}:")
    for i, idea in enumerate(upcycle_ideas[item], 1):
        st.write(f"{i}. {idea}")
