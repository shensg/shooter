from src.models.sys import User

username = "admin"
user_data = User.select().where(User.name == username).get()
print(user_data.name)

# curl -X POST http://127.0.0.1:8000/login -H "Content-Type: application/json" -d '{"username": "admin", "password": "123456"}'

