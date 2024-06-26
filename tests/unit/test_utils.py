import pytest
from backend.app.utils import *
import hashlib
import json
from unittest.mock import mock_open, patch

def test_read_user_data():
    mock_file_data = json.dumps({"users" : [{"name": "Alice", "username": "Wonderland", "email": "Alice@example.de", "password": "hashed_password"}]})
    with patch('builtins.open', mock_open(read_data=mock_file_data)):
        user = read_user_data()
        assert user == [{"name": "Alice", "username": "Wonderland", "email": "Alice@example.de", "password": "hashed_password"}]


def test_read_user_data_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError):
        users = read_user_data()
        assert users == []

def test_read_user_data_json_decode_error():
    mock_file_data = "{invalid json}"
    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        users = read_user_data()
        assert users == []

def test_hash_password():
    password = "mysecretpassword"
    expected_hash = hashlib.sha256(password.encode()).hexdigest()
    assert hash_password(password) == expected_hash
