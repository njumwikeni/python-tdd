rooms = {'empty':{'name':'an empty room','east':'bedroom','north':'temple',
                  'text':'The stone floors and walls and cold and damp'},
         'temple':{'name':'a small temple','east':'torture','south':'empty',
                  'text':'There are three rows of benches facing the statue'},
         'torture':{'name':'a torture chamber','west':'temple','south':'bedroom',
                  'text':'There is a rack and an iron maiden agains teh wall\nand some chains and thumbscrews on the floor.'},
         'bedroom':{'name':'a bedroom','north':'torture','west':'empty',
                  'text':'There is a large bed with black, silk sheets on it.'}}
directions = ['north','south','east','west']
current_room = rooms ['empty']
print (current_room['east'])
bad_text = "You can't go that way!"
bad_input = "I don't understand the command!"

#game loop
while True:
    #display current location
    print()
    print ('*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*')
    print ("You're in {}.".format(current_room['name']))
    print (current_room['text'])

    #get user input
    command = input ('\nWhere to? ').strip()

    #movement
    if command in directions:
        if command in current_room:
            current_room = rooms[current_room[command]]
        else:
            #bad movement
            print (bad_text)
    elif command.lower() in ('q','quit'):
        break
    else:
        print(bad_input)
    
