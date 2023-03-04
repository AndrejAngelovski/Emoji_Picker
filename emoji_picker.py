import emoji

# Define the color and pattern options
COLORS = {'1': '🟥', '2': '🟩', '3': '🟦', '4': '⬜️'}
PATTERNS = {'1': '🟨', '2': '🟪', '3': '🟥🟦', '4': '🟥🟩'}

# Define the emoji options
EMOJIS = {'1': '🐶', '2': '🐱', '3': '🐭', '4': '🐹', '5': '🦊', '6': '🐻'}

# Define the default values
DEFAULT_BG_COLOR = '4'
DEFAULT_PATTERN = '3'
DEFAULT_FG_COLOR = '1'
DEFAULT_EMOJI = '1'


def get_input(prompt, options):
    """
    Display a menu with the given prompt and options,
    and return the user's choice as a string.
    """
    print(prompt)
    for key, value in options.items():
        print(f'  {key}. {value}')
    return input('> ')


def create_art(bg_color, pattern, fg_color, emoji):
    """
    Create an art grid with the given background color, pattern,
    foreground color, and emoji, and return it as a list of lists.
    """
    rows = 5
    cols = 7
    grid = [[bg_color] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if pattern[(i + j) % len(pattern)] == '🟥':
                grid[i][j] = fg_color
            elif pattern[(i + j) % len(pattern)] == '🟦':
                grid[i][j] = f'{fg_color}{fg_color}'
            elif pattern[(i + j) % len(pattern)] == '🟪':
                grid[i][j] = f'{bg_color}{fg_color}'
    emoji_row = 3
    emoji_col = 4
    grid[emoji_row][emoji_col] = emoji
    return grid


def display_art(grid):
    """
    Display the art grid in the console using emoji characters.
    """
    for row in grid:
        for cell in row:
            print(emoji.emojize(COLORS[cell]), end='')
        print()


def save_art(grid, filename):
    """
    Save the art grid to a file with the given filename.
    """
    with open(filename, 'w') as f:
        for row in grid:
            for cell in row:
                f.write(emoji.emojize(COLORS[cell]))
            f.write('\n')


def main():
    # Get the user's input
    bg_color = get_input('Choose a background color:', COLORS)
    pattern = get_input('Choose a pattern:', PATTERNS)
    fg_color = get_input('Choose a foreground color:', COLORS)
    emoji = get_input('Choose an emoji:', EMOJIS)

    # Create the art and display it
    art = create_art(bg_color, pattern, fg_color, EMOJIS[emoji])
    display_art(art)

    # Ask the user if they want to save the art
    save = input('Save to file? (Y/N) ').lower() == 'y'
    if save:
        filename = input('Enter file name: ')
        save_art(art, filename)


if __name__ == '__main__':
    print('Welcome to Emoji Art Maker!\n')
    main
