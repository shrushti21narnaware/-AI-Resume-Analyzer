 🚀 AI Resume Analyzer Pro

An intelligent" ATS (Applicant Tracking System) Resume Analyzer" built using Streamlit + OpenRouter AI.
This app compares your resume with a job description and provides insights like match score, missing skills, and improvement suggestions.

 📌 Features

 📂 Upload Resume (PDF)
 🧠 AI-powered Resume Analysis
 📊 Match Percentage Score
 📉 Missing Skills Identification
 💡 Improvement Suggestions
 📌 Final Verdict
 ⚡ Clean & Interactive UI (Streamlit)

---

🛠️ Tech Stack

Frontend: Streamlit
Backend: Python
AI API: OpenRouter (LLM integration)
PDF Parsing: PyPDF2


📂 Project Structure

genai_resume_analyzer/
│── app.py              # Streamlit UI
│── utils.py            # Core logic (AI + PDF extraction)
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```


 ⚙️ Installation & Setup

 1️⃣ Clone the repository

```
git clone https://github.com/your-username/genai_resume_analyzer.git
cd genai_resume_analyzer
```

 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

 3️⃣ Add API Key

Create a `.streamlit/secrets.toml` file and add:

```
OPENROUTER_API_KEY = "your_api_key_here"
```

---

▶️ Run the App

```
streamlit run app.py
```

---

 🌐 Live Demo

👉 (Add your deployed link here after hosting)

---

 📊 How It Works

1. Upload your resume (PDF)
2. Paste job description
3. AI compares both using LLM
4. Get:

   * Match Score (%)
   * Missing Skills
   * Suggestions
   * Final Evaluation

---

 🎯 Use Cases

* Students preparing for placements
* Job seekers optimizing resumes
* Quick ATS compatibility check

---

 ⚠️ Limitations

* PDF parsing may fail for scanned resumes
* AI output depends on prompt quality
* Requires internet connection for API

---

 🚀 Future Improvements

 📊 Skill match visualization (charts)
 📄 Support for DOCX resumes
 🧠 Keyword highlighting
 🌐 Deploy with custom domain
 📈 Resume scoring breakdown

---

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first.



📜 License

This project is for educational purposes.

---

👩‍💻 Author

Shrushti Narnaware
Aspiring Data Scientist & AI Enthusiast

---

⭐ If you like this project, give it a star on GitHub!
