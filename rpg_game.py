rooms = {
         1:{'name':'Hall',
            'east':2,
            'south':3},
         2:{'name':'Bedroom',
            'west':1,
            'south':4},
         3:{'name':'Kitchen',
            'north':1},
         4:{'name':'Bathroom',
            'north':2}

         }
         

current_room = 1
while True:
    print("You are in room: " + str(current_room))
    print ("This is the Room's name: "+ rooms[current_room]['name'])

    move = input(">")
    current_room = rooms [current_room][move]
