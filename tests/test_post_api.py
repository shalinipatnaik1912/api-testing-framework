import pytest

class TestPostsAPI:
    """Test suite for Posts API endpoints"""
    
    @pytest.mark.smoke
    def test_get_single_post(self, api_client, base_url):
        """Test GET /posts/1 - Get single post"""
        response = api_client.get(f"{base_url}/posts/1")
        
        assert response.status_code == 200, "Status code should be 200"
        assert response.json()['id'] == 1, "Post ID should be 1"
        assert 'title' in response.json(), "Response should have title"
        assert 'body' in response.json(), "Response should have body"
    
    @pytest.mark.smoke
    def test_get_all_posts(self, api_client, base_url):
        """Test GET /posts - Get all posts"""
        response = api_client.get(f"{base_url}/posts")
        
        assert response.status_code == 200, "Status code should be 200"
        assert len(response.json()) == 100, "Should return 100 posts"
        assert isinstance(response.json(), list), "Response should be a list"
    
    @pytest.mark.regression
    def test_create_post(self, api_client, base_url, valid_post_data):
        """Test POST /posts - Create new post"""
        response = api_client.post(f"{base_url}/posts", json=valid_post_data)
        
        assert response.status_code == 201, "Status code should be 201 (Created)"
        assert response.json()['title'] == valid_post_data['title'], "Title should match"
        assert response.json()['body'] == valid_post_data['body'], "Body should match"
        assert response.json()['userId'] == valid_post_data['userId'], "UserID should match"
    
    @pytest.mark.regression
    def test_update_post(self, api_client, base_url):
        """Test PUT /posts/1 - Update post"""
        updated_data = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated Body",
            "userId": 1
        }
        response = api_client.put(f"{base_url}/posts/1", json=updated_data)
        
        assert response.status_code == 200, "Status code should be 200"
        assert response.json()['title'] == "Updated Title", "Title should be updated"
        assert response.json()['body'] == "Updated Body", "Body should be updated"
    
    @pytest.mark.regression
    def test_delete_post(self, api_client, base_url):
        """Test DELETE /posts/1 - Delete post"""
        response = api_client.delete(f"{base_url}/posts/1")
        
        assert response.status_code == 200, "Status code should be 200"
    
    @pytest.mark.smoke
    def test_response_time(self, api_client, base_url):
        """Test API response time is acceptable"""
        response = api_client.get(f"{base_url}/posts/1")
        
        response_time = response.elapsed.total_seconds()
        assert response_time < 2, f"Response time should be under 2 seconds, got {response_time}"
    
    @pytest.mark.smoke
    def test_response_content_type(self, api_client, base_url):
        """Test response content type is JSON"""
        response = api_client.get(f"{base_url}/posts/1")
        
        assert 'json' in response.headers.get('content-type', ''), "Should return JSON content type"
    
    @pytest.mark.negative
    def test_get_invalid_post(self, api_client, base_url):
        """Test GET with invalid post ID"""
        response = api_client.get(f"{base_url}/posts/999999")
        
        # JSONPlaceholder returns 404 for invalid IDs
        assert response.status_code == 404, "Status code should be 404 for a missing post"