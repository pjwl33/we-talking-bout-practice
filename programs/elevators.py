# Designing a scalable multi-elevator control system in Python involves creating a set of classes that manage elevators, handle requests, and determine the most efficient way to allocate elevators to service those requests. Let's start by outlining a simple design for a 4-elevator system that can be easily scaled to more elevators.

# Design Outline
# Elevator:
# This class represents a single elevator, keeping track of its current floor, destination floors, direction, and whether it's idle or in motion.
# ElevatorController:
# The controller manages multiple elevators, assigns requests to the best available elevator, and makes decisions about movement and direction.
# Request:
# This class represents a request from a passenger, which includes the pickup and drop-off floors.
# ElevatorSystem:
# This class is the main interface for the user to interact with the system, allowing for adding elevators, handling requests, and controlling the elevators.

from collections import deque
import random
import heapq


# How Priority Handling Works in This Implementation
# Request Class: Requests are created with a priority attribute. Lower priority numbers mean higher priority.
# Priority Queue for Requests: Each elevator’s requests queue is a heap-based priority queue. When a new floor is requested, it’s added to this queue according to its priority.
# Request Fulfillment: The elevator always services the highest-priority request in its queue first.
# ElevatorController’s Best Elevator Selection: The controller finds the best available elevator to handle each request, prioritizing idle or direction-matching elevators for optimal performance.

class Request:
    def __init__(self, pickup_floor, direction, priority=1):
        self.pickup_floor = pickup_floor
        self.direction = direction
        self.priority = priority  # 1 is high, 2 is medium, 3 is low
    
    def __lt__(self, other):
        return self.priority < other.priority  # Lower numbers indicate higher priority

# Elevator Class:

# Each elevator keeps track of its current floor, state, direction, and a queue of requests.
# request_floor: Adds a new floor request to the elevator's queue if it’s not already in the queue.
# move: Moves the elevator one floor at a time in the current direction. When it reaches a floor in its request queue, it stops and removes that request from the queue.
# update_direction: Determines the elevator’s next movement based on its requests.

class Elevator:
    def __init__(self, id, total_floors):
        self.id = id
        self.current_floor = 0
        self.total_floors = total_floors
        self.direction = 0  # 0: idle, 1: up, -1: down
        self.requests = deque()
        self.state = 'idle'

    # def request_floor(self, floor):
    #     if floor not in self.requests:
    #         self.requests.append(floor)
    #         self.update_direction()
    def request_floor(self, request):
        heapq.heappush(self.requests, request)
        self.update_direction()

    def update_direction(self):
        if not self.requests:
            self.direction = 0
            self.state = 'idle'
            return
        next_floor = self.requests[0]
        if next_floor > self.current_floor:
            self.direction = 1
            self.state = 'moving up'
        elif next_floor < self.current_floor:
            self.direction = -1
            self.state = 'moving down'
        else:
            self.requests.popleft()
            self.update_direction()

    def move(self):
        if self.direction == 1:
            self.current_floor += 1
        elif self.direction == -1:
            self.current_floor -= 1
        print(f"Elevator {self.id} is on floor {self.current_floor}")

        if self.requests and self.current_floor == self.requests[0]:
            print(f"Elevator {self.id} has reached floor {self.current_floor}")
            self.requests.popleft()
            self.update_direction()

# ElevatorController Class:

# The controller oversees the elevators and assigns the best elevator to each incoming request based on the distance and direction.
# request_elevator: Finds the most suitable elevator and assigns it to the requested floor.
# find_best_elevator: Finds the closest elevator moving in the desired direction or an idle elevator if no elevator is available in the requested direction.
# step: Moves all elevators by one step, updating their positions based on requests.

