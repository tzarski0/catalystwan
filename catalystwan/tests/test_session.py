import unittest
from typing import Optional
from unittest.mock import patch

import pytest  # type: ignore
from parameterized import parameterized  # type: ignore

from catalystwan.session import ManagerSession


@pytest.mark.skip(reason="Session is not mocked property (#149)")
class TestSession(unittest.TestCase):
    def setUp(self):
        self.url = "example.com"
        self.username = "admin"
        self.password = "admin_password"

    def test_session_str(self):
        # Arrange, Act
        session = ManagerSession(self.url, self.username, self.password, port=111)

        # Assert
        self.assertEqual(str(session), "admin@https://example.com:111")

    @parameterized.expand(
        [
            (None, "http://example.com:666", "http://example.com:666"),
            (None, "www.example.com", "https://www.example.com"),
            (123, "example.com", "https://example.com:123"),
            (123, "http://example.com", "http://example.com:123"),
            (123, "https://example.com", "https://example.com:123"),
            (None, "https://example.com", "https://example.com"),
        ]
    )
    def test_base_url(self, port: Optional[int], user_url: str, expected_url: str):
        # Arrange, Act
        session = ManagerSession(user_url, self.username, self.password, port=port)
        # Assert
        self.assertEqual(session.base_url, expected_url)

    def test_session_repr(self):
        # Arrange, Act
        session = ManagerSession("domain.com", "user1", "$password", port=111)
        session_str = "ManagerSession('domain.com', 'user1', '$password', port=111, subdomain='None')"
        # Assert
        self.assertEqual(repr(session), session_str)

    def test_session_repr_different_sessions(self):
        # Arrange, Act
        session = ManagerSession("domain.com", "user1", "$password", port=111)
        session_str = "ManagerSession('not.domain.com', 'different_user', '$password', port=111, subdomain='None')"
        # Assert
        self.assertNotEqual(repr(session), session_str)

    @patch("catalystwan.session.Session.__repr__")
    def test_session_eval_repr(self, mock_repr):
        # Arrange, Act
        mock_repr.return_value = "ManagerSession('domain.com', 'user1', '$password', port=111, subdomain='None')"
        session = ManagerSession("domain.com", "user1", "$password", port=111)
        # Assert
        self.assertEqual(eval(mock_repr()), session)

    @patch("catalystwan.session.ManagerSession.check_vmanage_server_connection")
    @patch("catalystwan.session.Session.__repr__")
    def test_session_eval_repr_different_sessions(self, mock_repr, mock_check_connection):
        # Arrange, Act
        mock_check_connection.return_value = True
        mock_repr.return_value = "ManagerSession('domain.com', 'user1', '$password', port=111, subdomain='None')"
        session = ManagerSession("not.domain.com", "different_user", "$password", port=111)
        # Assert
        self.assertNotEqual(eval(mock_repr()), session)

    def test_session_eq(self):
        # Arrange, Act
        session_1 = ManagerSession("domain.com", "user1", "$password", port=111)
        session_2 = ManagerSession("domain.com", "user1", "$password", port=111)
        # Assert
        self.assertEqual(session_1, session_2)

    @patch("catalystwan.session.ManagerSession.check_vmanage_server_connection")
    def test_session_eq_different_sessions(self, mock_check_connection):
        # Arrange, Act
        mock_check_connection.return_value = True
        session_1 = ManagerSession("domain.com", "user1", "$password", port=111)
        session_2 = ManagerSession("not.domain.com", "different_user", "$password", port=111)
        # Assert
        self.assertNotEqual(session_1, session_2)

    @parameterized.expand(
        [
            (123, "/devices", "https://example.com:123/devices"),
            (123, "devices", "https://example.com:123/devices"),
            (None, "/devices", "https://example.com/devices"),
            (None, "devices", "https://example.com/devices"),
        ]
    )
    def test_get_full_url(self, port: Optional[int], url: str, full_url: str):
        # Arrange, Act
        session = ManagerSession(self.url, self.username, self.password, port=port)

        # Assert
        self.assertEqual(session.get_full_url(url), full_url)

    @patch("catalystwan.session.head")
    def test_check_vmanage_server_with_port(self, mock_head):
        # Arrange, Act
        mock_head.return_value = None
        session = ManagerSession("domain.com", "user1", "$password", port=111)
        answer = session.check_vmanage_server_connection()
        # Assert
        self.assertEqual(answer, True)

    @patch("catalystwan.session.head")
    def test_check_vmanage_server_no_port(self, mock_requests):
        # Arrange, Act
        mock_requests.return_value = None
        session = ManagerSession("domain.com", "user1", "$password")
        answer = session.check_vmanage_server_connection()
        # Assert
        self.assertEqual(answer, True)


if __name__ == "__main__":
    unittest.main()
