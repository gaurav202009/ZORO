from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# Tumhari API Key (Wahi purani wali)
genai.configure(api_key="AIzaSyB6dG7MKS88xbz2zuHZ463x5RNksy-ZXZ8")

# YAHAN HAI CHANGE: Humne 'gemini-pro' kar diya hai jo stable hai
model = genai.GenerativeModel('gemini-pro')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_query = data.get("message")
        
        # Zoro AI Personality Instruction
        prompt = f"Tu Zoro AI hai, Gaurav Wadekar ka assistant. Smartly answer kar: {user_query}"
        
        response = model.generate_content(prompt)
        return jsonify({"reply": response.text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "Bhai, model ya internet ka kuch locha hai!"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)