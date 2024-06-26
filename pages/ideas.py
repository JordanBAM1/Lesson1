import streamlit as st  
  
st.title("Streamlit Examples")  
#https://streamlit.io/gallery?category=favorites
st.write("Welcome to the Streamlit Examples page! Here you'll find a collection of Streamlit apps and code snippets to help you learn more about Streamlit and its capabilities. Feel free to explore the examples below and get inspired to create your own Streamlit apps!")

st.write("For more examples, check out the [Streamlit Gallery](https://streamlit.io/gallery).")

st.write("Streamlit comes in with [a ton of additional powerful elements](https://docs.streamlit.io/develop/api-reference) to spice up your data apps and delight your viewers. Some examples:")  
  
# Add the HTML content  
html_content = """  
<table border="0">  
  <tr>  
    <td>  
      <a target="_blank" href="https://docs.streamlit.io/develop/api-reference/widgets">  
        <img src="https://user-images.githubusercontent.com/7164864/217936099-12c16f8c-7fe4-44b1-889a-1ac9ee6a1b44.png" style="max-height:150px; width:auto; display:block;">  
      </a>  
    </td>  
    <td>  
      <a target="_blank" href="https://docs.streamlit.io/develop/api-reference/data/st.dataframe">  
        <img src="https://user-images.githubusercontent.com/7164864/215110064-5eb4e294-8f30-4933-9563-0275230e52b5.gif" style="max-height:150px; width:auto; display:block;">  
      </a>  
    </td>  
    <td>  
      <a target="_blank" href="https://docs.streamlit.io/develop/api-reference/charts">  
        <img src="https://user-images.githubusercontent.com/7164864/215174472-bca8a0d7-cf4b-4268-9c3b-8c03dad50bcd.gif" style="max-height:150px; width:auto; display:block;">  
      </a>  
    </td>  
    <td>  
      <a target="_blank" href="https://docs.streamlit.io/develop/api-reference/layout">  
        <img src="https://user-images.githubusercontent.com/7164864/217936149-a35c35be-0d96-4c63-8c6a-1c4b52aa8f60.png" style="max-height:150px; width:auto; display:block;">  
      </a>  
    </td>  
    <td>  
      <a target="_blank" href="https://docs.streamlit.io/develop/concepts/multipage-apps">  
        <img src="https://user-images.githubusercontent.com/7164864/215173883-eae0de69-7c1d-4d78-97d0-3bc1ab865e5b.gif" style="max-height:150px; width:auto; display:block;">  
      </a>  
    </td>  
    <td>  
      <a target="_blank" href="https://streamlit.io/gallery">  
        <img src="https://user-images.githubusercontent.com/7164864/215109229-6ae9111f-e5c1-4f0b-b3a2-87a79268ccc9.gif" style="max-height:150px; width:auto; display:block;">  
      </a>  
    </td>  
  </tr>  
  <tr>  
    <td>Input widgets</td>  
    <td>Dataframes</td>  
    <td>Charts</td>  
    <td>Layout</td>  
    <td>Multi-page apps</td>  
    <td>Fun</td>  
  </tr>  
</table>  
"""  
  
st.markdown(html_content, unsafe_allow_html=True)  


st.header("Video Example")
# Add the video  
video_url = "https://s3-us-west-2.amazonaws.com/assets.streamlit.io/videos/hero-video.mp4"  
st.video(video_url)  