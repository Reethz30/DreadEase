import streamlit as st
import sqlite3

# Function to connect to the database
def connect_db():
    return sqlite3.connect('users.db')

# Function to check login credentials
def login_user(email, password):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email=? AND password=?', (email, password))
    result = c.fetchone()
    conn.close()
    return result

# Function to create a new user
def create_user(email, password):
    conn = connect_db()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users (email, password) VALUES (?, ?)', (email, password))
        conn.commit()
        st.success("Account created successfully!")
    except sqlite3.IntegrityError:
        st.error("An account with this email already exists.")
    conn.close()

# Login page layout
st.title("Login Page")

email = st.text_input("Email", placeholder="Enter your email")
password = st.text_input("Password", placeholder="Enter your password", type="password")

if st.button("Login"):
    if login_user(email, password):
        st.success("Login successful!")
    else:
        st.error("Invalid email or password")

st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    if st.button("Forgot Password"):
        st.info("Password recovery options will be sent to your email.")

with col2:
    if st.button("Create Account"):
        new_email = st.text_input("New Email", placeholder="Enter a new email")
        new_password = st.text_input("New Password", placeholder="Enter a new password", type="password")
        if st.button("Submit"):
            create_user(new_email, new_password)
