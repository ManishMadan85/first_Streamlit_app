import streamlit
import pandas as pd
streamlit.title("My parents New health dinner")
streamlit.header("🥗 🐔 🥑🍞 Breakfast Menu 🥗 🐔 🥑🍞")
streamlit.text("Omega 3 sandwich 🍞")
streamlit.text("Spanich,Rice 🥣")
streamlit.text("Brown Bread 🥗 🍞")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
My_fruits_List=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
my_fruit_list = my_fruit_list.set_index('Fruit')
streamlit.dataframe(My_fruits_List)

