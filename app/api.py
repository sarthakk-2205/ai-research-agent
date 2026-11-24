
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from app.workflow import research_graph
from app.database import (
    init_db,
    save_research,
    get_research_history,
    get_research_by_id
)


# Initialize FastAPI application
app = FastAPI(
    title="AI Research Agent",
    description="Multi-agent research and report generation system",
    version="1.0.0"
)


# Initialize SQLite database
init_db()


# Request format
class ResearchRequest(BaseModel):
    query: str = Field(
        ...,
        min_length=5,
        max_length=500,
        description="Research topic or question"
    )


# Home endpoint
@app.get("/")
def home():
    return {
        "project": "AI Research Agent",
        "message": "Research API is running successfully"
    }


# Health check endpoint
@app.get("/health")
def health():
    return {"status": "healthy"}


# Research endpoint
@app.post("/research")
def conduct_research(request: ResearchRequest):

    try:
        # Prepare initial LangGraph state
        initial_state = {
            "query": request.query,
            "subtopics": [],
            "research_results": [],
            "analysis": "",
            "review": "",
            "revision_count": 0,
            "review_failed": False,
            "report": "",
            "report_path": ""
        }

        # Execute complete multi-agent workflow
        result = research_graph.invoke(initial_state)

        # Save completed research in SQLite
        research_id = save_research(
            query=request.query,
            review_status=result["review"],
            revision_attempts=result["revision_count"],
            review_failed=result["review_failed"],
            report=result["report"],
            report_path=result["report_path"]
        )

        # Return research result
        return {
            "research_id": research_id,
            "query": request.query,
            "review_status": result["review"],
            "revision_attempts": result["revision_count"],
            "review_failed": result["review_failed"],
            "report": result["report"],
            "report_path": result["report_path"]
        }

    except Exception as error:
        print("Research API error:", error)

        raise HTTPException(
            status_code=500,
            detail="Research workflow failed. Please try again."
        )




    # Research history endpoint
@app.get("/history")
def research_history():

    try:
        history = get_research_history()

        return {
            "total_records": len(history),
            "history": history
        }

    except Exception as error:
        print("History API error:", error)

        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve research history."
        )




    
@app.get("/history/{research_id}")
def get_previous_research(research_id: int):

    try:
        record = get_research_by_id(research_id)

        if record is None:
            raise HTTPException(
                status_code=404,
                detail="Research record not found."
            )

        return record

    except HTTPException:
        raise

    except Exception as error:
        print("Research detail error:", error)

        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve research report."
        )

