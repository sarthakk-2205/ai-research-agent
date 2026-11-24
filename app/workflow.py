
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from app.agents.planner import create_research_plan
from app.agents.researcher import research_subtopics
from app.agents.analyst import analyze_research
from app.agents.reviewer import review_analysis
from app.agents.report_generator import (
    generate_research_report,
    save_report
)


# 1. Define the shared state
class ResearchState(TypedDict):
    query: str
    subtopics: list[str]
    research_results: list[dict]
    analysis: str
    review: str
    revision_count: int
    review_failed: bool
    report: str
    report_path: str


# 2. Planner Agent
def planner_node(state: ResearchState):
    print("\n========== PLANNER ==========")

    plan = create_research_plan(state["query"])

    return {
        "subtopics": plan.subtopics
    }


# 3. Researcher Agent
def researcher_node(state: ResearchState):
    print("\n========== RESEARCHER ==========")

    results = research_subtopics(
        state["subtopics"],
        max_results=2
    )

    return {
        "research_results": results
    }


# 4. Analyst Agent
def analyst_node(state: ResearchState):
    print("\n========== ANALYST ==========")

    feedback = state["review"]
    revision_count = state["revision_count"]

    if feedback:
        revision_count += 1
        print("Improving analysis using reviewer feedback...")

    print("Revision count:", revision_count)

    analysis = analyze_research(
        state["query"],
        state["research_results"],
        review_feedback=feedback
    )

    return {
        "analysis": analysis,
        "revision_count": revision_count
    }


# 5. Reviewer Agent
def reviewer_node(state: ResearchState):
    print("\n========== REVIEWER ==========")

    try:
        review = review_analysis(
            state["query"],
            state["research_results"],
            state["analysis"]
        )

        print("\nReviewer completed successfully.")

        return {
            "review": review,
            "review_failed": False
        }

    except ValueError as error:
        print("\nReviewer failed:", error)

        fallback_review = """
## Overall Decision
NEEDS REVISION

## Final Reviewer Comments
The Reviewer could not complete its evaluation.
This report must be treated as unreviewed and unapproved.
"""

        return {
            "review": fallback_review,
            "review_failed": True
        }


# 6. Conditional routing after Reviewer
def review_decision(state: ResearchState):

    # If reviewer failed, do not retry indefinitely
    if state["review_failed"]:
        print("\nReviewer failed. Generating report with warnings.")
        return "generate_report"

    review_text = state["review"]
    decision_section = ""

    if "## Overall Decision" in review_text:
        decision_section = (
            review_text.split("## Overall Decision", 1)[1]
            .split("##", 1)[0]
            .upper()
        )

    approved = (
        "APPROVED" in decision_section
        and "NEEDS REVISION" not in decision_section
    )

    if approved:
        print("\nReview approved!")
        return "generate_report"

    if state["revision_count"] < 2:
        print("\nReview requires revision. Sending feedback to Analyst...")
        return "revise"

    print("\nMaximum revisions reached. Generating report with warnings.")
    return "generate_report"


# 7. Report Generator Agent
def report_generator_node(state: ResearchState):
    print("\n========== REPORT GENERATOR ==========")

    report = generate_research_report(
        state["query"],
        state["research_results"],
        state["analysis"],
        state["review"]
    )

    saved_path = save_report(
        state["query"],
        report
    )

    print("\nReport saved:", saved_path)

    return {
        "report": report,
        "report_path": str(saved_path)
    }


# 8. Build LangGraph workflow
builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("researcher", researcher_node)
builder.add_node("analyst", analyst_node)
builder.add_node("reviewer", reviewer_node)
builder.add_node("report_generator", report_generator_node)

# Define workflow sequence
builder.add_edge(START, "planner")
builder.add_edge("planner", "researcher")
builder.add_edge("researcher", "analyst")
builder.add_edge("analyst", "reviewer")

# Reviewer decides the next step
builder.add_conditional_edges(
    "reviewer",
    review_decision,
    {
        "revise": "analyst",
        "generate_report": "report_generator"
    }
)

builder.add_edge("report_generator", END)

# Compile graph
research_graph = builder.compile()


# 9. Run workflow
if __name__ == "__main__":

    result = research_graph.invoke({
        "query": "Compare Generative AI and Agentic AI",
        "subtopics": [],
        "research_results": [],
        "analysis": "",
        "review": "",
        "revision_count": 0,
        "review_failed": False,
        "report": "",
        "report_path": ""
    })

    print("\n========== WORKFLOW COMPLETED ==========")

    print("\nReview status:")

    if "## Overall Decision" in result["review"]:
        print(
            result["review"]
            .split("## Overall Decision", 1)[1]
            .split("##", 1)[0]
            .strip()
        )

    print("\nRevision attempts:", result["revision_count"])
    print("Reviewer failed:", result["review_failed"])
    print("Report location:", result["report_path"])

