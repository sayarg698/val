import streamlit as st
import base64

# Function to encode image to Base64
def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Get Base64 string of the image
image_base64 = get_base64_of_image("image2.jpg")  # Replace with your image filename

# Set page title and layout
st.set_page_config(page_title="Valentine's Day", layout="centered")

# Custom styling with Base64 background image
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{image_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            text-align: center;
        }}
        .heart-text {{
            font-size: 48px;
            color: #ff4b5c;
            font-weight: bold;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        }}
        .button-container {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }}
        .stButton>button {{
            font-size: 28px;
            padding: 15px 40px;
            border-radius: 30px;
            background-color: #ff4b5c;
            color: white;
            border: none;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            transition: transform 0.2s ease-in-out;
        }}
        .stButton>button:hover {{
            transform: scale(1.1);
            background-color: #ff1c3d;
        }}
    </style>
""", unsafe_allow_html=True)

# Display the message
st.markdown("<p class='heart-text'> Will you be my Valentine? PhwarPhwar Kayley❤️</p>", unsafe_allow_html=True)

# Add buttons in a horizontal layout
col1, col2 = st.columns(2)
with col1:
    if st.button("Yes! 💖"):
        st.success("Yay! I am sorry that these days I have been busy and haven't been able to spend every moment with you. But please know that you are always in my heart. I am working hard to become the best version of myself, and I hope to make you proud every single day. Thank you for being patient with me. I love you! 💖🎉")
with col2:
    if st.button("No! 😈"):
        st.markdown("Unlucky! You can't say 'NO' to me, you're already stuck with me! Click 'YES' Please! 😜")
