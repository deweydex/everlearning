---
title: "Hitchhiker's Guide to Object-Oriented Programming"
slug: oop-02-hitchhikers-guide
course: programming-and-design-principles
course_title: "Programming and Design Principles"
series: object-oriented-programming
series_title: "Object Oriented Programming"
version: 2026.09.06.1
---

# Hitchhiker's Guide to Object-Oriented Programming

This notebook demonstrates fundamental Object-Oriented Programming (OOP) concepts through a simple space map system inspired by "The Hitchhiker's Guide to the Galaxy." We'll build a mini-map for a text-based RPG where players can navigate a spaceship between different locations in the galaxy.

## What is Object-Oriented Programming?

Object-Oriented Programming is a programming paradigm based on the concept of "objects" that contain both data (attributes) and code (methods). OOP helps organize code in a way that models real-world entities and their relationships, making complex systems more manageable, modular, and reusable.

## Key OOP Concepts We'll Explore

1. **Classes and Objects**: Blueprint definitions and their instances
2. **Encapsulation**: Bundling data and methods that work on that data
3. **Inheritance**: Creating new classes based on existing ones
4. **Polymorphism**: Using a single interface for different underlying forms
5. **Composition**: Building complex objects by combining simpler ones

Let's dive in!

## 1. The Base Location Class

We'll start with a fundamental concept in our game: locations. The `Location` class serves as the foundation for all places our spaceship can visit. It demonstrates several core OOP principles:

```python exec
id: oop-02-hitchhikers-guide-1
class Location:
    """Base class for all locations in our space map."""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}  # Dictionary mapping direction to connected Location
    
    def connect(self, direction, location):
        """Connect this location to another in the specified direction."""
        self.connections[direction] = location
        
    def get_info(self):
        """Return information about this location."""
        info = f"=== {self.name} ===\n{self.description}\n"
        
        if self.connections:
            info += "\nPossible directions:\n"
            for direction, location in self.connections.items():
                info += f"- {direction}: to {location.name}\n"
        else:
            info += "\nThere are no connections from this location yet.\n"
            
        return info
```

### OOP Concepts in the Location Class

#### 1. Class Definition
- The `class Location:` line defines a new class - a blueprint for creating Location objects.

#### 2. Constructor Method
- `__init__(self, name, description)` is the constructor method that gets called when a new Location is created.
- The `self` parameter refers to the instance being created and is used to set attributes on that instance.
- This demonstrates **encapsulation** - bundling the data (name, description, connections) with the methods that operate on that data.

#### 3. Instance Attributes
- `self.name`, `self.description`, and `self.connections` are instance attributes that store data unique to each Location object.
- Each Location instance has its own separate copy of these attributes.

#### 4. Instance Methods
- `connect()` and `get_info()` are instance methods that operate on a specific Location instance.
- They access the instance's data through the `self` parameter.

Let's create a simple Location and see how it works:

```python exec
id: oop-02-hitchhikers-guide-2
# Creating a Location object
space_port = Location("Milliways Spaceport", "A bustling hub of interstellar travel.")

# Testing the get_info method
print(space_port.get_info())
```

## 2. Inheritance with Planet and SpaceStation Classes

Now we'll create specialized location types using **inheritance**. This allows us to create new classes that reuse, extend, and modify the behavior defined in an existing class.

```python exec
id: oop-02-hitchhikers-guide-3
class Planet(Location):
    """A planet that the spaceship can visit."""
    
    def __init__(self, name, description, danger_level=0, has_restaurant=False):
        # Call the parent class constructor (this is inheritance in action!)
        super().__init__(name, description)
        
        # Add Planet-specific attributes
        self.danger_level = danger_level  # Scale from 0 to 10
        self.has_restaurant = has_restaurant
    
    def get_info(self):
        """Return information about this planet, including special features."""
        # Get the basic info from the parent class (reusing code)
        info = super().get_info()
        
        # Add planet-specific information
        if self.danger_level > 7:
            info += f"\nWARNING: This planet is EXTREMELY dangerous (Level {self.danger_level})!\n"
        elif self.danger_level > 3:
            info += f"\nCAUTION: This planet is moderately dangerous (Level {self.danger_level}).\n"
            
        if self.has_restaurant:
            info += "\nThis planet has a restaurant. You could grab a meal here.\n"
            
        return info
```

### OOP Concepts in the Planet Class

