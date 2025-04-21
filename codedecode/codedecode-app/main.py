import streamlit as st

# Title of the app
st.title("Discord Bot Simulation")

# Input field for user message
user_message = st.text_input("Your Message:")

# Bot response logic
if user_message:
    if "hello" in user_message.lower():
        bot_response = "Bot says: Hello, how can I help you?"
    elif "bye" in user_message.lower():
        bot_response = "Bot says: Goodbye, see you later!"
    else:
        bot_response = "Bot says: I'm not sure what you're saying!"

    # Display the bot's response
    st.write(bot_response)
