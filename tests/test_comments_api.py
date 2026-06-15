import pytest

class TestCommentsAPI:
    """Test suite for Comments API endpoints"""
    
    @pytest.mark.smoke
    def test_get_single_comment(self, api_client, base_url):
        """Test GET /comments/1 - Get single comment"""
        response = api_client.get(f"{base_url}/comments/1")
        
        assert response.status_code == 200, "Status code should be 200"
        assert response.json()['id'] == 1, "Comment ID should be 1"
        assert 'body' in response.json(), "Response should have body"
        assert 'email' in response.json(), "Response should have email"
    
    @pytest.mark.smoke
    def test_get_all_comments(self, api_client, base_url):
        """Test GET /comments - Get all comments"""
        response = api_client.get(f"{base_url}/comments")
        
        assert response.status_code == 200, "Status code should be 200"
        assert len(response.json()) == 500, "Should return 500 comments"
        assert isinstance(response.json(), list), "Response should be a list"
    
    @pytest.mark.regression
    def test_get_post_comments(self, api_client, base_url):
        """Test GET /posts/:id/comments - Get comments for a post"""
        response = api_client.get(f"{base_url}/posts/1/comments")
        
        assert response.status_code == 200, "Status code should be 200"
        assert len(response.json()) > 0, "Post should have comments"
        # All comments should be for post 1
        for comment in response.json():
            assert comment['postId'] == 1, "Comment should belong to post 1"
    
    @pytest.mark.regression
    def test_comment_has_required_fields(self, api_client, base_url):
        """Test comment object has required fields"""
        response = api_client.get(f"{base_url}/comments/1")
        comment = response.json()
        
        required_fields = ['id', 'postId', 'name', 'email', 'body']
        for field in required_fields:
            assert field in comment, f"Comment should have '{field}' field"
    
    @pytest.mark.smoke
    def test_comment_email_format(self, api_client, base_url):
        """Test comment email has valid format"""
        response = api_client.get(f"{base_url}/comments/1")
        comment = response.json()
        email = comment['email']
        
        assert '@' in email, "Email should contain @"
        assert '.' in email, "Email should contain ."