import requests

# Test 1: GET single post
def test_get_single_post():
    """Test getting a single post"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    print(f"\n📍 Test 1: GET /posts/1")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Assertions
    assert response.status_code == 200, "Status code should be 200"
    assert response.json()['id'] == 1, "Post ID should be 1"
    assert 'title' in response.json(), "Response should have title"
    
    print("✅ Test 1 PASSED")

# Test 2: GET all posts
def test_get_all_posts():
    """Test getting all posts"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f"\n📍 Test 2: GET /posts")
    print(f"Status Code: {response.status_code}")
    print(f"Number of posts: {len(response.json())}")
    
    # Assertions
    assert response.status_code == 200, "Status code should be 200"
    assert len(response.json()) == 100, "Should return 100 posts"
    assert isinstance(response.json(), list), "Response should be a list"
    
    print("✅ Test 2 PASSED")

# Test 3: POST - Create new post
def test_create_new_post():
    """Test creating a new post"""
    url = "https://jsonplaceholder.typicode.com/posts"
    
    # Data to send
    payload = {
        "title": "My API Test Post",
        "body": "This is a test from Python",
        "userId": 1
    }
    
    response = requests.post(url, json=payload)
    
    print(f"\n📍 Test 3: POST /posts")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Assertions
    assert response.status_code == 201, "Status code should be 201 (Created)"
    assert response.json()['title'] == "My API Test Post", "Title should match"
    assert response.json()['body'] == "This is a test from Python", "Body should match"
    
    print("✅ Test 3 PASSED")

# Test 4: PUT - Update post
def test_update_post():
    """Test updating an existing post"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    
    # Updated data
    payload = {
        "id": 1,
        "title": "Updated Post Title",
        "body": "This post has been updated",
        "userId": 1
    }
    
    response = requests.put(url, json=payload)
    
    print(f"\n📍 Test 4: PUT /posts/1")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
    
    # Assertions
    assert response.status_code == 200, "Status code should be 200"
    assert response.json()['title'] == "Updated Post Title", "Title should be updated"
    
    print("✅ Test 4 PASSED")

# Test 5: DELETE post
def test_delete_post():
    """Test deleting a post"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    
    print(f"\n📍 Test 5: DELETE /posts/1")
    print(f"Status Code: {response.status_code}")
    
    # Assertions
    assert response.status_code == 200, "Status code should be 200"
    
    print("✅ Test 5 PASSED")

# Test 6: Response time
def test_response_time():
    """Test API response time is acceptable"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    response_time = response.elapsed.total_seconds()
    
    print(f"\n📍 Test 6: Response Time Check")
    print(f"Response Time: {response_time} seconds")
    
    # Assertions
    assert response_time < 2, "Response should be under 2 seconds"
    
    print("✅ Test 6 PASSED")

# Test 7: Check response headers
def test_response_headers():
    """Test response headers"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    print(f"\n📍 Test 7: Response Headers")
    print(f"Content-Type: {response.headers.get('content-type')}")
    
    # Assertions
    assert 'json' in response.headers.get('content-type'), "Should return JSON"
    
    print("✅ Test 7 PASSED")

# Run all tests
if __name__ == "__main__":
    print("=" * 60)
    print("🧪 Running API Tests")
    print("=" * 60)
    
    try:
        test_get_single_post()
        test_get_all_posts()
        test_create_new_post()
        test_update_post()
        test_delete_post()
        test_response_time()
        test_response_headers()
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED! 🎉")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")