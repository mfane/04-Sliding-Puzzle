#!/usr/bin/env python
import sys, pygame, random
from square import Square

assert sys.version_info >= (3, 4), 'This script requires at least Python 3.4'

screen_size = (600, 600)
dimensions = (rows, columns) = (4, 4)
FPS = 60
black = (0, 0, 0)
# colors taken from https://yeun.github.io/open-color/
colors = [(134, 142, 150), (250, 82, 82), (230, 73, 128), (190, 75, 219), (121, 80, 242), (76, 110, 245),
          (34, 138, 230), (21, 170, 191), (18, 184, 134), (64, 192, 87), (130, 201, 30), (250, 176, 5), (253, 126, 20),
          (233, 236, 239), (255, 236, 153), (163, 218, 255)]


def calculate_xy(pos):
    ''' calculates which square is the target '''
    w = 600 / columns
    h = 600 / rows
    to_return = (int(pos[0] // w), int(pos[1] // h))
    return to_return


def win(ls1, ls2):
    for i in range(0, 16):
        if not ls1[i].equals(ls2[i]):
            return False
    return True


def shuffle(ls):
    mover = 15
    for i in range(0, 1):
        if mover == 15:
            check = random.randint(0, 1)
            if check == 0:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 4].get_pos())
                ls[mover - 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 4]
                ls[mover - 4] = hold
                mover = mover - 4
            else:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 1].get_pos())
                ls[mover - 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 1]
                ls[mover - 1] = hold
                mover = mover - 1
        elif mover == 12:
            check = random.randint(0, 1)
            if check == 0:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 4].get_pos())
                ls[mover - 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 4]
                ls[mover - 4] = hold
                mover = mover - 4
            else:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 1].get_pos())
                ls[mover + 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 1]
                ls[mover + 1] = hold
                mover = mover + 1
        elif mover == 0:
            check = random.randint(0, 1)
            if check == 0:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 1].get_pos())
                ls[mover + 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 1]
                ls[mover + 1] = hold
                mover = mover + 1
            else:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 4].get_pos())
                ls[mover + 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 4]
                ls[mover + 4] = hold
                mover = mover + 4
        elif mover == 3:
            check = random.randint(0, 1)
            if check == 0:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 1].get_pos())
                ls[mover - 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 1]
                ls[mover - 1] = hold
                mover = mover - 1
            else:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 4].get_pos())
                ls[mover + 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 4]
                ls[mover + 4] = hold
                mover = mover + 4
        elif mover == 4 or mover == 8:
            check = random.randint(0, 2)
            if check == 0:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 4].get_pos())
                ls[mover - 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 4]
                ls[mover - 4] = hold
                mover = mover - 4
            elif check == 1:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 1].get_pos())
                ls[mover + 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 1]
                ls[mover + 1] = hold
                mover = mover + 1
            else:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 4].get_pos())
                ls[mover + 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 4]
                ls[mover + 4] = hold
                mover = mover + 4
        elif mover == 7 or mover == 11:
            check = random.randint(0, 2)
            if check == 0:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 4].get_pos())
                ls[mover - 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 4]
                ls[mover - 4] = hold
                mover = mover - 4
            elif check == 1:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 1].get_pos())
                ls[mover - 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 1]
                ls[mover - 1] = hold
                mover = mover - 1
            else:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 4].get_pos())
                ls[mover + 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 4]
                ls[mover + 4] = hold
                mover = mover + 4
        elif mover == 1 or mover == 2:
            check = random.randint(0, 2)
            if check == 0:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 1].get_pos())
                ls[mover - 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 1]
                ls[mover - 1] = hold
                mover = mover - 1
            elif check == 1:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 1].get_pos())
                ls[mover + 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 1]
                ls[mover + 1] = hold
                mover = mover + 1
            else:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 4].get_pos())
                ls[mover + 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 4]
                ls[mover + 4] = hold
                mover = mover + 4
        elif mover == 13 or mover == 14:
            check = random.randint(0, 2)
            if check == 0:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 4].get_pos())
                ls[mover - 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 4]
                ls[mover - 4] = hold
                mover = mover - 4
            elif check == 1:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 1].get_pos())
                ls[mover + 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 1]
                ls[mover + 1] = hold
                mover = mover + 1
            else:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 1].get_pos())
                ls[mover - 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 1]
                ls[mover - 1] = hold
                mover = mover - 1
        else:
            check = random.randint(0, 3)
            if check == 0:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 4].get_pos())
                ls[mover - 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 4]
                ls[mover - 4] = hold
                mover = mover - 4
            elif check == 1:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 1].get_pos())
                ls[mover + 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 1]
                ls[mover + 1] = hold
                mover = mover + 1
            elif check == 2:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover - 1].get_pos())
                ls[mover - 1].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover - 1]
                ls[mover - 1] = hold
                mover = mover - 1
            else:
                hold_pos = ls[mover].get_pos()
                ls[mover].change_pos(ls[mover + 4].get_pos())
                ls[mover + 4].change_pos(hold_pos)
                hold = ls[mover]
                ls[mover] = ls[mover + 4]
                ls[mover + 4] = hold
                mover = mover + 4
    return mover


