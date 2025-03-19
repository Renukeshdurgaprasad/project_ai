from flask import Flask, request, jsonify
import google.generativeai as genai
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Enable frontend connection
import logging
import os
from dotenv import load_dotenv
load_dotenv()



# Initialize Flask App
app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

# Configure Logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# Database Setup (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interactions.db'
db = SQLAlchemy(app)

# Database Model
class Interaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_input = db.Column(db.String(500), nullable=False)
    ai_response = db.Column(db.String(2000), nullable=False)

# Create Database Tables
with app.app_context():
    db.create_all()

# AI Agent Classes with Logging
class GenerationAgent:
    def process(self, input_data):
        logging.info(f"Generating response for: {input_data}")
        return f"Generated hypothesis: {input_data} - AI-enhanced solution"

class ReflectionAgent:
    def process(self, input_data):
        logging.info(f"Checking coherence for: {input_data}")
        return f"Validated response: {input_data} - Relevant to topic"

class RankingAgent:
    def process(self, input_data):
        logging.info(f"Ranking response for: {input_data}")
        return f"Ranked response: {input_data} - Score 9/10"

class EvolutionAgent:
    def process(self, input_data):
        logging.info(f"Refining response for: {input_data}")
        return f"Refined hypothesis: {input_data} - Updated AI approach"

# Supervisor Agent for Multi-Cycle Processing
class SupervisorAgent:
    def __init__(self):
        self.history = {}

    def assign_task(self, agent, input_data):
        return agent.process(input_data)

    def multi_cycle_processing(self, input_data, cycles=3):
        result = input_data
        for _ in range(cycles):
            result = self.assign_task(EvolutionAgent(), result)
            result = self.assign_task(ReflectionAgent(), result)
            result = self.assign_task(RankingAgent(), result)
        return result

# Gemini AI Function
def gemini_search(query):
    model = genai.GenerativeModel("gemini-2.0-flash")  # Use the latest Gemini model
    response = model.generate_content(query)
    return response.text if response else "No relevant data found."

# Recommendation System
def get_recommendations(query):
    topic_map = {
        "AI": ["Machine Learning", "Neural Networks", "Deep Learning"],
        "Python": ["Flask", "Django", "FastAPI"],
        "Chatbot": ["NLP", "Conversational AI", "Voice Assistants"],
    }
    
    for topic, suggestions in topic_map.items():
        if topic.lower() in query.lower():
            return suggestions
    return ["No recommendations found."]

# Store chat history
def store_chat(user_input, ai_response):
    new_interaction = Interaction(user_input=user_input, ai_response=ai_response)
    db.session.add(new_interaction)
    db.session.commit()

# API Routes
@app.route('/chat_multi', methods=['POST'])
def chat_multi():
    data = request.get_json()
    user_input = data.get("message")

    # Get AI response
    ai_response = gemini_search(user_input)

    # Get recommended topics
    recommendations = get_recommendations(user_input)

    # Store interaction in database
    store_chat(user_input, ai_response)

    return jsonify({
        "response": ai_response,
        "recommendations": recommendations
    })

@app.route("/history", methods=["GET"])
def get_history():
    interactions = Interaction.query.all()
    history = [{"input": i.user_input, "response": i.ai_response} for i in interactions]
    return jsonify(history)

if __name__ == "__main__":
    app.run(debug=True)
