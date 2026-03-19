from app.model.application import Application

def _schema_to_dict(schema) -> dict:
    if isinstance(schema, dict):
        return schema
    if hasattr(schema, "model_dump"):
        return schema.model_dump()
    return schema.dict()


def apply_for_job(db, application):
    db_application = Application(**_schema_to_dict(application))
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application