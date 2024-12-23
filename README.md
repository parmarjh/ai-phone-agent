---
title: AIPhoneAgent
emoji: 🦀
colorFrom: purple
colorTo: green
sdk: gradio
sdk_version: 4.31.3
app_file: app.py
pinned: false
---

# AIPhoneAgent

AIPhoneAgent is a Gradio-based application that allows users to make API calls to `bland.ai` for phone-based tasks using a specified model. The application is designed to send tasks to a phone number provided by the user, with various customizable parameters.

## Features
- Make API calls with customizable task prompts to any internation phone number.
- Logging of API call details and responses.

## Requirements
Ensure you have the following dependencies installed:
- `gradio`
- `requests`
- Python's built-in `logging` module (no need to install separately).

You can install the necessary packages using:
```bash
pip install gradio requests
```

## Usage
1. **Set up your environment**: Make sure Python is installed along with the required packages (`gradio` and `requests`).
2. **Get your API Key**: Create an account at [bland.ai](https://app.bland.ai/signup) and obtain your API key from the dashboard settings under the 'API Key' tab.
3. **Run the application**: Navigate to the project directory and run the following command:
   ```bash
   python app.py
   ```
   This will launch a Gradio interface where you can input your API key, the task description, and the phone number to which the call should be made.

4. **Interact with the interface**: Enter the required details in the Gradio web interface and submit to make the API call.

## Deployment
This application can instantly run locally. For web deployment, consider using platforms like Heroku, AWS, or Google Cloud to host the application. Currently it is deployed under Hugging Face Spaces with Free setup. https://huggingface.co/spaces/skyvera/AIPhoneAgent
Details on Hugging Face Deployment: https://www.gradio.app/guides/using-hugging-face-integrations#hosting-your-gradio-demos-on-spaces

## Configuration Reference
For more details on configuration, visit the [Hugging Face Spaces configuration reference](https://huggingface.co/docs/hub/spaces-config-reference).
