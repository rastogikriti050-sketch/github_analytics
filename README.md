# 🚀 GitHub Analytics Dashboard

An interactive web application that analyzes GitHub user data and presents meaningful insights through dynamic visualizations.

---

## 📌 Project Overview

This project allows users to enter a GitHub username and fetches real-time data using the GitHub REST API. The data is then processed and visualized using interactive charts to provide insights into user activity, repository performance, and technology usage.

---

## 🎯 Objectives

•⁠  ⁠To analyze GitHub user data
•⁠  ⁠To visualize repository insights effectively
•⁠  ⁠To build an interactive dashboard using modern tools
•⁠  ⁠To integrate DevOps practices like containerization and CI/CD

---

## 🔥 Features

•⁠  ⁠🔍 Search any GitHub user
•⁠  ⁠📊 Language distribution (Pie Chart)
•⁠  ⁠⭐ Repository performance (Stars & Forks)
•⁠  ⁠📈 Repository creation timeline
•⁠  ⁠🔥 Activity heatmap visualization
•⁠  ⁠📦 Total repositories, stars, and forks
•⁠  ⁠🏆 Top repository detection
•⁠  ⁠⚡ Real-time API data fetching

---

## 🧠 Key Insights Generated

•⁠  ⁠Most used programming languages
•⁠  ⁠Most popular repositories
•⁠  ⁠User activity trends over time
•⁠  ⁠Repository creation patterns
•⁠  ⁠Overall GitHub engagement

---

## 🛠️ Tech Stack

### 🔹 Frontend & App Framework

•⁠  ⁠Streamlit

### 🔹 Data Processing

•⁠  ⁠Pandas

### 🔹 Visualization

•⁠  ⁠Plotly

### 🔹 API

•⁠  ⁠GitHub REST API

### 🔹 DevOps

•⁠  ⁠Docker
•⁠  ⁠GitHub Actions (CI/CD)

---

## 🏗️ System Architecture

User Input → Streamlit App → GitHub API → Data Processing → Visualization

---

## 📊 Visualizations Included

•⁠  ⁠Pie Chart (Language Distribution)
•⁠  ⁠Bar Charts (Stars & Forks)
•⁠  ⁠Line Chart (Timeline)
•⁠  ⁠Heatmap (Activity Patterns)

---
## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

bash
git clone https://github.com/rastogikriti050-sketch/github_analytics.git
cd github_analytics


### 2️⃣ Install dependencies

bash
pip install -r requirements.txt


### 3️⃣ Run the application

bash


## 🐳 Docker Setup

bash
docker build -t github-analytics .
docker run -p 8501:8501 github-analytics


---

## 🔄 CI/CD Pipeline

* Automated build using GitHub Actions
* Docker image creation on push
* Continuous integration workflow

---

## 📸 Screenshots

<img width="1249" height="569" alt="image" src="https://github.com/user-attachments/assets/cd2fc515-e2f2-4471-944b-09b314ac8633" />
<img width="1321" height="530" alt="image" src="https://github.com/user-attachments/assets/744bc4a6-ffa7-45b6-818c-f0ea93999082" />

<img width="1290" height="569" alt="image" src="https://github.com/user-attachments/assets/71aeac10-f55a-4e64-9c03-4f0f5c6cd3ec" />


<img width="1325" height="551" alt="image" src="https://github.com/user-attachments/assets/ecbd343d-de0d-419a-b48e-5a3faa53fd17" /><img width="1291" height="513" alt="image" src="https://github.com/user-attachments/assets/472b8b2c-9614-46ff-ba2a-5c8e39086bb9" />


<img width="1305" height="463" alt="image" src="https://github.com/user-attachments/assets/dfdde44b-117b-4128-ba95-b38bac19d6e0" />









---

## ⚠️ Limitations

* GitHub API rate limits
* Heatmap is based on repository creation (not actual commits)
* Limited historical contribution data

---

## 🚀 Future Enhancements

* Compare multiple GitHub users
* Add authentication (GitHub token)
* Real contribution heatmap using GraphQL API
* Export analytics as PDF
* Deploy on cloud (Render/AWS)

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

* GitHub: https://github.com/rastogikriti050-sketch

---

## 💡 Conclusion

This project enhances GitHub’s default interface by providing deeper analytical insights through interactive visualizations, making it easier to understand user activity and repository trends.
streamlit run app.py


---

