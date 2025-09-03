class VectorDBAdapter:
    def upsert(self, key: str, vec):
        return True

    def query(self, qvec, k=3):
        return []
