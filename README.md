# TSA Career Pathway Visualizer

## Overview

The TSA Career Pathway Visualizer is a web application that helps students explore potential career paths using artificial intelligence. Users enter a career they are interested in, and the application generates a step-by-step roadmap showing how someone can progress from a beginner level to a successful career in that field. The roadmap is then displayed as an interactive flowchart, making the path easier to understand and follow.

This project was created for the Technology Student Association (TSA) and was my **first complete software project from start to finish**. More importantly, it was the project that introduced me to AI-powered software development. Through building it, I learned how to connect a website to an AI model, send requests through an API, process AI-generated responses, and display the results in a meaningful way for users.

Prior to this project, I had limited experience working with APIs or full-stack development. Creating the Career Pathway Visualizer taught me how modern web applications integrate external services and showed me how artificial intelligence can be used to solve real-world problems. This project became the foundation for many of the programming concepts and technologies I would continue to learn afterward.

---

## Problem Statement

Many students know what careers interest them but do not know the steps required to reach those goals. Information about education, skills, certifications, and career progression is often scattered across multiple sources.

The TSA Career Pathway Visualizer addresses this problem by generating a clear, AI-powered roadmap that outlines the progression from beginner to professional, helping students better understand the journey toward their desired career.

---

## Features

### AI-Powered Career Guidance

* Accepts a career goal from the user.
* Generates a customized career progression roadmap.
* Uses AI to provide structured recommendations.

### Visual Career Roadmaps

* Converts career steps into a flowchart format.
* Displays progression in an easy-to-follow visual structure.
* Uses Mermaid.js for diagram rendering.

### Full-Stack Architecture

* Frontend built using HTML, CSS, and JavaScript.
* Backend powered by Flask and Python.
* API-based communication between frontend and backend.

### Database Integration

* Utilizes SQLite and SQLAlchemy.
* Provides a foundation for storing future user-generated data.

---

## Technologies Used

### Frontend

* HTML
* CSS
* JavaScript
* Mermaid.js

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Pydantic

### Database

* SQLite

### AI & APIs

* Ollama API
* Minimax M2.5 Language Model

### Development Tools

* Git
* GitHub

---

## Project Structure

```text
TSAProject/
│
├── backend/
│   ├── config.py
│   ├── main.py
│   └── models.py
│
├── frontend/
│   ├── static/
│   │   ├── main.js
│   │   └── style.css
│   │
│   └── templates/
│       └── index.html
│
└── .gitignore
```

---

## How It Works

1. The user enters a career they want to explore.
2. The frontend sends the request to the Flask backend.
3. The backend communicates with an AI model through the Ollama API. Communicates to my custom server using a temporary IP address **Please do not try and access**
4. The AI generates a structured sequence of career-development steps.
5. The backend converts those steps into Mermaid diagram syntax.
6. Mermaid.js renders the roadmap as an interactive flowchart.
7. The user receives a visual representation of the path toward their chosen career.

---

## What I Learned

This project served as a major milestone in my programming journey and taught me many concepts that I continue to use today:

* Building my first complete software project from idea to implementation.
* Creating a full-stack web application.
* Connecting frontend and backend systems.
* Understanding how APIs work.
* Integrating AI into a website.
* Sending and processing API requests.
* Working with databases using SQLAlchemy.
* Organizing code into a maintainable project structure.
* Using Git and GitHub for version control.
* Debugging real-world software issues.

Most importantly, this project introduced me to AI development and showed me how large language models can be incorporated into practical applications to create meaningful user experiences.

---

## Future Improvements

Potential future enhancements include:

* User authentication and accounts.
* Saving generated career roadmaps.
* Improved AI prompting and validation.
* Additional visualization styles.
* Career comparison features.
* Exporting diagrams as PDF files.
* Mobile-responsive design.
* Expanded career resources and recommendations.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/tanishpatel751-gif/TSAProject.git
cd TSAProject
```

### Install Dependencies

```bash
pip install flask
pip install flask-sqlalchemy
pip install pydantic
pip install requests
```

### Run the Application

```bash
python backend/main.py
```

Open your browser and navigate to the local address provided by Flask.

---

## Author

**Tanish Patel**

Technology Student Association (TSA) Competitor
Aspiring Software Engineer | AI Enthusiast | Student Developer

This project represents my first experience building a complete AI-powered web application and marks the beginning of my journey into full-stack development and artificial intelligence.

---

## License

This project is intended for educational purposes and personal learning.
