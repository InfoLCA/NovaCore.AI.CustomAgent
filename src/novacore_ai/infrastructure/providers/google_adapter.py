class GoogleAdapter:
    def name(self) -> str:
        return "google"

    def call(self, prompt: str) -> dict:
        return {"provider": "google", "prompt": prompt}
