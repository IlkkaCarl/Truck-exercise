import math

# Inner dimensions of the truck
TRUCK_WIDTH = 1780
TRUCK_HEIGHT = 2450
TRUCK_DEPTH = 4500

# Dimensions of the boxes
SMALL_BOX_WIDTH = 330
SMALL_BOX_LENGTH = 275
SMALL_BOX_HEIGHT = 406

AVERAGE_BOX_WIDTH = 330
AVERAGE_BOX_LENGTH = 550
AVERAGE_BOX_HEIGHT = 406

LARGE_BOX_WIDTH = 330
LARGE_BOX_LENGTH = 550
LARGE_BOX_HEIGHT = 812

def calculate_trips(boxes):
    total_volume = boxes["small"] * SMALL_BOX_WIDTH * SMALL_BOX_LENGTH * SMALL_BOX_HEIGHT \
                   + boxes["average"] * AVERAGE_BOX_WIDTH * AVERAGE_BOX_LENGTH * AVERAGE_BOX_HEIGHT \
                   + boxes["large"] * LARGE_BOX_WIDTH * LARGE_BOX_LENGTH * LARGE_BOX_HEIGHT

    truck_volume = TRUCK_WIDTH * TRUCK_HEIGHT * TRUCK_DEPTH

    trips = math.ceil(total_volume / truck_volume)
    return trips

def main():
    boxes = {}
    while True:
        try:
            boxes["small"] = int(input("Enter the number of small boxes: "))
            boxes["average"] = int(input("Enter the number of average boxes: "))
            boxes["large"] = int(input("Enter the number of large boxes: "))
            break
        except ValueError:
            print("Please enter a valid number.")

    trips = calculate_trips(boxes)

    print(f"The truck needs to make {trips} trip(s) to transport the boxes.")

if __name__ == "__main__":
    main()
