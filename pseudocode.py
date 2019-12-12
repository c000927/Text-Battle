title_screen()

title_help()

main_game()
    if player_alive == True:
        move()
        if enemy_alive == True:
            attack()
        else:
            move()
    else:
        game_over()

X..1..
...1..
...1..
"""
