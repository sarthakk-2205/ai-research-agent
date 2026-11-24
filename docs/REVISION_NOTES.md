# AI RESEARCH AGENT
## Multi-Agent Research & Report Generation System

**Project Type:** Generative AI / Agentic AI  
**Language:** Python  
**Development Environment:** Windows + VS Code  
**Current Progress:** Phase 1 and Phase 2 Completed

---

# PART A — DETAILED TECHNICAL NOTES

# PHASE 1: PROJECT UNDERSTANDING AND ARCHITECTURE

## 1. Project Overview

The AI Research Agent is an AI-powered system that automates the research process.

It accepts a research question, creates a research plan, retrieves information from the internet, analyzes the findings, verifies important claims and generates a structured research report with source references.

### Example

User Query:

"Compare the latest developments in Generative AI and Agentic AI."

The system should:
1. Understand the research question.
2. Break it into smaller research tasks.
3. Search the internet for relevant information.
4. Extract useful information.
5. Analyze and compare findings.
6. Check claims against supporting sources.
7. Generate a structured research report.

## 2. Problem Statement

Traditional research requires manually:
- Searching multiple websites.
- Reading lengthy articles.
- Extracting relevant information.
- Comparing different sources.
- Verifying facts.
- Preparing research reports.

This process consumes time and effort.

Our AI Research Agent aims to automate these steps using LLMs, web search tools and an orchestrated AI workflow.

## 3. Project Objectives

- Automate research workflows.
- Retrieve information from external sources.
- Generate structured research plans.
- Analyze information from multiple sources.
- Reduce unsupported AI-generated claims.
- Maintain source references.
- Generate downloadable research reports.
- Build a practical multi-agent AI application.

## 4. Complete System Workflow

```text
             USER QUERY
                 |
                 v
          RESEARCH PLANNER
                 |
                 v
           WEB RESEARCHER
                 |
                 v
         INFORMATION EXTRACTION
                 |
                 v
          INFORMATION ANALYST
                 |
                 v
           FACT REVIEWER
                 |
                 v
          REPORT GENERATOR
                 |
                 v
          FINAL RESEARCH REPORT
```

### Explanation of Each Component

**1. Research Planner**

- Understands the user's research question.
- Breaks complex topics into smaller subtopics.
- Creates a research plan.

**2. Researcher**

- Searches the internet.
- Retrieves relevant articles and documents.
- Collects source URLs and useful content.

**3. Analyst**

- Extracts important findings.
- Summarizes information.
- Compares different sources.
- Identifies patterns and trends.

**4. Reviewer**

- Checks whether claims have supporting evidence.
- Identifies conflicting information.
- Detects unsupported statements.
- Identifies research gaps.

**5. Report Generator**

- Organizes the findings.
- Creates an executive summary.
- Generates structured sections.
- Includes source references.

Note: These are planned responsibilities. They are not yet implemented as separate agents.

## 5. Proposed Architecture

The application will eventually have four major layers.

### Layer 1: Frontend
Technology: Streamlit

Responsibilities:
- Accept research questions.
- Display research progress.
- Show generated reports.
- Display source references.
- Allow report downloads.

### Layer 2: Backend
Technology: FastAPI

Responsibilities:
- Receive frontend requests.
- Validate user inputs.
- Execute research workflows.
- Return results.

### Layer 3: AI Research Engine
Technologies: Python, Groq, LangGraph, Pydantic

Responsibilities:
- LLM inference.
- Research planning.
- Tool calling.
- Information analysis.
- Multi-agent orchestration.
- Report generation.

### Layer 4: External Tools and Storage

Technologies: Tavily, SQLite

Responsibilities:
- Web information retrieval.
- Research history storage.
- Report persistence.

## 6. Technology Stack and Why We Selected It

| Technology | Purpose | Reason |
|---|---|---|
| Python | Core development | Simple ecosystem for AI development |
| Groq | LLM inference | API-based model inference |
| Tavily | Web search | Search designed for AI applications |
| LangGraph | Agent orchestration | Stateful multi-step workflows |
| Pydantic | Data validation | Structured data handling |
| FastAPI | Backend | API development |
| Streamlit | Frontend | Quick AI application UI |
| SQLite | Database | Lightweight persistence |
| Docker | Deployment | Consistent application environment |

### Important Design Decision

We will first build a functional single-workflow MVP.

After that, we will introduce LangGraph and specialized agents.

Reason: A working research pipeline is more valuable than a complicated architecture that we cannot explain or test.

## 7. MVP Scope

The first working version should support:

- Research query input.
- LLM integration.
- Research planning.
- Web search.
- Information extraction.
- Summarization.
- Structured report generation.
- Source references.

Advanced features such as multi-agent orchestration, reviewer agents, research history, evaluation and deployment will be introduced gradually.

## 8. Important Concepts

**LLM (Large Language Model):** A model trained on large amounts of text that can understand and generate natural language.

**AI Agent:** An AI-powered system that can work towards a goal using reasoning, tools and actions.

**Multi-Agent System:** A system in which multiple specialized agents collaborate to accomplish a task.

**Tool Calling:** Allowing an LLM-based workflow to invoke external functions or APIs.

**Orchestration:** Coordinating the execution of multiple workflow steps or agents.

**State:** Information maintained and shared throughout a workflow.

**Hallucination:** An AI-generated statement that is incorrect, fabricated or unsupported.

**Citation:** A reference connecting a statement or finding to its information source.

**RAG:** Retrieval-Augmented Generation. A technique that retrieves relevant external information and provides it to an LLM as context for generating an answer.

## 9. Development Roadmap

1. Project understanding and architecture.
2. Environment setup and basic LLM integration.
3. Web search and information retrieval.
4. Research workflow and report generation.
5. Multi-agent architecture with LangGraph.
6. Reviewer, verification and memory.
7. FastAPI and Streamlit integration.
8. Evaluation, testing and error handling.
9. Docker and deployment.
10. Documentation and interview preparation.

