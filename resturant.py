class Resturant():
    def __init__(self,resturant_type,cuisine_type):
        self.resturant_type = resturant_type
        self.cuisine_type = cuisine_type
    def describe_resturant(self):
        print("This is  " + self.resturant_type + " resturant")
        print("we serve " + self.cuisine_type + " food")

    def open_resturant(self):
        print("Resturant is now open to serve customers")

my_rest = Resturant("International","Desi" )
print(my_rest.resturant_type)
print(my_rest.cuisine_type)
my_rest.describe_resturant()
my_rest.open_resturant()

## creatibg
