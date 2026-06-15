import pytest

class TestUsersAPI:
    """Test suite for Users API endpoints"""
    
    @pytest.mark.smoke
    def test_get_single_user(self, api_client, base_url):
        """Test GET /users/1 - Get single user"""
        response = api_client.get(f"{base_url}/users/1")
        
        assert response.status_code == 200, "Status code should be 200"
        assert response.json()['id'] == 1, "User ID should be 1"
        assert 'name' in response.json(), "Response should have name"
        assert 'email' in response.json(), "Response should have email"
    
    @pytest.mark.smoke
    def test_get_all_users(self, api_client, base_url):
        """Test GET /users - Get all users"""
        response = api_client.get(f"{base_url}/users")
        
        assert response.status_code == 200, "Status code should be 200"
        assert len(response.json()) == 10, "Should return 10 users"
        assert isinstance(response.json(), list), "Response should be a list"
    
    @pytest.mark.regression
    def test_user_has_required_fields(self, api_client, base_url):
        """Test user object has all required fields"""
        response = api_client.get(f"{base_url}/users/1")
        user = response.json()
        
        required_fields = ['id', 'name', 'email', 'username', 'phone', 'website']
        for field in required_fields:
            assert field in user, f"User should have '{field}' field"
    
    @pytest.mark.smoke
    def test_user_email_format(self, api_client, base_url):
        """Test user email has valid format"""
        response = api_client.get(f"{base_url}/users/1")
        user = response.json()
        email = user['email']
        
        assert '@' in email, "Email should contain @"
        assert '.' in email, "Email should contain ."
    
    @pytest.mark.regression
    def test_get_user_posts(self, api_client, base_url):
        """Test GET /posts?userId=1 - Get posts by user"""
        response = api_client.get(f"{base_url}/posts?userId=1")
        
        assert response.status_code == 200, "Status code should be 200"
        assert len(response.json()) > 0, "User should have posts"
        # All posts should belong to user 1
        for post in response.json():
            assert post['userId'] == 1, "Post should belong to user 1"