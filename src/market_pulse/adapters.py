from __future__ import annotations
from abc import ABC, abstractmethod
from pathlib import Path
import json

class EvidenceAdapter(ABC):
    """Approved acquisition systems implement this boundary and return schema-compatible records."""
    @abstractmethod
    def collect(self, start_date: str, end_date: str) -> list[dict]: ...

class JsonFileAdapter(EvidenceAdapter):
    def __init__(self, path: str | Path): self.path=Path(path)
    def collect(self, start_date: str, end_date: str) -> list[dict]:
        return json.loads(self.path.read_text())

class ProductIntelligenceAdapter(ABC):
    """Must use official OpenAI sources only. Output is never accepted by sentiment scoring."""
    @abstractmethod
    def refresh(self) -> list[dict]: ...
