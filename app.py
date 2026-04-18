import streamlit as st
from utils import extract_text_from_pdf, analyze_resume
import re

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# 🎨 Custom Styling
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Header
st.title("🚀 AI Resume Analyzer Pro")
st.markdown("### Smart ATS Resume Screening Dashboard")

# Layout
col1, col2 = st.columns([1, 1])

with col1:
    uploaded_file = st.file_uploader("📂 Upload Resume (PDF)", type=["pdf"])

with col2:
    job_desc = st.text_area("📝 Paste Job Description", height=200)

# Resume preview
if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    
    with st.expander("📑 Preview Resume Text"):
        st.write(resume_text[:2000] + "...")

# Analyze
if st.button("🔍 Analyze Resume", use_container_width=True):

    if uploaded_file and job_desc:
        with st.spinner("Running AI Analysis... 🤖"):

            resume_text = extract_text_from_pdf(uploaded_file)
            result = analyze_resume(resume_text, job_desc)

        st.success("✅ Analysis Complete")

        # 🎯 Extract match %
        match = re.search(r'(\d{1,3})\s*%', result)
        score = int(match.group(1)) if match else 60

        # 📊 Metrics Row
        m1, m2, m3 = st.columns(3)

        m1.metric("📊 Match Score", f"{score}%")
        m2.metric("📄 Resume Length", f"{len(resume_text.split())} words")
        m3.metric("🧠 JD Length", f"{len(job_desc.split())} words")

        # Progress bar
        st.progress(score / 100)

        # 🔍 Structured Sections
        st.markdown("---")

        colA, colB = st.columns(2)

        with colA:
            st.subheader("📉 Missing Skills")
            missing = re.findall(r'Missing Skills[:\-]*([\s\S]*?)(Suggestions|Final Verdict)', result, re.IGNORECASE)
            st.write(missing[0][0] if missing else result)

        with colB:
            st.subheader("💡 Suggestions")
            suggestions = re.findall(r'Suggestions[:\-]*([\s\S]*?)(Final Verdict)', result, re.IGNORECASE)
            st.write(suggestions[0][0] if suggestions else result)

        st.markdown("---")

        st.subheader("📌 Final Verdict")
        verdict = re.findall(r'Final Verdict[:\-]*([\s\S]*)', result, re.IGNORECASE)
        st.write(verdict[0] if verdict else result)

    else:
        st.warning("⚠️ Please upload resume and enter job description")