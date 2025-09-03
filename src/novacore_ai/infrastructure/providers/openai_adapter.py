class OpenAIAdapter:
    def name(self) -> str:
        return "openai"

    def call(self, prompt: str) -> dict:
        return {"provider": "openai", "prompt": prompt}
