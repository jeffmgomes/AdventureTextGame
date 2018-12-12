class Room:
    def __init__(self,name):
        self.name = name
    
    up = ""
    down = ""
    right =""
    left = ""

class House:
    livingRoom = Room("Living Room")
    kitchen = Room("Kitchen")
    bathroom = Room("Bathroom")
    laundry = Room("Laundry")
    library = Room("Library")
    office = Room("Office")
    bedroom = Room("Bedroom")
    
    livingRoom.up = kitchen
    livingRoom.down = "Exit"
    livingRoom.right = library
    livingRoom.left = "Wall"
        
    kitchen.up = bathroom
    kitchen.down = livingRoom
    kitchen.right = "Wall"
    kitchen.left = "Wall"
    
    bathroom.up = laundry
    bathroom.down = kitchen
    bathroom.right = "Wall"
    bathroom.left = "Wall"
    
    laundry.up = "Wall"
    laundry.down = bathroom
    laundry.right = "Wall"
    laundry.left = "Wall"
    
    library.up = "Wall"
    library.down = office
    library.right = bedroom
    library.left = livingRoom
    
    office.up = library
    office.down = "Wall"
    office.right = "Wall"
    office.left = "Wall"
    
    bedroom.up = "Wall"
    bedroom.down = "Wall"
    bedroom.right = "Wall"
    bedroom.left = library
    
class Player:            
    house = House()
    roomIn = ""
    message = ""
    
    def walk(self,step):
        hit = step
        if hit == "Wall":
            self.message = "Oops you hit a wall. You cannot go on that direction."
        elif hit == "Exit":
            self.message = "Exit"
        else:
            self.roomIn = hit
            self.message = f"You enter {self.roomIn.name}"
    
    def move(self,direction):
        if self.roomIn == "":
            if direction == "u":
                self.roomIn = self.house.livingRoom
                self.message = "You enter a safe place!"
            else:
                self.message = "Exit"
        else:
            if direction == "u":
                self.walk(self.roomIn.up)
            elif direction == "d":
                self.walk(self.roomIn.down)
            elif direction == "r":
                self.walk(self.roomIn.right)
            elif direction == "l":
                self.walk(self.roomIn.left)
            else:
                self.message = "Wrong way. Try again."

def displayInstructions():
    print("Choose the letter r,l,u,d to move around the rooms")
    print("r = right, l = left, u = up, d = down")
    
def displayIntro():
    print("You are facing a door... move up to enter...")
    
def main():
    
    p = Player()    
    
    displayInstructions()
    displayIntro()
    
    direction = ""
    Exit = False
    while True:
        if Exit:
            break
        direction = input("Where do you want to move?")
        p.move(direction)
        if p.message == "Exit":
            print("Bye bye!")
            Exit = True
        else:
            print(p.message)
        
if __name__ == '__main__': main()
    