## 10. Phase 1 Design Decisions

- Build a working MVP before advanced features.
- Use Groq initially for LLM inference.
- Use Tavily for web research.
- Introduce LangGraph when the basic workflow is understood.
- Keep agents modular.
- Avoid unnecessary abstractions.
- Keep source references throughout the research process.

---

# PHASE 2: ENVIRONMENT SETUP AND BASIC LLM INTEGRATION

## 1. Objective

Set up the Python development environment and establish communication between our Python application and an LLM using the Groq API.

## 2. Environment Setup

Development environment:
- Operating System: Windows
- Code Editor: VS Code
- Language: Python 3.12
- Virtual Environment: `.venv`

### Project Initialization

Created the project directory:

```powershell
mkdir ai-research-agent
cd ai-research-agent
```

Opened the project in VS Code:

```powershell
code .
```

### Created Virtual Environment

```powershell
python -m venv .venv
```

Activated it:

```powershell
.venv\Scripts\Activate.ps1
```

A virtual environment isolates project dependencies from other Python projects.

This prevents dependency conflicts.

### Upgraded pip

```powershell
python -m pip install --upgrade pip
```

## 3. Initial Folder Structure

```text
ai-research-agent/
│
├── app/
│   └── __init__.py
│
├── docs/
│   └── REVISION_NOTES.md
│
├── tests/
├── reports/
│
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

This is our initial implemented structure. Additional folders will be created as development progresses.

## 4. Installed Dependencies

Command:

```powershell
pip install groq python-dotenv
```

### Groq

Purpose:
- Communicate with Groq's inference API.
- Send prompts to an LLM.
- Receive generated responses.

### python-dotenv

Purpose:
- Load environment variables from a `.env` file.
- Keep API credentials separate from application source code.

Updated dependencies:

```powershell
pip freeze > requirements.txt
```

## 5. Environment Variables and API Security

Created a Groq account and generated an API key through:

https://console.groq.com/

### .env

```env
GROQ_API_KEY=your_actual_api_key
GROQ_MODEL=openai/gpt-oss-20b
```

### .env.example

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-20b
```

The actual API key is stored only in `.env`.

### .gitignore

```gitignore
.env
.venv/
__pycache__/
*.pyc
.pytest_cache/
```

Why?

- API keys should never be committed to GitHub.
- Virtual environments should not be uploaded.
- Python cache files are unnecessary in the repository.

## 6. Basic LLM Integration

Created:

`app/llm.py`

### Complete Implemented Code

```python
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Read API configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)

# Validate API key
if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Check your .env file."
    )

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


def generate_response(prompt: str) -> str:
    """
    Send a prompt to the LLM and return its response.
    """

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI research assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        max_completion_tokens=500
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    answer = generate_response(
        "Explain what an AI agent is in simple terms."
    )

    print("\nAI Response:")
    print(answer)
```

## 7. Understanding the Code

### A. Importing Libraries

```python
import os
from dotenv import load_dotenv
from groq import Groq
```

- `os`: Access operating system environment variables.
- `load_dotenv`: Load environment variables from `.env`.
- `Groq`: Initialize the Groq API client.

### B. Loading Environment Variables

```python
load_dotenv()
```

Loads the variables stored in `.env` into the environment.

### C. Reading Configuration

```python
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "openai/gpt-oss-20b"
)
```

`os.getenv()` retrieves environment variables.

The second argument provides a default model if the environment variable is unavailable.

### D. API Key Validation

```python
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing.")
```

Prevents the application from proceeding without an API key.

### E. Initializing the Groq Client

```python
client = Groq(api_key=GROQ_API_KEY)
```

Creates the client used to communicate with Groq.

### F. Creating a Reusable Function

```python
def generate_response(prompt: str) -> str:
```

This function accepts a string prompt and returns a generated string response.

Why create a function?

Because different components of our application will need LLM responses.

Instead of repeating API communication code, we can reuse this function.

### G. Sending the API Request

```python
response = client.chat.completions.create(
    model=GROQ_MODEL,
    messages=[...],
    temperature=0.3,
    max_completion_tokens=500
)
```

This sends a chat completion request to Groq.

Important parameters:

**model:** Specifies which LLM should process the request.

**messages:** Contains the instructions and user input.

**temperature:** Controls the randomness of generation. Lower values generally produce more consistent outputs.

**max_completion_tokens:** Limits the number of generated completion tokens.

### H. Understanding Message Roles

System message:

```python
{
    "role": "system",
    "content": "You are a helpful AI research assistant."
}
```

Defines the model's behavior and instructions.

User message:

```python
{
    "role": "user",
    "content": prompt
}
```

Contains the actual user request.

### I. Extracting the Response

```python
return response.choices[0].message.content
```

Breakdown:

- `response`: Complete API response object.
- `choices`: Generated completion choices.
- `[0]`: First generated choice.
- `message`: Generated message.
- `content`: Actual response text.

### J. Main Execution Block

```python
if __name__ == "__main__":
```

Ensures that the test code runs when this file is executed directly as a module.

It does not execute the test block when imported by another Python module.

## 8. How to Execute the Application

Command:

```powershell
python -m app.llm
```

Why use `-m`?

It executes the Python module using its package context.

This is useful when working with structured Python packages.

## 9. Actual Test Result

Test prompt:

"Explain what an AI agent is in simple terms."

Execution:

```text
(.venv) PS C:\Users\Asus\OneDrive\Desktop\ai-research-agent>

python -m app.llm

AI Response:

An AI agent is basically a little computer
program that can see or receive data about
its surroundings, think about what to do,
and then take an action to try to reach a goal.
```

