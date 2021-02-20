
def process(code: str, *args):
    code_cells = list(code)
    cell_ptr, code_ptr = 0, 0
    cells: list = [0]
    loop = False
    loop_start: int = 0
    _file = open("output.txt",'a')
    for element in args:
        if element == "--debug":
            flag.debug = True

    while code_ptr < len(code_cells):
        char = code_cells[code_ptr]

        if char == '+':
            cells[cell_ptr] += 1

        if char == '-':
            cells[cell_ptr] -= 1

        if char == '>':
            cell_ptr += 1
            if cell_ptr == len(cells):
                cells.insert(cell_ptr, 0)

        if char == '<':
            cell_ptr -= 1
            if cell_ptr < 0:
                cells.insert(0, 0)
                cell_ptr = 0

        if char == '.':
            f.write(cells[cell_ptr])

        if char == ',':
            cells[cell_ptr] = input()

        if char == '[':
            loop = True
            loop_start = code_ptr

        if char == ']':
            if loop:
                if cells[cell_ptr] == 0:
                    loop = False
                    continue
                elif cells[cell_ptr] != 0:
                    code_ptr = loop_start
            else:
                print("Loop end")


        code_ptr += 1
    f.close()


process(input("::"))