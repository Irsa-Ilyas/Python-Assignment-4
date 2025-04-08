import streamlit as st
import streamlit as st

st.title("📕Mad Lib  Story Generator")

# Input fields for user input
name = st.text_input("Enter a name:", "Lena")
adjective1 = st.text_input("Enter an adjective:", "foggy")
place = st.text_input("Enter a place:", "ancient ruin")
adjective2 = st.text_input("Enter another adjective:", "glowing")
object_ = st.text_input("Enter an object:", "Magic Gem")
color = st.text_input("Enter a color:", "blue")
magical_feature = st.text_input("Enter a magical world feature (plural):", "floating islands and talking dragons")
magical_being = st.text_input("Enter a title (magical being):", "Ancient Wizard")
adjective3 = st.text_input("Enter another adjective:", "shimmering")
magical_object = st.text_input("Enter a magical object:", "staff of light")
villain = st.text_input("Enter a villain name:", "Shadow King")
kingdom = st.text_input("Enter a kingdom name:", "Kingdom of Eldoria")
if st.button("📝Generate Story"):
    st.markdown("***Here is your mad lib story:***", unsafe_allow_html=True)

    story = f"""
    One evening, ***{name}*** was walking through a ***{adjective1} {place}*** when they stumbled upon a ***{adjective2} {object_}***. 🌟
    Curious, they touched it, and suddenly, a ***{color}*** light flashed! ⚡✨
    When the light faded, they found themselves in a mystical world filled with ***{magical_feature}***. 🌍🔮

    The  ***{magical_being}*** approached and handed them a ***{adjective3} {magical_object}***. ⚔️🪄
    "You are  chosen one," they said. "Only you can defeat the {villain} and restore balance!"
    With determination in their heart, ***{name}*** set off on a daring quest to save the ***{kingdom}***. 🏰
    """

    st.write(story)