**Result: SUCCESS**

The application successfully:
1. Loaded the API key.
2. Initialized the Groq client.
3. Sent a prompt to the model.
4. Received an LLM-generated response.
5. Extracted and printed the response.

This is our first successfully tested AI component.

## 10. Important Concepts Learned

### What is Groq?

Groq provides an API for accessing language models through inference requests.

### What is an API?

An Application Programming Interface allows different software systems to communicate through defined interfaces.

### What is an LLM client?

An LLM client is a software interface used by an application to communicate with an LLM provider.

### What is inference?

Inference is the process through which a trained model generates predictions or outputs from an input.

### What is an environment variable?

A configuration value stored outside the application source code.

### What is temperature?

A generation parameter that influences the randomness of model outputs.

### What is the difference between an LLM and an AI agent?

An LLM generates responses based on input.

An AI agent uses an LLM or other decision-making logic together with tools, state and actions to accomplish a goal.

**Important:** Our current application is LLM-powered, but it is not yet an autonomous AI agent.

## 11. Design Decisions

| Decision | Reason |
|---|---|
| Groq API | Simple API-based LLM integration |
| GPT-OSS 20B | Initial model selected for the project |
| python-dotenv | Secure configuration management |
| Separate llm.py | Reusable LLM communication logic |
| Environment-based model configuration | Easier model switching |
| Reusable generate_response() | Avoid duplicate API logic |

## 12. Current Limitations

At the end of Phase 2:

- The application can communicate with an LLM.
- It can accept a prompt and generate a response.
- It does not yet search the internet.
- It does not have research planning.
- It does not have external tools.
- It does not have multi-agent orchestration.
- It does not generate research reports.
- It does not have persistent memory.

These are future milestones, not completed features.

## 13. Common Errors and Solutions

| Error | Possible Solution |
|---|---|
| ModuleNotFoundError | Activate virtual environment and install dependencies |
| Missing API key | Check `.env` and `load_dotenv()` |
| Authentication error | Verify Groq API key |
| Model unavailable | Check supported Groq model IDs |
| Command not recognized | Verify Python installation and PATH |
| PowerShell activation blocked | Configure PowerShell execution policy appropriately |

## 14. Interview Questions and Answers

**Q1. What is Groq?**

Groq provides an inference API that allows applications to communicate with supported language models.

**Q2. Why did you use Groq?**

I selected Groq for convenient API-based LLM integration and fast inference.

**Q3. Why use python-dotenv?**

It allows us to load sensitive configuration from environment files instead of hardcoding API keys in source code.

**Q4. What is the purpose of the Groq client?**

It provides an interface for sending requests to Groq and receiving model responses.

**Q5. What is the difference between system and user messages?**

System messages define the model's behavior, while user messages contain the actual request.

**Q6. What is temperature?**

It is a parameter that influences the randomness of generated responses.

**Q7. What is model inference?**

It is the process of generating an output from a trained model based on an input.

**Q8. Have you built an AI agent?**

At this stage, I have integrated an LLM into a Python application. The tool-using, stateful and orchestrated agent workflow will be implemented in later milestones.

**Q9. Why separate the LLM logic into its own file?**

It improves modularity and reusability. Other application components can use the same LLM function without duplicating API communication logic.

**Q10. What happens if the API key is missing?**

Our validation raises a ValueError before attempting to make an API request.

---

# PART B — QUICK INTERVIEW REVISION

## 1. Project in One Line

An AI-powered research system that automates research planning, web information retrieval, analysis, verification and structured report generation.

## 2. Project Workflow

```text
User Query
    |
    v
Research Planning
    |
    v
Web Search
    |
    v
Information Extraction
    |
    v
Analysis
    |
    v
Verification
    |
    v
Report Generation
```

## 3. Technology Cheat Sheet

| Technology | Remember |
|---|---|
| Python | Core programming |
| Groq | LLM inference |
| Tavily | Web search |
| LangGraph | Agent orchestration |
| Pydantic | Data validation |
| FastAPI | Backend API |
| Streamlit | Frontend |
| SQLite | Persistence |
| Docker | Containerization |

## 4. Important Terminology

- LLM = Large Language Model.
- API = Application Programming Interface.
- SDK = Software Development Kit.
- Inference = Model generates output.
- Prompt = Input instructions or request.
- System Message = Model behavior instructions.
- User Message = Actual user input.
- Temperature = Generation randomness control.
- Agent = AI system that can use tools and take actions.
- Orchestration = Coordination of workflow execution.
- State = Shared workflow information.
- Hallucination = Unsupported or fabricated model output.
- Citation = Reference to supporting information.

## 5. Commands to Remember

```powershell
# Create virtual environment
python -m venv .venv

# Activate environment
.venv\Scripts\Activate.ps1

# Install dependencies
pip install groq python-dotenv

# Update requirements
pip freeze > requirements.txt

# Execute LLM module
python -m app.llm
```

## 6. Important Files

| File | Responsibility |
|---|---|
| `.env` | API credentials and configuration |
| `.env.example` | Configuration template |
| `.gitignore` | Files excluded from Git |
| `requirements.txt` | Python dependencies |
| `app/llm.py` | LLM communication |
| `docs/REVISION_NOTES.md` | Project revision documentation |

## 7. 30-Second Project Explanation

I am building an AI Research Agent that automates research workflows. It takes a user's research question, creates a research plan, retrieves information from the web, analyzes findings and generates structured reports with source references. The project uses Python and Groq for LLM integration, with Tavily for web search and LangGraph planned for multi-agent orchestration.

## 8. Two-Minute Project Explanation

The AI Research Agent is a Generative AI project designed to automate multi-step research.

The motivation behind this project is that traditional research involves manually searching multiple websites, reading articles, extracting information, comparing findings and preparing reports.

Our system aims to automate this workflow.

