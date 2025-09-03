class MistralAdapter:
    def name(self) -> str:
        return "mistral"

    def call(self, prompt: str) -> dict:
        return {"provider": "mistral", "prompt": prompt}
