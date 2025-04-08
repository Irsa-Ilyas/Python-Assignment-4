import streamlit as st
import string
import random
st.set_page_config(page_title="Password Generator",page_icon="🔒")
st.title("Password Generator")
st.markdown("Generate a strong and secure password.")
passsword_length=st.slider("Select you passswrod length",min_value=6,max_value=20,value=12)
letters=string.ascii_letters
numbers=st.checkbox("Include numbers")
symbols=st.checkbox("Include symbols")
if numbers:
    letters+=string.digits
if symbols:
    letters+="!@#$%^&*(){}[]"
if st.button("Generate Password"):
    mypass="".join(random.choices(letters,k=passsword_length))
    st.subheader(mypass)

    


