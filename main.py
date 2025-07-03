from colorama import init, Back, Fore, Style
import time

# Initialize colorama
init(autoreset=True)

# List of background colors
bg_colors = [
    Back.RED,
    Back.GREEN,
    Back.YELLOW,
    Back.BLUE,
    Back.MAGENTA,
    Back.CYAN,
    Back.WHITE
]

# Print "Hello, World!" with different background colors
for i, bg in enumerate(bg_colors):
    print(f"{bg}{Fore.BLACK} Hello, World! - Color {i+1}")
    time.sleep(0.5)  # Optional: Delay for effect

