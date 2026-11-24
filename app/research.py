
from datetime import datetime
from pathlib import Path

from app.llm import generate_response
from app.tools.web_search import search_web


def conduct_research(query: str) -> str:
    """Search the web and generate a structured research report."""

    print("\nSearching the web...")
    search_results = search_web(query, max_results=5)

    if not search_results:
        return "No relevant search results found."

    research_context = ""

    for index, result in enumerate(search_results, start=1):
        research_context += f"""
Source {index}
Title: {result['title']}
URL: {result['url']}
Content: {result['content']}
"""

    prompt = f"""
You are an AI research analyst.

Research Question:
{query}

Web Search Information:
{research_context}

Instructions:
1. Answer the research question clearly.
2. Organize the report using meaningful headings.
3. Identify important findings and trends.
4. Compare different perspectives where relevant.
5. Do not invent facts unsupported by the sources.
6. Mention information gaps and limitations.
7. Cite claims using [Source 1], [Source 2], etc.
8. Only cite sources provided below.
9. Do not invent authors or publication dates.
10. Include a numbered list of source titles and URLs.

Generate a structured research report.
"""

    print("Analyzing search results and generating report...")
    report = generate_response(
        prompt,
        max_completion_tokens=2000
    )

    return report


def save_report(query: str, report: str) -> Path:
    """Save the research report as a Markdown file."""

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"research_report_{timestamp}.md"

    report_path = reports_dir / filename

    report_content = f"# Research Query\n\n{query}\n\n{report}"

    report_path.write_text(report_content, encoding="utf-8")

    return report_path


if __name__ == "__main__":
    research_query = "Compare Generative AI and Agentic AI"

    final_report = conduct_research(research_query)

    print("\n" + "=" * 60)
    print("FINAL RESEARCH REPORT")
    print("=" * 60)
    print(final_report)

    if final_report != "No relevant search results found.":
        saved_path = save_report(research_query, final_report)
        print(f"\nReport saved successfully: {saved_path}")

