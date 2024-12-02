import streamlit as st
import json

def load_data():
    try:
        with open("education_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "education": [
                {
                    "level": "Elementary",
                    "details": "Graduated at St. Paul University Surigao Elementary Department",
                },
                {
                    "level": "High School",
                    "details": "Graduated at St. Paul University Surigao High school Department",
                },
                {
                    "level": "University",
                    "details": "Currently studying at Surigao del Norte State University\nBachelor of Science in Computer Engineering",
                },
            ],
            "achievements": [
            ],
        }


def save_data(data):
    with open("education_data.json", "w") as f:
        json.dump(data, f)


data = load_data()

st.title("My Educational Attainment")

st.write("---")
st.subheader("Educational Attainment")

education = data["education"]

for i, entry in enumerate(education):
    with st.expander(f"{entry['level']}"):
        if st.checkbox(f"Edit {entry['level']}", key=f"edit_edu_{i}"):
            level = st.text_input("Education Level", entry["level"], key=f"level_{i}")
            details = st.text_area("Details", entry["details"], key=f"details_{i}")

            if st.button(f"Save {entry['level']}", key=f"save_edu_{i}"):
                education[i] = {"level": level, "details": details}
                data["education"] = education
                save_data(data)
                st.success(f"{level} updated!")
                st.rerun()

        if st.button(f"Delete {entry['level']}", key=f"delete_edu_{i}"):
            education.pop(i)
            data["education"] = education
            save_data(data)
            st.success(f"{entry['level']} deleted!")  
            st.rerun()
        else:
            st.write(entry["details"])

st.write("---")
st.subheader("Add Educational Attainment")
if st.checkbox("Add New Education Level"):
    level = st.text_input("Education Level", key="new_level")
    details = st.text_area("Details", key="new_details")

    if st.button("Add Education"):
        new_entry = {"level": level, "details": details}
        education.append(new_entry)
        data["education"] = education
        save_data(data)
        st.success(f"{level} added!")
        st.rerun()

st.write("---")
st.subheader("Achievements")

achievements = data["achievements"]

for i, achievement in enumerate(achievements):
    with st.expander(f"Achievement {i + 1}: {achievement}"):
        if st.checkbox(f"Edit Achievement {i + 1}", key=f"edit_ach_{i}"):
            updated_achievement = st.text_area("Achievement", achievement, key=f"achievement_{i}")

            if st.button(f"Save Achievement {i + 1}", key=f"save_ach_{i}"):
                achievements[i] = updated_achievement
                data["achievements"] = achievements
                save_data(data)
                st.success("Achievement updated!")
                st.rerun()

        if st.button(f"Delete Achievement {i + 1}", key=f"delete_ach_{i}"):
            achievements.pop(i)
            data["achievements"] = achievements
            save_data(data)
            st.success("Achievement deleted!")
            st.rerun()
        else:
            st.write(achievement)

st.write("---")
st.subheader("Add Achievement")
if st.checkbox("Add New Achievement"):
    new_achievement = st.text_area("Achievement", key="new_achievement")

    if st.button("Add Achievement"):
        achievements.append(new_achievement)
        data["achievements"] = achievements
        save_data(data)
        st.success("Achievement added!")
        st.rerun()
