# IPL Win Predictor - Machine Learning Web App

This project predicts the win probability of an IPL match based on live inputs such as batting team, bowling team, city, overs completed, wickets lost, and target. The prediction is made using a **Logistic Regression model** trained on historical IPL data and deployed as a web application using **Streamlit**, built in **PyCharm**, and hosted via **GitHub**.

---

## Features
- Select **batting** and **bowling teams**
- Choose the **match venue (city)**
- Enter **target**, **current score**, **overs completed**, and **wickets lost**
- Instantly view **win probability** of both teams
- Clean and user-friendly interface
- Live demo powered by Streamlit Cloud


## Machine Learning
### Algorithm Used
- **Logistic Regression** (Binary Classification)
  - Predicts probability of match outcome (Win vs Loss)
  - Suitable for binary outcome with probabilities
- **OneHotEncoder**

### Input Features
- Batting team
- Bowling team
- City (venue)
- Target score
- Current score (used to compute runs left)
- Overs completed
- Wickets lost (used to compute wickets left)
- Derived features: `runs_left`, `balls_left`, `current_rr`, `required_rr`


### Preprocessing
- Categorical Encoding using **ColumnTransformer** and **OneHotEncoder**
- Feature Scaling using **StandardScaler** or left as-is
- Final model: `Pipeline(ColumnTransformer + LogisticRegression)`

---

## Tech Stack

| Tool           | Purpose                          |
|----------------|----------------------------------|
| Python         | Core language                    |
| Pandas         | Data preprocessing               |
| scikit-learn   | Model training and pipeline      |
| Streamlit      | Web app frontend & deployment    |
| PyCharm        | Local development environment    |
| GitHub         | Code hosting and version control |
| Streamlit Cloud| Final web deployment             |

---

