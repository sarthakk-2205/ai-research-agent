
import os

from dotenv import load_dotenv
from tavily import TavilyClient

# Load environment variables
load_dotenv()

# Read Tavily API key
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY is missing. Check your .env file.")

# Initialize Tavily client
client = TavilyClient(api_key=TAVILY_API_KEY)


def search_web(query: str, max_results: int = 5) -> list[dict]:
    """
    Search the web using Tavily and return structured results.
    """

    response = client.search(
        query=query,
        search_depth="basic",
        max_results=max_results,
        include_answer=False
    )

    results = []

    for item in response.get("results", []):
        results.append({
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", ""),
            "score": item.get("score", 0.0)
        })

    return results


if __name__ == "__main__":
    query = "Recent developments in Generative AI"

    search_results = search_web(query)

    for index, result in enumerate(search_results, start=1):
        print(f"\n--- Result {index} ---")
        print("Title:", result["title"])
        print("URL:", result["url"])
        print("Score:", result["score"])
        print("Content:", result["content"][:500])
