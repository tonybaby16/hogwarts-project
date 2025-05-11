import streamlit as st
import base64

# Set background image
def set_bg_img(main_bg):
    main_bg_ext = "png"
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
set_bg_img("BACKGROUND.png")

# Title and subtitles
st.title("Find your Hogwarts House!!!")
st.image("HAT.png")
st.write("In this test, you will be able to find your Hogwarts House!")
st.write("Hope you have fun!")

# Radio for liked_colour
liked_colour = st.radio(
    "Choose a colour combo.",
    ["Yellow and black", "Green and silver", "Blue and bronze", "Red and gold"],
    index=None)

# Score for liked_colour
if liked_colour == "Yellow and black":
    score_colour = 25  # Hufflepuff
elif liked_colour == "Green and silver":
    score_colour = 35  # Slytherin
elif liked_colour == "Blue and bronze":
    score_colour = 15  # Ravenclaw
elif liked_colour == "Red and gold":
    score_colour = 10  # Gryffindor

# Radio for liked_animal
liked_animal = st.radio(
    "Pick an animal",
    ["Snake", "Lion", "Eagle", "Badger"],
    index=None)

# Score for liked_animal
if liked_animal == "Snake":
    score_animal = 35  # Slytherin
elif liked_animal == "Lion":
    score_animal = 10  # Gryffindor
elif liked_animal == "Eagle":
    score_animal = 20  # Ravenclaw
elif liked_animal == "Badger":
    score_animal = 25  # Hufflepuff

# Radio for liked_element
liked_element = st.radio(
    "Choose an element.",
    ["Air", "Water", "Earth", "Fire"],
    index=None)

# Score for liked_element
if liked_element == "Air":
    score_element = 20  # Ravenclaw
elif liked_element == "Water":
    score_element = 25  # Hufflepuff
elif liked_element == "Earth":
    score_element = 35  # Slytherin
elif liked_element == "Fire":
    score_element = 10  # Gryffindor

# Radio for liked_personality
liked_personality = st.radio(
    "Which sounds most like you?",
    ["Ambitious, resourceful", "Intelligent, dreamy", "Hardworking, loyal", "Brave, determined"],
    index=None)

# Score for liked_personality
if liked_personality == "Ambitious, resourceful":
    score_personality = 35  # Slytherin
elif liked_personality == "Intelligent, dreamy":
    score_personality = 20  # Ravenclaw
elif liked_personality == "Hardworking, loyal":
    score_personality = 25  # Hufflepuff
elif liked_personality == "Brave, determined":
    score_personality = 10  # Gryffindor

button_disabled = True

if liked_element and liked_animal and liked_colour and liked_personality != None:
    button_disabled = False
    score_total = score_personality + score_animal + score_colour + score_element

# Process and display House
if not button_disabled:
    if st.button("Find your House", type="primary", disabled = button_disabled):
        if score_total <= 60:
            st.title("You are in..... GRYFFINDOR!!!!!")
            st.image("GRYFFINDOR_CREST.png")
        elif score_total <= 85:
            st.title("You are in..... RAVENCLAW!!!!!")
            st.image("RAVENCLAW_CREST.png")
        elif score_total <= 110:
            st.title("You are in..... HUFFLEPUFF!!!!!")
            st.image("HUFFLEPUFF_CREST.png")
        else:
            st.title("You are in..... SLYTHERIN!!!!!")
            st.image("SLYTHERIN_CREST.png")
        st.balloons()
