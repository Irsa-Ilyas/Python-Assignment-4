import streamlit as st
import random
import time
st.title("📝 Interactive Quiz App")
questions = [
    {"question": "What is the capital of Pakistan?", "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"], "answer": "Islamabad"},
    {"question": "Who is the founder of Pakistan?", "options": ["Allama Iqbal", "Liaquat Ali Khan", "Muhammad Ali Jinnah", "Benazir Bhutto"], "answer": "Muhammad Ali Jinnah"},
    {"question": "Which is the national language of Pakistan?", "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"], "answer": "Urdu"},
    {"question": "What is the currency of Pakistan?", "options": ["Rupee", "Dollar", "Taka", "Riyal"], "answer": "Rupee"},
    {"question": "Which city is known as the City of Lights in Pakistan?", "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"], "answer": "Karachi"},
]
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
    st.session_state.score = 0
    random.shuffle(questions)  

if st.session_state.current_index < len(questions):
    question = questions[st.session_state.current_index]
    st.subheader(question["question"])
    

    selected_option = st.radio("Choose your answer:", question["options"], key=f"answer_{st.session_state.current_index}")
    countdown_placeholder = st.empty()
    for i in range(5, 0, -1):  
        countdown_placeholder.markdown(f"### ⏳ Time Left: {i} sec")
        time.sleep(1)
    countdown_placeholder.empty()
    if st.button("Submit Answer"):
        if selected_option == question["answer"]:
            st.success("✅ Correct!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is {question['answer']}")
        
        time.sleep(2)  
        st.session_state.current_index += 1
        st.rerun()
else:
    st.markdown("## 🎉 Quiz Completed!")
    st.write(f"Your Final Score: **{st.session_state.score}/{len(questions)}**")
    if st.button("Restart Quiz"):
        st.session_state.current_index = 0
        st.session_state.score = 0
        random.shuffle(questions)
        st.rerun()