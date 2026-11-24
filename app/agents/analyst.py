
from app.llm import generate_response


def analyze_research(
    query: str,
    research_results: list[dict],
    review_feedback: str = ""
) -> str:
    """Analyze collected research sources using the LLM."""

    if not research_results:
        return "No research data available for analysis."

    research_context = ""

    # Limit the amount of source content sent to the LLM
    for index, result in enumerate(research_results[:10], start=1):
        research_context += f"""
[Source {index}]
Subtopic: {result['subtopic']}
Title: {result['title']}
URL: {result['url']}
Content: {result['content'][:300]}
"""

    prompt = f"""
You are an expert research analyst.

Research Question:
{query}

Collected Research:
{research_context}

Previous Reviewer Feedback:
{review_feedback[:1500]}

Your tasks:
1. Identify the most important findings.
2. Compare different perspectives.
3. Explain major similarities and differences.
4. Identify important trends.
5. Highlight information gaps.
6. Address previous reviewer feedback.
7. Do not invent unsupported facts.
8. Use citations such as [Source 1].

Write a concise, structured analysis with these headings:
- Key Findings
- Comparison
- Major Trends
- Information Gaps
- Conclusion

Keep the analysis focused and avoid unnecessary repetition.
"""

    print("\nAnalyst Agent is analyzing research...")

    analysis = generate_response(
        prompt,
        max_completion_tokens=1200
    )

    return analysis


if __name__ == "__main__":

    from app.agents.researcher import research_subtopics

    query = "Compare Generative AI and Agentic AI"

    topics = [
        "Core concepts of Generative AI",
        "Real-world applications of Agentic AI"
    ]

    results = research_subtopics(topics)

    analysis = analyze_research(query, results)

    print("\n" + "=" * 60)
    print("RESEARCH ANALYSIS")
    print("=" * 60)
    print(analysis)

