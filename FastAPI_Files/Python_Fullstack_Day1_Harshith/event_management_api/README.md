# Event Management API

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

- POST /events
- GET /events
- GET /events/{event_id}
- GET /events?location=Chennai
- POST /participants
- GET /participants/{participant_id}

## Sample Payloads

Create event:

```json
{
  "name": "Python Workshop",
  "location": "Chennai",
  "capacity": 100
}
```

Register participant:

```json
{
  "name": "Bhuvaneswari",
  "email": "bhuvi@email.com",
  "event_id": 1
}
```
