
import streamlit as st  
from pages.ideas import html_content
  
st.title("Welcome to BSMP Coding Class on Streamlit 🤖")  
st.header("Lesson 1: Hello World")  
  
st.write("""  
Welcome to the first lesson of our coding class! In this lesson, we will cover the basics of Python and Streamlit, and guide you through creating your first Streamlit app.  
  
### Instructions for Running This App in GitHub Codespaces:  
1. **Open GitHub Codespaces**: Navigate to the repository and open it in GitHub Codespaces.  
2. **Run the App**: Start the Streamlit app by running: `streamlit run app.py` 
  
Use the sidebar to navigate to different sections of this lesson.  
""")  


with st.expander("Streamlit references and content",icon="📚",expanded=False):
    st.write("This is the content of the lesson.")
    st.write("It will cover the basics of Streamlit and Python.")
    st.write("By the end, you'll be able to create your first Streamlit app.")
    #video_url = "https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4"  
    #st.video(video_url)  
    #st.write("Watch the video above to learn more about Streamlit!")
    st.write("Streamlit comes in with [a ton of additional powerful elements](https://docs.streamlit.io/develop/api-reference) to spice up your data apps and delight your viewers. Some examples:")  
    st.markdown(html_content, unsafe_allow_html=True)
    st.write("https://docs.streamlit.io/develop/api-reference")
    st.write("Ready to get started? Let's dive in!")