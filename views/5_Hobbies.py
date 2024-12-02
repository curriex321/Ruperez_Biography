import streamlit as st
from PIL import Image
import json

def load_hobbies():
    try:
        with open("hobbies.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"title": "Playing Guitar", "image": "https://web.facebook.com/messenger_media?attachment_id=7267002772975076816&message_id=7267002777649848265&thread_id=100058582239209g", "caption": "1st Live Gig (2022)"},
            {"title": "Gym🦾", "image": "https://web.facebook.com/messenger_media?attachment_id=1785328672276871&message_id=mid.%24cAABbALRAR-mZl5qkw2TZlIYnmJ_J&thread_id=100058582239209", "caption": "Back day pump🔥"},
            {"title": "Playing Video Games", "images": [
                {"image": "https://web.facebook.com/messenger_media?attachment_id=1590563738515999&message_id=mid.%24cAABbALRAR-mZl5qkw2TZlIYnmJ_J&thread_id=100058582239209", "caption": "Valorant"},
                {"image": "https://web.facebook.com/messenger_media?attachment_id=961211555861122&message_id=mid.%24cAABbALRAR-mZl5qkw2TZlIYnmJ_J&thread_id=100058582239209", "caption": "Mobile Legends"}
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

