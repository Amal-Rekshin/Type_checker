import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyBtXejj5FH0jPY9aQX3OSqeorP22NbmapI")

st.set_page_config(page_title="AI Job Interview Simulation", page_icon="💼")
model =genai.GenerativeModel("gemini-1.5-flash")

st.markdown(
    """
    <style>
    .main {background-color: #f5f5f5;}
    .block-container {padding-top: 2rem;}
    .header {font-size: 2.5rem; color: #fff; font-weight: 600; text-align: center;}
    .question-box {padding: 10px; border-radius: 8px;}
    .response-box {border-radius: 8px;}
    .feedback-box {padding: 10px; border-radius: 8px;}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='header'>AI Job Interview Simulation</div>", unsafe_allow_html=True)
st.write("Prepare for job interviews with AI-powered feedback!")

def generate_question():
    response = model.generate_content("Generate a challenging interview question for a software developer must be upto 10 lines.")
    return  response.text if response else "Unable to generate summary at the moment."


def evaluate_response(response):
    response = model.generate_content(f"Give feedback on this interview for the response the response must be in 2 lines like short and sweat giving opion about the answer: {response}")
    return  response.text if response else "Unable to generate summary at the moment."

if 'question' not in st.session_state:
    st.session_state.question = ""
    
if 'feedback' not in st.session_state:
    st.session_state.feedback = ""
    
if st.button("Start Interview"):
    st.session_state.question = generate_question()
    st.session_state.feedback = ""
    
if st.session_state.question:
    st.markdown("<div class='question-box'><b>Question:</b></div>", unsafe_allow_html=True)
    st.write(st.session_state.question)
    
    st.markdown("<div class='response-box'>Your Response:</div>", unsafe_allow_html=True)
    response = st.text_area("Type your response here...", height=150)

    if st.button("Submit Response"):
        st.session_state.feedback = evaluate_response(response)
        
        st.markdown("<div class='feedback-box'><b>Feedback:</b></div>", unsafe_allow_html=True)
        st.write(st.session_state.feedback)
        
        st.success("Thank you for your response!")
st.markdown("<hr style='border-top: 1px solid #d3d3d3;'>", unsafe_allow_html=True)