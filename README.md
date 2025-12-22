# API-INTEGRATION-AND-DATA-VISUALIZATION

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SAKHARAM SAWANT

*INTERN ID*: CT04DR2481

*DOMAIN*: PYTHON PROGRAMMING

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTHOSH

📧 Task 4: Spam Email Classification using Machine Learning
📌 Introduction

This project has been developed as part of the CODTECH Python Programming Internship. Task 4 focuses on implementing a predictive machine learning model using Scikit-learn to classify text-based data. In this task, a Spam Email Classification System is created to determine whether a given email message is Spam or Not Spam (Ham).

Spam detection is one of the most common and practical applications of machine learning in real-world systems. It plays a crucial role in enhancing email security, improving user experience, and protecting users from fraudulent or unwanted content. This project provides hands-on exposure to building a complete machine learning pipeline for text classification.

The task aims to strengthen understanding of supervised learning concepts and the practical use of machine learning libraries in Python.

🎯 Objective

The main objectives of this task are:

To understand the fundamentals of supervised machine learning

To implement a text classification model using Scikit-learn

To convert raw text data into numerical features suitable for machine learning models

To train and evaluate a classification algorithm

To test the trained model using new and unseen email messages

To gain practical experience with an end-to-end machine learning workflow

🛠️ Tools and Technologies Used

The following tools and technologies were used in this project:

Python – for implementing the machine learning logic

Pandas – for creating, managing, and preprocessing the dataset

Scikit-learn – for model training, evaluation, and prediction

CountVectorizer – for transforming text data into numerical feature vectors

Multinomial Naive Bayes – as the classification algorithm

Jupyter Notebook – for interactive coding and result visualization

📊 Dataset Description

A small text-based dataset was created for demonstration purposes. The dataset consists of short email messages labeled as either spam or ham.

Spam emails include promotional, prize-related, or suspicious messages.

Ham emails represent normal, personal, or informational messages.

The textual labels are converted into numerical values so that the machine learning model can process them effectively. This dataset serves as a simple but effective example for understanding text classification.

⚙️ Model Implementation

The implementation follows a structured machine learning workflow:

The dataset is loaded into a Pandas DataFrame

The data is split into training and testing sets to evaluate model performance

Since machine learning models cannot directly process text, CountVectorizer is used to convert text into numerical features based on word frequency

A Multinomial Naive Bayes classifier is trained using the vectorized training data

Multinomial Naive Bayes is particularly suitable for text classification tasks due to its simplicity, efficiency, and strong performance with word-count features.

After training, the model is evaluated using:

Accuracy Score

Classification Report

These metrics help assess how well the model performs on unseen data.

📈 Results and Output

The trained model successfully classifies email messages as spam or not spam with good accuracy on the sample dataset. The Jupyter Notebook displays evaluation metrics and prediction results in a clear and understandable format.

Additionally, the model is tested using a custom email message, demonstrating its ability to make real-time predictions. An output screenshot has been included in the repository to showcase the final results.

✅ Conclusion

This task demonstrates the practical application of machine learning concepts for text classification using Scikit-learn. It provides hands-on experience in data preparation, feature extraction, model training, evaluation, and prediction.

The project successfully fulfills the requirements of Task 4 of the CODTECH Python Programming Internship and serves as a foundational example of implementing a spam detection system using machine learning in Python.

*OUTPUT*: <img width="1919" height="1018" alt="Image" src="https://github.com/user-attachments/assets/f9202c90-a71b-4ebc-88ff-9ba8f38df4ca" />
