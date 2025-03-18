
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

# Initialize Flask App
app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key="AIzaSyAuHvTMhABLBFXtALbhE0-HgapP93PGqGg")

# Sample dataset for recommendations
data = {
    "name": ["Python Basics", "AI Fundamentals", "Web Development", "Data Science", "Machine Learning"],
    "category": ["Programming", "AI", "Web", "Data", "AI"]
}
df = pd.DataFrame(data)

# Convert categories to numeric values
df["category_encoded"] = df["category"].astype("category").cat.codes
features = df[["category_encoded"]].values

# Helper function: Get Gemini API response
def gemini_search(query):
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(query)
    return response.text

# Helper function: Content-based recommendation
def recommend_courses(user_interest):
    input_feature = np.array([[df[df["name"] == user_interest]["category_encoded"].values[0]]])
    similarities = cosine_similarity(input_feature, features)
    recommended_indices = similarities.argsort()[0][-3:][::-1]
    return df.iloc[recommended_indices]["name"].tolist()

# Flask Routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chatbot():
    user_message = request.json.get("message")
    response = gemini_search(f"Answer as a chatbot: {user_message}")
    return jsonify({"response": response})

@app.route("/recommend", methods=["POST"])
def recommend():
    user_interest = request.json.get("interest")
    recommendations = recommend_courses(user_interest)
    return jsonify({"recommendations": recommendations})

@app.route("/automate", methods=["POST"])
def automate():
    task = request.json.get("task")
    automation_responses = {
        "send email": "Email sent successfully!",
        "set reminder": "Reminder set!",
        "weather update": "Today's weather is sunny."
    }
    return jsonify({"result": automation_responses.get(task.lower(), "Task not recognized.")})

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query")
    result = gemini_search(query)
    return jsonify({"result": result})

# Run the App
if __name__ == "__main__":
    app.run(debug=True)
