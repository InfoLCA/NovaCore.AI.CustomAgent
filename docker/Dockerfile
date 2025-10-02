FROM platform-base:1.0.0
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
# Minimal deps for serving
RUN pip install --no-cache-dir fastapi uvicorn
# Copy source
COPY src ./src
# Default service
EXPOSE 8000
CMD ["uvicorn","novacore_ai.api:app","--host","0.0.0.0","--port","8000"]
