from typing import Protocol


class ModelProtocol(Protocol):
    def answer(self, question: str) -> str: ...


class FakeModel:
    def answer(self, question: str) -> str:
        self.question = question
        return "fake answer"
