# 🚨 DDoS Attack Detection & Prediction

This project is a **Machine Learning based DDoS (Distributed Denial of Service) Attack Detection System**.  
It uses **XGBoost Classifier** to analyze network traffic data and classify flows as **Benign** or **DDoS Attack**.  
A **Streamlit web app** is provided for easy interaction and real-time predictions.

---

## 📌 Features
- 🧹 **Data Preprocessing** – Cleaned raw traffic datasets and removed unnecessary columns.  
- 🤖 **ML Model (XGBoost)** – Trained for high accuracy on binary classification (Benign vs DDoS).  
- 📊 **Evaluation Metrics** – Accuracy, Confusion Matrix, Classification Report.  
- 🌐 **Web App (Streamlit)** – Upload CSV traffic files and get predictions instantly.  
- 🔎 **Attacker Detection Script** – Optional script (`detect_attackers.py`) to trace suspicious IP addresses.  

---

## 🛠️ Tech Stack
- **Python 3.12**  
- **Pandas / NumPy** – Data handling  
- **Scikit-learn** – Preprocessing & metrics  
- **XGBoost** – ML model  
- **Joblib** – Model saving/loading  
- **Streamlit** – Web application interface  

---

## 📂 Project Structure
DDOS-CLASSIFICATION_AND_PREDICTION/
│
├── app/
│ ├── app.py # Streamlit Web App
│ ├── ddos_xgb_model.pkl # Trained XGBoost model
│ └── detect_attackers.py # Script for attacker detection
│
├── Dataset/ # Network traffic datasets (CSV)
├── notebooks/ # Jupyter notebooks (data preprocessing & experiments)
├── models/ # Saved/alternate models
├── reports/ # Reports, logs, results
├── requirements.txt # Dependencies
└── README.md # Project documentation

## ⚡ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/DDOS-CLASSIFICATION_AND_PREDICTION.git
cd DDOS-CLASSIFICATION_AND_PREDICTION
2️⃣ Create Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Requirements
pip install -r requirements.txt
🚀 Usage
🔹 Train the Model (optional if .pkl already exists)
python evaluate_model.py

🔹 Run Attacker Detection Script
python app/detect_attackers.py

🔹 Launch Web App
streamlit run app/app.py


👉 Open your browser at: http://localhost:8501

📊 Example Output

Prediction Results in Web App:

🟢 Benign

🔴 DDoS Attack

Confusion Matrix & Accuracy shown in console during training.

📌 Future Improvements

Multi-class classification for different types of attacks.

Integration with real-time packet capture (using Scapy).
👨‍💻 Author
P. Raga Sai Harsha 
https://github.com/Varshapolamarasetty
