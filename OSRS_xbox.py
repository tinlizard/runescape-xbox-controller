import pygame
import pyautogui

# initialize pygame
pygame.init()

# initialize the joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

# set the mouse speed
mouse_speed = 40

# read the joystick input and map it to mouse movements and WASD controls
while True:
    # handle Pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # read the joystick axes and buttons
    x_axis = joystick.get_axis(0)
    y_axis = joystick.get_axis(1)
    lt_axis = joystick.get_axis(4)  # left trigger
    rt_axis = joystick.get_axis(5)  # right trigger

    # map the joystick axes to mouse movements
    mouse_x = x_axis * mouse_speed
    mouse_y = y_axis * mouse_speed

    # move the mouse
    pyautogui.moveRel(mouse_x, mouse_y)

    # simulate WASD controls with the right joystick and LT/RT buttons
    if joystick.get_button(4):  # move camera left (A)
        pyautogui.press('a')
    elif joystick.get_button(5):  # move camera right (D)
        pyautogui.press('d')
    elif lt_axis > 0.5:  # move camera up (W)
        pyautogui.press('w')
    elif rt_axis > 0.5:  # move camera down (S)
        pyautogui.press('s')

    # simulate a left mouse click when the A button is pressed
    if joystick.get_button(0):
        pyautogui.click()

    # simulate a right mouse click when the Y button is pressedsssssaaadddddssssdaaa
    if joystick.get_button(3):
        pyautogui.rightClick()

    # exit the program when the B button is pressed
    if joystick.get_button(1):
        break
