import streamlit as st
import datetime

# ---- Page Configuration ----
st.set_page_config(page_title="Bartley's Biography", page_icon="📘", layout="wide")

# ---- Apply Custom CSS for Styling ----
st.markdown(
    """
    <style>
        body {
            background-color: #1E1E2F;
            color: #EDEDED;
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #FFD700;
            font-size: 40px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        .subheader {
            color: #FFD700;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .section {
            background: #2A2A3B;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.3);
        }
        hr {
            border: 0;
            border-top: 1px solid #444;
            margin: 20px 0;
        }
        .stButton>button {
            background-color: #FFD700;
            color: black;
            border: none;
            border-radius: 5px;
            font-weight: bold;
            padding: 10px 20px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #E5C100;
        }
        footer {
            text-align: center;
            color: #A9A9A9;
            font-size: 14px;
            margin-top: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Header Section ----
st.markdown('<div class="title">Bartley\'s Biography</div>', unsafe_allow_html=True)

# ---- Initialize Session State ----
if 'bio_data' not in st.session_state:
    st.session_state['bio_data'] = {
        'name': "Enter your name",
        'age': "19",
        'gender': "Male",
        'mother': "Enter mother's name",
        'mother_bday': datetime.date(1970, 1, 1),
        'father': "Enter father's name",
        'guardian': "Enter guardian's name",
        'high_school': "Crossing Bayabas National High School",
        'senior_high_school': "Crossing Bayabas National High School",
        'college': "Surigao del Norte State University",
        'profile_picture': None,
        'achievements': [
            {"Year": "2020", "Achievement": "Graduated with honors from high school"},
            {"Year": "2022", "Achievement": "Top 10 in senior high school class"},
            {"Year": "2023", "Achievement": "Best Student in Research Awardee"}
        ]
    }

# ---- Editable Form ----
with st.form("edit_bio_form"):
    st.markdown('<div class="subheader">Personal Information</div>', unsafe_allow_html=True)
    with st.container():
        st.session_state['bio_data']['name'] = st.text_input("Full Name", st.session_state['bio_data']['name'])
        st.session_state['bio_data']['age'] = st.selectbox("Age", [str(i) for i in range(18, 101)], index=int(st.session_state['bio_data']['age']) - 18)
        st.session_state['bio_data']['gender'] = st.radio("Gender", ["Male", "Female"], index=["Male", "Female"].index(st.session_state['bio_data']['gender']))

    st.markdown('<div class="subheader">Family Background</div>', unsafe_allow_html=True)
    with st.container():
        st.session_state['bio_data']['mother'] = st.text_input("Mother's Name", st.session_state['bio_data']['mother'])
        st.session_state['bio_data']['mother_bday'] = st.date_input("Mother's Birthday", st.session_state['bio_data']['mother_bday'])
        st.session_state['bio_data']['father'] = st.text_input("Father's Name", st.session_state['bio_data']['father'])
        st.session_state['bio_data']['guardian'] = st.text_input("Guardian's Name", st.session_state['bio_data']['guardian'])

    st.markdown('<div class="subheader">Educational Attainment</div>', unsafe_allow_html=True)
    with st.container():
        st.session_state['bio_data']['high_school'] = st.text_input("High School", st.session_state['bio_data']['high_school'])
        st.session_state['bio_data']['senior_high_school'] = st.text_input("Senior High School", st.session_state['bio_data']['senior_high_school'])
        st.session_state['bio_data']['college'] = st.text_input("College", st.session_state['bio_data']['college'])

    st.markdown('<div class="subheader">Profile Picture</div>', unsafe_allow_html=True)
    with st.container():
        uploaded_image = st.file_uploader("Upload Your Photo", type=["jpg", "png", "jpeg"])
        if uploaded_image:
            st.session_state['bio_data']['profile_picture'] = uploaded_image

    # Submit Button
    submitted = st.form_submit_button("Save Changes")

# ---- Display Biography ----
if submitted:
    st.success("Biography updated successfully!")

st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<div class="subheader">📄 Your Biography</div>', unsafe_allow_html=True)
with st.container():
    st.write(f"**Name:** {st.session_state['bio_data']['name']}")
    st.write(f"**Age:** {st.session_state['bio_data']['age']}")
    st.write(f"**Gender:** {st.session_state['bio_data']['gender']}")
    st.write(f"**Mother's Name:** {st.session_state['bio_data']['mother']} (Born: {st.session_state['bio_data']['mother_bday']})")
    st.write(f"**Father's Name:** {st.session_state['bio_data']['father']}")
    st.write(f"**Guardian's Name:** {st.session_state['bio_data']['guardian']}")
    st.write(f"**High School:** {st.session_state['bio_data']['high_school']}")
    st.write(f"**Senior High School:** {st.session_state['bio_data']['senior_high_school']}")
    st.write(f"**College:** {st.session_state['bio_data']['college']}")

    if st.session_state['bio_data']['profile_picture']:
        st.image(st.session_state['bio_data']['profile_picture'], caption="Your Profile Picture", use_column_width=True)

# ---- Display Achievements Table ----
st.markdown('<div class="subheader">🏆 Achievements</div>', unsafe_allow_html=True)
achievements = st.session_state['bio_data']['achievements']
st.table(achievements)

# ---- Display Social Media Tabs ----
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<div class="subheader">🌐 Social Media</div>', unsafe_allow_html=True)
with st.container():
    st.markdown("[Facebook](https://facebook.com) | [LinkedIn](https://linkedin.com) | [Upwork](https://upwork.com)", unsafe_allow_html=True)

st.markdown('<footer>Created with 💻 using Streamlit</footer>', unsafe_allow_html=True)
