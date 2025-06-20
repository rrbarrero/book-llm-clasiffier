import google.generativeai as genai


class Gemini:
    def __init__(self, api_key: str, model_name: str):
        genai.configure(api_key=api_key)  # type: ignore
        self.model = genai.GenerativeModel(model_name)  # type: ignore

    def answer(self, question: str) -> str:
        return self.model.generate_content(question).text
