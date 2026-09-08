---
title: "Object-Oriented Programming in Python"
slug: oop-03-shapes-and-a-game-map
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: object-oriented-programming
series_title: "Object Oriented Programming"
version: 2026.09.06.1
---

# Object-Oriented Programming in Python

This notebook contains several examples of Object-Oriented Programming (OOP) in Python, from simple to more complex.

Let's start learning about OOP through these practical examples!

## 1. Simple Shapes Example

This is a beginner-friendly example of inheritance and polymorphism using geometric shapes. We'll create a base `Shape` class and then derive specific shapes from it.

```python exec
id: oop-03-shapes-and-a-game-map-1
import math

class Shape:
    """Base class for all shapes"""
    
    def __init__(self, color="white"):
        self.color = color
    
    def area(self):
        """Calculate the area of the shape"""
        pass
    
    def perimeter(self):
        """Calculate the perimeter of the shape"""
        pass
    
    def describe(self):
        """Return a description of the shape"""
        return f"A {self.color} shape"


class Circle(Shape):
    """Circle shape class"""
    
    def __init__(self, radius, color="white"):
        super().__init__(color)  # Call the parent class constructor
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def describe(self):
        return f"A {self.color} circle with radius {self.radius}"


class Rectangle(Shape):
    """Rectangle shape class"""
    
    def __init__(self, width, height, color="white"):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def describe(self):
        return f"A {self.color} rectangle with width {self.width} and height {self.height}"


class Triangle(Shape):
    """Triangle shape class"""
    
    def __init__(self, a, b, c, color="white"):
        super().__init__(color)
        self.a = a  # First side length
        self.b = b  # Second side length
        self.c = c  # Third side length
    
    def area(self):
        # Heron's formula for triangle area
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self):
        return self.a + self.b + self.c
    
    def describe(self):
        return f"A {self.color} triangle with sides {self.a}, {self.b}, and {self.c}"

# Create different shapes
circle = Circle(5, "red")
rectangle = Rectangle(4, 6, "blue")
triangle = Triangle(3, 4, 5, "green")

# Put them in a list to demonstrate polymorphism
shapes = [circle, rectangle, triangle]

# Print information about each shape
for shape in shapes:
    print(shape.describe())
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print()
```

```python exec
id: oop-03-shapes-and-a-game-map-2
class Person:
    """Base class for all people at the college"""
    
    def __init__(self, name, age, id_number):
        self.name = name
        self.age = age
        self.id_number = id_number
    
    def get_info(self):
        """Return basic information about the person"""
        return f"Name: {self.name}, Age: {self.age}, ID: {self.id_number}"
    
    def is_affiliated(self):
        """Check if the person is affiliated with the college"""
        return True


class Student(Person):
    """Student class for college students"""
    
    def __init__(self, name, age, id_number, major, year, gpa=0.0):
        super().__init__(name, age, id_number)
        self.major = major
        self.year = year
        self.gpa = gpa
        self.courses = []
    
    def enroll(self, course):
        """Enroll the student in a course"""
        self.courses.append(course)
        return f"{self.name} has enrolled in {course}"
    
    def calculate_tuition(self, cost_per_credit=500):
        """Calculate the student's tuition based on enrolled courses"""
        total_credits = len(self.courses) * 3  # Assuming each course is 3 credits
        return total_credits * cost_per_credit
    
    def get_info(self):
        """Return detailed information about the student"""
        basic_info = super().get_info()
        return f"{basic_info}, Major: {self.major}, Year: {self.year}, GPA: {self.gpa}"


class Professor(Person):
    """Professor class for college faculty"""
    
    def __init__(self, name, age, id_number, department, rank, salary):
        super().__init__(name, age, id_number)
        self.department = department
        self.rank = rank
        self.salary = salary
        self.courses_taught = []
    
    def assign_course(self, course):
        """Assign a course to the professor"""
        self.courses_taught.append(course)
        return f"Prof. {self.name} has been assigned to teach {course}"
    
    def calculate_pay(self, months=9):
        """Calculate the professor's pay for the academic year"""
        return self.salary * months / 12
    
    def get_info(self):
        """Return detailed information about the professor"""
        basic_info = super().get_info()
        return f"{basic_info}, Department: {self.department}, Rank: {self.rank}"


class Course:
    """Course class for college courses"""
    
    def __init__(self, name, code, credits, department, capacity=30):
        self.name = name
        self.code = code
        self.credits = credits
        self.department = department
        self.capacity = capacity
        self.students = []
        self.professor = None
    
    def add_student(self, student):
        """Add a student to the course"""
        if len(self.students) < self.capacity:
            self.students.append(student)
            return f"{student.name} added to {self.name}"
        else:
            return f"Cannot add {student.name}. Course {self.name} is full."
    
    def assign_professor(self, professor):
        """Assign a professor to teach the course"""
        self.professor = professor
        professor.assign_course(self.name)
        return f"Prof. {professor.name} assigned to teach {self.name}"
    
    def get_roster(self):
        """Get the roster of students in the course"""
        roster = f"Course: {self.name} ({self.code})\n"
        if self.professor:
            roster += f"Instructor: {self.professor.name}\n"
        roster += "Students:\n"
        for i, student in enumerate(self.students, 1):
            roster += f"{i}. {student.name}\n"
        return roster

# Create students
alice = Student("Alice Smith", 20, "S12345", "Computer Science", "Sophomore", 3.8)
bob = Student("Bob Johnson", 19, "S23456", "Mathematics", "Freshman", 3.5)

# Create professor
dr_jones = Professor("Emily Jones", 45, "P98765", "Computer Science", "Associate", 85000)

# Create courses
python_course = Course("Intro to Python", "CS101", 3, "Computer Science")
data_structures = Course("Data Structures", "CS201", 4, "Computer Science")

# Assign professor to courses
python_course.assign_professor(dr_jones)
data_structures.assign_professor(dr_jones)

# Enroll students in courses
alice.enroll("Intro to Python")
alice.enroll("Data Structures")
bob.enroll("Data Structures")
```

