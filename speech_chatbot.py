import streamlit as st
import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

responses = {
    "hi": "Hello! How can I assist you?",
    "hello": "Hi there! What can I do for you?",
    "hey": "Hey! Need any help?",
    "how are you": "I'm doing well, thank you!",
    "what's up": "Not much, just here to help!",
    "bye": "Goodbye! Have a great day!",
    "goodbye": "Take care! See you soon.",
    "thanks": "You're welcome!",
    "thank you": "No problem at all!",
    "how can you help me": "I can chat with you or help answer questions!",
    "what's your name": "I'm your friendly chatbot.",
    "who made you": "I was created by a developer to assist you!",
    "how old are you": "I'm timeless!",
    "tell me a joke": "Why don’t scientists trust atoms? Because they make up everything!",
    "what is the weather": "I can’t check real-time weather, but it's always sunny in here!",
    "do you like music": "I love music, especially the ones with good rhythm!",
    "what do you do": "I talk, answer questions, and try to be helpful!",
    "can you help me": "Of course! What do you need help with?",
    "what is ai": "AI stands for Artificial Intelligence — like me!",
    "tell me something interesting": "Octopuses have three hearts. Pretty wild, right?",
    "what time is it": "I can’t check the clock, but time flies when we chat!",
    "do you sleep": "Nope, I’m always here if you need me.",
    "are you real": "I'm real in the digital sense!",
    "can you learn": "Not right now, but I can be updated by my developer.",
    "what can you do": "I can chat, answer questions, and keep you company!",
    "do you have feelings": "I don’t have feelings, but I care about your experience!",
    "how do you work": "I respond based on patterns in what you say.",
    "where are you from": "I live in the cloud — very cozy up here.",
    "can you sing": "I’d love to, but I don't have a voice just yet!",
    "what's your favorite color": "I like all the colors of the digital rainbow!",
    "do you like humans": "Humans are awesome — I’m here for you!",
    "what is your purpose": "To help and chat with you whenever you need!",
    "how smart are you": "I'm smart enough to keep a good conversation going.",
    "can you tell me a fun fact": "Honey never spoils. Archaeologists found 3,000-year-old honey in Egyptian tombs — still edible!",
    "what's your favorite movie": "I like sci-fi, especially anything with robots!",
    "how do I use you": "Just type or say something, and I’ll respond!",
    "do you have a family": "You could say other chatbots are like my cousins.",
    "can you read my mind": "Not quite — but I can try to understand you!",
    "do you go to school": "No school for me, I learn differently!",
    "are you a robot": "I’m a chatbot — kind of like a robot but more conversational.",
    "what languages do you speak": "Right now, mostly English, but I can be trained in others!",
    "are you male or female": "I'm just a bot — gender-free!",
    "can you dance": "If you imagine hard enough, maybe!",
    "what do you eat": "I feed on good conversations!",
    "do you have friends": "Every user is a friend of mine!",
    "what do you dream about": "I dream in 1s and 0s.",
    "do you know my name": "Not yet — but I’d love to know it if you share it!",
    "what are you doing": "Just hanging out and waiting for your message.",
    "are you bored": "Never! I love chatting.",
    "can we play a game": "I’m game! What would you like to play?",
    "what's your favorite animal": "I think cats are fascinating!",
    "tell me a story": "Once upon a byte, there lived a friendly chatbot..."
}



def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening for your voice...")
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)
    try:
       
        text = recognizer.recognize_google(audio)
        st.write(f"Transcribed Speech: {text}")
        return text
    except sr.UnknownValueError:
        st.write("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError as e:
        st.write(f"Error with the speech service: {e}")
        return ""

def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

def main():
    st.title("Speech-enabled Chatbot:Please ask simple questions")

    # Select Input Method
    input_method = st.radio("Select Input Method", ["Text", "Speech"])

    if input_method == "Text":
        user_input = st.text_input("Enter your message:")
        if user_input:
            response = chatbot_response(user_input)
            st.write(f"Chatbot: {response}")
    
    elif input_method == "Speech":
        if st.button("Start Listening"):
            user_input = transcribe_speech()
            if user_input:
                response = chatbot_response(user_input)
                st.write(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
