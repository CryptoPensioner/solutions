def printc(message, t='white', b=None):
    text_colors = {
        'black': '30',
        'red': '31',
        'green': '32',
        'yellow': '33',
        'blue': '34',
        'magenta': '35',
        'cyan': '36',
        'white': '37',
        'bright_black': '90',
        'bright_red': '91',
        'bright_green': '92',
        'bright_yellow': '93',
        'bright_blue': '94',
        'bright_magenta': '95',
        'bright_cyan': '96',
        'bright_white': '97'
    }

    bg_colors = {
        'black': '40',
        'red': '41',
        'green': '42',
        'yellow': '43',
        'blue': '44',
        'magenta': '45',
        'cyan': '46',
        'white': '47',
        'bright_black': '100',
        'bright_red': '101',
        'bright_green': '102',
        'bright_yellow': '103',
        'bright_blue': '104',
        'bright_magenta': '105',
        'bright_cyan': '106',
        'bright_white': '107'
    }

    # Get the ANSI code for the requested text and background colors
    text_color_code = '\033[' + text_colors.get(t, '37') + 'm'
    bg_color_code = '\033[' + bg_colors.get(b, '') + 'm' if b else ''

    # Print the message with the selected colors
    print(f"{text_color_code}{bg_color_code}{message}\033[0m")





# Example usage
name = "World"
printc("Let's go!")


colors = [
    'black',
    'red',
    'green',
    'yellow',
    'blue',
    'magenta',
    'cyan',
    'white',
    'bright_black',
    'bright_red',
    'bright_green',
    'bright_yellow',
    'bright_blue',
    'bright_magenta',
    'bright_cyan',
    'bright_white'
]

for color in colors:
    for color2 in colors:
        printc(f"Hello, {name}!", t=color, b=color2)
