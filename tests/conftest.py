import pytest
import requests

@pytest.fixture
def api_client():
    """Fixture to provide API client (requests.Session)"""
    session = requests.Session()
    return session

@pytest.fixture
def base_url():
    """Base URL for JSONPlaceholder API"""
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def valid_post_data():
    """Valid post data for testing"""
    return {
        "title": "Test Post",
        "body": "This is a test post body",
        "userId": 1
    }

@pytest.fixture
def valid_user_data():
    """Valid user data for testing"""
    return {
        "name": "Test User",
        "email": "testuser@example.com",
        "username": "testuser",
        "phone": "1234567890",
        "website": "https://test.com"
    }

@pytest.fixture
def valid_comment_data():
    """Valid comment data for testing"""
    return {
        "body": "This is a test comment",
        "email": "test@example.com",
        "name": "Test Comment",
        "postId": 1
    }

@pytest.fixture
def valid_todo_data():
    """Valid todo data for testing"""
    return {
        "title": "Test Todo",
        "completed": False,
        "userId": 1
    }