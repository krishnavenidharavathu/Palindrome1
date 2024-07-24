import streamlit as st
st.title("Palindrome")
a=st.text_input(label="enter the  number")
st.button("submit",type="primary")
b=a[::-1]
if (a==b):
    st.title("palindrome")
else:
    st.title("Not palindrome")
