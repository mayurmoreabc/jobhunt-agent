"""
JobHunt Agent — Multi-step AI Agent for Job Application Automation
Author: Mayur More | github.com/mayurmoreabc
"""

import os
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

@tool
def extract_skills_from_jd(job_description: str) -> str:
    """Extracts required technical skills, experience, and responsibilities from a job description."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = f"""Analyze this job description and extract:
1. Required technical skills (list each)
2. Preferred/bonus skills (list each)
3. Years of experience required
4. Key responsibilities (top 5)
5. Seniority level

Job Description: {job_description}

Return as a clean structured list."""
    return llm.invoke(prompt).content


@tool
def analyze_skill_gap(jd_skills: str, candidate_skills: str) -> str:
    """Compares job description skills with candidate skills. Returns matches, gaps, and recommendations."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    prompt = f"""Compare these skill sets:

REQUIRED BY JOB: {jd_skills}
CANDIDATE HAS: {candidate_skills}

Provide:
1. Skills the candidate ALREADY has
2. Skills the candidate is MISSING
3. Quick recommendations to bridge the gaps
4. Overall match percentage (estimate)"""
    return llm.invoke(prompt).content


@tool
def research_company(company_name: str) -> str:
    """Researches a company and returns key facts for cover letters and interview prep."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.3)
    prompt = f"""Provide a research summary about "{company_name}" covering:
1. What the company does
2. Company culture and values
3. Recent news or achievements
4. Why an AI Engineer might want to work there
5. 2-3 smart interview questions to ask them"""
    return llm.invoke(prompt).content


@tool
def generate_cover_letter(context: str) -> str:
    """Generates a tailored, professional cover letter. Context should include job title, company, and candidate background."""
    llm = ChatOpenAI(model="gpt-4", temperature=0.7)
    prompt = f"""Write a compelling, professional cover letter (NOT generic).

Context: {context}

Requirements:
- 3-4 paragraphs, ~300 words
- Opening: Genuine enthusiasm + something specific about the company
- Middle: Connect 2-3 specific skills to the role
- Closing: Clear call to action
- Tone: Professional but human

Start with: Dear Hiring Manager,"""
    return llm.invoke(prompt).content


@tool
def generate_interview_prep(job_title: str, required_skills: str, company_name: str) -> str:
    """Creates a tailored interview prep cheat sheet with questions, answers, and key topics."""
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
    prompt = f"""Create an interview prep cheat sheet for a {job_title} role at {company_name}.
Required Skills: {required_skills}

Include:
1. Top 5 technical questions with answer guidance
2. Top 3 behavioral questions (STAR format hints)
3. Key concepts to revise
4. 3 smart questions to ask the interviewer
5. "Tell me about yourself" one-liner starter"""
    return llm.invoke(prompt).content


def create_jobhunt_agent():
    llm = ChatOpenAI(model="gpt-4", temperature=0)
    tools = [extract_skills_from_jd, analyze_skill_gap, research_company,
             generate_cover_letter, generate_interview_prep]

    system_prompt = """You are JobHunt Agent — an expert AI career assistant.
    
Given a job description, run ALL 5 steps in order:
Step 1: extract_skills_from_jd
Step 2: analyze_skill_gap  
Step 3: research_company
Step 4: generate_cover_letter (use all context gathered)
Step 5: generate_interview_prep

Present results with clear headers. End with a 'Next Steps' summary."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])
    agent = create_openai_tools_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True, max_iterations=10)


def run_agent(job_description: str, candidate_profile: str, company_name: str):
    agent = create_jobhunt_agent()
    user_input = f"""Run the full pipeline for:
COMPANY: {company_name}
JOB DESCRIPTION: {job_description}
MY PROFILE: {candidate_profile}"""
    print("\n🤖 JOBHUNT AGENT — Starting...\n" + "="*50)
    result = agent.invoke({"input": user_input})
    print("\n✅ COMPLETE\n" + "="*50)
    print(result["output"])
    return result["output"]


if __name__ == "__main__":
    JOB_DESCRIPTION = """
    Gen AI Engineer — 1-3 years experience
    Required: LangChain, RAG, OpenAI API, Python, Hugging Face
    Plus: Agentic AI (LangGraph, AutoGen), Vector DBs (Pinecone)
    Role: Build LLM apps, design RAG pipelines, develop agentic workflows
    """
    CANDIDATE_PROFILE = """
    Mayur More — 1+ year Gen AI at Square Yards
    Skills: LangChain, LangSmith, OpenAI API, RAG, Prompt Engineering,
    Hugging Face, Python, PyTorch, Agentic AI, Vertex AI
    Projects: Fraud detection system, Customer intelligence platform (95% accuracy)
    Certs: Google Cloud Generative AI, Google LLMs (2024)
    """
    run_agent(JOB_DESCRIPTION, CANDIDATE_PROFILE, "Anthropic")