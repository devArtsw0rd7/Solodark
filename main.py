from character import Character
from utils import prompt_to_roll, clear_console, roll_dice_animation, determine_article_for_value, determine_article_for_text

def main():
    while True:
        user_input = prompt_to_roll()

        if user_input == "":
            character = Character()

            # Roll Dice animation
            roll_dice_animation(2)  # Animation duration in seconds
            clear_console()

            # Determine the correct article for the ancestry and ancestry_roll
            article_roll = determine_article_for_value(character.ancestry_roll)
            article_ancestry = determine_article_for_text(character.ancestry)
            
            # Output
            print(f"You rolled {article_roll} {character.ancestry_roll}!")
            print("_______________________")
            print(f"Your character is {article_ancestry} {character.ancestry}!\n\n")
            
        elif user_input.lower() == "q":
            break
        else:
            print("Invalid input. Please press Enter to roll or type 'q' to exit.")

if __name__ == "__main__":
    main()
