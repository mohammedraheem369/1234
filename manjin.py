import streamlit as st
from groq import Groq
client = Groq(api_key='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')

st.title('Manjin AI') # title 
st.subheader('Created by Huzaifah Altaf')
st.write('---')
st.write('\n'*3)
st.write('Ask me anything')

def main():
    message = st.text_input('Write the Question here')

    lower_message = message.lower()
    if  'your creator' in lower_message or 'huzaifah' in lower_message:
         st.write('Huzaifah Altaf, the creator of Manjin AI (that is me), is a student of Computer Science & Engineering at Guru Nanak Institutions.'
                  '\t You can contact with him on LinkedIn: www.linkedin.com/in/huzaifah-altaf-0874a628b')

    elif message.lower() in ['Manjin ai','MANJIN AI','manjin ai','who are you','who are you?','what is your name','what is your name?']:
         st.write(
            'I am Manjin AI, created by Huzaifah Altaf.'
        )

    elif st.button('Submit'):
        st.write('You asked:', message)

        chat_completions = client.chat.completions.create(
            model="llama3-70b-8192",
            messages = [
                {
                   "role":"user",
                   'content':message

                }

            ],     
        )
        if chat_completions:
            st.write('BOT : '+ chat_completions.choices[0].message.content)
        else:
            st.write('No response from the bot')
if _name_ == '_main_':
    main() 