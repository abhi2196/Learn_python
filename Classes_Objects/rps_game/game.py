#!/usr/bin/env python3

import random

from actors import Player, roll

def main():
    print_header()
    rolls = build_the_three_rolls()
    name = get_player_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)

def print_header():
    print('------------------------------')
    print('  Rock Paper Scissors Game')
    print('------------------------------')
    print('')

def build_the_three_rolls():
    rock = roll('rock')
    paper = roll('paper')
    scissor = roll('scissor')

    rock.update_roll([scissor], [paper])
    paper.update_roll([rock], [scissor])
    scissor.update_roll([paper], [rock])

    return [rock, paper, scissor,]

def get_player_name():
    name = input('enter your name ... \n')
    name.strip()
    return name

def game_loop(player1, player2, rolls):
    count = 1
    p1_wins = 0
    p2_wins = 0
    while count <= 3:
        p2_roll = random.choice(rolls)
        p1_roll_type = input('enter your roll type [r] rock, [p] paper, [s] scissor ...')
        if p1_roll_type == 'r':
            p1_roll = rolls[0]
        elif p1_roll_type == 'p':
            p1_roll = rolls[1]
        elif p1_roll_type == 's':
            p1_roll = rolls[2]
        else:
            print('please choose a valid roll !')
            continue
        print('* {} rolled {} *'.format(player1.name, p1_roll.roll_name))
        print('* {} rolled {} *'.format(player2.name, p2_roll.roll_name))
		
        if p1_roll.roll_name == p2_roll.roll_name:
            print('Please play again !')
            continue

        if p1_roll.can_defeat(p2_roll):
            p1_wins += 1
            winner = player1.name
        else:
            p2_wins += 1
            winner = player2.name

        print('** {} wins this round **'.format(winner))
        if p1_wins == 2 or p2_wins == 2:
            break
        count += 1

    if p1_wins > p2_wins:
        winner = player1.name
    elif p2_wins > p1_wins:
        winner = player2.name
    
    print('\n*** Congrats! {} won the game ***'.format(winner))
    print('\n*** Final Score: {}:{} - {}:{} ****'.format(player1.name, p1_wins, player2.name, p2_wins))
    print('\n*** Good Bye! ***')
    
if __name__ == "__main__":
    main()
