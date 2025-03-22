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

