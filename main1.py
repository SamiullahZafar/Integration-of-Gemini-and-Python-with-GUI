import tkinter as tk
from tkinter import scrolledtext
import os
import google.generativeai as genai
import re  # Import for text cleaning

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction="I need assistance in creating and managing a database in Oracle, including designing tables, writing SQL queries, and managing data. I will also provide access to my Oracle system for building reports and forms. I will specify the type of reports and forms I want, and the system will guide me through creating them or generate them based on my instructions. This instruction clearly conveys your expectations for help with both database management and the development of forms and reports. Let me know if you want to customize it further",
)

chat_session = model.start_chat(history=[])

# Function to clean bot response
def clean_response(text):
    # Remove * only if it is at the start of a line
    text = re.sub(r"^\*+", "", text, flags=re.MULTILINE)
    # Add periods to the end of lines if they are missing, without altering spaces
    text = re.sub(r"([a-zA-Z0-9])(\n)", r"\1.\n", text)  # Add period before newlines if missing
    text = text.strip()  # Remove leading/trailing whitespace
    return text

# Function to handle user input and display responses
def send_message():
    user_message = input_box.get("1.0", tk.END).strip()
    if not user_message:
        return

    # Display user message in the chat area
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"You: {user_message}\n")
    chat_area.config(state=tk.DISABLED)

    input_box.delete("1.0", tk.END)

    # Generate bot response
    try:
        response = chat_session.send_message(user_message)
        bot_response = clean_response(response.text)
    except Exception as e:
        bot_response = f"Error: {str(e)}"

    # Display bot response in the chat area
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)  # Scroll to the bottom

# Initialize the GUI
root = tk.Tk()
root.title("Oracle Database Assistant")

# Chat display area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=20, width=70)
chat_area.pack(pady=10)

# Input box
input_box = tk.Text(root, height=6, width=70)
input_box.pack(pady=5)

# Send button
send_button = tk.Button(root, text="Send", command=send_message, width=10)
send_button.pack()

# Run the GUI loop
root.mainloop()
