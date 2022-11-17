import streamlit
import pandas as pd
streamlit.title("My parents New health dinner")
streamlit.header("🥗 🐔 🥑🍞 Breakfast Menu 🥗 🐔 🥑🍞")
streamlit.text("Omega 3 sandwich 🍞")
streamlit.text("Spanich,Rice 🥣")
streamlit.text("Brown Bread 🥗 🍞")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
My_fruits_List=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(My_fruits_List)
