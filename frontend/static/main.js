import mermaid from 'https://jsdelivr.net';
mermaid.initialize({ startOnLoad: true });
// Adding form submission for the first form to determine the career
const form = document.getElementById('form'); 

form.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior
    const formData = new FormData(form); // Create a FormData object from the form
    
    fetch('/submit', {
        method: 'POST', // Use POST method to submit the form data
        body: formData // Send the form data as the request body
    })    .then(response => response.json()) // Parse the JSON response from the server
    .then(data => {
        console.log('Success:', data); // Log the success response from the server
        // You can also update the UI or display a success message here
    })
    .catch((error) => {
        console.error('Error:', error); // Log any errors that occur during the fetch request
        // You can also display an error message to the user here
    });

});   

const response = await fetch('http://100.101.119.116:11434/api/generate', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        "model": "minimax-m2.5:cloud",
        "prompt": prompt,
        "stream": false
    })
}); 
//Taken from Mermaid Syntax and Rendering
const mermaidResponse = await fetch('/get-diagram'); // Fetch the mermaid syntax from the backend
const data = await mermaidResponse.json();
const mermaidSyntax = data.response; // e.g., "graph TD; A[Start] --> B[Water];"

// 2. Render it (requires mermaid library loaded)
import mermaid from 'mermaid';
mermaid.initialize({ startOnLoad: true });

// Pass mermaidSyntax to a <div> with class "mermaid", put in HTML file
document.getElementById('chart').innerHTML = mermaidSyntax;
mermaid.contentLoaded();