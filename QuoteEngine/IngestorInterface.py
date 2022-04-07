"""Abstract class to serve as interface for the importation."""
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """Interface for the quotes' importation."""

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path):
        """Check if the file extention is allowed."""
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Abstract - Implemented in Ingestor.py."""
        pass
