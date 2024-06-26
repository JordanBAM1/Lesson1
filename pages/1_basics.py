import streamlit as st  

with st.expander("Introduction to Python and Streamlit",icon="🔥",expanded=False):
  st.title("Introduction to Python and Streamlit")  
    
  st.header("What is Python?")  
  st.write("""  
  - Python is a high-level, interpreted programming language known for its ease of use and readability.  
  - It is widely used in web development, data analysis, artificial intelligence, scientific computing, and more.  
  """)  
    
  st.header("What is Streamlit?")  
  st.write("""  
  - Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science.  
  - Streamlit apps are Python scripts that run in a web browser.  
  """)  
    
  st.header("Getting Started with Streamlit")  
  st.write("""  
  1. **Basic Streamlit Commands:**  
      - `st.title("Title")` - Adds a title to your app.  
      - `st.header("Header")` - Adds a header.  
      - `st.write("Text")` - Writes text to the app.  
  2. **Adding Images:**
      - `st.image(image_path, caption="Caption")` - Adds an image to the app.

  3. **Interactive Elements:**
      - `st.text_input("Label")` - Adds a text input box.
      - `st.button("Button")` - Adds a button.
      - `st.selectbox("Label", options)` - Adds a select box.
      - `st.slider("Label", min_value, max_value, value)` - Adds a slider.
      - `st.checkbox("Label")` - Adds a checkbox.
      - `st.radio("Label", options)` - Adds a radio button.
      - `st.file_uploader("Label", type="file_type")` - Adds a file uploader.
  4. **Layouts:**
      - `st.columns(num_columns)` - Creates a layout with the specified number of columns.
      - `st.sidebar` - Adds a sidebar to the app.
      - `st.expander("Label")` - Adds an expander to the app.
          
  """)  
  
#st.header("Interactive Element")  
#st.write("Below is an example of an interactive element in Streamlit.")  
#name = st.text_input("Enter your name")  
#st.write(f"Hello, {name}!")  


# place holder on adding imaegs

# place holder on adding interactive elements


# place holder for adding columns