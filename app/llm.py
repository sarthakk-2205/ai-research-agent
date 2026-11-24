
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Check your .env file.")

client = Groq(api_key=GROQ_API_KEY)


def generate_response(
    prompt: str,
    max_completion_tokens: int = 2000
) -> str:

    response = client.chat.completions.create(
    model=GROQ_MODEL,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful AI research assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ],
    temperature=0.3,
    max_completion_tokens=max_completion_tokens,
    reasoning_effort="low"
)
    choice = response.choices[0]
    message = choice.message

    print("\nDEBUG: LLM finish reason:", choice.finish_reason)
    print("DEBUG: LLM response content:", repr(message.content))

    if not message.content:
        raise ValueError(
            f"LLM returned an empty response. "
            f"Finish reason: {choice.finish_reason}"
        )

    return message.content


if __name__ == "__main__":
    answer = generate_response(
        "Explain what an AI agent is in simple terms."
    )

    print("\nAI Response:")
    print(answer)


