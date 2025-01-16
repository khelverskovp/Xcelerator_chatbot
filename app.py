from flask import Flask, request, jsonify
import random

app = Flask(__name__)

def chatbot_response(user_input):
    responses = {
        "hello": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
        "what is siemens xcelerator": [
            "Siemens Xcelerator is an open digital business platform designed to accelerate digital transformation. It includes software, hardware, and services tailored for various industries."
        ],
        "services": [
            "Siemens Xcelerator offers a range of digital solutions, including industrial automation, IoT, AI-driven analytics, and cloud computing. Do you need help with a specific service?"
        ],
        "pricing": [
            "Pricing for Siemens Xcelerator solutions depends on the service and implementation scale. Would you like to be connected with a sales representative?"
        ],
        "support": [
            "For support, you can visit the Siemens Xcelerator support portal or provide details about your issue so I can assist you."
        ],
        "thank you": ["You're welcome! Let me know if you need further assistance.", "Glad to help! Have a great day!"]
    }

    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    
    return "I'm sorry, I didn't quite understand that. Can you please rephrase?"

@app.route("/")
def home():
    return "Siemens Xcelerator Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    bot_response = chatbot_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
