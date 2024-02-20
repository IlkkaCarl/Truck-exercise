# This is the code

# Carl's solution

# First define truck
truck_original = [1780, 4500, 2450]
truck = [1780, 4500, 2450]

# Define boxes
box_small = [330, 275, 406]
box_average = [330, 550, 406]
box_large = [330, 550, 812]

# Ask for amount of boxes
amount_small = int(input("How many small boxes do you have?: "))
amount_average = int(input("How many average boxes do you have?: "))
amount_large = int(input("How many large boxes do you have?: "))
total_boxes_left = amount_small + amount_average + amount_large
trips = 0

while total_boxes_left > 0:
    while amount_large > 0 and (box_large[0] <= truck[0]) and (box_large[1] <= truck[1]) and (box_large[2] <= truck[2]):
        amount_large -= 1
        total_boxes_left -= 1
        truck[0] -= box_large[0]
        truck[1] -= box_large[1]
        truck[2] -= box_large[2]
    while amount_average > 0 and (box_average[0] <= truck[0]) and (box_average[1] <= truck[1]) and (box_average[2] <= truck[2]):
        amount_average -= 1
        total_boxes_left -= 1
        truck[0] -= box_average[0]
        truck[1] -= box_average[1]
        truck[2] -= box_average[2]
    while amount_small > 0 and (box_small[0] <= truck[0]) and (box_small[1] <= truck[1]) and (box_small[2] <= truck[2]):
        amount_small -= 1
        total_boxes_left -= 1
        truck[0] -= box_small[0]
        truck[1] -= box_small[1]
        truck[2] -= box_small[2]
    if total_boxes_left > 0:
        trips += 1
        truck = truck_original.copy()
        continue
#This is a test line for debugging purposes
#print("You have {} large, {} average and {} small boxes left".format(amount_large, amount_average, amount_small))

print("It took {} trips.".format(trips))
