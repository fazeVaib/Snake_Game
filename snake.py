import random
import curses

stdscr = curses.initscr()
curses.curs_set(0)
screenH, screenW = 25, 60
w = curses.newwin(screenH, screenW, 0, 0)
w.border(0)
curses.noecho()
w.keypad(1)
w.timeout(100)
score = 0

snake_x = screenW // 5
snake_y = screenH // 5

snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

food = [int(screenH / 2), int(screenW / 2)]
w.addch(food[0], food[1], '@')
w.addstr(0, 3, 'Score: ')
w.addstr(24, 28, 'Snake')
key = curses.KEY_RIGHT

while True:
    nextKey = w.getch()
    w.addstr(0, 3, 'Score: ' + str(score))
    key = key if nextKey == -1 else nextKey

    if snake[0][0] in [0, screenH-1] or \
            snake[0][1] in [0, screenW-1] or \
            snake[0] in snake[1:]:
        curses.endwin()
        print("You scored " + str(score) + ". Better luck next time!")
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
        score += 1
        food = None
        while food is None:
            nf = [
                random.randint(1, screenH - 2),
                random.randint(1, screenW - 2)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], '@')
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], '*')
