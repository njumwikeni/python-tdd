print ("Welcome to Ichapod's Text Adventure")
current_room ='empty'
#game loop
while True:
    #display rooms contents
    print()
    if current_room == 'empty':
        print('You are in an empty room.')
        print ('The stone floors and walls are cold and damp.')
    elif current_room == 'temple':
        print('You are in a small temple.')
        print ('There are three rows of benches facing the statue.')
    elif current_room == 'torture':
        print('You are in a torture chamber.')
        print ('There is a rack and an iron maiden against the wall '
               'and some chains and thumbscrews on the floor.')
    elif current_room == 'bedroom':
        print('You are in a bedroom.')
        print ('There is a large bed with black, silk sheets on it.')
    #get User input

    command = input('\nWhat do you do? ').strip()
    #movement
    if command.lower() in ('n','north'):
        if current_room == 'empty':
            current_room = 'temple'
        elif current_room == 'bedroom':
            current_room = 'torture'
        else:
            print ("You can't go that way")
    elif command.lower() in ('s','south'):
        if current_room == 'temple':
            current_room = 'empty'
        elif current_room == 'torture':
            current_room = 'bedroom'
        else:
            print ("You can't go that way")
    elif command.lower() in ('e','east'):
        if current_room == 'empty':
            current_room = 'bedroom'
        elif current_room == 'temple':
            current_room = 'torture'
        else:
            print ("You can't go that way")
    elif command.lower() in ('w','west'):
        if current_room == 'bedroom':
            current_room = 'empty'
        elif current_room == 'torture':
            current_room = 'temple'
        else:
            print ("You can't go that way")
    elif command.lower() in ('q','quit'):
        break
    #bad command
    else:
        print ("I don't understand the command.")
