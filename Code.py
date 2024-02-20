# Inner dimensions of the truck's cargo space
TRUCK_WIDTH = 1780
TRUCK_HEIGHT = 2450
TRUCK_DEPTH = 4500

# Dimensions of the boxes
small_box_width = 330
small_box_height = 406
small_box_length = 275

average_box_width = 330
average_box_height = 406
average_box_length = 550

large_box_width = 330
large_box_height = 812
large_box_length = 550

# Ask the user for the number of each size of box
num_small_boxes = int(input("Enter the number of small boxes: "))
num_average_boxes = int(input("Enter the number of average boxes: "))
num_large_boxes = int(input("Enter the number of large boxes: "))

# Calculate the volume of each type of box
small_box_volume = small_box_width * small_box_height * small_box_length
average_box_volume = average_box_width * average_box_height * average_box_length
large_box_volume = large_box_width * large_box_height * large_box_length

# Calculate the total volume of all boxes
total_volume = (small_box_volume * num_small_boxes) + (average_box_volume * num_average_boxes) + (large_box_volume * num_large_boxes)

# Calculate the volume of the truck's cargo space
truck_volume = TRUCK_WIDTH * TRUCK_HEIGHT * TRUCK_DEPTH

# Calculate the number of trips needed
num_trips = total_volume / truck_volume
if num_trips > int(num_trips):
    num_trips = int(num_trips) + 1
else:
    num_trips = int(num_trips)

# Output the result
print(f"The truck needs to make {int} trips to transport all the boxes.")
