# 🌦 Live Weather Application

A Python-based **Live Weather Application** that fetches real-time weather information using the OpenWeather API.

This project demonstrates **API integration**, **environment variable management**, and both **CLI-based** and **Web-based** application development workflows.

---

## 🚀 Live Demo

🔗 *(https://live-weather-api-kmhrbuybyi8jdvivrjgrje.streamlit.app/)*

---

## 📌 Features

* 🌍 Search weather by city name
* 🌡 Real-time temperature data
* ☁️ Weather condition description
* 🔐 Secure API key handling using `.env`
* 🖥 CLI version for backend learning
* 🌐 Streamlit web app for interactive usage

---

## 🛠 Tech Stack

* Python
* Requests Library
* Streamlit
* OpenWeather API
* dotenv (.env configuration)

---

## 📂 Project Structure

```
live-weather-api/
│
├── app.py           # Streamlit Web Application
├── cli_weather.py   # Command Line Version
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository

```
git clone https://github.com/Lohith158/live-weather-api.git
cd live-weather-api
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Create `.env` File

Create a `.env` file in the project root:

```
API_KEY=your_openweather_api_key
```

---

## ▶️ Run CLI Version

```
python cli_weather.py
```

Type city name to get weather data.

Exit using:

```
exit
```

---

## 🌐 Run Streamlit Web App

```
python -m streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## 🔐 Environment Variables

API keys are stored securely using:

* `.env` file (local development)
* Streamlit Secrets (deployment)

---

## 🎯 Learning Objectives

This project was built to practice:

* REST API consumption
* JSON data handling
* Python backend logic
* Transition from CLI applications to deployable web apps
* Git & GitHub workflow
* Application deployment concepts

---

## 📈 Future Improvements

* 📅 7-day weather forecast
* 🌎 Auto location detection
* 📊 Weather analytics dashboard
* 🤖 AI-based weather insights

---

## 👨‍💻 Author

**Lohith**

AI/ML Engineering Student focused on building practical AI-driven applications and learning real-world software development workflows.

---

⭐ If you find this project useful, consider giving it a star!
