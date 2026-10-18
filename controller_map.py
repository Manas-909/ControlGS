import pygame

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller found")
    pygame.quit()
    raise SystemExit

controller = pygame.joystick.Joystick(0)
controller.init()

print(f"{controller.get_name()} conected")

axis_direction = {}

try:
    while True:
        for event in pygame.event.get():

            if event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")

            elif event.type == pygame.JOYHATMOTION:
                print(f"D-pad button {event.value}")

            elif event.type == pygame.JOYAXISMOTION:
                value = event.value
                axis = event.axis
                print(f"Axis {axis} moved {value:.2f}")

        pygame.time.wait(10)

except KeyboardInterrupt:
    print("quitting test")

finally:
    pygame.quit()