When a user submits a research question, the system first creates a research plan and breaks the question into smaller subtopics. It then uses web search tools to retrieve relevant information from external sources.

The retrieved information is analyzed by an LLM to extract important findings and compare different sources. A reviewer component will check whether important claims are supported by evidence and identify conflicting information.

Finally, the system generates a structured research report with source references.

I have started by setting up the Python environment and integrating Groq for LLM inference. The next step is integrating Tavily for web search, followed by building the complete research pipeline and introducing LangGraph for stateful multi-agent orchestration.

---

# PART C — PROJECT PROGRESS TRACKER

## Completed

- [x] Phase 1: Project understanding and architecture.
- [x] Phase 2: Environment setup and basic LLM integration.

## Upcoming

- [ ] Phase 3: Web search and information retrieval.
- [ ] Phase 4: Research workflow and report generation.
- [ ] Phase 5: Multi-agent architecture using LangGraph.
- [ ] Phase 6: Reviewer, verification and memory.
- [ ] Phase 7: FastAPI and Streamlit integration.
- [ ] Phase 8: Evaluation, testing and error handling.
- [ ] Phase 9: Docker and deployment.
- [ ] Phase 10: GitHub documentation and interview preparation.

**Documentation Rule:** Only mark a feature completed after it has been implemented and tested. Update these notes after every major milestone.

**Current Project Status:** Phase 1 and Phase 2 completed. Basic LLM integration successfully tested using Groq.





# Phase 3 — Web Search Integration with Tavily

## 1. Objective

Integrate an external web-search API into the AI Research Agent so it can retrieve current information from the internet instead of relying only on the LLM's pretrained knowledge.

## 2. Technology Used

- **Tavily:** Web-search API designed for AI applications.
- **tavily-python:** Python SDK used to communicate with Tavily.
- **python-dotenv:** Loads API keys from the `.env` file.

## 3. Installation

```powershell
pip install tavily-python
pip freeze > requirements.txt
```

## 4. Environment Configuration

Added to `.env`:

```env
TAVILY_API_KEY=your_actual_api_key
```

Added to `.env.example`:

```env
TAVILY_API_KEY=your_tavily_api_key_here
```

The actual API key must never be committed to GitHub.

## 5. Files Created

```text
app/
├── __init__.py
├── llm.py
└── tools/
    ├── __init__.py
    └── web_search.py
```

## 6. Implementation

Created a reusable `search_web()` function in `app/tools/web_search.py`.

It:
1. Loads the Tavily API key.
2. Initializes the Tavily client.
3. Accepts a search query.
4. Calls the Tavily search API.
5. Extracts title, URL, content, and relevance score.
6. Returns structured search results as a list of dictionaries.

## 7. Important Concepts

| Concept | Meaning |
|---|---|
| Search API | Allows an application to search external information sources |
| Search result | A web page returned for a query |
| Retrieved content | Text returned about a particular page |
| URL | Original source link |
| Relevance score | Indicates how relevant a result is to the query |
| SDK | A software development kit that simplifies API usage |

**Important:** A high relevance score does not prove that a source is trustworthy or factually correct.

## 8. Groq vs Tavily

- Groq provides LLM inference: reasoning, summarization, and text generation.
- Tavily provides web search: finding relevant pages and retrieving information.
- Together, they allow the application to search first and analyze the retrieved information using an LLM.

## 9. Testing and Actual Result

Executed:

```powershell
python -m app.tools.web_search
```

**Result: SUCCESS**

The application returned five search results for:

`Recent developments in Generative AI`

The output contained:
- Page titles
- Source URLs
- Relevance scores
- Retrieved content

This confirms that Tavily authentication, API communication, and result extraction are working.

## 10. Current Limitations

- Search results can contain different source types, including videos and articles.
- Retrieved content may be snippets rather than complete web pages.
- Relevance does not guarantee credibility.
- Sources may contain outdated, conflicting, or inaccurate claims.
- We have not yet implemented source validation or full-page content extraction.

## 11. Interview Questions

**Q1. Why did you integrate Tavily?**

To allow the research agent to retrieve current external information instead of depending entirely on the LLM's pretrained knowledge.

**Q2. What is the difference between Groq and Tavily?**

Groq provides access to an LLM for reasoning and generation, while Tavily retrieves relevant information from the web.

**Q3. What does Tavily return?**

Search results containing fields such as title, URL, content, and relevance score.

**Q4. Does a high relevance score mean the information is true?**

No. It indicates relevance to the query, not factual accuracy or source credibility.

**Q5. Why preserve source URLs?**

To maintain traceability and allow the final research report to reference its original sources.

## 12. Phase 3 Progress

- [x] Installed Tavily SDK
- [x] Configured Tavily API key
- [x] Created reusable web-search module
- [x] Retrieved web search results
- [x] Extracted structured result fields
- [x] Successfully tested the module




# Phase 4 — End-to-End Research Pipeline

## 1. Objective

Connect the Tavily web-search module and Groq LLM module to create an end-to-end research workflow.

The application now accepts a research question, retrieves web information, analyzes it using an LLM, generates a structured report, and saves that report locally.

## 2. Architecture

User Query → Tavily Search → Search Results → Research Context → Groq LLM → Research Report → Markdown File

## 3. Files Used

```text
app/
├── llm.py
├── research.py
└── tools/
    └── web_search.py

reports/
    └── research_report_<timestamp>.md
```

## 4. Main Functions

### conduct_research(query)

Responsibilities:
1. Accepts a research question.
2. Calls `search_web()` to retrieve relevant information.
3. Checks whether search results exist.
4. Organizes the retrieved information into research context.
5. Constructs a research prompt.
6. Calls `generate_response()` to generate the report.
7. Returns the generated report.

### save_report(query, report)

