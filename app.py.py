import streamlit as st

st.header("Hello")

isClicked = st.button("버튼")
if isClicked :
  st.write("버튼 클릭됨")
