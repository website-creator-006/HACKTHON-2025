from flask import Flask, request, jsonify
from bs4 import BeautifulSoup
import os
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

def extract_data_from_html(file_path):
    """Extract text content from an HTML file."""
    if not os.path.exists(file_path):
        return ""
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "html.parser")
        return soup.get_text().lower()

# Load event and workshop data from HTML files
event_data = extract_data_from_html("events.html")
workshop_data = extract_data_from_html("workshops.html")

@app.route("/chatbot", methods=["POST"])
def chatbot():
    user_input = request.json.get("message", "").lower().strip()

    if not user_input:
        return jsonify({"response": "Please enter a valid question."})

    # Improved keyword matching for events
    event_keywords = ["event", "tech talk", "coding hackathon", "robotics expo"]
    if any(keyword in user_input for keyword in event_keywords):
        return jsonify({"response": "Here’s information about upcoming events: " + event_data[:500] + "..."})

    # Improved keyword matching for workshops
    workshop_keywords = ["workshop", "ai workshop", "copyright workshop", "future ai"]
    if any(keyword in user_input for keyword in workshop_keywords):
        return jsonify({"response": "Here’s information about available workshops: " + workshop_data[:500] + "..."})

    # Default response if no match
    return jsonify({"response": "I'm not sure about that. Try asking about events or workshops!"})

if __name__ == "__main__":
    app.run(debug=True)
