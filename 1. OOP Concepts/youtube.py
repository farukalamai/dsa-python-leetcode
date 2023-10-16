
class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0):
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user): # method means function under the class
        user.subscribers +=1
        self.subscriptions +=1

        
user1 = Youtube("Faruk")
user2 = Youtube("Alam")

print("When user 1 suscrbie user 2")
user1.subscribe(user2) 
print(user1.username)
print(f"User 1 Subscriber: {user1.subscribers}")
print(f"User 1 Subscription: {user1.subscriptions}")
print(user2.username)
print(f"User 2 Subscriber: {user2.subscribers}")
print(f"User 2 Subscription: {user2.subscriptions}")

print("-------------------------------------------------------------------------------------")

print("When user 2 suscrbie user 1")
user2.subscribe(user1)
print(user1.username)
print(f"User 1 Subscriber: {user1.subscribers}")
print(f"User 1 Subscription: {user1.subscriptions}")
print(user2.username)
print(f"User 2 Subscriber: {user2.subscribers}")
print(f"User 2 Subscription: {user2.subscriptions}")







# intializing the object
# attribute is variable whihc is assocoiated with a object
# class 
# code templete for creating programming object
# class commponent
# name, attribute, methods ( to  do some aaction and return some value)