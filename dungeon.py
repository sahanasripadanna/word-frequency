dungeon = [['Rm 101', 'Rm 102', 'Rm 103', 'Rm 104', 'Elevator'],
           ['Rm 201', 'Rm 202 (my room)', 'Rm 203', 'Rm 204', 'Elevator'],
           ['Rm 301', 'secret stairs', 'Rm 303', 'Rm 304', 'Elevator'],
           ['Rm 401', 'secret stairs', 'maintenance closet', 'Rm 404', 'dead end']]

floor_number = 1
room_number = 1
print("Started at " + dungeon[floor_number][room_number])

#tell me what room i should move to
def move_left_from(room_number):
    return room_number - 1

def move_right_from(room_number):
    #len(dungeon[floor_number]) tells me how many floors there are
    try_to_move = room_number + 1
    if try_to_move == len(dungeon[floor_number]):
        print ("you can't do that homeslice")
        return room_number
    else:
        return try_to_move

for times in range(5):
    room_number = move_right_from(room_number)

print("Moved to " + dungeon[floor_number][room_number])
