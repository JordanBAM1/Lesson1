## Favorite School Subject

Radio buttons are perfect for situations where you need to make a single choice from a list of options. In this example, we'll use Streamlit's `st.radio` function to let students select their favorite school subject. This approach is not only straightforward but also engaging, allowing for a personalized interaction with the app.

### Example Usage

Here's how you can use `st.radio` in a Streamlit app to ask students about their favorite school subject:

```python
import streamlit as st

st.title('What is Your Favorite School Subject?')

# Define the options
subjects = ['Math', 'Science', 'History', 'English', 'Art', 'Physical Education']

# Use st.radio to render the radio buttons
favorite_subject = st.radio("Choose your favorite subject:", subjects)

# Display the user's choice
st.write(f'Your favorite subject is: {favorite_subject}')
```

This snippet creates a set of radio buttons labeled with common school subjects. When a student selects a subject, the app immediately reflects their choice.

### Visual Example

The radio buttons in the app will look something like this:

![Streamlit Radio Buttons Example](https://global.discourse-cdn.com/business7/uploads/streamlit/optimized/2X/d/d4b57eafb1f4c39ee49e476f011a1012f492ff34_2_690x305.png)

### Video Tutorial

For a hands-on learning experience, check out this video tutorial on using radio buttons in Streamlit:

[![Streamlit Radio Buttons Video Tutorial](https://img.youtube.com/vi/CVHIMGVAzwA/0.jpg)](https://youtu.be/CVHIMGVAzwA?list=TLGGBEGH7F1BsLIyOTA2MjAyNA)

### Further Reading

Dive deeper into customizing and using radio buttons in your Streamlit apps by visiting the official documentation:

[Streamlit Radio Documentation](https://docs.streamlit.io/develop/api-reference/widgets/st.radio)