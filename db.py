from __future__ import annotations

import uuid
from functools import lru_cache
from typing import Any

from supabase import Client, create_client

from figures import FIGURE_VERSION, SOURCE_VERSION
from utils import compact_answer_for_storage, get_config


class DatabaseUnavailable(RuntimeError):
    pass


@lru_cache(maxsize=1)
def _client() -> Client:
    url = get_config("SUPABASE_URL")
    key = get_config("SUPABASE_SECRET_KEY") or get_config("SUPABASE_KEY")
    if not url or not key:
        raise DatabaseUnavailable("Supabase設定がありません。")
    return create_client(url, key)


def is_configured() -> bool:
    return bool(get_config("SUPABASE_URL") and (get_config("SUPABASE_SECRET_KEY") or get_config("SUPABASE_KEY")))


def save_consultation(figure_name: str, concern: str, answer: dict[str, Any]) -> str:
    consultation_id = str(uuid.uuid4())
    payload = {
        "id": consultation_id,
        "figure_name": figure_name,
        "concern": concern,
        "answer": compact_answer_for_storage(answer),
        "figure_version": FIGURE_VERSION,
        "source_version": SOURCE_VERSION,
    }
    _client().table("consultations").insert(payload).execute()
    return consultation_id


def save_feedback(helpful: bool, consultation_id: str | None = None) -> str:
    feedback_id = str(uuid.uuid4())
    payload = {
        "id": feedback_id,
        "consultation_id": consultation_id,
        "helpful": bool(helpful),
    }
    _client().table("feedback").insert(payload).execute()
    return feedback_id
