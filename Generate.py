import streamlit as st
from Home import face_rec
import datetime

def session():
    d = st.date_input("Generate a class session below", datetime.date(2023, 12, 17))
    st.write('Your class session is on:', d)

if __name__ == "__main__":
    session()

