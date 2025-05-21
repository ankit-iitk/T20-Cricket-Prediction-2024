# 🏏 T20 Cricket Match Prediction 2024 using Machine Learning

This project predicts the outcomes of T20 cricket matches (2024 season) using machine learning models. It uses historical match data and current team statistics to build a predictive model that forecasts match winners.

---

##  Project Overview

Cricket is a game filled with uncertainties. With the rise of data-driven strategies, this project aims to harness machine learning techniques to predict the outcomes of T20 matches for the 2024 season.

### Key Objectives:
- Analyze historical T20 data
- Engineer relevant features (team strength, toss, venue, player performance, etc.)
- Train classification models to predict the match winner
- Evaluate performance using appropriate metrics
- (Optional) Deploy as a web app using Streamlit

---

## Project Structure
t20-cricket-prediction-2024/
│
├── data/
│ ├── deliveries.csv
├── notebooks/
│ └── ML_Project_Cricket_Score_Prediction.ipynb
├── models/
│ └── pipeline.pkl
├── app/
│ └── app.py
├── requirements.txt
├── README.md
└── .gitignore

##  Technologies Used

- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- XGBoost (optional)
- Streamlit (for web app)
- Jupyter Notebook

---


##  How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/ankit-iitk/T20-Cricket-Prediction-2024.git
   cd t20-cricket-prediction-2024
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
4. **Run the Jupyter Notebook**
   ```bash
   jupyter notebook notebooks/ML_Project_Cricket_Score_Prediction.ipynb
5. **Run the web app**
   ```bash
   streamlit run app.py
