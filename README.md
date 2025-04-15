📰 Fake News Detector using SVM Model
A Machine Learning-based Fake News Detector that classifies news articles as Fake (0) or True (1) using a Support Vector Classifier (SVC) model. The project includes a simple chatbot interface where users can input a news statement and receive instant classification results.

🚀 Project Overview
In this project, a dataset containing news descriptions and their labels (1 for True, 0 for Fake) was used to train an SVM model. After training, the model was integrated into a chatbot-like application that allows users to input news text and receive predictions about its authenticity.

💡 Features
Binary classification of news as True (1) or Fake (0).

Simple and intuitive chatbot interface for interaction.

Machine Learning model built using Support Vector Machine (SVC).

Preprocessed real-world dataset.

Modular and clean Python code.

🧑‍💻 Technologies Used
Python

scikit-learn

pandas

NumPy

Flask (for chatbot/web interface)

HTML, CSS (for front-end if applicable)

📂 Dataset Structure

Description	Label
"The government has announced a new policy to tackle climate change."	1
"Aliens have landed in New York and met the president."	0
Description: Text content of the news.

Label: 1 (True) / 0 (Fake).

⚙️ How It Works
Data Preprocessing

Clean and vectorize the news text using TfidfVectorizer.

Model Training

Train a Support Vector Classifier (SVC) on the labeled dataset.

Prediction

User inputs a news statement via chatbot.

The model predicts whether the statement is likely True (1) or Fake (0).

🧑‍🏫 Setup Instructions
Clone the Repository
git clone https://github.com/your-username/fake-news-detector.git
cd fake-news-detector
Install Dependencies
pip install -r requirements.txt
Run the Application
python app.py
Open your web browser and go to:
http://127.0.0.1:5000/

💬 Sample Usage
Input: "The stock market hits record highs amid economic recovery."

Output: Predicted: True News ✅

📊 Model Evaluation
Accuracy: 95.30%

F1 Score: 0.94

Test Results: Consistent performance on unseen data.

📌 Future Improvements
Expand the dataset for better generalization.

Implement sentiment analysis for deeper context understanding.

Add database support for user queries and history.

Enhance the chatbot UI using JavaScript frameworks.
