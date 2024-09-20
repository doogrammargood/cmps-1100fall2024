class Bird(object):
    def __init__(self,name):
        self.name = name

    def get_feather(self):
        #should return the type of feather of the bird.
        return self.feather_type

    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
    def __init__(self,name):
        super().__init__(name)
        self.feather_type = "sparrow feather"

    def flight(self):
        print("Sparrows can fly.")

class ostrich(Bird):
    def __init__(self,name):
        super().__init__(name)
        self.feater_type="ostrich feather"



    def flight(self):
        print("Ostriches cannot fly.")

obj_bird = Bird("birdname")
obj_spr = sparrow("sparrowname")
obj_ost = ostrich("ostrichname")

# obj_bird.intro()
# obj_bird.flight()

# obj_spr.intro()
# obj_ost.intro()

print(obj_spr.get_feather())
# obj_spr.flight()

# obj_ost.intro()
# obj_ost.flight()


particular_Sparrow = sparrow("sparrowname")

print(particular_Sparrow)