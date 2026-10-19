import pygame
from pynput.keyboard import Controller, Key

pygame.init()
pygame.joystick.init()

keyboard = Controller()

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

held_keys = {}

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

            elif event.type == pygame.JOYBUTTONUP:
                if event.button in button_map:
                    key = button_map[event.button]
                    key_release(key, f"button{event.button}")

            elif event.type == pygame.JOYAXISMOTION:
                axis = event.axis
                value = event.value
                
                direction = None

                if value < -0.3:
                    direction = "negative"
                elif value > 0.3:
                    direction = "positive"

                for side in ("negative", "positive"):
                    mapp = (axis, side)
                    key = axis_map.get(mapp)

                    if key is None:
                        continue

                    source = f"axis_{axis}_{side}"
                    hold_if = direction == side

                    if hold_if:
                        key_press(key, source)
                    elif not hold_if:
                        key_release(key, source)

        pygame.time.wait(10)

except KeyboardInterrupt:
    print("quittin test")

finally:
    for key in list(held_keys):
        keyboard.release(key)

    pygame.quit()