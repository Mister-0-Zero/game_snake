from game_over import  Game_over

def Check_game_over(snake, x_change, y_change):
    """ Проверяет ударилась ли змея о край карты или об свой хвост """
    next_x = snake.snake_list[0][0] + x_change
    next_y = snake.snake_list[0][1] + y_change

    if next_x >= snake.width or next_x < 0 or next_y >= snake.height or next_y < 0:
        return Game_over(snake.screen, snake.width, snake.height)

    for x, y, orientation in snake.snake_list[1:]:
        if next_x == x and next_y == y:
            return Game_over(snake.screen, snake.width, snake.height)

    return 0
