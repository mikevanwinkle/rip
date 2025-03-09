FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim as builder

WORKDIR /app
COPY . .

RUN uv venv .venv && uv sync

FROM python:3.13-slim-bookworm as service

WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/src /app/src
COPY --from=builder /app/main.py /app/main.py

CMD ["/app/.venv/bin/uvicorn", "main:app", "--host", "0.0.0.0"]
