"""
JobHunt Agent — Streamlit Web UI
Run: streamlit run app.py
"""
import streamlit as st
import os
from agent import create_jobhunt_agent
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="JobHunt Agent", page_icon="🎯", layout="wide")

st.title("🎯 JobHunt Agent")
st.markdown("##### Multi-step AI Agent for Job Applications | Built by **Mayur More**")
st.markdown("*LangChain · OpenAI GPT-4 · Agentic AI · Streamlit*")
st.divider()

with st.expander("How this Agent works (5 automated steps)"):
    st.markdown("""
    1. **Extract Skills** — Parses the JD for required skills & experience  
    2. **Gap Analysis** — Compares JD with your profile, finds matches & gaps  
    3. **Company Research** — Gathers context about the target company  
    4. **Cover Letter** — Writes a tailored, human-sounding cover letter  
    5. **Interview Prep** — Role-specific questions & study cheat sheet  
    """)

col1, col2 = st.columns([3, 2])
with col1:
    st.subheader("📋 Job Details")
    company_name = st.text_input("Company Name", placeholder="e.g. Google, Anthropic, Cohere...")
    job_description = st.text_area("Paste Job Description", height=260,
        placeholder="Paste the full job description here...")

with col2:
    st.subheader("👤 Your Profile")
    candidate_profile = st.text_area("Your Skills & Experience", height=260,
        placeholder="e.g. 1+ year Gen AI, LangChain, OpenAI API, RAG, Python...")

api_key = st.sidebar.text_input("🔑 OpenAI API Key", type="password")
st.sidebar.markdown("---")
st.sidebar.markdown("### Agent Tools")
for t in ["extract_skills_from_jd", "analyze_skill_gap", "research_company",
          "generate_cover_letter", "generate_interview_prep"]:
    st.sidebar.markdown(f"- `{t}`")
st.sidebar.markdown("---")
st.sidebar.markdown("**Mayur More** | [GitHub](https://github.com/mayurmoreabc)")

if st.button("🚀 Run JobHunt Agent", type="primary", use_container_width=True):
    if not all([api_key, job_description.strip(), candidate_profile.strip(), company_name.strip()]):
        st.error("Please fill in all fields and add your API key in the sidebar.")
    else:
        os.environ["OPENAI_API_KEY"] = api_key
        with st.spinner("🤖 Agent running 5 steps... (~60 seconds)"):
            try:
                agent = create_jobhunt_agent()
                result = agent.invoke({"input": f"""Run full pipeline:
COMPANY: {company_name}
JOB: {job_description}
MY PROFILE: {candidate_profile}"""})
                st.success("✅ All 5 steps complete!")
                st.divider()
                tab1, tab2 = st.tabs(["📄 Output", "💾 Copy"])
                with tab1:
                    st.markdown(result["output"])
                with tab2:
                    st.code(result["output"], language="markdown")
            except Exception as e:
                st.error(f"Error: {e}")