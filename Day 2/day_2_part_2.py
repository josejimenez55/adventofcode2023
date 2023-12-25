with open('day_2_input.txt', 'r') as day_input:
    # data structure is a list of lists where the index is the game id
    # each item in the list contains a list of sets played
    all_games = [[(0,0,0)]] # [(num_red, num_green, num_blue)]. index is game id
    condition = (12, 13, 14) # 12 red, 13 green, 14 blue
    possible_games = [] # list of games that could be played using above condition

    # get all input into data structure
    for line in day_input:
        game = []
        # find colon
        idx_colon = line.find(':')
        line = line[idx_colon:]

        # get number of sets played
        num_sets = 1
        index_of_sets = [0]
        for i in range(len(line)):
            index = line[i:].find(';', 0, 1)
            if(index > -1):
                num_sets += 1
                index_of_sets.append(i)

        print(index_of_sets)

        for i in range(len(index_of_sets)):
            end_index = i + 1
            line_slice = []
            if(end_index >= len(index_of_sets)):
                line_slice = line[index_of_sets[i]:]
            else:
                line_slice = line[index_of_sets[i]:index_of_sets[end_index]]
            print(line_slice)
            subslice = line_slice[2:].split(', ')
            num_red = 0
            num_green = 0
            num_blue = 0

            for s in subslice:
                a = s.split(' ')
                num = int(a[0])
                color = a[1].rstrip()
                if(color == 'red'):
                    num_red = num
                elif(color == 'green'):
                    num_green = num
                else:
                    num_blue = num

            game.append((num_red, num_green, num_blue))
            
        all_games.append(game)
    
    power = 0
    for game_id, game in enumerate(all_games):
        print(game)
        red = max([c[0] for c in game])
        green = max([c[1] for c in game])
        blue = max([c[2] for c in game])

        power += red * green * blue


    print('Power:', power)
