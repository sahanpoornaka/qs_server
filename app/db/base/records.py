from app.services.deta import get_deta

DB_NAME = "records"


def get_base():
    deta = get_deta()
    db = deta.Base(DB_NAME)
    return db
