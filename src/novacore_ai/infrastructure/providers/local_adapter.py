class LocalAdapter:
    def name(self) -> str:
        return "local"

    def call(self, prompt: str) -> dict:
        return {"provider": "local", "prompt": prompt}
