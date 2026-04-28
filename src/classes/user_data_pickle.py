import pickle
from user import User

f = open("user_names_log","rb")
file_content = f.read()
user = pickle.loads(file_content)
f.close()

for user in users:
    print(user)

f = open("user.pkl","wb")
f.write(pickle.dumps(user))
f.close()