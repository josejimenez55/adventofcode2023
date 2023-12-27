with open('day_4_input.txt', 'r') as inputs:
    points = 0
    for cards in inputs:
        card = cards.split(':')[1].split('|')
        winning_numbers = card[0].strip().split(' ')
        winning_numbers = [num for num in winning_numbers if num.isnumeric()]
        numbers = card[1].strip().split(' ')
        numbers = [num for num in numbers if num.isnumeric()]


        print(winning_numbers)
        print(numbers)

        game_point = 0
        for number in numbers:
            if(number in winning_numbers):
                if(game_point == 0):
                    game_point = 1
                else:
                    game_point *= 2
                print('Number', number, 'is a match! Running points:', game_point)
        points += game_point

    print(points)

