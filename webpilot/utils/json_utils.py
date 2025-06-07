
import json
import structlog
from typing import Any, Dict, Optional

logger = structlog.get_logger()

def safe_json_parse(response_text: str, fallback: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    try:
        return json.loads(response_text)
    except json.JSONDecodeError as e:
        logger.error("llm.json_parse_error", error=str(e), raw=response_text)
        return fallback or {"error": "Failed to parse LLM response"}
