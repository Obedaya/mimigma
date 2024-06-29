import pytest
import app.routes.history as history
from app.database import SessionLocal
from app.models import History


def test_get_history():
    db_session = SessionLocal()

    user_id = 200

    # Testdaten in die Datenbank einfügen
    db_session.query(History).filter(History.user_id == user_id).delete()
    history_entry = History(user_id=user_id, plain="A", encrypted="B")
    db_session.add(history_entry)
    db_session.commit()

    assert history.get_history(user_id) == {"plain": "A", "encrypted": "B"}
