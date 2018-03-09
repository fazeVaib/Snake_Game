import random
import curses

stdscr = curses.initscr()
curses.curs_set(0)
snakeH, snakeW = stdscr.getmaxyx()
w = curses.newwin(snakeH, snakeW, 0, 0)
w.keypad(1)
w.timeout(150)

snake_x = snakeW // 5
snake_y = snakeH // 5

snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [int(snakeH / 2), int(snakeW / 2)]
w.addch(food[0], food[1], '*')

key = curses.KEY_RIGHT

while True:
    nextKey = w.getch()
    key = key if nextKey == -1 else nextKey

    if snake[0][0] in [0, snakeH] or snake[0][1] in [0, snakeW] or snake[0] in snake[1:]:
        curses.endwin()
        quit()

    newHead = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        newHead[0] += 1
    if key == curses.KEY_UP:
        newHead[0] -= 1
    if key == curses.KEY_LEFT:
        newHead[1] -= 1
    if key == curses.KEY_RIGHT:
        newHead[1] += 1

    snake.insert(0, newHead)

    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, snakeH - 1),
                random.randint(1, snakeW - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], '*')
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], '=')
