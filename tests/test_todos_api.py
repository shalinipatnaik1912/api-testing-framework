import pytest

class TestTodosAPI:
    """Test suite for Todos API endpoints"""
    
    @pytest.mark.smoke
    def test_get_single_todo(self, api_client, base_url):
        """Test GET /todos/1 - Get single todo"""
        response = api_client.get(f"{base_url}/todos/1")
        
        assert response.status_code == 200, "Status code should be 200"
        assert response.json()['id'] == 1, "Todo ID should be 1"
        assert 'title' in response.json(), "Response should have title"
        assert 'completed' in response.json(), "Response should have completed status"
    
    @pytest.mark.smoke
    def test_get_all_todos(self, api_client, base_url):
        """Test GET /todos - Get all todos"""
        response = api_client.get(f"{base_url}/todos")
        
        assert response.status_code == 200, "Status code should be 200"
        assert len(response.json()) == 200, "Should return 200 todos"
        assert isinstance(response.json(), list), "Response should be a list"
    
    @pytest.mark.regression
    def test_get_user_todos(self, api_client, base_url):
        """Test GET /todos?userId=1 - Get todos for specific user"""
        response = api_client.get(f"{base_url}/todos?userId=1")
        
        assert response.status_code == 200, "Status code should be 200"
        assert len(response.json()) > 0, "User should have todos"
        # All todos should belong to user 1
        for todo in response.json():
            assert todo['userId'] == 1, "Todo should belong to user 1"
    
    @pytest.mark.regression
    def test_todo_completion_status(self, api_client, base_url):
        """Test todo completion status is boolean"""
        response = api_client.get(f"{base_url}/todos/1")
        todo = response.json()
        
        assert isinstance(todo['completed'], bool), "Completed should be boolean"
    
    @pytest.mark.positive
    def test_create_todo(self, api_client, base_url):
        """Test POST /todos - Create new todo"""
        new_todo = {
            "title": "Test Todo",
            "completed": False,
            "userId": 1
        }
        response = api_client.post(f"{base_url}/todos", json=new_todo)
        
        assert response.status_code == 201, "Status code should be 201"
        assert response.json()['title'] == "Test Todo", "Title should match"