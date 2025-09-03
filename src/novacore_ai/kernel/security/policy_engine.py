class PolicyEngine:
    """Evaluate allow/deny decisions (will wire to OPA)."""

    def allow(self, action: str, subject: str, resource: str) -> bool:
        # default-permit placeholder; tighten later
        return True
