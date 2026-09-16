import json
import os
import re
from typing import Any

from dotenv import load_dotenv

load_dotenv()

try:
    import streamlit as st
except Exception:  # pragma: no cover - allows non-Streamlit utility imports
    st = None


def get_config(key: str, default: str | None = None) -> str | None:
    value = os.getenv(key)
    if value not in (None, ""):
        return value
    if st is not None:
        try:
            value = st.secrets.get(key)
            if value not in (None, ""):
                return str(value)
        except Exception:
            pass
    return default


def parse_json_object(text: str) -> dict[str, Any]:
    """Parse an LLM response that should contain one JSON object."""
    if not text:
        raise ValueError("AI response was empty")

    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:json)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned)

    try:
        parsed = json.loads(cleaned)
        if isinstance(parsed, dict):
            return parsed
    except json.JSONDecodeError:
        pass

    start = cleaned.find("{")
    end = cleaned.rfind("}")
    if start >= 0 and end > start:
        parsed = json.loads(cleaned[start : end + 1])
        if isinstance(parsed, dict):
            return parsed

    raise ValueError("AI response was not valid JSON")


def compact_answer_for_storage(answer: dict[str, Any]) -> dict[str, Any]:
    return {
        "one_liner": answer.get("one_liner", ""),
        "analysis": answer.get("analysis", ""),
        "next_steps": answer.get("next_steps", []),
        "fact_ids": answer.get("fact_ids", []),
        "safety_note": answer.get("safety_note", ""),
        "safety_category": answer.get("safety_category", "general"),
    }
