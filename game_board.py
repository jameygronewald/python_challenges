

height = int(input(f"How many squares tall would you like the game-board to be? Please enter an integer.   "))
width = int(input(f"How many squares wide would you like the game-board to be? Please enter an integer.   "))

horizontal_line = """ ---"""
vertical_line = """|   """
end_ver_line = "|"

def print_horizontal(width):
    horizontal_string = horizontal_line * width
    print(horizontal_string)

def print_vertical(width):
    vertical_string = vertical_line * width + end_ver_line
    print(vertical_string)

def print_board(height):
    for _ in range(height):
        print_horizontal(width)
        print_vertical(width)
    print_horizontal(width)

print_board(height) 
