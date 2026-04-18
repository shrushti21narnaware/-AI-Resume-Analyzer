from openai import OpenAI
import PyPDF2
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def analyze_resume(resume_text, job_desc):
    prompt = f"""
    Compare the resume with the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_desc}

    Give:
    - Match score
    - Missing skills
    - Suggestions
    """

    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",   # safe working model
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content