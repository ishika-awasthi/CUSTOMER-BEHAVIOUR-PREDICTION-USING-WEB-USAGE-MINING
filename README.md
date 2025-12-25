# Customer Behaviour Prediction using Web Usage Mining

## 📌 Project Overview

This project focuses on **predicting customer behaviour** (purchase intention) using **web usage data**.
By analyzing user browsing patterns, session details, and interaction metrics, a machine learning model is trained to predict whether a customer is likely to make a purchase.

This project demonstrates the practical application of **Web Usage Mining and Machine Learning** concepts.

---

## 🎯 Problem Statement

Businesses collect large amounts of web usage data but often fail to utilize it effectively.
The objective of this project is to:

* Analyze customer browsing behaviour
* Build predictive models
* Identify users with high purchase intent

---

Here is a **clear, academic, ready-to-paste Dataset Description** section.
You can use it **as-is** in your report or README.

---

## 📂 Dataset Description

The **Online Shoppers Purchasing Intention Dataset** contains real-world e-commerce session data collected from an online retail website. Each record represents a **single user session**, capturing browsing behavior, interaction patterns, and session characteristics.

The dataset is primarily used to predict whether a visitor will generate **revenue (make a purchase)** during the session, making it suitable for **customer behaviour analysis and web usage mining**.

---

### 📊 Dataset Characteristics

* **Number of Instances:** 12,330 user sessions
* **Number of Features:** 18
* **Target Variable:** `Revenue` (Boolean: Purchase / No Purchase)
* **Data Type:** Structured tabular data
* **Domain:** E-commerce / Web Analytics

---

### 🧾 Feature Categories

**1. Page Interaction Features**

* `Administrative`, `Administrative_Duration`
* `Informational`, `Informational_Duration`
* `ProductRelated`, `ProductRelated_Duration`
  These features represent the number of pages visited and the time spent on different page types.

**2. Behavioural Metrics**

* `BounceRates`
* `ExitRates`
* `PageValues`
* `SpecialDay`
  These metrics describe user engagement and likelihood of conversion.

**3. Session & User Attributes**

* `OperatingSystems`
* `Browser`
* `Region`
* `TrafficType`
* `VisitorType`
* `Weekend`

---

### 🎯 Target Variable

* **`Revenue`**

  * `True` → User completed a purchase
  * `False` → No purchase made

---

### 📌 Dataset Purpose

The dataset is designed to:

* Analyze customer browsing behaviour
* Identify patterns leading to purchase decisions
* Support predictive modeling using machine learning techniques


---


### Key Features:

* Administrative, Informational, ProductRelated pages
* BounceRates, ExitRates
* PageValues, SpecialDay
* VisitorType, Weekend
* **Target Variable:** Revenue (Purchase / No Purchase)

---

## ⚙️ Technologies Used

* **Programming Language:** Python
* **Libraries:**

  * NumPy
  * Pandas
  * Matplotlib
  * Seaborn
  * Scikit-learn
* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Flask
* **IDE:** Google Colab / VS Code

---

## 🧠 Machine Learning Models Used

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* K-Nearest Neighbors (KNN)

Each model is evaluated using accuracy and performance metrics.

---

## 🔄 Project Workflow

1. Data Loading
2. Data Preprocessing

   * Handling missing values
   * Encoding categorical features
   * Feature scaling
3. Exploratory Data Analysis (EDA)
4. Model Training
5. Model Evaluation
6. Frontend Integration (Demo Interface)

---

## ▶️ How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ishika-awasthi/customer-behaviour-prediction-web-usage-mining.git
cd customer-behaviour-prediction-web-usage-mining
```

### 2️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
python app.py
```

### 4️⃣ Open in Browser

```
http://127.0.0.1:5000/
```

---

## 📊 Results

* The models successfully predict customer purchase intention.
* Random Forest achieved higher accuracy compared to other classifiers due to its ensemble learning approach.
* The project demonstrates how web usage data can support business decision-making.

---

## 🚀 Future Enhancements

* Real-time data collection from website logs
* Database integration (MySQL / Firebase)
* User authentication
* Deployment on cloud (Heroku / AWS)
* Improved UI/UX

---

## 👥 Team Members
- Ishika Awasthi – Machine Learning, Data Analysis
- Mishti Verma – Frontend and Backend Development


---

## 📌 Conclusion

This project effectively combines **machine learning and web usage mining** to predict customer behaviour.
It serves as a strong foundation for advanced analytics and real-world e-commerce applications.

---

