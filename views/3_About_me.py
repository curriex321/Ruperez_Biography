import os
import streamlit as st
from PIL import Image
import json

def load_data():
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {
            "personal_info": {
                "name": "Lorenz Pio Gara Chua",
                "sex": "Male",  
                "birthday": "September 4, 2005",
                "birth_place": "Caraga Regional Hospital",
                "address": "San Isidro, Gigaquit, Surigao del Norte",
            },
            "family": [
                {
                    "relation": "Father",
                    "name": "Joel Pingal Chua",
                    "sex": "Male",  
                    "birthday": "January 26, 1962",
                    "age": 62,
                    "nationality": "Filipino",
                    "education": "College Graduate",
                    "occupation": "Registered Master Electrician",
                },
                {
                    "relation": "Mother",
                    "name": "Rosemarie Gara Chua",
                    "sex": "Female", 
                    "birthday": "January 30, 1976",
                    "age": 48,
                    "nationality": "Filipino",
                    "education": "College Undergraduate",
                    "occupation": "Housewife",
                },
                {
                    "relation": "Sibling",
                    "name": "Joerie Mayle Gara Chua",
                    "sex": "Male",  
                    "birthday": "May 11, 1999",
                    "age": 25,
                    "nationality": "Filipino",
                    "education": "College Graduate",
                    "occupation": "GIS Operator",
                },
            ],
        }
    if "sex" not in data["personal_info"]:
        data["personal_info"]["sex"] = "Male"  

    for member in data["family"]:
        if "sex" not in member:
            member["sex"] = "Male"  

    return data


def save_data(data):
    with open("data.json", "w") as f:
        json.dump(data, f)

data = load_data()

st.title("About Me")

st.subheader("Profile Picture")
uploaded_file = st.file_uploader("Upload Profile Picture", type=["png", "jpg", "jpeg"])

profile_picture_path = "profile_picture.png"  

if uploaded_file:
    with open(profile_picture_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Profile picture updated!")

if os.path.exists(profile_picture_path):
    st.image(profile_picture_path, caption="Profile Picture", width=200)
    
    if st.button("Delete Profile Picture"):
        os.remove(profile_picture_path)
        st.success("Profile picture deleted!")
        st.rerun()  
else:
    st.image("https://via.placeholder.com/200", caption="Default Profile Picture", width=200)

st.write("---")

st.subheader("Personal Information")
personal_info = data["personal_info"]
if st.checkbox("Edit Personal Information"):
    name = st.text_input("Name", personal_info["name"])
    sex = st.selectbox("Sex", ["Male", "Female"], index=0 if personal_info["sex"] == "Male" else 1)
    birthday = st.text_input("Birthday", personal_info["birthday"])
    birth_place = st.text_input("Birth Place", personal_info["birth_place"])
    address = st.text_input("Address", personal_info["address"])

    if st.button("Save Personal Information"):
        data["personal_info"] = {
            "name": name,
            "sex": sex,
            "birthday": birthday,
            "birth_place": birth_place,
            "address": address,
        }
        save_data(data)
        st.success("Personal information updated!")
else:
    st.write(
        f"""
        **Name:** {personal_info['name']}  
        **Sex:** {personal_info['sex']}  
        **Birthday:** {personal_info['birthday']}  
        **Birth Place:** {personal_info['birth_place']}  
        **Address:** {personal_info['address']}  
        """
    )

st.write("---")
st.subheader("Family Background")
family = data["family"]

for i, member in enumerate(family):
    with st.expander(f"{member['relation']}: {member['name']}"):
        if st.checkbox(f"Edit {member['relation']}", key=f"edit_{i}"):
            relation = st.text_input("Relation", member["relation"], key=f"relation_{i}")
            name = st.text_input("Name", member["name"], key=f"name_{i}")
            sex = st.selectbox("Sex", ["Male", "Female"], index=0 if member["sex"] == "Male" else 1, key=f"sex_{i}")
            birthday = st.text_input("Birthday", member["birthday"], key=f"birthday_{i}")
            age = st.number_input("Age", value=member["age"], key=f"age_{i}")
            nationality = st.text_input("Nationality", member["nationality"], key=f"nationality_{i}")
            education = st.text_input("Educational Attainment", member["education"], key=f"education_{i}")
            occupation = st.text_input("Occupation", member["occupation"], key=f"occupation_{i}")

            if st.button(f"Save {member['relation']}", key=f"save_{i}"):
                family[i] = {
                    "relation": relation,
                    "name": name,
                    "sex": sex,
                    "birthday": birthday,
                    "age": age,
                    "nationality": nationality,
                    "education": education,
                    "occupation": occupation,
                }
                data["family"] = family
                save_data(data)
                st.success(f"{relation} information updated!")
                st.rerun()

        if st.button(f"Delete {member['relation']}", key=f"delete_{i}"):
            family.pop(i)
            data["family"] = family
            save_data(data)
            st.success(f"{member['relation']} deleted!") 
            st.rerun()
        else:
            st.write(
                f"""
                **Relation:** {member['relation']}  
                **Name:** {member['name']}  
                **Sex:** {member['sex']}  
                **Birthday:** {member['birthday']}  
                **Age:** {member['age']}  
                **Nationality:** {member['nationality']}  
                **Educational Attainment:** {member['education']}  
                **Occupation:** {member['occupation']}  
                """
            )

st.write("---")
st.subheader("Add a New Family Member")
if st.checkbox("Add Family Member"):
    relation = st.text_input("Relation", key="new_relation")
    name = st.text_input("Name", key="new_name")
    sex = st.selectbox("Sex", ["Male", "Female"], key="new_sex")
    birthday = st.text_input("Birthday", key="new_birthday")
    age = st.number_input("Age", key="new_age")
    nationality = st.text_input("Nationality", key="new_nationality")
    education = st.text_input("Educational Attainment", key="new_education")
    occupation = st.text_input("Occupation", key="new_occupation")

    if st.button("Add Member"):
        new_member = {
            "relation": relation,
            "name": name,
            "sex": sex,
            "birthday": birthday,
            "age": age,
            "nationality": nationality,
            "education": education,
            "occupation": occupation,
        }
        family.append(new_member)
        data["family"] = family
        save_data(data)
        st.success(f"{relation} added!") 
        st.rerun()
