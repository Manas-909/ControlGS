import pygame
from pynput.keyboard import Controller, Key
from pynput.mouse import Controller as Mcontrol, Button

pygame.init()
pygame.joystick.init()

keyboard = Controller()
mouse = Mcontrol()

if pygame.joystick.get_count() == 0:
    print("No Controller Found")
    pygame.quit()
    raise SystemExit

Controller = pygame.joystick.Joystick(0)
Controller.init()

axis_map = {

    (1, "negative") : "w",
    (1, "positive") : "s",
    (0, "negative") : "a",
    (0, "positive") : "d"
    
}

button_map = {
    0: Key.space
}

mouse_map = {
    2: "left",
    1: "right"
}

held_click = set()

Mouse_speed = 900

Mouse_X = 0.0
Mouse_Y = 0.0

held_keys = {}

def Mouse_move(value):
    if abs(value) < 0.15:
        return 0.0
    if value > 0:
        return (value - 0.15) / 0.85
    else:
        return (value + 0.15) / 0.85

def key_press(key, source):
    if key not in held_keys:
        held_keys[key] = set()

    if source in held_keys[key]:
        return

    if not held_keys[key]:
        keyboard.press(key)

    held_keys[key].add(source)

def key_release(key, source):
    if not (key in held_keys):
        return

    held_keys[key].discard(source)

    if not held_keys[key]:
        keyboard.release(key)
        del held_keys[key]


try:
    while True:

        for event in pygame.event.get():
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button in button_map:
                    key = button_map[event.button]
                    key_press(key, f"button{event.button}")

                elif event.button in mouse_map:
                    mouse_click = mouse_map[event.button]
                    if mouse_click == "left":
                        mouse.press(Button.left)
                        held_click.add(Button.left)
                    elif mouse_click == "right":
                        mouse.press(Button.right)
                        held_click.add(Button.right)

            elif event.type == pygame.JOYBUTTONUP:
                if event.button in button_map:
                    key = button_map[event.button]
                    key_release(key, f"button{event.button}")

                elif event.button in mouse_map:
                    mouse_click = mouse_map[event.button]
                    if mouse_click == "left":
                        mouse.release(Button.left)
                        held_click.discard(Button.left)
                    elif mouse_click == "right":
                        mouse.release(Button.right)
                        held_click.discard(Button.right)


            elif event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = event.value

                if axis == 2:
                    Mouse_X = value
                elif axis == 3:
                    Mouse_Y = value
                
                direction = None

                if value < -0.3:
                    direction = "negative"
                elif value > 0.3:
                    direction = "positive"

                for side in ("negative", "positive"):
                    key = axis_map.get((axis, side))

                    if key is None:
                        continue

                    source = f"axis_{axis}_{side}"

                    if direction == side:
                        key_press(key, source)
                    elif not direction == side:
                        key_release(key, source)

        Frame_time = pygame.time.Clock().tick(60) / 1000.0

        X_Move = Mouse_move(Mouse_X) * Mouse_speed * Frame_time
        Y_Move = Mouse_move(Mouse_Y) * Mouse_speed * Frame_time

        if X_Move or Y_Move:
            mouse.move(round(X_Move), round(Y_Move))

except KeyboardInterrupt:
    print("quittin test")

finally:
    for key in list(held_keys):
        keyboard.release(key)

    for click in held_click:
        mouse.release(click)

    held_click.clear()

    pygame.quit()