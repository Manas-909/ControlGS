# ControlGS
ControlGS is python script for mapping controller input to keyboard input

it let users configure controller buttons to Keyboard keys such as W, A, S, D, Space, and Shift so users can use their controllers to play browser based games directly with their controller. It uses pygame to take input from a controller and uses pynput to simulate key presses.

# How to run it
you can clone this repo with ```git clone https://github.com/Manas-909/ControlGS``` and run key_map.py
The butttons are configured according to my contoller, in case if you have a different configuration of buttons, run controller_map.py to check if your intended button is mapped to the right key.

# Where did i got the idea
Nowdays a number of popular pc games are ported to browser with web assembly, which means you can now play games like GTA V on your browser but i saw that your controller doen't actually work on these browser based games. so i researched how can i take input from my controller and turn that into key board key presses. I found out that i can use pygame to take input from controller and pynput to simulate key presses so i built this, i also wanted to add a GUI to this and thought PySide6 was a good option, it actually good for people who know how to use it but the problem was i never used it before, so i thought to take help of tutorials and ChatGPT but it didn't actually worked out as i intended it to and i didn't wanted to add ai slop that i don't understand, so i dropped the idea of GUI and went with python script instead.