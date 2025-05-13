from flask import Flask, render_template, request, jsonify
# import openai
from datetime import datetime
import os
import requests

app = Flask(__name__)

# Configure OpenAI API
# openai.api_key = os.getenv('OPENAI_API_KEY')

# class PropertyAnalyzer:
#     def __init__(self):
#         self.model = "gpt-4"  # or whatever model you're using
        
#     def analyze_property(self, price, location, property_type):
#         prompt = f"""
#         Analyze this property investment:
#         Price: ${price:,}
#         Location: {location}
#         Type: {property_type}
        
#         Provide:
#         1. Investment potential (1-10)
#         2. Expected ROI over 5 years
#         3. Market analysis
#         4. Risk factors
#         5. Recommendations
#         """
        
#         response = openai.ChatCompletion.create(
#             model=self.model,
#             messages=[{"role": "user", "content": prompt}]
#         )
        
#         return response.choices[0].message.content

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     try:
#         data = request.form
#         price = float(data.get('property_price'))
#         location = data.get('location')
#         property_type = data.get('property_type')
        
#         analyzer = PropertyAnalyzer()
#         analysis = analyzer.analyze_property(price, location, property_type)
        
#         return jsonify({
#             'success': True,
#             'analysis': analysis,
#             'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         })
    
    # except Exception as e:
    #     return jsonify({
    #         'success': False,
    #         'error': str(e)
    #     }), 400

# Configure static files directory
app.static_folder = 'static'

aaapi_key = "sk-jPf2AKxYQ1XDdQ4z7FX5ToDNPRwrhjJ36aIyL8wBtJrVZePB"  # Replace with your actual API key
base_url = "https://api.gptgod.online/v1/chat/completions"

def get_ai_response(text):
    response = requests.post(
        base_url,
        headers={"Authorization": f"Bearer {aaapi_key}"},
        json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": f"never say you made by openai and never say your name is chatgpt and you made to answer to questions like What homes are available under $400,000?, Show me houses with 3 bedrooms, Which properties have pools?, Comparing Options, What's the price range for 4-bedroom homes?, Tell me about downtown properties, Compare houses with large yards also you made to only help with property inquiries nothing else. also you now answer me: {text}"}]}
    )

    if response.status_code == 200:
        generated_text = response.json()["choices"][0]["message"]["content"]
        return generated_text
    else:
        return "Error: Unable to get a response from the API."

@app.route('/get-ai-response', methods=['POST'])
def ai_response():
    data = request.get_json()
    user_message = data.get('message')
    response = get_ai_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)