def main():
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    font = pygame.font.SysFont("arial", 64)
    clock = pygame.time.Clock()
    screen.fill(black)
    puzzle = []
    win_case = []
    (w, h) = (screen_size[0] / columns, screen_size[1] / rows)
    for i in range(rows):
        for j in range(columns):
            position = j * rows + i
            color = colors[position]
            if i == 3 & j == 3:
                puzzle.append(Square(i, j, " ", w, h, black, font))
                win_case.append(Square(i, j, " ", w, h, black, font))
            else:
                puzzle.append(Square(i, j, str(position + 1), w, h, color, font))
                win_case.append(Square(i, j, str(position + 1), w, h, color, font))
    mover = shuffle(puzzle)
    print(mover)
    while True:
        clock.tick(FPS)

        if win(win_case, puzzle):
            screen.fill(black)
            s = Square(1, 1, "You win!", 250, 250, (204, 93, 232), font)
            s.draw_square(pygame.draw, screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
            pygame.display.flip()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        if mover > 3:
                            hold_pos = puzzle[mover].get_pos()
                            puzzle[mover].change_pos(puzzle[mover - 4].get_pos())
                            puzzle[mover - 4].change_pos(hold_pos)
                            hold = puzzle[mover]
                            puzzle[mover] = puzzle[mover - 4]
                            puzzle[mover - 4] = hold
                            mover = mover - 4
                    elif event.key == pygame.K_RIGHT:
                        if mover < 12:
                            hold_pos = puzzle[mover].get_pos()
                            puzzle[mover].change_pos(puzzle[mover + 4].get_pos())
                            puzzle[mover + 4].change_pos(hold_pos)
                            hold = puzzle[mover]
                            puzzle[mover] = puzzle[mover + 4]
                            puzzle[mover + 4] = hold
                            mover = mover + 4
                    elif event.key == pygame.K_UP:
                        if mover != 12 and mover != 8 and mover != 4 and mover != 0:
                            hold_pos = puzzle[mover].get_pos()
                            puzzle[mover].change_pos(puzzle[mover - 1].get_pos())
                            puzzle[mover - 1].change_pos(hold_pos)
                            hold = puzzle[mover]
                            puzzle[mover] = puzzle[mover - 1]
                            puzzle[mover - 1] = hold
                            mover = mover - 1
                    elif event.key == pygame.K_DOWN:
                        if mover != 15 and mover != 11 and mover != 7 and mover != 3:
                            hold_pos = puzzle[mover].get_pos()
                            puzzle[mover].change_pos(puzzle[mover + 1].get_pos())
                            puzzle[mover + 1].change_pos(hold_pos)
                            hold = puzzle[mover]
                            puzzle[mover] = puzzle[mover + 1]
                            puzzle[mover + 1] = hold
                            mover = mover + 1

                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    sq_mover = puzzle[mover].get_pos()
                    sq_target = calculate_xy(pos)
                    x_target = sq_target[0]
                    y_target = sq_target[1]
                    x_mover = sq_mover[0]
                    y_mover = sq_mover[1]
                    if x_target == x_mover and y_target == y_mover + 1:
                        hold_pos = puzzle[mover].get_pos()
                        puzzle[mover].change_pos(puzzle[mover + 1].get_pos())
                        puzzle[mover + 1].change_pos(hold_pos)
                        hold = puzzle[mover]
                        puzzle[mover] = puzzle[mover + 1]
                        puzzle[mover + 1] = hold
                        mover = mover + 1
                    elif x_target == x_mover and y_target == y_mover - 1:
                        hold_pos = puzzle[mover].get_pos()
                        puzzle[mover].change_pos(puzzle[mover - 1].get_pos())
                        puzzle[mover - 1].change_pos(hold_pos)
                        hold = puzzle[mover]
                        puzzle[mover] = puzzle[mover - 1]
                        puzzle[mover - 1] = hold
                        mover = mover - 1
                    elif x_target == x_mover + 1 and y_target == y_mover:
                        hold_pos = puzzle[mover].get_pos()
                        puzzle[mover].change_pos(puzzle[mover + 4].get_pos())
                        puzzle[mover + 4].change_pos(hold_pos)
                        hold = puzzle[mover]
                        puzzle[mover] = puzzle[mover + 4]
                        puzzle[mover + 4] = hold
                        mover = mover + 4
                    elif x_target == x_mover - 1 and y_target == y_mover:
                        hold_pos = puzzle[mover].get_pos()
                        puzzle[mover].change_pos(puzzle[mover - 4].get_pos())
                        puzzle[mover - 4].change_pos(hold_pos)
                        hold = puzzle[mover]
                        puzzle[mover] = puzzle[mover - 4]
                        puzzle[mover - 4] = hold
                        mover = mover - 4
            for p in puzzle:
                p.draw_square(pygame.draw, screen)
            pygame.display.flip()




if __name__ == '__main__':
    main()
