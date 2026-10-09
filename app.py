import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")
st.write("Welcome! Upload your resume to get started.")

resume = st.file_uploader("Upload your resume", type=["pdf", "txt"])
job_role = st.text_input("Enter the job role you want to apply for")

if st.button("Analyze Resume"):
    if resume is not None and job_role:
        st.success("Resume uploaded successfully!")
        st.write("Target Job Role:", job_role)
        st.info("Next step: We will add resume skills analysis.")
    else:
        st.warning("Please upload your resume and enter a job role.")

