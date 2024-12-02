import streamlit as st
from PIL import Image
import json

def load_hobbies():
    try:
        with open("hobbies.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"title": "Karate", "image": "https://www.facebook.com/ad448f17-19e2-437a-b693-86af5219d033", "caption": "Karate kidss"},
            {"title": "Gym🦾", "image": "https://www.facebook.com/cf40a6aa-b407-4723-bd5b-7b75f383423d", "caption": "Gym with the homies🔥"},
            {"title": "Playing Video Games", "images": [
                {"image": "https://web.facebook.com/messenger_media?attachment_id=1590563738515999&message_id=mid.%24cAABbALRAR-mZl5qkw2TZlIYnmJ_J&thread_id=100058582239209", "caption": "Valorant"},
                {"image": "https://www.facebook.com/2a262e7f-7028-4e42-912b-02cabc3b9fd1", "caption": "Minecraft"}
            ]}
        ]

def save_hobbies(hobbies):
    with open("hobbies.json", "w") as file:
        json.dump(hobbies, file)

hobbies = load_hobbies()

st.title("My Hobbies")
with st.container():
    st.write("---")
    
    for idx, hobby in enumerate(hobbies):
        if isinstance(hobby.get("images"), list): 
            st.subheader(hobby["title"])
            for image in hobby["images"]:
                img = Image.open(image["image"])
                st.image(img, caption=image["caption"], width=200)
        else: 
            st.subheader(hobby["title"])
            img = Image.open(hobby["image"])
            st.image(img, caption=hobby["caption"], width=400)

        if st.checkbox(f"Edit '{hobby['title']}'", key=f"edit_{idx}"):
            title = st.text_input("Hobby Title", value=hobby["title"])
            if isinstance(hobby.get("images"), list):
                for img_idx, img_data in enumerate(hobby["images"]):
                    img_data["image"] = st.text_input(f"Image Path {img_idx+1}", value=img_data["image"])
                    img_data["caption"] = st.text_input(f"Caption {img_idx+1}", value=img_data["caption"])
            else:
                hobby["image"] = st.text_input("Image Path", value=hobby["image"])
                hobby["caption"] = st.text_input("Caption", value=hobby["caption"])

            if st.button(f"Save '{hobby['title']}'", key=f"save_{idx}"):
                hobby["title"] = title
                hobbies[idx] = hobby
                save_hobbies(hobbies)
                st.success("Hobby updated!")
                st.experimental_rerun()

        if st.button(f"Delete '{hobby['title']}'", key=f"delete_{idx}"):
            hobbies.pop(idx)
            save_hobbies(hobbies)
            st.success("Hobby deleted!")
            st.rerun()

    st.write("---")
    st.subheader("Add a New Hobby")
    title = st.text_input("New Hobby Title", key="new_title")
    image = st.text_input("Image Path", key="new_image")
    caption = st.text_input("Caption", key="new_caption")

    if st.button("Add Hobby"):
        new_hobby = {"title": title, "image": image, "caption": caption}
        hobbies.append(new_hobby)
        save_hobbies(hobbies)
        st.success("New hobby added!")
        st.rerun()

