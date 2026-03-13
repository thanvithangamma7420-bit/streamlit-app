import streamlit as st
import sqlite3
from Backend.matching_engine import calculate_similarity
from Backend.skill_analyzer import extract_skills
from Backend.ats_checker import calculate_ats_score

# ---------------- DATABASE FUNCTIONS ---------------- #

def create_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS users(username TEXT, password TEXT)")
    c.execute("INSERT INTO users VALUES (?,?)", (username, password))

    conn.commit()
    conn.close()


def login_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))

    data = c.fetchone()
    conn.close()

    return data


# ---------------- UI ---------------- #

st.title("AI Resume Matcher Platform")

menu = ["Login", "Sign Up"]
choice = st.sidebar.selectbox("Menu", menu)


# ---------------- SIGN UP ---------------- #

if choice == "Sign Up":

    st.subheader("Create New Account")

    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if st.button("Create Account"):

        create_user(new_user, new_password)
        st.success("Account Created Successfully")


# ---------------- LOGIN ---------------- #

if choice == "Login":

    st.subheader("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        result = login_user(username, password)

        if result:

            st.success("Login Successful")
            st.header("Welcome to AI Resume ATS Analyzer")

            st.subheader("Resume Matching Dashboard")
        
        st.subheader("Resume Matching Dashboard")

resume_text = st.text_area("Paste Resume Text")

job_description = st.text_area("Paste Job Description")

if st.button("Analyze Resume"):

    similarity = calculate_similarity(resume_text, job_description)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    ats_score, matched, missing = calculate_ats_score(resume_skills, job_skills)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Match Score", f"{similarity:.2f}%")

    with col2:
        st.metric("ATS Score", f"{ats_score:.2f}%")

    st.subheader("Matched Skills")
    st.success(matched)

    st.subheader("Missing Skills")
    st.error(missing)

