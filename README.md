# Flight Management Web

## Overview

Flight Management Web is a Django-based backend system for managing pilot flight operations, aircraft utilization, RFID authentication, and automated flight hour tracking.

The system integrates with an ESP32-S3 RFID terminal that allows pilots to check in and check out of flights using RFID cards.

---

## Features

### Pilot Management

* Pilot registration
* Pilot RFID assignment
* Flight hour tracking
* Pilot profile management

### Aircraft Management

* Aircraft registration
* Aircraft utilization tracking
* Maintenance monitoring
* Aircraft grounding controls

### Flight Logging

* Automated flight check-in
* Automated flight check-out
* Flight duration calculation
* Pilot flight hour accumulation
* Aircraft hour accumulation

### RFID Integration

* RFID card authentication
* Pilot verification
* Real-time communication with ESP32 terminals

### Analytics

* Aircraft utilization reports
* Flight activity tracking
* Pilot hour summaries

---

## Technology Stack

### Backend

* Python
* Django
* MySQL

### IoT Integration

* ESP32-S3
* RC522 RFID Reader
* REST API
* JSON

### Frontend

* Django Templates
* HTML
* CSS
* Bootstrap

---

## System Architecture

ESP32 Terminal
↓
WiFi Network
↓
Django REST API
↓
MySQL Database
↓
Pilot / Aircraft / Flight Records

---

## Project Structure

```text
FlightHoursSystem/
│
├── aircraft/
├── flights/
├── pilots/
│
├── templates/
├── static/
│
├── FlightHoursSystem/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── manage.py
└── requirements.txt
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/flight-management-web.git
```

```bash
cd flight-management-web
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5. Configure Database

Create a MySQL database:

```sql
CREATE DATABASE flight_management_db;
```

Update:

```python
settings.py
```

Example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'flight_management_db',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

---

### 6. Run Migrations

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

---

### 7. Create Administrator

```bash
python manage.py createsuperuser
```

---

### 8. Start Development Server

```bash
python manage.py runserver 0.0.0.0:8000
```

Open:

```text
http://127.0.0.1:8000/admin
```

---

## API Endpoints

### Ping

#### GET

```text
/api/ping/
```

Response:

```json
{
    "status":"ok",
    "message":"UAMS Online"
}
```

---

### RFID Verification

#### POST

```text
/api/verify-rfid/
```

Request:

```json
{
    "uid":"315433AA"
}
```

Response:

```json
{
    "status":"success",
    "pilot_id":1,
    "pilot_name":"Issac"
}
```

---

### Flight Processing

#### POST

```text
/api/process-flight/
```

Request:

```json
{
    "uid":"315433AA",
    "aircraft_id":1
}
```

Check-In Response:

```json
{
    "status":"success",
    "action":"CHECK_IN",
    "pilot":"Issac"
}
```

Check-Out Response:

```json
{
    "status":"success",
    "action":"CHECK_OUT",
    "pilot":"Issac",
    "hours":1.75
}
```

---

## Database Models

### Pilot

* Name
* License Number
* RFID UID
* Total Flight Hours

### Aircraft

* Registration Number
* Aircraft Name
* Manufacturer
* Total Hours
* Next Service Hours
* Status

### Flight Log

* Pilot
* Aircraft
* Check In
* Check Out
* Flight Hours
* Status

---

## Aircraft Statuses

* ACTIVE
* MAINTENANCE_DUE
* GROUNDED
* IN_MAINTENANCE

---

## ESP32 Integration

The ESP32 terminal communicates with Django through HTTP requests.

Functions include:

* Pilot authentication
* Flight check-in
* Flight check-out
* Aircraft validation

---

## Future Improvements

* HTTPS support
* JWT Authentication
* Multi-aircraft terminal support
* Flight analytics dashboard
* Maintenance scheduling
* Cloud deployment
* Email notifications
* Mobile application

---


