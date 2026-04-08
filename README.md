# 🌤 Weather App — Django Project

A beautiful weather app built with Django, featuring a glassmorphism UI with animated background.

---

## 📁 Project Structure

```
weather_project/
├── manage.py
├── requirements.txt
├── weather_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── weather_app/
    ├── __init__.py
    ├── views.py
    ├── urls.py
    ├── templates/
    │   └── weather_app/
    │       └── index.html
    └── static/
        └── weather_app/
            ├── css/
            │   └── style.css
            └── js/
                └── main.js
```

---

## 🚀 Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get a FREE API Key
- Go to: https://openweathermap.org/api
- Sign up and get your free API key

### 3. Add your API Key
Open `weather_project/settings.py` and replace:
```python
WEATHER_API_KEY = 'YOUR_API_KEY_HERE'
```
with your actual key.

### 4. Run the server
```bash
python manage.py runserver
```

### 5. Open in browser
```
http://127.0.0.1:8000/
```

---

## 🎨 Features

- Glassmorphism card UI with blur effects
- Animated floating particles background
- Live weather via OpenWeatherMap API
- Temperature, humidity, wind speed, feels like
- Smooth animations and hover effects
- Fully responsive design
- Error handling for invalid cities

---

## 🔑 API Info

Uses the **OpenWeatherMap Current Weather API** (free tier):
- 60 calls/min free
- Sign up at: https://openweathermap.org/api
