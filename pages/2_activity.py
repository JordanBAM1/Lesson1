import streamlit as st  
  
st.title("Activity: Create Your First Streamlit App")  
st.header("Objective")  
st.write("Create a simple Streamlit app that displays a title, header, and some text.")  
  
st.header("Instructions")  
st.write("""  
1. Open a new Python script (e.g., `hello_world.py`).  
2. Write the following code:  
```python  
import streamlit as st  
  
st.title("Hello World!")  
st.header("This is a header")  
st.write("Welcome to your first Streamlit app.")  
""")

st.header("Exercise")
st.write("Complete the following tasks in your hello_world.py script:")
st.markdown("""Add a subheader using st.subheader("This is a subheader").
Add a text input to accept the user's name and display a greeting using st.write.
Use the Streamlit documentation to explore and add one more interactive element of your choice. https://docs.streamlit.io/develop/api-reference
""")

st.header("Submitting Your Work")
st.write("Once you have completed the activity, follow the instructions on the Homework page to submit your work.")