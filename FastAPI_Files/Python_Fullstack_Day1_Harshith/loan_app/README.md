# Loan Management API

Clean Architecture FastAPI project using in-memory storage.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## Endpoints

- POST /loans
- GET /loans
- GET /loans/{loan_id}
- PUT /loans/{loan_id}/approve
- PUT /loans/{loan_id}/reject
