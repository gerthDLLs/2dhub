# krisk.py
class WindowManager:
    def create_window(self, title, subtitle="", rows=10, cols=40):
        print("+" + "-"*cols + "+")
        print(f"| {title}".ljust(cols) + " |")
        print(f"| {subtitle}".ljust(cols) + " |")
        for _ in range(rows):
            print("|" + " "*cols + "|")
        print("+" + "-"*cols + "+\n")