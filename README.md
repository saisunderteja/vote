# Vote


## Installation and Setup

### **1. Clone the Repository**
```
git clone https://github.com/saisunderteja/vote.git
cd vote
```
### **2. Create a Virtual Environment**
```
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows
```
### **3. Install Dependencies**
Install the required dependencies listed in `requiements.txt`:
```
pip install -r requirements.txt
```



### **4. Run the Application**
Start the FastAPI server using:
```
uvicorn app.main:app --reload
```
Access the API documentation at:
- Swagger UI: `http://127.0.0.1:8000/docs`
---

# 🗳️ Vote System API

A secure online voting system built with **FastAPI** and **MongoDB**.  
Supports poll creation, Aadhaar-verified voting, vote counting, and winner declaration.

---

## 🚀 Features

- Create polls with custom options and duration
- Cast votes with Aadhaar number validation
- Prevent duplicate voting
- Count votes per option
- Declare winner or detect tie
- Environment-based MongoDB configuration

---

## 🛠️ Tech Stack

| Layer      | Technology        |
|------------|-------------------|
| Backend    | FastAPI (Python)  |
| Database   | MongoDB           |
| Validation | Pydantic          |
| ODM        | PyMongo           |
| Config     | python-dotenv     |

---

## 📁 Project Structure
vote/   
├── app/   
│   ├── db/   
│   │   └── vote_db.py   
│   ├── models/   
│   │   └── vote_schemas.py   
│   ├── routes/   
│   │   ├── poll_routes.py   
│   │   └── vote_routes.py   
│   ├── services/   
│   │   ├── poll_service.py   
│   │   └── vote_service.py   
│   └── main.py     
├── .venv   
├── requirements.txt   
└── README.md   

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/saisunderteja/vote.git
cd vote
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create `.env` file
```env
MONGO_URI=mongodb://localhost:27017/
```

### 5. Run the server
```bash
uvicorn app.main:app --reload
```

### 6. Open API docs
http://127.0.0.1:8000/docs 

---

## 📌 API Endpoints

### Poll

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/create_poll` | Create a new poll |

#### Request Body
```json
{
  "question": "Who should be the next president?",
  "options": ["Alice", "Bob", "Charlie"],
  "duration": 3600
}
```

#### Response
```json
{
  "poll_id": "664f1a2b3c4d5e6f7a8b9c0d"
}
```

---

### Vote

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/vote` | Cast a vote |
| GET | `/count_votes/{poll_id}` | Get vote counts |
| GET | `/winner/{poll_id}` | Get poll winner |

#### Cast Vote Request Body
```json
{
  "poll_id": "664f1a2b3c4d5e6f7a8b9c0d",
  "first_name": "Ravi",
  "last_name": "Kumar",
  "phone_number": "9876543210",
  "aadhar_number": "234567890123",
  "choice": "Alice"
}
```

#### Count Votes Response
```json
{
  "poll_id": "664f1a2b3c4d5e6f7a8b9c0d",
  "results": {
    "Alice": 42,
    "Bob": 20,
    "Charlie": 13
  }
}
```

#### Winner Response
```json
{
  "message": "Winner announced!",
  "winning_option": "Alice",
  "votes": 42,
  "total_votes": 75,
  "all_results": {
    "Alice": 42,
    "Bob": 20,
    "Charlie": 13
  }
}
```

---

## 🔒 Validations

- ✅ Aadhaar must be 12 digits and start with 1–9
- ✅ Phone number must be valid Indian mobile format (starts with 6–9)
- ✅ One vote per Aadhaar per poll
- ✅ Voting only allowed within poll time window
- ✅ Choice must match one of the poll options

---

## 🌱 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MONGO_URI` | MongoDB connection string | `mongodb://localhost:27017/` |

---

## 👨‍💻 Author

**Sai Sunder Teja Ryagalla**  
📧 saisunderteja999@gmail.com.com  
🔗 [GitHub](https://github.com/saisunderteja)

---
