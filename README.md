Oracle Database Assistant using Gemini AI

This Python application provides a graphical user interface (GUI) that allows users to interact with an Oracle Database Assistant powered by Google's Gemini AI. It helps with tasks like database management, creating tables, writing SQL queries, and generating reports.

Features
 User-friendly GUI built using Tkinter.
 Integration with Google's Gemini AI for natural language processing.
 Handles database management queries and SQL generation.
 Cleans up the AI's response by removing unnecessary characters and ensuring proper punctuation.
 Displays the AI's response in a scrollable chat area.

Requirements
 Python 3.x
  google-generativeai library
  Tkinter (usually comes pre-installed with Python)
  python-dotenv` (for environment variable management)
An API key from Google Gemini AI

## Installation

1. Install required libraries:
   bash
   pip install google-generativeai python-dotenv
   

2. Set up your Google API key:
    Create a .env file in the project directory with the following content:
     
     GEMINI_API_KEY=your_google_api_key
     

Usage

1. Run the application:
   bash
   python oracle_assistant.py
   

2. Type your Oracle-related queries or commands in the input box and click "Send."
3. The AI will process your input and display the response in the chat window.
4. The response will be cleaned of leading asterisks and will include proper punctuation.

Customization

You can adjust the system instructions in the `generation_config` for specific tasks.
Modify the AI model configuration to change the behavior of the assistant (e.g., temperature, max tokens).