Now let's test our college model with some examples:

## 3. Game Map Example

This example builds a simple game world with locations, items, and characters.

```python exec
id: oop-03-shapes-and-a-game-map-3
class Location:
    """A location on the game map"""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connected_locations = {}  # Direction: Location
        self.items = []
        self.characters = []
    
    def connect(self, direction, location):
        """Connect this location to another in the specified direction"""
        self.connected_locations[direction] = location
        # Create the reverse connection automatically
        reverse_directions = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east",
            "up": "down",
            "down": "up"
        }
        if direction in reverse_directions:
            location.connected_locations[reverse_directions[direction]] = self
    
    def get_exits(self):
        """Get all available exit directions from this location"""
        return list(self.connected_locations.keys())
    
    def move(self, direction):
        """Get the location connected in the specified direction"""
        if direction in self.connected_locations:
            return self.connected_locations[direction]
        return None
    
    def add_item(self, item):
        """Add an item to this location"""
        self.items.append(item)
    
    def remove_item(self, item):
        """Remove an item from this location"""
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def add_character(self, character):
        """Add a character to this location"""
        self.characters.append(character)
        character.location = self
    
    def remove_character(self, character):
        """Remove a character from this location"""
        if character in self.characters:
            self.characters.remove(character)
            return True
        return False
    
    def get_details(self):
        """Get a detailed description of the location"""
        details = f"\n{self.name}\n"
        details += f"{'-' * len(self.name)}\n"
        details += f"{self.description}\n\n"
        
        # List available exits
        exits = self.get_exits()
        if exits:
            details += "Exits: " + ", ".join(exits) + "\n"
        else:
            details += "There are no obvious exits.\n"
        
        # List items in the location
        if self.items:
            details += "\nYou can see:\n"
            for item in self.items:
                details += f"- {item.name}: {item.description}\n"
        
        # List characters in the location
        if self.characters:
            details += "\nCharacters present:\n"
            for character in self.characters:
                details += f"- {character.name}\n"
                
        return details


class Item:
    """An item that can be found in the game"""
    
    def __init__(self, name, description, weight=1):
        self.name = name
        self.description = description
        self.weight = weight  # Weight affects how many items a player can carry
    
    def __str__(self):
        return self.name
    
    def get_details(self):
        """Get details about the item"""
        return f"{self.name}: {self.description} (Weight: {self.weight})"


class Character:
    """A character in the game (player or NPC)"""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.location = None
        self.inventory = []
        self.health = 100
    
    def move(self, direction):
        """Move the character in the specified direction"""
        if self.location:
            new_location = self.location.move(direction)
            if new_location:
                # Remove from current location
                self.location.remove_character(self)
                # Add to new location
                new_location.add_character(self)
                return new_location
        return None
    
    def take_item(self, item_name):
        """Take an item from the current location"""
        if self.location:
            for item in self.location.items:
                if item.name.lower() == item_name.lower():
                    self.inventory.append(item)
                    self.location.remove_item(item)
                    return f"You picked up the {item.name}."
            return f"There is no {item_name} here."
        return "You are nowhere."
    
    def drop_item(self, item_name):
        """Drop an item from inventory to the current location"""
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                self.inventory.remove(item)
                self.location.add_item(item)
                return f"You dropped the {item.name}."
        return f"You don't have a {item_name}."
    
    def inventory_weight(self):
        """Calculate the total weight of items in inventory"""
        return sum(item.weight for item in self.inventory)
    
    def get_inventory(self):
        """Get a list of items in the inventory"""
        if not self.inventory:
            return "Your inventory is empty."
        
        result = "Inventory:\n"
        for item in self.inventory:
            result += f"- {item.name}\n"
        result += f"\nTotal weight: {self.inventory_weight()}"
        return result


class Player(Character):
    """The player character with additional functionality"""
    
    def __init__(self, name):
        super().__init__(name, "The main player character")
        self.max_weight = 20  # Maximum weight the player can carry
        self.score = 0
    
    def take_item(self, item_name):
        """Override to check weight limits"""
        if self.location:
            for item in self.location.items:
                if item.name.lower() == item_name.lower():
                    if self.inventory_weight() + item.weight > self.max_weight:
                        return f"The {item.name} is too heavy to carry with your current inventory."
                    self.inventory.append(item)
                    self.location.remove_item(item)
                    return f"You picked up the {item.name}."
            return f"There is no {item_name} here."
        return "You are nowhere."
    
    def add_score(self, points):
        """Add points to the player's score"""
        self.score += points
        return f"You gained {points} points! Current score: {self.score}"


class GameMap:
    """A collection of locations that form the game world"""
    
    def __init__(self, name):
        self.name = name
        self.starting_location = None
        self.locations = []
    
    def add_location(self, location, is_starting=False):
        """Add a location to the map"""
        self.locations.append(location)
        if is_starting:
            self.starting_location = location
    
    def get_location_by_name(self, name):
        """Find a location by name"""
        for location in self.locations:
            if location.name.lower() == name.lower():
                return location
        return None
    
    def get_map_info(self):
        """Get information about the map"""
        info = f"Map: {self.name}\n"
        info += f"Number of locations: {len(self.locations)}\n"
        if self.starting_location:
            info += f"Starting location: {self.starting_location.name}\n"
        return info
```

