
# 🧠 Data Intepreter Assistant

A voice-enabled chatbot that interprets natural language queries and provides real-time insights from sales data.


## 📌 Problem Statement
Sales managers and business analysts often deal with large datasets in CSV or Excel formats. Extracting specific insights like "How did the North region perform in March?" typically involves filtering and manual analysis.
### Challenge
There is no intuitive and natural way to ask data-related questions in plain English and get immediate insights.

## ✅ Solution
Data Intepreter Assistant allows users to ask questions using their voice or text and get instant, human-friendly responses from backend sales data. It mimics the experience of talking to a personal business analyst.
## 💡Features

- 🎤 Voice input and speaker output for true hands-free interaction
- 🔍 Understands natural language queries like:
 ->"What were the sales in the South region in April?"

 ->"Did we meet the target in February for North?"
- 📊 Responds with easy-to-understand summaries
- ⚡ Lightweight, no external LLM API dependency

## 🛠️ Tech Stack

| Layer             | Tools Used                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Frontend | HTML, CSS, JavaScript, Web Speech API |
| Backend | Python, Flask |
| Voice Input | Web Speech API (Speech-to-Text) |
| Voice Output | browser’s speechSynthesis API |
| Data Storage | Static JSON file (sales_data.json) |
| Deployment | Yet To be hosted (e.g., GitHub Pages + Render)|


## 📁 Project Structure
- data-intepreter-assistant

  -  backend
      -  app.py
      -  query_handler.py
      -  sales_data.json
  -  frontend
      -  index.html
      -  style.css
      -  script.js
- README.md

## 🚀 How to Run Locally

Clone the project

```bash
  git clone https://github.com/aspirant-22/data-intepreter-assistant.git
cd data-intepreter-assistant

```
Flask server starts at: http://127.0.0.1:5000

Setup Backend

```bash
cd backend
pip install -r requirements.txt
python app.py

```

Open Frontend


`` Open frontend/index.html in a browser (preferably Chrome). ``


## 🖼️ Screenshots

### Before Asking Assistant : 
![Screenshot 2025-04-29 212418](https://github.com/user-attachments/assets/0169fc69-7255-4777-8fff-cbea1a36051f)
### Response : 
![Screenshot 2025-04-29 212452](https://github.com/user-attachments/assets/41cb6e40-caeb-4e19-a956-b559c1ce13f6)

## 🌍 Hosting Instructions
### Backend (Flask):
Use platforms like:
 - Render.com (Free tier)
 - Replit (for lightweight hosting)

### Frontend:
 - GitHub Pages (drag and drop frontend folder)
 - Netlify / Vercel
## 🙌 Acknowledgements

 - Inspired by real-world sales teams' needs.
 - Developed using beginner-friendly tech for rapid prototyping.
 - Special thanks to the open-source libraries used in this project.


## Author

- [@aspirant-22](https://www.github.com/aspirant-22)

## Feedback
Have suggestions or want to contribute?

Feel free to reach out via GitHub Issues.
