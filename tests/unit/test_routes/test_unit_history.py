import pytest
import app.routes.history as history
from app.database import SessionLocal
from app.models import History


def test_get_history():
    db_session = SessionLocal()

    # Testdaten in die Datenbank einfügen
    history_entry = History(plain="A", encrypted="B")
    db_session.add(history_entry)
    db_session.commit()

    assert history.get_history() == {"plain": "A", "encrypted": "B"}

    # TODO: Überprüfen, ob die History korrekt gespeichert wurde