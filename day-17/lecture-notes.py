# PascalCase vs. camelCase vs. snake_case

class User:

    # initialising an object
    # will be called everytime we create a new user
    # required arguments
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "zeyno")
user_2 = User("002", "hazal")

print(user_1.id)
print(user_2.username)

user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)