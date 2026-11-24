
from datetime import datetime
from pathlib import Path

from app.llm import generate_response


def generate_research_report(
    query: str,
    research_results: list[dict],
    analysis: str,
    review: str
) -> str:
    """
    Generate a final research report using research,
    analysis, and reviewer feedback.
    """

    if not research_results:
        raise ValueError("Cannot generate a report without research sources.")

    # Prepare source references
    references = ""

    for index, result in enumerate(research_results, start=1):
        references += f"""
[Source {index}]
Title: {result['title']}
URL: {result['url']}
Subtopic: {result['subtopic']}
"""

    prompt = f"""
You are a professional research report writer.

Research Question:
{query}

Research Analysis:
{analysis}

Reviewer Feedback:
{review}

Available Sources:
{references}

Instructions:

1. Create a professional, well-structured research report.
2. Include an executive summary.
3. Include the research findings and detailed analysis.
4. Include important comparisons and trends.
5. Include limitations and information gaps.
6. Address the reviewer's identified problems.
7. Do not introduce unsupported claims.
8. Use inline citations such as [Source 1].
9. Include a numbered references section with source titles and URLs.
10. Clearly mention the review decision.

Important:
If the reviewer says NEEDS REVISION, clearly mark
the report as NEEDS REVISION.
Do not claim that the report is verified or approved.

Use Markdown formatting.
"""

    print("\nReport Generator Agent is creating the report...")

    report = generate_response(
        prompt,
        max_completion_tokens=3000
    )

    return report


def save_report(query: str, report: str) -> Path:
    """Save the final research report as a Markdown file."""

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = f"final_report_{timestamp}.md"

    report_path = reports_dir / filename

    content = f"""# Research Query

{query}

{report}
"""

    report_path.write_text(content, encoding="utf-8")

    return report_path


if __name__ == "__main__":

    from app.agents.researcher import research_subtopics
    from app.agents.analyst import analyze_research
    from app.agents.reviewer import review_analysis

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

    # Step 4: Generate report
    report = generate_research_report(
        query,
        results,
        analysis,
        review
    )

    # Step 5: Display report
    print("\n" + "=" * 60)
    print("FINAL RESEARCH REPORT")
    print("=" * 60)

    print(report)

    # Step 6: Save report
    saved_path = save_report(query, report)

    print("\nReport saved successfully:", saved_path)
