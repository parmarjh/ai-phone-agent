import gradio as gr
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def make_api_call(authorization_key, prompt, phone_number):
    logging.info(f"Making API call with prompt: {prompt} and phone number: {phone_number}")

    headers = {
        'Authorization': authorization_key
    }
    
    data = {
        "phone_number": phone_number,
        "from": None,
        "task": prompt,
        "model": "enhanced",
        "language": "eng",
        "voice": "maya",
        "voice_settings": {},
        "local_dialing": False,
        "max_duration": 12,
        "answered_by_enabled": False,
        "wait_for_greeting": False,
        "record": False,
        "amd": False,
        "interruption_threshold": 100,
        "temperature": None,
        "transfer_list": {},
        "metadata": {},
        "pronunciation_guide": [],
        "start_time": None,
        "request_data": {},
        "tools": [],
        "webhook": None
    }
    
    response = requests.post('https://api.bland.ai/v1/calls', json=data, headers=headers)
    logging.info(f"API call response: {response.json()}")
    return response.json()

def analyze_call(authorization_key, call_id, goal, questions, types):
    logging.info(f"Analyzing call with ID: {call_id}")
    
    formatted_questions = format_questions(questions, types)

    url = f"https://api.bland.ai/v1/calls/{call_id}/analyze"
    payload = {
        "goal": goal,
        "questions": formatted_questions
    }
    headers = {
        "Authorization": authorization_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        try:
            response_data = response.json()
            logging.info(f"Call analysis response: {response_data}")
            return response_data
        except ValueError:
            logging.error("Invalid JSON response received.")
            return {"error": "Invalid JSON response received"}
    else:
        logging.error(f"Failed to analyze call: {response.status_code}")
        return {"error": "API call failed", "status_code": response.status_code}

def format_questions(questions, types):
    # Split the input strings into individual questions and types
    question_list = questions.split(';')
    type_list = types.split(';')
    
    # Combine questions and types into a formatted list
    formatted_questions = []
    for question, type in zip(question_list, type_list):
        formatted_questions.append([question.strip(), type.strip()])
    
    return formatted_questions

# Interface for making API calls
make_call_interface = gr.Interface(
    fn=make_api_call,
    inputs=[
        gr.Textbox(label="API Key", placeholder="Enter your API Key, e.g., sk-n ·································································"),
        gr.Textbox(label="Task", lines=4, placeholder="Describe the task for the phone agent"),
        gr.Textbox(label="Phone Number", placeholder="Enter phone number in international format, e.g., +1234567890")
    ],
    outputs="json",
    description="Create your bland.ai account if you don't have one yet through [this link](https://app.bland.ai/signup). After creating your account, you can find your API key under the 'API Key' tab in your dashboard settings [here](https://app.bland.ai/dashboard?page=settings)."
)

# Interface for analyzing calls
analyze_call_interface = gr.Interface(
    fn=analyze_call,
    inputs=[
        gr.Textbox(label="API Key", placeholder="Enter your API Key, e.g., sk-n ·································································"),
        gr.Textbox(label="Call ID", placeholder="Enter the ID of the call to analyze"),
        gr.Textbox(label="Goal", placeholder="Enter the goal of the call analysis", info="This is the overall purpose of the call. Provides context for the analysis to guide how the questions/transcripts are interpreted."),
        gr.Textbox(label="Questions", lines=2, placeholder="Enter questions separated by semicolons, e.g., 'Who answered the call?;Was the customer satisfied?;What was the customer's main concern?'"),
        gr.Textbox(label="Answer Types", lines=2, placeholder="Enter answer types for each question separated by semicolons, e.g., 'human or voicemail;boolean;string'", info="Specify the expected answer type for each question, corresponding to the order of questions. Types include 'string', 'boolean', etc. Unanswerable questions will default to null.")
    ],
    outputs="json",
    description="Analyze the results of your phone calls. Enter questions in one textbox and their corresponding expected answer types in another, separated by semicolons for multiple entries."
)

# Combine interfaces into tabs
demo = gr.TabbedInterface([make_call_interface, analyze_call_interface], ["Make Call", "Analyze Call"])
demo.launch()