Responsibilities:
1. Creates the reports directory if necessary.
2. Generates a timestamp for the filename.
3. Combines the research question and generated report.
4. Saves the report as a Markdown file.
5. Returns the saved file path.

## 5. Important Concepts

| Concept | Meaning |
|---|---|
| Research pipeline | Connected sequence of steps that completes a research task |
| Context engineering | Preparing relevant information and instructions for an LLM |
| Prompt engineering | Designing instructions to guide LLM output |
| Source attribution | Linking claims to the sources used |
| Markdown | Lightweight format for structured documents |
| Path | Python object for handling file and directory paths |
| Timestamp | Date and time used to distinguish saved reports |

## 6. Why Markdown?

Markdown is lightweight, readable, easy to edit, and suitable for storing structured research reports. It also supports headings, lists, tables, links, and code blocks.

## 7. Improvements Made

- Increased the default LLM response limit from 500 to 2000 tokens.
- Added source labels such as `[Source 1]`.
- Instructed the LLM not to invent references or unsupported facts.
- Added a reusable report-saving function.
- Added timestamp-based report filenames.

## 8. Testing

Executed:

```powershell
python -m app.research
```

**Result: SUCCESS**

The application:
- Retrieved web search results through Tavily.
- Generated a structured research report through Groq.
- Included source references and a source list.
- Saved the report in the `reports/` directory as a Markdown file.

## 9. Current Limitations

- The research process is still a single sequential workflow.
- There is no dedicated planning agent.
- Search results are not independently verified.
- No automatic retry or fallback mechanism is implemented.
- Reports have a fixed generation workflow.
- Research history is not stored in a database.

## 10. Interview Questions

**Q1. How does your research pipeline work?**

It accepts a query, retrieves relevant web information using Tavily, prepares the retrieved information as context, sends it to Groq, and generates a structured report with source references.

**Q2. Why do you separate web search and LLM integration into different modules?**

Separation of concerns makes the application easier to maintain, test, debug, and extend.

**Q3. Why did you introduce a separate `save_report()` function?**

To separate report generation from file storage and make report persistence reusable.

**Q4. What is context engineering?**

It is the process of selecting, organizing, and supplying relevant information and instructions to an LLM so it can produce a more useful response.

**Q5. Is the current system a multi-agent system?**

No. It is a sequential research pipeline using one LLM generation step and a web-search tool. We plan to introduce specialized agents and orchestration in the next phase.

## 11. Phase 4 Progress

- [x] Created `research.py`
- [x] Connected Tavily and Groq
- [x] Prepared research context
- [x] Generated structured research reports
- [x] Improved source attribution instructions
- [x] Increased response token limit
- [x] Implemented Markdown report saving






# Phase 5 — LangGraph Fundamentals

## 1. Objective

Understand LangGraph and build a basic stateful workflow with multiple nodes, shared state, normal edges, conditional edges, and retry logic.

## 2. Installation

```powershell
pip install langgraph
pip freeze > requirements.txt
```

Verified installation successfully.

## 3. Important Concepts

### State

A shared data structure that stores information passed between nodes.

Implemented using Python `TypedDict`.

### Node

A Python function responsible for performing a particular task.

Examples:
- Planner node
- Researcher node
- Reviewer node
- Report Generator node

### Edge

Defines the execution flow between nodes.

### Conditional Edge

Routes execution to different nodes depending on the current state.

Implemented using:

```python
builder.add_conditional_edges()
```

### START and END

Special markers that define the beginning and end of graph execution.

### Compile

```python
graph = builder.compile()
```

Builds the executable graph.

### Invoke

```python
result = graph.invoke(initial_state)
```

Starts graph execution with the supplied initial state.

## 4. First Graph Implementation

Created `app/graph_demo.py`.

Initial workflow:

START → Planner → Researcher → END

Verified that:
- Both nodes executed in order.
- Each node returned a state update.
- The final state contained the accumulated message.

## 5. Conditional Routing Implementation

Extended the graph:

START → Planner → Researcher → Reviewer

Reviewer decision:
- Sufficient research → Report Generator
- Insufficient research → Researcher again
- Maximum retries reached → Report Generator with an insufficient-evidence status

## 6. Retry Logic

Added:

```python
retry_count: int
```

The researcher increments this counter after each attempt.

The routing function checks the counter to prevent unlimited execution.

Maximum retry limit in the demo: 3 research attempts.

The reviewer currently uses simulated logic and approves after the second attempt.

## 7. Actual Testing

Executed:

```powershell
python -m app.graph_demo
```

**Result: SUCCESS**

Observed execution:

```text
Planner is working...
Researcher is working...
Reviewer is checking research...
Researcher is working...
Reviewer is checking research...
Generating final report...
```

Final state included:

```python
{
    "is_sufficient": True,
    "retry_count": 2
}
```

This confirms that conditional routing and the feedback loop work correctly.

## 8. Why Retry Limits Matter

- Prevent unnecessary API calls and costs.
- Prevent indefinite execution.
- Control execution time.
- Improve workflow reliability.

## 9. Current Limitations

- Nodes currently use simulated logic.
- Reviewer does not use an LLM.
- Researcher does not yet call Tavily inside the graph.
- No real planning or analysis is performed by specialized agents.

## 10. Interview Questions

**Q1. What is LangGraph?**

LangGraph is a framework for building stateful, multi-step LLM workflows using nodes, edges, shared state, and conditional routing.

**Q2. What is the difference between a node and an edge?**

A node performs a task, whereas an edge determines which node executes next.

**Q3. What is shared state?**

It is the common data structure through which workflow nodes read and update information.

**Q4. What is a conditional edge?**

It determines the next node based on a condition or routing function.

**Q5. Why do we need retry limits?**

To avoid infinite loops, unnecessary API costs, and excessive execution time.

