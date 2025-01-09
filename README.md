Generative AI Chatbot with Tkinter
This project is a desktop application built with Python and tkinter, designed as an interactive chatbot using Google's Generative AI (Gemini-2.0). The chatbot provides intelligent and context-aware responses, making it a useful tool for conversational AI experiments.
Features
•	Interactive GUI: A simple and user-friendly chat interface built with tkinter.
•	Google Generative AI Integration: Uses the Gemini-2.0 model for high-quality, context-aware responses.
•	Text Cleaning: Ensures well-formatted bot responses with proper punctuation.
•	Scrollable Chat Area: Keeps the conversation history accessible.
•	Error Handling: Gracefully handles exceptions during AI response generation.
Installation
Prerequisites
1.	Python 3.7 or later.
2.	A Google Generative AI API key, set in your environment as GEMINI_API_KEY.
3.	Required Python libraries: 
o	tkinter (pre-installed with Python on most platforms)
o	google-generativeai
o	re
Setup
1.	Clone the repository:
2.	git clone https://github.com/SamiullahZafar/Integration-of-Gemini-and-Python-with-GUI.git
3.	cd generative-ai-chatbot
4.	Install the required dependencies:
5.	pip install google-generativeai
6.	Set up the GEMINI_API_KEY environment variable:
7.	export GEMINI_API_KEY=your_api_key
8.	Run the application:
9.	python main1.py
Usage
1.	Launch the application.
2.	Type your query into the input box and click the Send button.
3.	The bot will generate a response using Google's Generative AI and display it in the chat area.
4.	Scroll through the chat area to review previous messages.
Code Highlights
•	Google Generative AI Configuration: Uses Gemini-2.0 model with parameters like temperature, top_p, and top_k for fine-tuned response creativity.
•	Text Cleaning: Bot responses are cleaned with regular expressions for proper formatting and punctuation.
•	GUI Implementation: The tkinter interface includes a scrollable chat area, input box, and send button.
Potential Use Cases
•	Interactive chatbot applications.
•	Experimentation with generative AI models.
•	Learning how to integrate AI models into GUI-based Python applications.
Future Enhancements
•	Add functionality to save or export chat history.
•	Provide options for user customization of the chat interface.
•	Extend integration to other AI models or APIs.
Contributing
Contributions are welcome! Feel free to fork the repository, open issues, or submit pull requests.
Contact
For questions or suggestions, feel free to contact me at ehsan.sumi1@gmail.com
