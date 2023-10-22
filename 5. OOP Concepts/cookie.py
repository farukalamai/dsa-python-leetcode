
class StarCookie: # Class name - Identifier
    milk = 0.5 # Global Variable

    def __init__(self, color, weight): # Intializer - Initilizing the all atrribute
        self.color = color # attirbute
        self.weight = weight # attirbute


star_cookie1 = StarCookie("Red", 10) # first object
print(star_cookie1.color)
print(star_cookie1.weight)

print(star_cookie1.__dict__) # It will just print the all attribute
print(StarCookie.__dict__) # It will also print milk as a global variable


star_cookie2 = StarCookie("Blue", 20) # Second Object
star_cookie2.milk = 1 # It will just change the value of milk for object 2
print(star_cookie2.color)
print(star_cookie2.weight)

print(star_cookie2.__dict__) # Here the milk value will just change for the pbject 2
print(StarCookie.__dict__) # original value of milk will not change

