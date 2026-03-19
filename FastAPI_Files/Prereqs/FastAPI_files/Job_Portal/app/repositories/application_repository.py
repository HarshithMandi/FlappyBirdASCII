from app.model.application import Application

def apply_for_job(db, application: dict):
    db_application = Application(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application