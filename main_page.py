import pygame
from menu import draw_button

WINDOW_SIZE = 600, 600
BACKGROUND_COLOR = (255, 255, 255)


def main():
    # задаю значения кнопки(текст, x, y, длинна, ширина)(можно добавить картинку кнопки, но яне нашел красивой)
    buttons = [("Start", 100, 100, 400, 100), ('Exit', 100, 400, 400, 100), ('Stats', 100, 250, 400, 100)]

    pygame.init()

    screen = pygame.display.set_mode(WINDOW_SIZE)
    screen.fill(BACKGROUND_COLOR)
    running = True
    draw_button(screen, buttons)
    pygame.display.flip()
    while running:
        # Обрабатываем каждое событие циклом for
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Завершаем игровой цикл, если программу закрыли
                running = False
            # отслеживание нажатий кнопки
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for i in buttons:
                        if i[1] < event.pos[0] < i[1] + i[3] and i[2] < event.pos[1] < i[2] + i[4]:
                            # выбор действия при нажатии
                            print("print my blanks please")
                            if i[0] == 'Start':
                                pass
                            elif i[0] == 'Stats':
                                pass
                            elif i[0] == 'Exit':
                                pass
                            pass

    pygame.quit()


if __name__ == '__main__':
    main()