**Q6. What happens if the reviewer rejects the research?**

The conditional edge routes execution back to the researcher for another attempt, subject to the retry limit.

## 11. Phase 5 Progress

- [x] Installed LangGraph
- [x] Understood state, nodes, and edges
- [x] Built the first sequential graph
- [x] Implemented conditional routing
- [x] Implemented retry counting
- [x] Tested the reviewer feedback loop






# Phase 6 — Multi-Agent Workflow Integration with LangGraph

## 1. Objective

Integrate five specialized AI agents into one automated research workflow using LangGraph.

The workflow:

User Query → Planner → Researcher → Analyst → Reviewer → Report Generator

If the Reviewer requests improvements, the workflow sends feedback to the Analyst for revision.

## 2. Five Agents and Their Responsibilities

| Agent | Responsibility |
|---|---|
| Planner | Breaks the main query into 3–5 research subtopics |
| Researcher | Searches the web using Tavily |
| Analyst | Analyzes collected information and produces structured findings |
| Reviewer | Checks claims, citations, unsupported information and gaps |
| Report Generator | Creates and saves the final Markdown report |

### Planner
- Uses Groq to generate research subtopics.
- Uses Pydantic to validate the generated research plan.
- Returns a structured list of subtopics.

### Researcher
- Searches every subtopic using Tavily.
- Collects titles, URLs, content snippets and relevance scores.
- Current configuration: 2 results per subtopic.

### Analyst
- Uses collected research to produce structured analysis.
- Includes citations such as [Source 1].
- Accepts Reviewer feedback and improves its previous analysis.
- Uses a limited amount of source context and output tokens to control API usage.

### Reviewer
- Compares the analysis against retrieved source snippets.
- Checks unsupported claims, citation problems and missing information.
- Returns either APPROVED or NEEDS REVISION.
- Provides recommendations for improving the analysis.

### Report Generator
- Combines the research, analysis and review into a Markdown report.
- Includes the review decision and reviewer feedback.
- Saves reports in the reports/ directory with timestamps.

## 3. LangGraph Concepts Used

### State
State is the shared data structure passed between nodes.

Our ResearchState contains:
- query
- subtopics
- research_results
- analysis
- review
- revision_count
- review_failed
- report
- report_path

### Nodes
Each agent is implemented as a node in the graph.

Examples:
- planner_node()
- researcher_node()
- analyst_node()
- reviewer_node()
- report_generator_node()

Each node reads the current state and returns updates.

### Edges
Edges define the execution order between nodes.

### Conditional Edges
The Reviewer determines what happens next:
- APPROVED → Report Generator
- NEEDS REVISION and revision limit not reached → Analyst
- Maximum revisions reached → Report Generator

### Feedback Loop
The Analyst receives feedback from the Reviewer and improves its analysis.

The workflow allows a maximum of two revisions.

This prevents endless agent execution and unnecessary API costs.

## 4. Workflow Architecture

START
  ↓
Planner
  ↓
Researcher
  ↓
Analyst
  ↓
Reviewer
  ↓
Decision
  ├── APPROVED → Report Generator
  ├── NEEDS REVISION → Analyst (maximum 2 revisions)
  └── Maximum revisions reached → Report Generator
  ↓
END

## 5. Important Implementation Decisions

1. Used LangGraph instead of manually calling agents one after another because it provides explicit state management and conditional execution.
2. Used Pydantic to validate Planner output.
3. Limited research results to control token consumption.
4. Limited Analyst output tokens to reduce Groq API usage.
5. Added a maximum revision count to prevent infinite loops.
6. Added reviewer failure handling so an unavailable or invalid review does not falsely approve the report.
7. Preserved NEEDS REVISION in the final report when approval was not achieved.

## 6. Testing

Run the workflow:

```powershell
python -m app.workflow
```

Check Python syntax:

```powershell
python -m compileall app
```

Generated reports:

```text
reports/
    final_report_<timestamp>.md
```

## 7. Latest Successful Test

Research query: Compare Generative AI and Agentic AI

Observed execution:
- Planner generated 5 subtopics.
- Researcher searched all 5 subtopics.
- Analyst generated the initial analysis.
- Reviewer requested revisions.
- Analyst revised the analysis twice.
- Reviewer completed the final review.
- Maximum revision limit was reached.
- Report Generator created the final report.

Final result:
- Workflow: COMPLETED
- Revision attempts: 2
- Reviewer failed: False
- Review decision: NEEDS REVISION
- Report: reports/final_report_20261124_135335.md

## 8. Important Concepts for Interviews

**Why LangGraph?**

LangGraph helps build stateful, multi-step AI workflows. It supports nodes, edges, conditional routing, shared state and cycles.

**Why separate agents?**

Each agent has a specialized responsibility. This makes the workflow modular, easier to debug, test and maintain.

**Why use a Reviewer agent?**

An LLM can generate unsupported or inaccurate information. The Reviewer provides an additional verification step before report generation.

**Why limit revisions?**

An unlimited feedback loop can increase latency, token consumption and API costs. A fixed revision limit guarantees termination.

**What happens if the Reviewer cannot complete its task?**

The workflow marks the review as failed and generates a report that must be treated as unreviewed and unapproved.

**What is the difference between a node and an edge?**

A node performs an operation. An edge determines which node executes next.

**What is shared state?**

It is the information passed between nodes so that each agent can access the outputs of previous agents.

## 9. Current Limitations

- Reviewer verification depends on retrieved source snippets.
- Search results may contain low-quality or incomplete sources.
- Citation numbering does not guarantee that every citation supports its claim.
- Groq API rate limits can interrupt execution.
- The system does not yet have a user-facing interface.
- Reports are saved locally in Markdown format.

## 10. 30-Second Interview Explanation

