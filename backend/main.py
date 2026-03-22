# app.py
from urllib import response

from click import prompt
from flask import Flask, render_template
import requests 
import ollama

# Create a Flask application instance
app = Flask(__name__)

# Define a route and the function to handle the request
@app.route("/submit", methods=["POST"])
#Add the research here in a clear if, else manner  
#Taken from the AI Bible and modified with Ollama documentation
@app.route("/query")
def query_ollama(prompt):
   response=requests.post(
    "http://100.101.119.116:11434/api/generate",
    json={
        "model":"minimax-m2.5:cloud",
        "prompt": prompt, 
        "stream": False,
        "temperature": 0.7,
    } 
    ) 
   return response.json() 
    #Add user prompt as a variable in the javascript code
if response.status_code == 200:
    answer=query_ollama(prompt) 
    print(answer)    
else: 
    print("Error:", response.status_code, response.text) 
# Optional: Run the app directly if the script is executed
if __name__ == "__main__":
    app.run(debug=True)

