import streamlit as st
import login
import create
import dashboard
import password

# Get the current page from query parameters
query_params = st.query_params.to_dict()
current_page = query_params.get('page', 'login')

# Function to handle navigation using query parameters
def navigate_to(page):
    st.query_params.from_dict({"page": page})

# Display the appropriate page based on the query parameter
if current_page == 'login':
    login.login_page(navigate_to)
elif current_page == 'password':
    password.reset_password_page(navigate_to)
elif current_page == 'create':
    create.create_account_page(navigate_to)
elif current_page == 'dashboard':
    dashboard.dashboard()
