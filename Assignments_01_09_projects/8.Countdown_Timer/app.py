import time
import streamlit as st
st.title("⏳ Countdown Timer")
input_seconds = st.number_input("Enter time in seconds:", min_value=1, step=1)

if st.button("Start Countdown"):
    countdown_placeholder = st.empty()
    while input_seconds > 0:
        mins, secs = divmod(input_seconds, 60)
        countdown_placeholder.markdown(f"## ⏱ {mins:02}:{secs:02}")  
        time.sleep(1)
        input_seconds -= 1

    countdown_placeholder.markdown("🎉 Time's up!")








