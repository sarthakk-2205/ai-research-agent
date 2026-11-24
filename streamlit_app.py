
import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔍",
    layout="wide"
)

import os

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")
RESEARCH_URL = f"{API_URL}/research"
HISTORY_URL = f"{API_URL}/history"


# Application heading
st.title("🔍 AI Research Agent")

st.write(
    "An AI-powered multi-agent system that researches topics, "
    "analyzes information, reviews findings, and generates reports."
)

st.divider()


# Function to display a research report
def display_report(result):

    st.subheader("Research Results")

    st.write("**Research ID:**", result.get("id", result.get("research_id", "N/A")))
    st.write("**Research Query:**", result["query"])

    st.write("**Reviewer Decision:**")
    st.markdown(result["review_status"])

    st.write("**Revision Attempts:**", result["revision_attempts"])

    if result.get("review_failed"):
        st.warning("The reviewer encountered an error.")
        
    st.divider()

    st.subheader("Generated Research Report")

    st.markdown(result["report"])

    st.download_button(
        label="📥 Download Research Report",
        data=result["report"],
        file_name=f"research_report_{result.get('id', result.get('research_id', 'latest'))}.md",
        mime="text/markdown",
        key=f"download_{result.get('id', result.get('research_id', 'latest'))}"
    )


# Sidebar: Research history
st.sidebar.title("📚 Research History")

try:
    history_response = requests.get(
        HISTORY_URL,
        timeout=10
    )

    history_response.raise_for_status()

    history_data = history_response.json()
    history_records = history_data.get("history", [])

    st.sidebar.write(
        f"Previous research runs: {len(history_records)}"
    )

    if history_records:

        history_options = {
            f"#{item['id']} - {item['query']}": item["id"]
            for item in history_records
        }

        selected_label = st.sidebar.selectbox(
            "Select previous research:",
            options=list(history_options.keys()),
            index=None,
            placeholder="Choose a research record"
        )

        if selected_label:

            selected_id = history_options[selected_label]

            try:
                detail_response = requests.get(
                    f"{HISTORY_URL}/{selected_id}",
                    timeout=10
                )

                detail_response.raise_for_status()

                previous_result = detail_response.json()

                st.sidebar.success(
                    f"Loaded research #{selected_id}"
                )

                display_report(previous_result)

            except requests.exceptions.RequestException as error:
                st.sidebar.error(
                    f"Could not load previous report: {error}"
                )

    else:
        st.sidebar.info("No previous research records found.")

except requests.exceptions.RequestException:
    st.sidebar.warning(
        "Could not connect to the research history API."
    )


# New research section
st.subheader("🚀 Start New Research")

query = st.text_area(
    "Enter your research topic:",
    placeholder="Example: Compare Generative AI and Agentic AI",
    height=120
)


if st.button("🚀 Start Research", type="primary"):

    if len(query.strip()) < 5:

        st.warning(
            "Please enter a research query with at least 5 characters."
        )

    else:

        try:
            with st.spinner(
                "Researching... Our AI agents are working. Please wait."
            ):

                response = requests.post(
                    RESEARCH_URL,
                    json={"query": query.strip()},
                    timeout=600
                )

            response.raise_for_status()

            result = response.json()

            st.success(
                f"Research completed! Research ID: {result['research_id']}"
            )

            display_report(result)

            st.info(
                "Refresh the page to see this research in the history section."
            )

        except requests.exceptions.ConnectionError:

            st.error(
                "Cannot connect to FastAPI. "
                "Please make sure the API server is running."
            )

        except requests.exceptions.Timeout:

            st.error(
                "The research request timed out. Please try again."
            )

        except requests.exceptions.HTTPError as error:

            st.error(f"API Error: {error}")

        except requests.exceptions.RequestException as error:

            st.error(f"Request failed: {error}")

        except Exception as error:

            st.error(f"An unexpected error occurred: {error}")
