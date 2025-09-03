class AuthManager:
    """Stubbed auth manager (will integrate with policy engine/OPA)."""

    def verify(self, credential: str) -> bool:
        return bool(credential)  # placeholder