I built a multi-agent research system using Python, Groq, Tavily and LangGraph. It takes a user query, breaks it into research subtopics, searches the web, analyzes the collected information and sends the analysis to a separate Reviewer agent. If the Reviewer identifies issues, the Analyst receives feedback and revises its output, with a maximum of two revisions. Finally, the Report Generator creates a structured Markdown report with sources and review status.

## 11. Two-Minute Interview Explanation

The project is designed to automate the research and report-generation process using multiple specialized AI agents.

First, the Planner agent takes the user's query and generates structured research subtopics. Pydantic validates the generated plan.

Next, the Researcher agent searches the web using Tavily and collects relevant information from multiple sources.

The Analyst agent processes the collected information and generates structured findings, comparisons and conclusions with source references.

After that, a separate Reviewer agent evaluates the analysis. It checks whether claims are supported by the collected sources, whether citations are appropriate and whether important information is missing.

If the review decision is NEEDS REVISION, the Analyst receives the feedback and improves its analysis. LangGraph manages this feedback loop using conditional edges and shared state. I have implemented a maximum of two revisions to prevent infinite loops and control API costs.

Finally, the Report Generator creates a Markdown report containing the findings, limitations, reviewer feedback and references.

I used LangGraph because it provides stateful orchestration and conditional workflows, making the overall system modular and easier to extend.


# Phase 7 — FastAPI Integration

## 1. Objective

Expose the multi-agent research workflow through REST API endpoints so that a frontend application can communicate with the AI system.

## 2. Technology Used

- FastAPI — API framework.
- Uvicorn — ASGI server used to run the API.
- Pydantic — request validation.
- LangGraph — executes the research workflow.

## 3. File Created

`app/api.py`

This file contains the FastAPI application and three endpoints.

| Endpoint | Method | Purpose |
|---|---|---|
| `/` | GET | Returns project information |
| `/health` | GET | Checks API health |
| `/research` | POST | Executes the complete research workflow |

## 4. API Architecture

Frontend → FastAPI → LangGraph Workflow → Planner → Researcher → Analyst → Reviewer → Report Generator → JSON Response

## 5. Important Concepts

### REST API
A REST API allows different applications to communicate through HTTP requests and responses.

### HTTP Methods
- GET: Retrieve information.
- POST: Send data and execute an operation.

### Pydantic Validation
The `ResearchRequest` model validates incoming requests.

The query field has:
- Minimum length: 5 characters.
- Maximum length: 500 characters.

### Uvicorn
Uvicorn runs the FastAPI application.

Command:

`uvicorn app.api:app --reload`

### Swagger UI
FastAPI automatically generates interactive API documentation.

URL: `http://127.0.0.1:8000/docs`

## 6. Successful Testing

Tested the research request:

`Compare Generative AI and Agentic AI`

Observed:
- Planner generated 5 subtopics.
- Researcher searched all 5 subtopics.
- Analyst completed the initial analysis.
- Reviewer requested revisions.
- Analyst revised the analysis twice.
- Reviewer completed the final review.
- Report Generator generated the report.
- API returned HTTP 200 OK.

Final report:

`reports/final_report_20261124_141145.md`

Final reviewer decision: NEEDS REVISION.

Important: HTTP 200 OK means the API request completed successfully. It does not mean the research report passed the review quality gate.

## 7. Error Handling

The `/research` endpoint uses try-except handling.

If the workflow raises an exception, FastAPI returns HTTP 500 with a generic error message. The detailed exception is printed in the server terminal.

## 8. Interview Questions

**Q1. Why did you use FastAPI?**

To expose the AI research workflow through REST endpoints so that a frontend or another application can interact with it.

**Q2. What is Uvicorn?**

Uvicorn is an ASGI server that runs the FastAPI application.

**Q3. What is Pydantic used for?**

It validates incoming request data and ensures that it follows the expected schema.

**Q4. How does the frontend communicate with your AI workflow?**

The frontend sends a POST request to `/research`. FastAPI validates the request, invokes the compiled LangGraph workflow, and returns the result as JSON.

**Q5. What does HTTP 200 OK mean?**

It means the HTTP request was processed successfully. It does not guarantee that the generated research passed the review process.

## 9. 30-Second Project Explanation

"I built a multi-agent AI research system using LangGraph and exposed it through FastAPI. The API accepts a research query, executes the complete agent workflow, and returns the generated report, review information, and report location as JSON. I also implemented request validation and error handling."

## 10. Current Project Status

Completed:
- Multi-agent architecture.
- LangGraph orchestration and review loop.
- Web search integration.
- Report generation.
- FastAPI REST API.

Remaining:
- Streamlit frontend.
- SQLite research history.
- Docker and deployment.
- Final testing and README documentation.





# Phase 8 — Streamlit Frontend

## 1. Objective

Build a simple browser-based interface for interacting with the AI Research Agent without requiring users to call API endpoints manually.

## 2. Technology Used

- Streamlit — Python-based frontend framework.
- Requests — HTTP communication with FastAPI.

## 3. File Created

`streamlit_app.py`

The frontend provides:
- Research topic input using `st.text_area()`.
- Research execution using `st.button()`.
- Loading indicator using `st.spinner()`.
- API communication using `requests.post()`.
- Generated report display using `st.markdown()`.
- Report download using `st.download_button()`.

## 4. Application Architecture

User → Streamlit UI → HTTP POST Request → FastAPI → LangGraph Workflow → JSON Response → Streamlit UI

## 5. How to Run the Application

Open two terminals from the project directory.

**Terminal 1 — FastAPI**

`uvicorn app.api:app --reload`

**Terminal 2 — Streamlit**

`streamlit run streamlit_app.py`

Frontend URL: `http://localhost:8501`

Backend URL: `http://127.0.0.1:8000`

## 6. Important Concepts

### Streamlit
A Python framework for building interactive web applications without writing frontend HTML, CSS, or JavaScript.

