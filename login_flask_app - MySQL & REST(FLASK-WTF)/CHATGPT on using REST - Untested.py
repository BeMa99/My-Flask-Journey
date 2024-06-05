Implementing a REST API in your Flask application involves creating endpoints that handle HTTP requests (GET, POST, PUT, DELETE) to perform CRUD operations
 (Create, Read, Update, Delete). You already have the basic structure and example for a GET and POST request in the previous blueprint. Let's expand on that
 and complete the REST API implementation.

### Step 1: Define RESTful Routes in Blueprint

Let's update the `example_blueprint/views.py` to include the rest of the CRUD operations:

**`app/blueprints/example_blueprint/views.py`**:

```python
# app/blueprints/example_blueprint/views.py
from flask import current_app, jsonify, request
from . import example_blueprint
from ...models import get_user, add_user, update_user, delete_user

@example_blueprint.route('/user/<int:user_id>', methods=['GET'])
def user_profile(user_id):
    user = get_user(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User not found'}), 404

@example_blueprint.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing data'}), 400

    add_user(username, email, password)
    return jsonify({'message': 'User created successfully'}), 201

@example_blueprint.route('/user/<int:user_id>', methods=['PUT'])
def update_user_profile(user_id):
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing data'}), 400

    if update_user(user_id, username, email, password):
        return jsonify({'message': 'User updated successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404

@example_blueprint.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user_profile(user_id):
    if delete_user(user_id):
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'error': 'User not found'}), 404
```

### Step 2: Implement CRUD Operations in `models.py`

Now, let's add the `update_user` and `delete_user` functions in `models.py`:

**`app/models.py`**:

```python
# app/models.py
from flask import current_app

def create_tables():
    cursor = current_app.mysql.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL
    )
    """)
    cursor.close()
    current_app.mysql.commit()

def drop_tables():
    cursor = current_app.mysql.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.close()
    current_app.mysql.commit()

def add_user(username, email, password):
    cursor = current_app.mysql.cursor()
    cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                   (username, email, password))
    cursor.close()
    current_app.mysql.commit()

def get_user(user_id):
    cursor = current_app.mysql.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return user

def update_user(user_id, username, email, password):
    cursor = current_app.mysql.cursor()
    cursor.execute("UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s",
                   (username, email, password, user_id))
    affected_rows = cursor.rowcount
    cursor.close()
    current_app.mysql.commit()
    return affected_rows > 0

def delete_user(user_id):
    cursor = current_app.mysql.cursor()
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    affected_rows = cursor.rowcount
    cursor.close()
    current_app.mysql.commit()
    return affected_rows > 0
```

### Step 3: Error Handling and Validation
Add error handling and data validation to your routes to make the API more robust.

### Step 4: Testing Your API
You can test your API using tools like Postman, curl, or by writing test scripts.

Here's how you can test the API using `curl`:

#### Create a User:
```sh
curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "email":"test@example.com", "password":"password123"}' http://127.0.0.1:5000/user
```

#### Get a User:
```sh
curl -X GET http://127.0.0.1:5000/user/1
```

#### Update a User:
```sh
curl -X PUT -H "Content-Type: application/json" -d '{"username":"updateduser", "email":"updated@example.com", "password":"newpassword123"}' http://127.0.0.1:5000/user/1
```

#### Delete a User:
```sh
curl -X DELETE http://127.0.0.1:5000/user/1
```

### Step 5: Running the Application
Make sure to run your application:

```sh
python run.py
```

This setup provides a full REST API with endpoints for creating, reading, updating, and deleting users. Adjust and expand the routes and model functions as needed
 for your specific application requirements.