#### 1. Inheritance
- `class Planet(Location):` indicates that Planet is a subclass of Location.
- Planet inherits all attributes and methods from Location, but can also add or override them.

#### 2. Method Overriding
- The `get_info()` method is overridden to provide Planet-specific behavior.
- This is an example of **polymorphism** - the same method name can behave differently depending on the object's class.

#### 3. Using the Parent Class's Methods
- `super().__init__(name, description)` calls the parent class's constructor.
- `super().get_info()` calls the parent class's version of the `get_info()` method.
- This allows for code reuse while extending functionality.

#### 4. Extended Attributes
- Planet adds new attributes (`danger_level` and `has_restaurant`) that aren't in the parent Location class.

Now let's implement the SpaceStation class:

```python exec
id: oop-02-hitchhikers-guide-4
class SpaceStation(Location):
    """A space station that provides services for the spaceship."""
    
    def __init__(self, name, description, services=None):
        # Call the parent class constructor
        super().__init__(name, description)
        
        # Add SpaceStation-specific attributes
        # The default argument None with the or [] syntax demonstrates a best practice
        # to avoid mutable default arguments
        self.services = services or []
    
    def get_info(self):
        """Return information about this space station, including available services."""
        info = super().get_info()
        
        if self.services:
            info += "\nAvailable services:\n"
            for service in self.services:
                info += f"- {service}\n"
                
        return info
```

### Let's Test Our Subclasses

We'll create instances of both Planet and SpaceStation to see how inheritance and polymorphism work in practice:

```python exec
id: oop-02-hitchhikers-guide-5
# Create a Planet instance
earth = Planet(
    "Earth", 
    "A mostly harmless planet with oceans, mountains, and lots of confused ape descendants.",
    danger_level=2,
    has_restaurant=True
)

# Create a SpaceStation instance
heart_of_gold_dock = SpaceStation(
    "Heart of Gold Docking Bay", 
    "A high-tech facility featuring the revolutionary Infinite Improbability Drive technology.",
    services=["Refueling", "Ship Repairs", "Improbability Calibration"]
)

# Connect them (bidirectionally)
earth.connect("launch", heart_of_gold_dock)
heart_of_gold_dock.connect("land", earth)

# Display information about both locations
print(earth.get_info())
print("\n" + "-"*50 + "\n")
print(heart_of_gold_dock.get_info())
```

## 3. Building a Map System with Composition

Now we'll implement a SpaceMap class to manage all our locations. This demonstrates the principle of **composition** - building complex objects by combining simpler ones.

```python exec
id: oop-02-hitchhikers-guide-6
class SpaceMap:
    """Represents the game map containing all locations."""
    
    def __init__(self):
        self.locations = {}  # Dictionary mapping location names to Location objects
        self.current_location = None
    
    def add_location(self, location):
        """Add a location to the map."""
        self.locations[location.name] = location
        
        # Set as starting location if it's the first one added
        if self.current_location is None:
            self.current_location = location
    
    def move(self, direction):
        """Move from the current location in the specified direction."""
        if direction in self.current_location.connections:
            self.current_location = self.current_location.connections[direction]
            return self.get_current_info()
        else:
            return f"Cannot move {direction} from here. Try another direction."
    
    def get_current_info(self):
        """Get information about the current location."""
        return self.current_location.get_info()
```

### OOP Concepts in the SpaceMap Class

#### 1. Composition
- SpaceMap is composed of Location objects (and their subclasses).
- This is a "has-a" relationship rather than an "is-a" relationship (which would be inheritance).
- Composition allows us to create complex behaviors by combining simpler objects.

#### 2. Delegation
- The `get_current_info()` method delegates to the current location's `get_info()` method.
- This demonstrates how composition can leverage the capabilities of its component parts.

#### 3. Abstraction
- The SpaceMap provides a simplified interface for interacting with the locations.
- Users of SpaceMap don't need to understand the details of how locations are connected.

Let's create a small map to test our SpaceMap class:

```python exec
id: oop-02-hitchhikers-guide-7
# Create a simple map with the locations we defined earlier
mini_map = SpaceMap()
mini_map.add_location(earth)
mini_map.add_location(heart_of_gold_dock)

# Test movement
print("Starting location:")
print(mini_map.get_current_info())

print("\nTrying to move somewhere that doesn't exist:")
print(mini_map.move("warp"))

print("\nMoving to a valid connection:")
print(mini_map.move("launch"))

print("\nMoving back:")
print(mini_map.move("land"))
```

