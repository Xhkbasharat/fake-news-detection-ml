"Animated Header" (https://capsule-render.vercel.app/api?type=waving&color=0:090979,50:302b63,100:00d4ff&height=220&section=header&text=FAKE%20NEWS%20DETECTOR&fontSize=38&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=AI%20%7C%20NLP%20%7C%20MACHINE%20LEARNING&descAlignY=58&descSize=16)

"Typing SVG" (https://readme-typing-svg.demolab.com?font=Orbitron&weight=600&size=22&duration=2500&pause=700&color=00D4FF&center=true&vCenter=true&width=650&lines=Detect+Fake+News+with+Machine+Learning;Powered+by+TF-IDF+and+Logistic+Regression;Explore+NLP+with+an+Interactive+Dashboard)

"Python" (https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python)
"Streamlit" (https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit)
"Scikit Learn" (https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn)
"License" (https://img.shields.io/badge/License-MIT-00C853?style=for-the-badge)

📰 Fake News Detection Using Machine Learning

An NLP-based project that classifies news articles as FAKE or REAL using TF-IDF and Logistic Regression.

---

✨ Features

- 🧠 Fake and real news classification
- ⚡ Text cleaning and preprocessing
- 📊 TF-IDF feature extraction
- 🎯 Logistic Regression model
- 📈 Prediction confidence score
- 🌐 Interactive Streamlit application
- 🧪 Automated tests with GitHub Actions

🛠️ Technology Stack

"Python" (https://skillicons.dev/icons?i=python)
"Git" (https://skillicons.dev/icons?i=git)
"GitHub" (https://skillicons.dev/icons?i=github)
"Docker" (https://skillicons.dev/icons?i=docker)

- Python
- Pandas and NumPy
- Scikit-learn
- NLP and TF-IDF
- Streamlit
- Pytest
- Docker

🏗️ Architecture

flowchart TD
    A["📰 News Article"] --> B["Text Preprocessing"]
    B --> C["TF-IDF Vectorization"]
    C --> D["Logistic Regression"]
    D --> E{"Prediction"}
    E -->|Fake| F["⚠️ Fake News"]
    E -->|Real| G["✅ Real News"]
    F --> H["Confidence Score"]
    G --> H
    H --> I["Streamlit Dashboard"]

📂 Project Structure

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

🚀 Installation

1. Clone repository

git clone https://github.com/Xhkbasharat/fake-news-detection-ml.git
cd fake-news-detection-ml

2. Install dependencies

pip install -r requirements.txt

3. Prepare dataset

Create "data/news.csv" with these columns:

text| label
News article text| real
News article text| fake

4. Train model

python -m training.train

5. Launch application

streamlit run app/streamlit_app.py

🧪 Testing

python -m pytest

GitHub Actions automatically runs tests when changes are pushed to the main branch.

🔮 Future Improvements

- [ ] Larger verified news dataset
- [ ] Better model evaluation
- [ ] Advanced NLP models
- [ ] Interactive prediction dashboard
- [ ] News source analysis
- [ ] Public deployment
- [ ] Model performance charts

⚠️ Disclaimer

This is an educational machine-learning project. Predictions are not verified fact-checks and should not be treated as proof that an article is true or false.

👨‍💻 Developer

Xhkbasharat

""GitHub" (https://img.shields.io/badge/GitHub-Xhkbasharat-181717?style=for-the-badge&logo=github)" (https://github.com/Xhkbasharat)

---

"Animated Footer" (https://capsule-render.vercel.app/api?type=waving&color=0:00d4ff,50:302b63,100:090979&height=120&section=footer)
