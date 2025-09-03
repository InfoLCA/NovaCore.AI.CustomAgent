class BlobStorageAdapter:
    def put(self, path: str, data: bytes):
        return len(data)

    def get(self, path: str) -> bytes:
        return b""
