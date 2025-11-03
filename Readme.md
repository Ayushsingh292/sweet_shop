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
```bash
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
```

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
### Backend (Django)
```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```
---
### Frontend (React)
```bash
cd frontend
npm install
npm start

```
---

### Screenshots:-
<img width="400" height="400" alt="image" src="https://github.com/user-attachments/assets/fa0c85de-4407-471d-a072-8e000bd6f410" />
<img width="400" height="400" alt="Screenshot 2025-11-03 221611" src="https://github.com/user-attachments/assets/c0d8e710-9cd9-40b0-b75f-162665c7836e" />
<img width="400" height="400" alt="Screenshot 2025-11-03 064040" src="https://github.com/user-attachments/assets/1600c159-72a0-4e10-9a42-d249dda303be" />
<img width="400" height="400" alt="Screenshot 2025-11-03 064147" src="https://github.com/user-attachments/assets/4667fa21-38c6-4e31-9fa9-736d2dcdc5e9" />
<img width="400" height="400" alt="Screenshot 2025-11-03 080657" src="https://github.com/user-attachments/assets/f42f8585-36ef-4534-865c-0be1806c1770" />



