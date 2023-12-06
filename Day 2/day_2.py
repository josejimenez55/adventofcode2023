with open('day_2_input_reduced.txt', 'r') as day_input:
    # data structure is a list of lists where the index is the game id
    # each item in the list contains a list of sets played
    game = [[(0,0,0)]] # [(num_red, num_green, num_blue)]. index is game id
    condition = (12, 13, 14) # 12 red, 13 green, 14 blue
    possible_games = [] # list of games that could be played using above condition

    colors = ['red', 'green', 'blue']
    # get all input into data structure
    for line in day_input:
        # find colon
        idx_colon = line.find(':')
        line = line[idx_colon:]

        for i in range(len(line)):
            if line[i].isnumeric():
                num = int(line[i])
                for color_idx, color in enumerate(colors):
                    if line[i:].find(color, 0, len(color)) > -1:
