import streamlit as st
st.title("hello world")
st.write("this is a simple Streamlit app.")

st.button("say hello")
st.text("hello, streamlit")
st.text_input("please enter your name")

st.radio("gender",["male","female"],index=None)

if name:
  st.write(f'hello,{name}!')
if st.file_uploader('pls upload file:',type=['txt,'csv']):
  st.write("thanks for uploading")
