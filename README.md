# Heart Disease Predictor

A Flask-based machine learning web application that predicts heart disease risk using user-provided health and lifestyle information. The project includes a trained ML model, a web interface, Docker support, GitHub Actions CI/CD workflows, Docker Hub image deployment, AWS EC2 hosting, and Nginx reverse proxy configuration.

> **Note:** This project is created for educational and demonstration purposes only. It should not be used as a substitute for professional medical diagnosis or clinical decision-making.

---

## Project Overview

The Heart Disease Predictor web application allows users to enter health-related details such as age, blood pressure, cholesterol level, BMI, smoking status, diabetes status, stress level, sleep hours, and other medical/lifestyle factors.

The Flask backend receives the form data, converts it into the required numerical format, sends it to a trained machine learning model, and displays the prediction result on the web page.

The prediction result is shown as:

- **No Heart Disease Detected**
- **Heart Disease Risk Detected**

---

## Features

- Heart disease risk prediction using a trained machine learning model
- Flask-based backend
- HTML and CSS frontend
- User-friendly web form
- Pickle-based ML model loading
- Dockerized application
- Gunicorn production server
- Docker Hub image publishing
- GitHub Actions CI workflow
- GitHub Actions CD workflow
- AWS EC2 deployment
- Nginx reverse proxy support
- Production-style deployment using Docker + Nginx

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Backend web framework |
| NumPy | Numerical processing |
| Pandas | Data handling |
| Scikit-learn | Machine learning |
| Pickle | Saving and loading trained ML model |
| HTML | Web page structure |
| CSS | Web page styling |
| Docker | Containerization |
| Docker Hub | Docker image registry |
| Gunicorn | Production WSGI server |
| GitHub Actions | CI/CD automation |
| AWS EC2 | Cloud deployment server |
| Nginx | Reverse proxy web server |

---

## Project Structure

```text
Heart_disease_predictor/
│
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
│
├── model/
│   ├── heart_disease.csv
│   ├── heart_disease_predic.ipynb
│   └── predictor.pickle
│
├── website/
│   ├── app.py
│   ├── requirements.txt
│   ├── model/
│   │   └── predictor.pickle
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── index.html
│
├── .dockerignore
├── Dockerfile
└── README.md