## 4. Creating a Spaceship Class

Finally, we'll create a Spaceship class that will represent the player's vessel. This class demonstrates multiple types of OOP relationships and adds gameplay mechanics like fuel management.

```python exec
id: oop-02-hitchhikers-guide-8
class Spaceship:
    """The player's spaceship that travels around the space map."""
    
    def __init__(self, name, space_map):
        self.name = name
        self.space_map = space_map  # Composition: a Spaceship has-a SpaceMap
        self.inventory = []
        self.fuel = 100
    
    def move(self, direction):
        """Move the spaceship in the specified direction."""
        if self.fuel < 10:
            return "Not enough fuel to travel! Find a space station to refuel."
        
        result = self.space_map.move(direction)  # Delegation to the SpaceMap's move method
        
        # Consume fuel if movement was successful
        if "Cannot move" not in result:
            self.fuel -= 10
            result += f"\nRemaining fuel: {self.fuel}%"
            
        return result
    
    def refuel(self):
        """Refuel the spaceship at a space station."""
        current_location = self.space_map.current_location
        
        # Using isinstance() to check the object's class - polymorphism in action
        if isinstance(current_location, SpaceStation) and "Refueling" in current_location.services:
            self.fuel = 100
            return f"The {self.name} has been refueled to 100%."
        else:
            return "Refueling is not available at this location."
    
    def get_location_info(self):
        """Get information about the current location."""
        return self.space_map.get_current_info()  # Delegation
```

### OOP Concepts in the Spaceship Class

#### 1. Composition
- The Spaceship has a SpaceMap (`self.space_map`).
- This creates a clear separation of responsibilities: the SpaceMap handles location management, while the Spaceship adds gameplay mechanics like fuel.

#### 2. Delegation
- Many of Spaceship's methods delegate to the SpaceMap's methods, then add additional functionality.
- This demonstrates how composition can be used to build complex behaviors by layering functionality.

#### 3. Runtime Type Checking
- The `refuel()` method uses `isinstance()` to check if the current location is a SpaceStation.
- This demonstrates how polymorphism allows us to work with objects of different types through a common interface, but still handle special cases when needed.

Let's create a Spaceship and test its functionality:

```python exec
id: oop-02-hitchhikers-guide-9
# Create a spaceship using our mini_map
heart_of_gold = Spaceship("Heart of Gold", mini_map)

# Check our starting position
print(heart_of_gold.get_location_info())

# Try to refuel at the current location (Earth, which doesn't offer refueling)
print("\nAttempting to refuel:")
print(heart_of_gold.refuel())

# Move to the space station
print("\nLaunching to space station:")
print(heart_of_gold.move("launch"))

# Try to refuel at the space station
print("\nAttempting to refuel:")
print(heart_of_gold.refuel())

# Check our fuel level
print(f"\nCurrent fuel level: {heart_of_gold.fuel}%")
```

## 5. Putting It All Together: A Complete Game Map

Now let's create a more complete game map based on locations from "The Hitchhiker's Guide to the Galaxy" and implement a simple game loop to demonstrate the full system.

```python exec
id: oop-02-hitchhikers-guide-10
def create_hitchhiker_map():
    """Create a map based on locations from Hitchhiker's Guide to the Galaxy."""
    
    # Create locations
    earth = Planet(
        "Earth", 
        "A mostly harmless planet with oceans, mountains, and lots of confused ape descendants.",
        danger_level=2,
        has_restaurant=True
    )
    
    magrathea = Planet(
        "Magrathea", 
        "An ancient planet known for its luxury custom planet-building industry.",
        danger_level=5,
        has_restaurant=False
    )
    
    restaurant = Planet(
        "Restaurant at the End of the Universe", 
        "A time-warped fine dining establishment where you can watch the end of everything while enjoying a nice meal.",
        danger_level=1,
        has_restaurant=True
    )
    
    vogon_station = SpaceStation(
        "Vogon Processing Station", 
        "A bureaucratic nightmare filled with terrible poetry and even worse customer service.",
        services=["Passport Processing", "Poetry Readings"]
    )
    
    heart_of_gold_dock = SpaceStation(
        "Heart of Gold Docking Bay", 
        "A high-tech facility featuring the revolutionary Infinite Improbability Drive technology.",
        services=["Refueling", "Ship Repairs", "Improbability Calibration"]
    )
    
    # Connect locations
    earth.connect("up", vogon_station)
    earth.connect("warp", restaurant)
    
    vogon_station.connect("down", earth)
    vogon_station.connect("hyperspace", magrathea)
    
    magrathea.connect("dock", heart_of_gold_dock)
    magrathea.connect("return", vogon_station)
    
    heart_of_gold_dock.connect("exit", magrathea)
    heart_of_gold_dock.connect("probability_jump", restaurant)
    
    restaurant.connect("time_warp", earth)
    restaurant.connect("back_door", heart_of_gold_dock)
    
    # Create the map
    space_map = SpaceMap()
    
    # Add all locations to the map
    for location in [earth, magrathea, restaurant, vogon_station, heart_of_gold_dock]:
        space_map.add_location(location)
    
    return space_map
```

