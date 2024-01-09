import streamlit as st
import streamlit_authenticator as stauths
from streamlit.source_util import _on_pages_changed, get_pages
from streamlit_extras.switch_page_button import switch_page
import face_rec
import subprocess
from Home import show_home
from RealTime import scan_Face
from RegistrationStaff import register
from Generate import session
from Report import report
from loginStaff import login
from signupStaff import signup

page_bg_img = """
<style>
[data-testid= "stSidebar"] {
background: linear-gradient(360deg, rgba(246, 243, 163, 0.83), rgba(203, 235, 141, 0.89))
}

[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}


</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
image_path = 'UMPSA.jpg'
# Center-align the title using HTML
st.markdown(
    """
    <div style="text-align: center;">
        <h1>Welcome to Attendance Monitoring System</h1>
    </div>
    """,
    unsafe_allow_html=True
)


# Create a session state to manage user authentication state
session_state = st.session_state

# Check if the user is authenticated
if not session_state.get("authentication_status", False):
    login_form_container = st.subheader(":white[Login]")
    login()

    # Check if the user is authenticated after login form submission
    if session_state.get("authentication_status", False):
        # Remove the login form from display
        login_form_container.empty()

# If authenticated, display welcome message and navigation
if session_state.get("authentication_status", False):
    st.sidebar.subheader('Welcome to ScanFace System')
    
    # Add navigation to other pages in the sidebar
    selected_page = st.sidebar.radio("Navigation", ["Home", "Scan Face", "Register", "Report"])
    
    if selected_page == "Home":
        show_home()
    elif selected_page == "Scan Face":
        scan_Face()
    elif selected_page == "Register":
        register()
    elif selected_page == "Report":
        report()

    # Logout button
    if st.sidebar.button("Log Out"):
        session_state.user_key = None
        session_state.authentication_status = False

# Display signup form
if not session_state.get("authentication_status", False):
    signup_form_container = st.subheader(":white[Sign Up]")
    signup()

    # Check if the user has signed up successfully
    if session_state.get("signup_status", False):
        # Remove the signup form from display
        signup_form_container.empty()
