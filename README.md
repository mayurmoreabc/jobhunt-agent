# 🎯 JobHunt Agent — Multi-Step AI Agent for Job Applications

[![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.2-green)](https://langchain.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?logo=openai)](https://openai.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit)](https://streamlit.io)

> **An autonomous AI agent that automates your job application — from analyzing a JD to writing a cover letter and interview prep sheet.**

---

## 🤖 What It Does

JobHunt Agent uses **LangChain + OpenAI GPT-4** to run 5 automated steps:

```
Job Description ──► Extract Skills ──► Gap Analysis ──► Company Research
                                                              │
                                              Cover Letter ◄──┘
                                                    │
                                          Interview Prep Sheet
                                                    │
                                      Complete Application Package ✅
```

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 JD Skill Extractor | Parses required skills, experience, and responsibilities |
| 📊 Skill Gap Analyzer | Shows what you have, what you're missing, and how to fix it |
| 🔍 Company Researcher | Gathers company context for cover letters and interviews |
| ✉️ Cover Letter Generator | Writes a tailored, human-sounding letter using GPT-4 |
| 📝 Interview Prep Sheet | Role-specific questions, STAR hints, key topics to revise |
| 🌐 Streamlit Web UI | Clean browser interface — no terminal needed |

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/mayurmoreabc/jobhunt-agent.git
cd jobhunt-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your OpenAI API key
cp .env.example .env
# Edit .env and paste your key

# 4. Run terminal version
python agent.py

# OR run the web app
streamlit run app.py
```

## 🧱 Tech Stack

- **LangChain** — Agent orchestration and tool calling
- **OpenAI GPT-4** — LLM backbone
- **Streamlit** — Web UI
- **Python** — Core language

## 🗺️ Roadmap

- [ ] Add Tavily for real web search (live company research)
- [ ] PDF resume parser (auto-extract your profile)
- [ ] Track multiple job applications
- [ ] LangGraph multi-agent version

---

**Built by Mayur More** — AI Engineer | Gen AI | Prompt Engineering  
📧 Smore5875@gmail.com | [LinkedIn](https://linkedin.com/in/data-scientist-mayur-more01/)
