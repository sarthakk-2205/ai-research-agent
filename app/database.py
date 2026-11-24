
import sqlite3
from pathlib import Path


# Database file location
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "research_history.db"


# Create database table
def init_db():

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS research_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            review_status TEXT,
            revision_attempts INTEGER,
            review_failed BOOLEAN,
            report TEXT,
            report_path TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


# Save a research result
def save_research(
    query,
    review_status,
    revision_attempts,
    review_failed,
    report,
    report_path
):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO research_history (
            query,
            review_status,
            revision_attempts,
            review_failed,
            report,
            report_path
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        query,
        review_status,
        revision_attempts,
        review_failed,
        report,
        report_path
    ))

    research_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return research_id


# Retrieve research history
def get_research_history():

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, query, review_status, revision_attempts,
               review_failed, report_path, created_at
        FROM research_history
        ORDER BY created_at DESC
    """)

    records = [dict(row) for row in cursor.fetchall()]

    conn.close()

    return records



def get_research_by_id(research_id):
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM research_history
        WHERE id = ?
    """, (research_id,))

    record = cursor.fetchone()
    conn.close()

    return dict(record) if record else None