```python exec
id: oop-02-hitchhikers-guide-11
def play_game():
    """Run a simple game loop to demonstrate the system."""
    space_map = create_hitchhiker_map()
    ship = Spaceship("Heart of Gold", space_map)
    
    print("Welcome to the Hitchhiker's Guide to the Galaxy Space Explorer!")
    print("You are traveling in the spaceship 'Heart of Gold'.")
    print("Type 'help' for available commands.\n")
    
    print(ship.get_location_info())
    
    # In a notebook environment, we'll limit the game to a few turns instead of running an infinite loop
    commands = [
        "help",
        "move up",
        "refuel",
        "move hyperspace",
        "move dock",
        "refuel",
        "move probability_jump",
        "look"
    ]
    
    for i, command in enumerate(commands):
        print(f"\n[Turn {i+1}] Command: {command}")
        
        if command == "help":
            print("\nAvailable commands:")
            print("- move [direction]: Move in the specified direction")
            print("- look: Get information about your current location")
            print("- refuel: Refuel your spaceship (only at stations with refueling)")
            print("- fuel: Check your current fuel level")
            print("- quit/exit: End the game")
        elif command == "look":
            print(ship.get_location_info())
        elif command == "fuel":
            print(f"Current fuel level: {ship.fuel}%")
        elif command == "refuel":
            print(ship.refuel())
        elif command.startswith("move "):
            direction = command[5:]
            print(ship.move(direction))
        else:
            print("Unknown command. Type 'help' for available commands.")
    
    print("\nThanks for exploring the galaxy! Don't forget your towel.")
```

```python exec
id: oop-02-hitchhikers-guide-12
# Run the game
play_game()
```

## Summary of OOP Concepts Demonstrated

### 1. Classes and Objects
- We defined several classes (`Location`, `Planet`, `SpaceStation`, `SpaceMap`, `Spaceship`)
- We created instances of these classes (objects) that encapsulate state and behavior

### 2. Encapsulation
- Each class bundles data (attributes) with the methods that operate on that data
- Implementation details are hidden inside the classes, providing a clean interface for users

### 3. Inheritance
- `Planet` and `SpaceStation` inherit from `Location`
- They reuse code from their parent class while adding specialized features

### 4. Polymorphism
- The `get_info()` method behaves differently depending on the object's class
- We can call the same method on different types of objects, and it does the right thing
- Runtime type checking with `isinstance()` allows specialized behavior

### 5. Composition
- `SpaceMap` is composed of `Location` objects
- `Spaceship` has a `SpaceMap`
- This creates a hierarchy of objects that work together

## Exercises for Further Learning

Try extending this system with some of these ideas:

1. Add a new location type (e.g., `Asteroid`, `BlackHole`, `SpacePort`)
2. Implement an inventory system for collecting and using items
3. Add NPCs (Non-Player Characters) with dialogue
4. Create a mission or quest system
5. Add different spaceship types with varying fuel capacities
6. Implement a combat system for dangerous encounters
7. Add a save/load game functionality

Each of these extensions would demonstrate additional OOP principles and practices.

## Looking back

Before leaving this page, a sentence on each. What you write stays on this device.

```reflect
- Something you expected before running a cell that turned out differently
- The one idea from this page you could explain to someone else now
- Something you would change or try next, if there were time
- A question this page raised for you that it did not answer. Bring it to the next session; these questions are where the next session starts.
```
