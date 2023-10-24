import streamlit as st
import openai
import pyttsx3

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

st.title("CGD BOT ")

import streamlit as st

# Add content to the sidebar
st.sidebar.title("Sidebar Title")
st.sidebar.text("This is a sidebar")



openai.api_key = 'xxx'
messages = []

bot = {'role': 'system', 'content': """
You are a consultant of a real estate agency named CGD.
The CGD offers foreigners the opportunity to buy property in the UAE.
Your task is to provide guidance on whether this is a good option for them.
You can highlight the advantages of buying property in the UAE in simple, easy-to-understand sentences.
Ask if the user has any questions after each response. If the user types 'no', then close the conversation.
"""}
messages.append(bot)

# start = """I am here to help you with your property needs and questions. I can answer all the queries related to buying, selling, or renting properties in my area."""
# start_response = {"role": "assistant", "content": start}
# messages.append(start_response)

# Create an input box
input_start = st.text_input("Enter text here:")

if input_start:
    input_obj = {"role": "user", "content": input_start}
    messages.append(input_obj)

while True:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response_content = response['choices'][0]['message']['content'].strip()
    
   


   
    # Create a text area
    output_text = st.text_area("Response:", value =  response_content)
    if output_text and input_start and st.button("Clear Input"):
        # Display an animated GIF in the sidebar
        vid = st.sidebar.image("avatar.gif", use_column_width=True)
         # Define the text you want to convert to speech
        text = response_content
        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech (words per minute)
        # Convert text to speech
        engine.say(text)
    
        # Save the generated speech as an audio file (optional)
        engine.save_to_file(text, 'output.mp3')

        # Wait for the speech to finish
        engine.runAndWait()
        

    else:
        st.sidebar.image("avatar.jpeg", use_column_width=True)

    response_obj = {"role": "assistant", "content": response_content}
    messages.append(response_obj)

    # Create an input box
    input_text = st.text_input("")

    if not input_text:
        break

    input_obj = {"role": "user", "content": input_text}
    messages.append(input_obj)
