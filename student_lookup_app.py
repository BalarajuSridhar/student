
"""Student Results Lookup Streamlit App
To run:
    streamlit run student_lookup_app.py
"""

import streamlit as st

# ----------------- Page configuration -----------------
st.set_page_config(
    page_title="Student Results Lookup",
    page_icon="🎓",
    layout="centered",
)

# ----------------- Custom CSS -----------------
st.markdown(
    """
    <style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        color: white;
    }
    /* Center the main container */
    section.main > div:first-child {
        max-width: 500px;
        margin: auto;
    }
    /* Input & button styling */
    input[type="text"] {
        padding: 10px;
        border-radius: 5px;
        font-size: 16px;
        width: 100%;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        border: none;
    }
    button[kind="primary"]  {
        background-color: #ff4e50 !important;
        color: white !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 5px !important;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    }
    button[kind="primary"]:hover {
        background-color: #fc913a !important;
        transform: scale(1.05);
    }
    a.result-link {
        color: yellow;
        font-weight: bold;
        font-size: 18px;
        text-decoration: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------- Data -----------------
STUDENT_DATA = {
    "22F11A0501": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2Mzcy",
    "502": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjA4",
    "503": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MzA4",
    "504": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2Mzc3",
    "505": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjM4",
    "506": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDMz",
    "508": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjMw",
    "509": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDY0",
    "510": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2Mzg1",
    "511": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MzM1",
    "512": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTY2",
    "513": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MzQ0",
    "515": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MzAz",
    "516": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTE5",
    "517": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDg5",
    "519": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDUw",
    "520": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2Mzky",
    "521": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTcz",
    "522": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDQ4",
    "523": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDM1",
    "524": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDk5",
    "525": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDg7",
    "526": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTE3",
    "527": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDAx",
    "528": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MzIz",
    "529": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjM4",
    "530": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTM2",
    "531": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDI1",
    "532": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDEz",
    "533": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTk5",
    "535": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTIw",
    "536": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MzA0",
    "537": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTk1",
    "538": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MzE3",
    "539": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDQy",
    "540": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTU1",
    "541": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MzM0",
    "543": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDE5",
    "544": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDU5",
    "545": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2Mjg5",
    "546": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDM7",
    "547": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTI5",
    "549": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTgy",
    "550": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDI5",
    "551": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDM1",
    "552": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MzY8",
    "553": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDQz",
    "554": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDMy",
    "555": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDM6",
    "556": "https://esc.ibomma.day/telugu-movies/",
    "557": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDU8",
    "558": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjA5",
    "559": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MTE4",
    "560": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDQy",
    "561": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MDE1",
    "562": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjA7",
    "564": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDU2",
    "565": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDU7",
    "566": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2NDU9",
    "23F15A0501": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMzA5MDI2MzYx",
    "23F15A0502": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMzA5MDI2MzEz",
    "23F15A0503": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMzA5MDI2MzEx",
    "23F15A0504": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjA7",
    "23F15A0505": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMzA5MDI2MzEy",
    "23F15A0506": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMzA5MDI2MzEw",
    "23F15A0507": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMzA5MDI2MzQy",
    "5B7": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjE1",
    "5C9": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjE2",
    "577": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjIw",
    "5B6": "https://narayanagroup.co.in/patient/EngAutonomousReport.aspx/MjAyMjA5MDI2MjM1",
}

# ----------------- UI -----------------
st.title("📊 Students Results")

roll = st.text_input("Enter Roll Number", max_chars=20)

# When user hits Enter or after input
if st.button("Get Data"):
    if roll.strip() == "":
        st.warning("Please enter a roll number.")
    elif roll in STUDENT_DATA:
        url = STUDENT_DATA[roll]
        st.success("Roll number found! 🎉")
        st.markdown(f'<a class="result-link" href="{url}" target="_blank">Click here to view the result</a>', unsafe_allow_html=True)
        # Optional: automatically open in new tab
        st.components.v1.html(f"""<script>window.open('{url}', '_blank')</script>""", height=0)
    else:
        st.error("Roll number not found. 😕")