class ElevatorController:
    def __init__(self, num_elevators, total_floors):
        self.elevators = [Elevator(i, total_floors) for i in range(num_elevators)]
        self.total_floors = total_floors

    # def request_elevator(self, pickup_floor, direction):
        # best_elevator = self.find_best_elevator(pickup_floor, direction)
        # if best_elevator is not None:
        #     best_elevator.request_floor(pickup_floor)
        #     print(f"Elevator {best_elevator.id} assigned to floor {pickup_floor}")
        # else:
        #     print("No available elevators")
    def request_elevator(self, pickup_floor, direction, priority=1):
        request = Request(pickup_floor, direction, priority)
        best_elevator = self.find_best_elevator(request)
        if best_elevator is not None:
            best_elevator.request_floor(request)
            print(f"Elevator {best_elevator.id} assigned to floor {pickup_floor} with priority {priority}")
        else:
            print("No available elevators")

    def find_best_elevator(self, pickup_floor, direction):
        best_elevator = None
        min_distance = float('inf')
        
        for elevator in self.elevators:
            if elevator.direction == 0:  # Idle elevator
                distance = abs(elevator.current_floor - pickup_floor)
                if distance < min_distance:
                    min_distance = distance
                    best_elevator = elevator
            elif elevator.direction == direction:
                if direction == 1 and elevator.current_floor <= pickup_floor:
                    distance = abs(elevator.current_floor - pickup_floor)
                    if distance < min_distance:
                        min_distance = distance
                        best_elevator = elevator
                elif direction == -1 and elevator.current_floor >= pickup_floor:
                    distance = abs(elevator.current_floor - pickup_floor)
                    if distance < min_distance:
                        min_distance = distance
                        best_elevator = elevator

        return best_elevator

    def step(self):
        for elevator in self.elevators:
            elevator.move()

# ElevatorSystem Class:

# The main interface for interacting with the elevator system. Allows requesting an elevator and advancing the system state in the simulation.

class ElevatorSystem:
    def __init__(self, num_elevators=4, total_floors=20):
        self.controller = ElevatorController(num_elevators, total_floors)
        self.total_floors = total_floors

    def request_elevator(self, pickup_floor, direction, priority=1):
        self.controller.request_elevator(pickup_floor, direction, priority)

    def update(self):
        self.controller.step()

# Example usage
if __name__ == "__main__":
    elevator_system = ElevatorSystem(num_elevators=4, total_floors=20)

    # Simulate a few requests
    # elevator_system.request_elevator(5, 1)  # Request for pickup on floor 5 going up
    # elevator_system.request_elevator(2, -1)  # Request for pickup on floor 2 going down
    # elevator_system.request_elevator(10, 1)  # Request for pickup on floor 10 going up

    # Simulate a few requests
    elevator_system.request_elevator(5, 1, priority=1)  # High-priority request
    elevator_system.request_elevator(2, -1, priority=2)  # Medium-priority request
    elevator_system.request_elevator(10, 1, priority=3)  # Low-priority request


    # Simulate steps in the elevator system
    for _ in range(15):
        elevator_system.update()

# Code Explanation
# Scaling to More Elevators
# To scale this system for more elevators:
# Add More Elevators: Increase the num_elevators parameter when instantiating ElevatorSystem.
# Optimize find_best_elevator: For larger systems, improve the efficiency of this function by filtering out irrelevant elevators.
# More Sophisticated Scheduling: Consider implementing a more advanced scheduling algorithm, like one that handles priority or groups requests by proximity.
# Parallel Movement Simulation: For real-world applications or high numbers of elevators, run each elevator's movement logic concurrently.
# This design can be further expanded by adding features like priority handling, additional request types, or better scheduling for more realistic elevator behavior.

# Adding priority handling to the elevator system can improve its ability to efficiently serve requests based on different levels of importance. There are a few different ways to implement priority handling, depending on the requirements:

# Priority Levels for Requests: Each request can be assigned a priority level (e.g., high, medium, or low). High-priority requests can come from emergency buttons or service calls, while medium and low priorities represent regular calls.

# Priority Queue: Use a priority queue (using Python’s heapq or other data structures) to manage requests. Higher-priority requests will be served first, even if they’re not the closest requests in terms of floor distance.

# Elevator Priority Algorithm: Modify the find_best_elevator function to prioritize elevators that can quickly serve high-priority requests. This might involve favoring idle elevators or interrupting elevators with low-priority tasks.

# Implementation Steps for Priority Handling
# To introduce priority handling, let’s make the following modifications to our existing design:

# Update Request Class: Define a Request class with a priority attribute.
# Update Elevator Requests: Modify the elevator’s request handling to prioritize high-priority requests first.
# ElevatorController Changes: Adjust the controller’s find_best_elevator method to consider priority.




