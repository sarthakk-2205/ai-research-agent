
from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from app.agents.planner import create_research_plan


# Shared state of our research workflow
class ResearchState(TypedDict):
    query: str
    subtopics: list[str]


# Actual Planner Agent node
def planner_node(state: ResearchState):
    print("\nPlanner Agent is working...")

    plan = create_research_plan(state["query"])

    return {
        "subtopics": plan.subtopics
    }


# Build the LangGraph workflow
builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)

builder.add_edge(START, "planner")
builder.add_edge("planner", END)

graph = builder.compile()


if __name__ == "__main__":

    result = graph.invoke({
        "query": "Compare Generative AI and Agentic AI",
        "subtopics": []
    })

    print("\nFinal Research State:")
    print(result)

    print("\nGenerated Subtopics:")

    for index, topic in enumerate(result["subtopics"], start=1):
        print(f"{index}. {topic}")

