from openai import OpenAI
import streamlit as st


#Read the api key and setup an openai client
f = open("keys\.openai_api_key.txt")
key = f.read()
client = OpenAI(api_key = key)

st.title("💬 Python Code Reviewer")

#Take user input
prompt = st.text_area("Enter your python code ✍")
#prompt = st.text_input("Enter your python code")

#Generate User Response
if st.button("Review") == True:
    response = client.chat.completions.create(
                model = "gpt-3.5-turbo",
                messages = [
                    {
                        "role": "system", "content": """You are a helpful AI Assistant.
                                                        Review the Python code and identify potential bugs, errors, or areas of improvement."""
                    },

                    {"role": "user", "content": prompt}


                    ]
    )
    #Print the response
    st.write(response.choices[0].message.content)