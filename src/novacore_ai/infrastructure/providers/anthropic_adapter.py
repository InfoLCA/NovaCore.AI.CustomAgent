class AnthropicAdapter:
    def name(self) -> str:
        return "anthropic"

    def call(self, prompt: str) -> dict:
        return {"provider": "anthropic", "prompt": prompt}
