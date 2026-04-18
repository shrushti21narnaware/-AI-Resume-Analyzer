# utils.py

from openai import OpenAI
import PyPDF2

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="your_new_key_here"
)

def extract_text_from_pdf(uploaded_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    for page in pdf_reader.pages:
        text += page.extract_text() or ""

    return text


def analyze_resume(resume_text, job_desc):
    prompt = f"""
You are an ATS system.

Compare the resume with the job description.

Resume:
{resume_text}

Job Description:
{job_desc}

Give:
1. Match Percentage
2. Missing Skills
3. Improvement Suggestions
4. Final Verdict
"""

    try:
        response = client.chat.completions.create(
            model="openrouter/auto",   # 🔥 FINAL FIX
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"API Error: {str(e)}"