Let's create a simple game map and try it out:

```python exec
id: oop-03-shapes-and-a-game-map-4
def create_sample_map():
    """Create a simple demo map"""
    # Create a new game map
    game_world = GameMap("Fantasy Kingdom")
    
    # Create locations
    town_square = Location("Town Square", "The central square of a small medieval town.")
    blacksmith = Location("Blacksmith", "A hot forge where the town blacksmith works.")
    tavern = Location("Tavern", "A cozy tavern filled with the smell of food and ale.")
    town_gate = Location("Town Gate", "The main gate leading out of town.")
    forest_path = Location("Forest Path", "A winding path through a dense forest.")
    
    # Connect locations
    town_square.connect("north", blacksmith)
    town_square.connect("east", tavern)
    town_square.connect("south", town_gate)
    town_gate.connect("south", forest_path)
    
    # Add locations to map
    game_world.add_location(town_square, is_starting=True)
    game_world.add_location(blacksmith)
    game_world.add_location(tavern)
    game_world.add_location(town_gate)
    game_world.add_location(forest_path)
    
    # Create items
    sword = Item("Sword", "A sharp steel sword", weight=5)
    shield = Item("Shield", "A sturdy wooden shield", weight=6)
    potion = Item("Potion", "A small healing potion", weight=1)
    key = Item("Key", "A small brass key", weight=0.5)
    
    # Place items in locations
    blacksmith.add_item(sword)
    blacksmith.add_item(shield)
    tavern.add_item(potion)
    forest_path.add_item(key)
    
    # Create NPCs
    blacksmith_npc = Character("Smith", "The town blacksmith")
    innkeeper = Character("Innkeeper", "The friendly tavern owner")
    
    # Place NPCs
    blacksmith.add_character(blacksmith_npc)
    tavern.add_character(innkeeper)
    
    return game_world
    # Demo the game functionality
def game_demo():
    # Create our game world
    game_world = create_sample_map()
    
    # Print map info
    print(game_world.get_map_info())
    
    # Create player and place at starting location
    player = Player("Adventurer")
    starting_location = game_world.starting_location
    starting_location.add_character(player)
    
    # Show current location
    print(starting_location.get_details())
    
    # Try some commands
    print("\n--- Moving around ---")
    print("Moving north...")
    new_location = player.move("north")
    if new_location:
        print(new_location.get_details())
    
    print("\n--- Interacting with items ---")
    print(player.take_item("sword"))
    print(player.take_item("shield"))
    print(player.get_inventory())
    
    print("\n--- Moving again ---")
    print("Moving south...")
    new_location = player.move("south")
    if new_location:
        print(new_location.get_details())
    
    print("\n--- Dropping items ---")
    print(player.drop_item("sword"))
    print(player.get_inventory())
    print(new_location.get_details())

# Run the demo
game_demo()
```

```python exec
id: oop-03-shapes-and-a-game-map-5
hint: Look back at the cell above this one: the pattern you need is there, with one thing changed.
# Your code here
```

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
