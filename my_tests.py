import pytest

@pytest.fixture
def mock_session_state():
    return {}

def test_session_state_updates(mock_session_state):
    mock_session_state["selected_option"] = "chatbot"
    mock_session_state["query"] = "Test input"
    mock_session_state["response"] = "Test response"

    assert mock_session_state["selected_option"] == "chatbot"
    assert mock_session_state["query"] == "Test input"
    assert mock_session_state["response"] == "Test response"
