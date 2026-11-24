
import json

from pydantic import BaseModel, Field

from app.llm import generate_response


# Define the expected structure of a research plan
class ResearchPlan(BaseModel):
    subtopics: list[str] = Field(
        min_length=3,
        max_length=5,
        description="Research subtopics generated from the user's query"
    )


def create_research_plan(query: str) -> ResearchPlan:
    """Generate a structured research plan using the LLM."""

    prompt = f"""
You are an expert research planner.

Break the following research question into 3 to 5
specific and meaningful research subtopics.

Research question:
{query}

Return ONLY valid JSON in this exact format:
{{
    "subtopics": [
        "First research subtopic",
        "Second research subtopic",
        "Third research subtopic"
    ]
}}

Do not include Markdown or explanations outside the JSON.
"""

    print("\nPlanner Agent is creating a research plan...")

    response = generate_response(
        prompt,
        max_completion_tokens=800
    )

    try:
        parsed_response = json.loads(response)
        research_plan = ResearchPlan.model_validate(parsed_response)

    except (json.JSONDecodeError, ValueError) as error:
        raise ValueError(
            f"Planner returned an invalid research plan: {error}"
        ) from error

    return research_plan


if __name__ == "__main__":
    query = "Compare Generative AI and Agentic AI"

    plan = create_research_plan(query)

    print("\nGenerated Research Plan:")

    for index, topic in enumerate(plan.subtopics, start=1):
        print(f"{index}. {topic}")
