from db import Data, User

u = Data()
print(u.user_register("Darshan", 23))
for i in u.get_users():
    print(i.name, i.age)