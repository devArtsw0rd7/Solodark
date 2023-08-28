import time

def prompt_to_roll():
    return input("Press Enter to roll the dice!")

def clear_console():
    print("\033[H\033[J")  # Clear the console

def roll_dice_animation(duration):
    # Define ASCII art frames for dice animation
    dice_frames = [
        "   _______\n  /       \\\n /         \\\n|     *     |\n \\         /\n  \\_______/",
        "   _______\n  /       \\\n /    *    \\\n|           |\n \\    *    /\n  \\_______/",
        "   _______\n  /       \\\n /  *      \\\n|     *     |\n \\      *  /\n  \\_______/",
        "   _______\n  / *     \\\n /    *    \\\n|           |\n \\    *    /\n  \\_______/",
        "   _______\n  / *     \\\n /         \\\n|     *     |\n \\         /\n  \\_______/"
    ]

    start_time = time.time()
    while time.time() - start_time < duration:
        for frame in dice_frames:
            print("\033[H\033[J")  # Clear the console
            print(frame)
            time.sleep(0.1)  # Delay between frames

def determine_article_for_value(value):
    if value == 8 or value == 11:
        return "an"
    return "a"

def determine_article_for_text(text):
    if text.lower() == "elf":
        return "an"
    return "a"


