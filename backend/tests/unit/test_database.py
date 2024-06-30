import pytest
from unittest.mock import patch, MagicMock
from app.database import check_db_connection, get_db, engine

def test_check_db_connection():
    with patch("app.database.engine.connect") as mock_connect:
        mock_connect.return_value.__enter__.return_value = MagicMock()
        check_db_connection(engine)
        mock_connect.assert_called_once()
        print("Database connection successful")

def test_get_db():
    with patch("app.database.SessionLocal") as MockSession:
        mock_session = MockSession.return_value
        mock_session.close = MagicMock()

        generator = get_db()
        db = next(generator)
        assert db is not None
        mock_session.close.assert_not_called()
        next(generator, None)
        mock_session.close.assert_called_once() 


