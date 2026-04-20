from classes.user import User
from classes.activity import Hobbie,Task


def app():
    user1 = User("Amalia", "std170663@ac.eap.gr", "pass123$", 8, 8)
    print(user1)
    print("hello")

    hobbie1 = Hobbie(2, 5, "tennis")
    print(hobbie1)

    hobbie1.edit_time(5)
    print(hobbie1)

    task1 = Task(5, 9, "job")
    print(task1)

    task1.edit_priority(7)
    print(task1)


if __name__ == "__main__":
    app()


# import pickle
# from user import User
#
# f = open("students.pkl","rb")
# file_content = f.read()
# users = pickle.loads(file_content)
# f.close()
#
# for user in users:
#     print(user)
#
# f = open("users.pkl","wb")
# f.write(pickle.dumps(users))
# f.close()