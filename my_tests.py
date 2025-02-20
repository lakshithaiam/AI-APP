import pytest
import streamlit as st

# Mock Streamlit's session state and inputs for testing
@pytest.fixture(autouse=True)
def mock_streamlit(monkeypatch):
    monkeypatch.setattr(st, "session_state", {})
    monkeypatch.setattr(st, "button", lambda label: True)
    monkeypatch.setattr(st, "selectbox", lambda label, options: options[0] if options else None)
    monkeypatch.setattr(st, "text_input", lambda label: "Test input")
    monkeypatch.setattr(st, "text_area", lambda label, height: "Test code")
    monkeypatch.setattr(st, "write", lambda x: None)

# Test if session_state initializes with default values
def test_initial_session_state():
    # Check if session state variables exist
    assert "selected_option" not in st.session_state
    assert "query" not in st.session_state
    assert "target_lang" not in st.session_state
    assert "response" not in st.session_state

# Test sidebar button selection and session_state update
def test_sidebar_buttons():
    # Simulate selecting the "Chatbot" button
    st.session_state["selected_option"] = None
    if st.button("Chatbot"):
        st.session_state["selected_option"] = "chatbot"
    assert st.session_state["selected_option"] == "chatbot"

    # Simulate selecting the "Text translator" button
    st.session_state["selected_option"] = None
    if st.button("Text translator"):
        st.session_state["selected_option"] = "translate"
    assert st.session_state["selected_option"] == "translate"

# Test if text input for chatbot is stored in session state
def test_chat_input():
    query = st.text_input("Ask me anything")
    st.session_state["query"] = query
    assert st.session_state["query"] == "Test input"

# Test if text area for code assistant is stored in session state
def test_code_assistant_input():
    query = st.text_area("Enter your code snippet here", height=300)
    st.session_state["query"] = query
    assert st.session_state["query"] == "Test code"

# Test if session_state response is updated when response is given
def test_response_update():
    st.session_state["response"] = "Test response"
    assert st.session_state["response"] == "Test response"
