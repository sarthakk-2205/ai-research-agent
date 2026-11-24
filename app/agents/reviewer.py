
from app.llm import generate_response


def review_analysis(
    query: str,
    research_results: list[dict],
    analysis: str
) -> str:
    """
    Review the analyst's output against collected research evidence.
    """

    if not research_results:
        return "Review cannot be completed: no research evidence available."

    # Prepare evidence for the reviewer
    research_context = ""

    for index, result in enumerate(research_results, start=1):
        research_context += f"""
[Source {index}]
Title: {result['title']}
URL: {result['url']}
Content: {result['content'][:100]}
"""

    # Create a concise review prompt
    prompt = f"""
You are a strict research quality reviewer.

Research Question:
{query}

Research Evidence:
{research_context}

Analyst Report:
{analysis[:3000]}

Review the report using the supplied evidence.

Check:
1. Are the major claims supported?
2. Are citations relevant and correctly numbered?
3. Are there unsupported or misleading claims?
4. Are there contradictions or information gaps?
5. What improvements are necessary?

Do not invent facts or sources.
Do not approve unsupported claims.

Return a concise review using EXACTLY these headings:

## Overall Decision
APPROVED or NEEDS REVISION

## Supported Claims
## Unsupported or Misleading Claims
## Citation Issues
## Information Gaps
## Recommended Improvements
## Final Reviewer Comments

Keep the entire review concise.
"""

    print("\nReviewer Agent is checking the analysis...")

    review = generate_response(
        prompt,
        max_completion_tokens=2000
    )

    return review


if __name__ == "__main__":

    from app.agents.researcher import research_subtopics
    from app.agents.analyst import analyze_research

    query = "Compare Generative AI and Agentic AI"

    topics = [
        "Core concepts of Generative AI",
        "Real-world applications of Agentic AI"
    ]

    # Step 1: Research
    results = research_subtopics(topics)

    # Step 2: Analyze
    analysis = analyze_research(query, results)

    # Step 3: Review
    review = review_analysis(query, results, analysis)

    print("\n" + "=" * 60)
    print("REVIEWER REPORT")
    print("=" * 60)

    print(review)
