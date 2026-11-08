Fake News Detection Using Machine Learning

A machine learning project that detects whether a news article is fake or real using Natural Language Processing (NLP).

Features

- Fake and real news classification
- Text preprocessing and cleaning
- TF-IDF vectorization
- Logistic Regression model
- Prediction confidence score
- Streamlit web application
- Automated testing with GitHub Actions

Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit
- Joblib
- Pytest

Project Structure

fake-news-detection-ml/
├── app/
│   ├── __init__.py
│   └── streamlit_app.py
├── data/
│   └── news.csv
├── models/
│   └── .gitkeep
├── src/
│   ├── __init__.py
│   ├── preprocess.py
│   └── predict.py
├── training/
│   └── train.py
├── tests/
│   ├── __init__.py
│   └── test_model.py
├── .github/workflows/
│   └── tests.yml
├── app.py
├── requirements.txt
├── Dockerfile
├── runtime.txt
├── .gitignore
└── LICENSE

Installation

Clone the repository:

git clone https://github.com/Xhkbasharat/fake-news-detection-ml.git
cd fake-news-detection-ml

Install dependencies:

pip install -r requirements.txt

Dataset

The dataset should be stored in "data/news.csv" with two columns:

Column| Description
text| News article text
label| fake or real

A larger verified dataset is needed for meaningful model evaluation.

Train the Model

python -m training.train

The trained model will be saved in:

"models/fake_news_model.pkl"

Run the Application

streamlit run app/streamlit_app.py

Run Tests

python -m pytest

Future Improvements

- Use a larger news dataset
- Improve model accuracy and evaluation
- Add advanced NLP models
- Create an interactive dashboard
- Deploy the application online

Disclaimer

This project is developed for educational purposes. Predictions are not verified fact-checks and should not be considered proof that an article is true or false.

Author

Xhkbasharat

GitHub: https://github.com/Xhkbasharat

License

This project is licensed under the MIT License.
