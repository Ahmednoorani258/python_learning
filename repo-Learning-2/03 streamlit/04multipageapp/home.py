import streamlit as st

pg = st.navigation([st.Page( "bike.py"), st.Page( "car.py")])
pg.run()