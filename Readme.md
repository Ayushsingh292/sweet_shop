#  Sweet Shop Management System

A full-stack web application for managing sweets in a store — built with **React (frontend)**, **Django REST Framework (backend)**, and **MongoDB**.  
Admins can add, update, or delete sweets, while users can browse and purchase them.  
The app includes secure login, JWT authentication, and an aesthetic UI.

---

##  Features

###  Authentication
- User registration and login using JWT tokens  
- Role-based access (Admin vs Customer)  
- Secure token handling (access and refresh tokens)

###  Sweet Management
- Add, update, delete, and search sweets  
- Category-based filtering  
- Purchase and restock functionalities  

###  Frontend (React.js)
- Responsive UI built using **React** and **CSS**  
- Modern gradient theme for dashboard and login pages  
- Fetches sweets dynamically from the backend API

###  Backend (Django REST Framework)
- RESTful APIs for sweets, authentication, and role control  
- MongoDB integration for persistent sweet data  
- Error handling and validation at each endpoint  

---

## Tech Stack

| Layer | Technology |
|-------|-------------|
| Frontend | React.js, CSS |
| Backend | Django REST Framework |
| Database | MongoDB |
| Authentication | JWT (SimpleJWT) |
| Version Control | Git & GitHub |

---

## Project Structure

sweet-shop/
│
├── backend/
│ ├── auth_app/
│ ├── sweets/
│ ├── manage.py
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── Login.js
│ │ │ ├── Dashboard.js
│ │ │ ├── Login.css
│ │ │ └── Dashboard.css
│ ├── package.json
│ └── public/
│
└── README.md


---

##  API Endpoints

### Authentication
| Method | Endpoint | Description |
|---------|-----------|-------------|
| `POST` | `/api/auth/register/` | Register a new user |
| `POST` | `/api/auth/login/` | Login and get JWT tokens |

###  Sweet Operations
| Method | Endpoint | Description |
|---------|-----------|-------------|
| `GET` | `/api/sweets/` | Get all sweets |
| `POST` | `/api/sweets/add/` | Add a new sweet *(admin only)* |
| `PUT` | `/api/sweets/update/<id>/` | Update a sweet *(admin only)* |
| `DELETE` | `/api/sweets/delete/<id>/` | Delete a sweet *(admin only)* |
| `POST` | `/api/sweets/purchase/<id>/` | Purchase a sweet *(user)* |

---

##  My AI Usage

### Tools Used
- **ChatGPT (OpenAI GPT-5)**  
- **GitHub Copilot**  

---

### How I Used AI
- I used **ChatGPT** extensively for:
  - Debugging backend errors (e.g., `UserManager object is not callable`, token validation issues).
  - Generating frontend UI improvements (modern CSS gradients, responsive dashboard layouts).
  - Structuring my Django REST views and serializers more efficiently.
  - Writing this README and documentation sections to maintain professional clarity.
- I used **GitHub Copilot** for:
  - Autocompleting repetitive React hooks and Django model methods.
  - Suggesting function names, imports, and variable structures during development.

---

### Reflection on AI Impact
Using AI significantly **enhanced my productivity and learning** throughout this project:
- It **accelerated debugging** by explaining Django and React errors clearly.
- It helped me **learn better coding patterns** (e.g., APIView vs. function-based views).
- It improved my **UI design sense** by suggesting aesthetic, accessible color combinations.
- However, I made sure to **review and test every AI suggestion** to ensure correctness and understanding.
  
Overall, AI acted as a **collaborative assistant**, not a replacement — helping me focus more on project logic, architecture, and creativity.

---

## Setup & Run Instructions

### Backend (Django)

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

Frontend (React)

cd frontend
npm install
npm start


Access

Visit:
Frontend: http://localhost:3000
Backend API: http://127.0.0.1:8000

Screenshots:-