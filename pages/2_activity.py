import streamlit as st  
  
st.title("🎉 Activity: Create Your First Streamlit App 🎉")  
st.header("Objective")  
st.write("Create a simple Streamlit app that displays a title, header, and some text.")  
  
st.header("Instructions")  
st.write("Follow these steps to create your first Streamlit app:")  
  
# Step 1  
st.subheader("Step 1: Open a New Python Script")  
st.write("Open a new Python script (e.g., `hello_world.py`).")  
  
# Step 2  
st.subheader("Step 2: Write the Following Code")  
st.write("Copy and paste the following code into your script:")  
st.code("""  
import streamlit as st  
  
st.title("Hello World!")  
st.header("This is a header")  
st.write("Welcome to your first Streamlit app.")  
""", language='python')  
  
# Step 3  
st.subheader("Step 3: Run Your App")  
st.write("Save your script and run the app using the command:")  
st.code("streamlit run hello_world.py", language='bash')  
  
# Step 4  
st.subheader("Step 4: Explore and Add Features")  
st.write("Complete the following tasks to enhance your app:")  
st.markdown("""  
- Add a subheader using `st.subheader("This is a subheader")`.  
- Add a text input to accept the user's name and display a greeting using `st.write`.  
- Use the Streamlit documentation to explore and add one more interactive element of your choice. [Streamlit API Reference](https://docs.streamlit.io/develop/api-reference)  
""")  
  
st.write("Here’s an example of how you can add a text input and display a greeting:")  
  
st.code("""  
import streamlit as st  
  
st.title("Hello World!")  
st.header("This is a header")  
st.subheader("This is a subheader")  
  
name = st.text_input("Enter your name")  
st.write(f"Hello, {name}!")  
""", language='python')  
  
st.header("Submitting Your Work")  
st.write("Once you have completed the activity, follow the instructions on the Homework page to submit your work.")  