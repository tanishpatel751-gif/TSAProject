# app.py
from flask import Flask, jsonify, render_template
import requests 
from pydantic import BaseModel, Field
# Create a Flask application instance
app = Flask(__name__) 

#Create a class for the career steps
class CareerSteps(BaseModel):
    steps: list[str] = Field(
        ..., 
        description="A list of 10 steps to achieve the career goal, whether that be from beginner to intermediate in a certain field or how to rise in the ranks of a certain company, in chronological order."
    )
# Define a route and the function to handle the request
@app.route("/submit", methods=["POST"])
#Add the research here in a clear if, else manner  
#Taken from the AI Bible and modified with Ollama documentation



@app.route("/query")
def query_ollama(prompt):
  for i in range(10):  
   response = requests.post(
    "http://100.101.119.116:11434/api/generate",
    json={
        "model":"minimax-m2.5:cloud",
        "prompt": prompt, 
        "stream": False,
        "temperature": 0.7,
        "options": { 
           "stop": ["\n"]
        }
    } 
    ) 
   if response.status_code == 200:
       answer = response.json()['response'].strip()
       return answer
   else: 
       print("Error:", response.status_code, response.text)
       return None

# Defining the number of steps to the career 
answers = []
answers.append(answer)
career_steps= {"1": answers[0], "2": answers[1], "3": answers[2], "4": answers[3], "5": answers[4], "6": answers[5], "7": answers[6], "8": answers[7], "9": answers[8], "10": answers[9]}

@app.route("/get-diagram")
def generate_mermaid_code(career_steps):
 mermaid_code = f""" 
    flowchart TD 
    A[Start] --> B[{career_steps['0']}] 
    B --> C[{career_steps['1']}] 
    C --> D[{career_steps['2']}] 
    D --> E[{career_steps['3']}] 
    E --> F[{career_steps['4']}] 
    F --> G[{career_steps['5']}]
    G --> H[{career_steps['7']}]
    H --> I[{career_steps['8']}]
    I --> J[{career_steps['9']}]
    K --> L[End]  
    """  
 return jsonify(mermaid_code)
# Optional: Run the app directly if the script is executed
if __name__ == "__main__":
    app.run(debug=True)

