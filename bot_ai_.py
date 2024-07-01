from flask import Flask, request, jsonify, render_template
import openai
import os

# Specify the custom template folder
template_dir = os.path.abspath('C:/Users/ethan/Downloads/templates')
app = Flask(__name__)

# Configure OpenAI API key
# Set your OpenAI API key
openai.api_key = "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"


def simplify_concept(concept):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Simplify this concept to: {concept}. Make simplifications similar to this: derivative is essentially just slope."}],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/simplify', methods=['POST'])
def simplify():
    data = request.json
    concept = data.get('concept')
    if not concept:
        return jsonify({"error": "Please provide a concept."}), 400
    simplified_text = simplify_concept(concept)
    return jsonify({"response": simplified_text})

if __name__ == '__main__':
    print("Current Working Directory:", os.getcwd())
    print("Templates Directory:", template_dir)
    app.run(debug=True)
