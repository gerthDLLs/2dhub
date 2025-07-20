# ascii_gpu.py
def draw_ascii_logo():
    cube = [
        "      ▄▄▄▄▄      ",
        "     ███████     ",
        "    ██░░░░░██    ",
        "   ███████████   ",
        "   ▓ ASCII-GPU ▓ ",
        "    ▀▀▀▀▀▀▀▀▀    "
    ]
    for line in cube:
        print(line)
    print("\n  ~ Interface ASCII Render Engine ~\n")