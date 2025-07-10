import streamlit as st

# Set page config for a tan background
st.set_page_config(page_title="Tutor Signup Form", page_icon="📝", layout="centered")

# Custom CSS for tan and brown theme with Google Fonts and icons
st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@500;700&family=Roboto:wght@400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css">
    <style>
    body, .stApp {
        background-color: #f5ecd7;
        font-family: 'Quicksand', 'Roboto', Arial, sans-serif;
    }
    .stTextInput > div > div > input, .stTextArea > div > textarea {
        background-color: #fff8ee;
        border: 2px solid #a67c52;
        border-radius: 10px;
        color: #4e342e;
        font-size: 1.1em;
        font-family: 'Roboto', Arial, sans-serif;
    }
    .stTextInput > label, .stTextArea > label {
        color: #6d4c2b;
        font-weight: bold;
        font-family: 'Quicksand', Arial, sans-serif;
        font-size: 1.1em;
    }
    .stButton > button {
        background-color: #a67c52;
        color: #fff8ee;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        padding: 0.5em 2em;
        font-size: 1.1em;
        margin-top: 1em;
        font-family: 'Quicksand', Arial, sans-serif;
        transition: background 0.2s;
    }
    .stButton > button:hover {
        background-color: #8d6741;
        color: #fff8ee;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #6d4c2b;
        font-family: 'Quicksand', Arial, sans-serif;
    }
    .icon-label {
        display: flex;
        align-items: center;
        gap: 0.5em;
        font-size: 1.1em;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<h1 style='display: flex; align-items: center; gap: 0.5em;'>
    <i class="fa-solid fa-chalkboard-user"></i> Tutor Signup Form
</h1>
<p style='font-size:1.15em; color:#6d4c2b;'>
    <i class="fa-solid fa-pen-to-square"></i> Please fill out the form below to sign up as a tutor.
</p>
""", unsafe_allow_html=True)



with st.form("signup_form"):

    first_name = st.text_input("First Name", placeholder="e.g. Jordan", help="Enter your first name")
    last_name = st.text_input("Last Name", placeholder="e.g. Smith", help="Enter your last name")
    background = st.text_area("Background", placeholder="Tell us about your experience or interests", help="Share a little about yourself")
    courses = st.text_input("List of Courses", placeholder="e.g. Math, Science", help="What subjects can you tutor?")
    email = st.text_input("Email Address", placeholder="e.g. you@email.com", help="Enter your email address")


    st.markdown("---")
    st.markdown("<span class='icon-label'><i class='fa-solid fa-calendar-days'></i> <b>Availability</b>: Please select the time ranges you are available to tutor on each day.</span>", unsafe_allow_html=True)

    days = [
        "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
    ]
    time_options = [
        "Not Available",
        "8:00 AM - 10:00 AM",
        "10:00 AM - 12:00 PM",
        "12:00 PM - 2:00 PM",
        "2:00 PM - 4:00 PM",
        "4:00 PM - 6:00 PM",
        "6:00 PM - 8:00 PM",
        "8:00 PM - 10:00 PM"
    ]
    availability = {}
    for day in days:
        availability[day] = st.selectbox(
            f"🗓️ {day} Availability", time_options, key=day
        )

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.success(f"<i class='fa-solid fa-circle-check'></i> Thank you, {first_name} {last_name}! Your information has been submitted.", icon="✅")
        st.markdown("<h4 style='margin-top:1em;'><i class='fa-solid fa-calendar-check'></i> Your Availability:</h4>", unsafe_allow_html=True)
        for day in days:
            st.markdown(f"<span class='icon-label'><i class='fa-regular fa-calendar'></i> <b>{day}:</b> {availability[day]}</span>", unsafe_allow_html=True)