# Heart Disease Predictor

A Flask-based machine learning web application that predicts heart disease risk using user-provided health and lifestyle information. The project includes a trained ML model, a web interface, Docker support, and GitHub Actions workflows for CI/CD deployment.

> **Note:** This project is created for educational and demonstration purposes. It should not be used as a substitute for professional medical diagnosis or clinical decision-making.

---

## Project Overview

The Heart Disease Predictor web application allows users to enter health-related details such as age, blood pressure, cholesterol level, BMI, smoking status, diabetes status, stress level, sleep hours, and other medical/lifestyle factors. The Flask backend collects the form data, sends it to a trained machine learning model, and displays the prediction result on the web page.

The prediction result is shown as:

- **No Heart Disease Detected**
- **Heart Disease Risk Detected**

---

## Features

- Heart disease risk prediction using a trained machine learning model
- Flask-based backend
- HTML and CSS frontend
- User-friendly form for health data input
- Pickle-based model loading
- Dockerized application
- Gunicorn support for production deployment
- GitHub Actions CI workflow
- GitHub Actions CD workflow for Docker Hub and EC2 deployment

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Web framework |
| NumPy | Numerical processing |
| Pandas | Data handling |
| Scikit-learn | Machine learning |
| Pickle | Saving/loading trained model |
| HTML | Web page structure |
| CSS | Web page styling |
| Docker | Containerization |
| Gunicorn | Production WSGI server |
| GitHub Actions | CI/CD automation |
| AWS EC2 | Deployment server |

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
└── Dockerfile
```

---

## Input Features

The web application collects the following input values:

1. Age
2. Gender
3. Blood Pressure
4. Cholesterol Level
5. Exercise Habits
6. Smoking
7. Family Heart Disease
8. Diabetes
9. BMI
10. High Blood Pressure
11. Low HDL Cholesterol
12. High LDL Cholesterol
13. Alcohol Consumption
14. Stress Level
15. Sleep Hours
16. Sugar Consumption
17. Triglyceride Level
18. Fasting Blood Sugar
19. CRP Level
20. Homocysteine Level

These values are converted into numerical format and passed to the trained machine learning model for prediction.

---

## Machine Learning Model

The machine learning model was trained using the dataset available in the `model/` folder. The training and testing process is included in the Jupyter notebook:

```text
model/heart_disease_predic.ipynb
```

The trained model is saved as:

```text
predictor.pickle
```

The Flask app loads this model and uses it to make predictions.

---

## Local Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Mihiranga2001/Heart_disease_predictor.git
cd Heart_disease_predictor
```

### 2. Go to the Website Folder

```bash
cd website
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Flask App

```bash
python app.py
```

### 7. Open the Application

Open the following URL in your browser:

```text
http://127.0.0.1:5000
```

---

## Run with Docker

The project includes a `Dockerfile`, so the application can be built and run inside a Docker container.

### 1. Build the Docker Image

Run this command from the root folder of the project:

```bash
docker build -t heart-disease-predictor .
```

### 2. Run the Docker Container

```bash
docker run -p 5000:5000 heart-disease-predictor
```

### 3. Open the App

```text
http://localhost:5000
```

---

## Dockerfile Explanation

The Dockerfile performs the following steps:

1. Uses a lightweight Python 3.11 image
2. Sets `/app` as the working directory
3. Copies `website/requirements.txt`
4. Installs the required Python packages
5. Copies the Flask application files
6. Exposes port `5000`
7. Runs the app using Gunicorn

---

## CI/CD Pipeline

This project includes GitHub Actions workflows inside:

```text
.github/workflows/
```

### CI Workflow

The CI workflow runs when code is pushed to the `main` branch or when a pull request is created.

It performs:

- Repository checkout
- Python setup
- Dependency installation
- Python syntax check
- Docker image build test

### CD Workflow

The CD workflow runs when code is pushed to the `main` branch.

It performs:

- Repository checkout
- Docker Hub login
- Docker image build
- Docker image push to Docker Hub
- SSH connection to EC2
- Pulling the latest Docker image on EC2
- Stopping and removing the old container
- Running the new container on port `80`

---

## Required GitHub Secrets for Deployment

To deploy the project using GitHub Actions, add these secrets in the GitHub repository settings:

| Secret Name | Purpose |
|---|---|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_TOKEN` | Docker Hub access token |
| `SERVER_HOST` | EC2 public IP address or hostname |
| `SERVER_USER` | EC2 username, for example `ubuntu` |
| `SERVER_SSH_KEY` | Private SSH key used to connect to EC2 |

---

## Deployment Commands Used on EC2

The deployment workflow runs commands similar to these on the EC2 instance:

```bash
sudo docker pull <docker-username>/heart_disease_app:latest
sudo docker stop heart-disease-app || true
sudo docker rm heart-disease-app || true
sudo docker run -d --name heart-disease-app --restart always -p 80:5000 <docker-username>/heart_disease_app:latest
sudo docker ps
```

### Simple Explanation

| Command | Meaning |
|---|---|
| `docker pull` | Downloads the latest image from Docker Hub |
| `docker stop` | Stops the old running container |
| `docker rm` | Removes the old container |
| `docker run -d` | Starts the new container in the background |
| `--restart always` | Restarts the app automatically if the server restarts |
| `-p 80:5000` | Maps EC2 port 80 to Flask container port 5000 |
| `docker ps` | Shows running containers |

---

## Important Notes

- Make sure `requirements.txt` has each package on a separate line.
- Make sure the `Dockerfile` has proper line breaks.
- Make sure the trained model file exists in `website/model/predictor.pickle`.
- Make sure Docker is installed on the EC2 instance before deployment.
- Make sure the EC2 security group allows inbound traffic on port `80`.
- Make sure GitHub repository secrets are correctly configured.

---

## Example Requirements File

```text
Flask==3.0.3
gunicorn==22.0.0
numpy==1.26.4
scikit-learn==1.5.1
pandas==2.2.2
```

---

## Future Improvements

- Add better input validation
- Add API endpoint for prediction
- Add unit tests
- Add model performance report
- Add screenshots to the README
- Add database support to store prediction history
- Add better UI design
- Add HTTPS support for production deployment

---

## Medical Disclaimer

This application is only for learning and demonstration. It does not provide professional medical advice. Users should consult a qualified healthcare professional for diagnosis and treatment decisions.

---

## Author

Developed by **Mihiranga2001**.
