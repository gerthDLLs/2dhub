# desktop.py
import sys
from ascii_gpu import draw_ascii_logo
from krisk import WindowManager

def start_desktop():
    print("💾 KRISPYPY Desktop iniciado.\n")
    draw_ascii_logo()

    wm = WindowManager()
    wm.create_window("Terminal", "Simulador Bash [GGH]", rows=12, cols=40)
    wm.create_window("Arquivos", "Árvore de diretórios", rows=12, cols=40)

if __name__ == "__main__":
    start_desktop()