### Requests
A Python library used to send HTTP requests to the FastAPI backend.

### JSON Communication
Streamlit sends the research query as JSON:

`{"query": "Your research question"}`

FastAPI returns the research result as JSON.

### Spinner
`st.spinner()` displays a loading message while the research workflow executes.

### Download Button
`st.download_button()` allows users to download the generated report in Markdown format.

## 7. Error Handling

The frontend handles:
- Connection errors when FastAPI is unavailable.
- Request timeouts.
- Other HTTP request exceptions.
- Invalid research queries.

## 8. Interview Questions

**Q1. Why did you use Streamlit?**

To quickly build an interactive Python-based frontend for demonstrating the AI research system.

**Q2. How does Streamlit communicate with FastAPI?**

Using the Requests library, which sends an HTTP POST request containing the research query as JSON.

**Q3. Why did you separate the frontend and backend?**

Separation makes the system modular. The frontend handles user interaction, while FastAPI handles API requests and invokes the AI workflow.

**Q4. What happens when the user clicks Start Research?**

Streamlit validates the query, sends it to FastAPI, waits for the workflow response, and displays the generated report.

## 9. Current Project Status

Completed:
- Five-agent architecture.
- LangGraph orchestration and reviewer feedback loop.
- Tavily web search.
- Research report generation.
- FastAPI REST API.
- Streamlit frontend.

Remaining:
- SQLite research history.
- Docker and deployment.
- Final testing, README, and interview preparation.






# Phase 9 — SQLite Research History Integration

## 1. Objective

Persist research requests and generated reports so users can access previous research without executing the multi-agent workflow again.

## 2. Technology Used

- SQLite
- Python `sqlite3`
- FastAPI
- Streamlit

SQLite is a lightweight, file-based relational database. It does not require a separate database server.

## 3. Database Design

Database file: `research_history.db`

Table: `research_history`

| Column | Purpose |
|---|---|
| id | Unique research ID |
| query | Original research question |
| review_status | Reviewer feedback and decision |
| revision_attempts | Number of revisions |
| review_failed | Whether reviewer execution failed |
| report | Generated Markdown report |
| report_path | Saved report location |
| created_at | Record creation timestamp |

## 4. Important Functions

In `app/database.py`:

- `init_db()` — creates the database table if it doesn't exist.
- `save_research()` — inserts a completed research record.
- `get_research_history()` — retrieves previous research metadata.
- `get_research_by_id()` — retrieves a complete research record using its ID.

### SQL Concepts

- `CREATE TABLE IF NOT EXISTS`: Creates a table only if it doesn't already exist.
- `INSERT INTO`: Stores a new research record.
- `SELECT`: Retrieves saved records.
- `WHERE id = ?`: Retrieves a specific record using a parameterized query.
- `ORDER BY created_at DESC`: Displays newest records first.

## 5. FastAPI Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Home endpoint |
| GET | `/health` | Health check |
| POST | `/research` | Executes research and saves the result |
| GET | `/history` | Retrieves previous research records |
| GET | `/history/{research_id}` | Retrieves a particular saved report |

### Research API Workflow

1. Receive the research query.
2. Execute `research_graph.invoke()`.
3. Collect the final workflow result.
4. Save the result using `save_research()`.
5. Return the result along with its unique `research_id`.

## 6. Streamlit Integration

The Streamlit application now supports:

- Submitting new research queries.
- Displaying research results.
- Viewing previous research records in the sidebar.
- Selecting an existing research record.
- Loading its saved report through FastAPI.
- Downloading reports as Markdown files.

### Important Concept

Previously generated reports are retrieved from SQLite through FastAPI. The agents are not executed again when a user opens an old report.

## 7. End-to-End Architecture

User → Streamlit UI → FastAPI → LangGraph Multi-Agent Workflow → SQLite Database

For previous reports:

User → Streamlit UI → GET `/history` → Select Research ID → GET `/history/{research_id}` → SQLite → Display Saved Report

## 8. Testing Completed

- Database initialization successful.
- POST `/research` successfully executed.
- Research record successfully saved.
- GET `/history` successfully returned saved records.
- Individual research retrieval endpoint added.
- Streamlit history integration implemented.
- Report download functionality retained.

## 9. Important Interview Questions

**Q1. Why did you use SQLite?**

SQLite is lightweight, serverless and built into Python. It was sufficient for persisting research history in this MVP without introducing database infrastructure.

**Q2. Why do you need a unique research ID?**

It allows users to retrieve a particular research result independently of other research runs.

**Q3. How do you prevent SQL injection?**

I use parameterized SQL queries with placeholders (`?`) rather than directly inserting user input into SQL statements.

**Q4. Does viewing an old report execute the agents again?**

No. The application retrieves the previously stored report from SQLite using its research ID.

**Q5. Why separate database operations from FastAPI routes?**

It separates database logic from API logic, making the application easier to maintain and test.

## 10. Current Limitations

- SQLite is suitable for this MVP but may need migration to PostgreSQL for larger multi-user deployments.
- Research history currently has no user authentication or ownership controls.
- Reviewer approval is not guaranteed; reports can retain a NEEDS REVISION status.
- Database backups and retention policies are not implemented.

## 11. Two-Minute Project Explanation

"I built a multi-agent AI research system that accepts a topic, breaks it into smaller research tasks, gathers information from the web, analyzes the findings, and reviews the generated analysis for unsupported claims.

I used LangGraph to orchestrate the agents and implemented a conditional review loop so the Analyst can revise its output based on Reviewer feedback.

I integrated the workflow with FastAPI and built a Streamlit interface. To make the application persistent, I added SQLite-based research history. Every completed research run receives a unique ID, and users can retrieve and download previous reports without executing the agents again."

---

**Phase 9 Status: Completed**