# SleepWise 🌙

SleepWise is a simple web application that helps users calculate recommended sleep and wake-up times based on 7-hour and 8-hour sleep durations.

## Features

* Calculate wake-up times based on bedtime
* Calculate bedtime based on wake-up time
* 7-hour and 8-hour sleep suggestions
* Detect when the recommended bedtime belongs to the previous night
* Responsive user interface
* REST API with FastAPI
* Docker support

## Tech Stack

* Python
* FastAPI
* HTML
* CSS
* JavaScript
* Docker
* Git & GitHub

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/EhsaN-AI13/SleepWise.git
cd SleepWise
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
uvicorn app:app --reload
```

Open your browser and go to:

```text
http://127.0.0.1:8000
```

## Run with Docker

### 1. Build the Docker image

```bash
docker build -t sleepwise .
```

### 2. Run the container

```bash
docker run -d --name sleepwise-container -p 8000:8000 sleepwise
```

Open your browser and go to:

```text
http://localhost:8000
```

## Project Structure

```text
SleepWise/
├── app.py
├── index.html
├── style.css
├── script.js
├── requirements.txt
├── Dockerfile
├── .gitignore
└── README.md
```

## API

SleepWise provides a simple API endpoint for calculating sleep and wake-up times.

### Endpoint

```text
GET /calculate
```

### Parameters

* `mode`: `sleep` or `wake`
* `time`: Time in `HH:MM` format

### Example Request

```text
/calculate?mode=sleep&time=23:30
```

### Example Response

```json
{
  "mode": "sleep",
  "time": "23:30",
  "result_7": "06:30",
  "result_8": "07:30"
}
```
