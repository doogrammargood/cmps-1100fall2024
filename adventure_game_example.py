#This comes from Chatgpt 3.5
def start_adventure():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a dark forest with two paths.")
    print("Do you go left or right?")

    choice1 = input("Type 'left' or 'right': ").lower()

    if choice1 == "left":
        print("\nYou walk down the left path and find a peaceful clearing with a small pond.")
        print("Do you sit by the pond or keep walking?")
        choice2 = input("Type 'sit' or 'walk': ").lower()

        if choice2 == "sit":
            print("\nYou sit by the pond and enjoy the serenity. Suddenly, a friendly fox appears and leads you to safety.")
            print("Congratulations, you have safely completed your adventure!")
        elif choice2 == "walk":
            print("\nYou keep walking and find a hidden treasure chest!")
            print("You open the chest and find gold and jewels. You win!")
        else:
            print("\nThat's not a valid choice. You get lost in the forest. Game over.")

    elif choice1 == "right":
        print("\nYou walk down the right path and find a spooky cave.")
        print("Do you enter the cave or run away?")
        choice2 = input("Type 'enter' or 'run': ").lower()

        if choice2 == "enter":
            print("\nYou bravely enter the cave and find a sleeping dragon!")
            print("Do you try to sneak past the dragon or leave quietly?")
            choice3 = input("Type 'sneak' or 'leave': ").lower()

            if choice3 == "sneak":
                print("\nYou successfully sneak past the dragon and find a mountain of treasure. You win!")
            elif choice3 == "leave":
                print("\nYou decide it's not worth the risk and leave the cave quietly. You find your way home safely.")
            else:
                print("\nThat's not a valid choice. The dragon wakes up and you have to run away. Game over.")

        elif choice2 == "run":
            print("\nYou run away from the cave and eventually find your way out of the forest. You're safe, but the adventure is over.")
        else:
            print("\nThat's not a valid choice. You get lost in the forest. Game over.")

    else:
        print("\nThat's not a valid choice. You get lost in the forest. Game over.")

# Start the adventure
start_adventure()

class story_element():
    def print_story_element(self):
        print(self.text)
        for c in choices:
            print(c)
    def choose_next_step(self):
        next_step = input()
        for c in choices:
            if input == c:
                return c

    def __init__(self, text, choices):
        self.text = text
        self.choices=choices