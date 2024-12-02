
import streamlit as st
#import streamlit_authenticator as stauth


# --- PAGE SETUP ---

st.html("""
  <style>
    [alt=Logo] {
      height: 3.5rem;
    }
  </style>
        """)
  


about_page = st.Page(
    page="views/about.py",
    title="О программе",
    icon=":material/info:",
    default=True,
)

project_1_page = st.Page(
    page="views/page1.py",
    title="ТРАНСПОРТНЫЕ ПРЕДПРИЯТИЯ",
    icon=":material/room_preferences:"
)

project_2_page = st.Page(
    page="views/page2.py",
    title="МАРШРУТЫ",
    icon=":material/directions_bus:"
)

# --- NAVIGATION SETUP ---
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "─────────────────────────── ": [about_page],
        "───────────────────────────": [project_1_page, project_2_page]
    }
)
# --- RUN NAVIGATION ---
pg.run()

# --- SHARED ON ALL PAGES
st.logo("assets/logo.png")
st.sidebar.text("© ГУ «Управление пассажирского транспорта и автомобильных дорог Карагандинской области»")