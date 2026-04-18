class User:
    def init(self, email, password, role):
        self.email = email
        self.password = password
        self.role = role

    def str(self):
        return f"{self.email},{self.password},{self.role}"


import pickle
from user import User

f = open("students.pkl","rb")
file_content = f.read()
users = pickle.loads(file_content)
f.close()

for user in users:
    print(user)

f = open("users.pkl","wb")
f.write(pickle.dumps(users))
f.close()