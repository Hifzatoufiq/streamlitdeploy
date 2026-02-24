import streamlit as st
from PIL import Image


st.title("chatgpt")


with st.sidebar:
        st.write("this ia sidebar")

st.header("this is a header")
st.subheader("this is a sub header")
st.text("Chhattisgarh is a state located in central India, formed on 1 November 2000 after being separated from Madhya Pradesh. Raipur is its capital city and an important center for trade and education. The state is rich in natural resources, especially coal, iron ore, and bauxite, which contribute significantly to its economy. Chhattisgarh is also known as the “Rice Bowl of India” because of its large production of rice. It has a vibrant tribal culture, colorful festivals, traditional dance forms like Panthi and Raut Nacha, and beautiful natural attractions such as Chitrakote Falls and Kanger Valley National Park. The state plays an important role in India’s steel and power industries and continues to develop in agriculture, education, and infrastructure.")

st.success("this is sucess button")
st.warning("this is a warning")
st.info("this is a info")
st.error("this is a error")


img = Image.open("download.png")
st.image(img, width=800)