
from app.tools.web_search import search_web


def research_subtopics(
    subtopics: list[str],
    max_results: int = 3
) -> list[dict]:
    """
    Search the web for every research subtopic.
    Return all collected sources.
    """

    all_results = []

    for index, topic in enumerate(subtopics, start=1):

        print(f"\nResearching topic {index}: {topic}")

        search_results = search_web(
            query=topic,
            max_results=max_results
        )

        if not search_results:
            print("No results found for this topic.")
            continue

        for result in search_results:
            all_results.append({
                "subtopic": topic,
                "title": result["title"],
                "url": result["url"],
                "content": result["content"],
                "score": result["score"]
            })

    return all_results


if __name__ == "__main__":

    test_topics = [
        "Core concepts of Generative AI",
        "Real-world applications of Agentic AI"
    ]

    results = research_subtopics(test_topics)

    print("\nTotal sources collected:", len(results))

    for index, result in enumerate(results, start=1):
        print(f"\n--- Source {index} ---")
        print("Subtopic:", result["subtopic"])
        print("Title:", result["title"])
        print("URL:", result["url"])
        print("Content:", result["content"][:300])
