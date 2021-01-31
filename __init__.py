# class Interpreter:
#     characters: list = ['+', '-', '>', '<', '[', ']', ',', '.']
#
#     def __init__(self, input_field: str):
#         self.space: list = [0]
#         self.location: int = 0
#         self.current_char: str
#         for char in Interpreter.characters:
#             if char in input_field:
#                 if char == '.': pass
#                 self.program: str = input_field
#
#
#
#
#     def move_left(self):
#         self.location += 1
#         try:
#             self.space[self.location] = 0
#         except IndexError:
#             self.space.insert(self.location, 0)
#
#     def move_right(self):
#         self.location -= 1
#         try:
#             self.space[self.location] = 0
#         except IndexError:
#             self.space.insert(self.location, 0)
#
#     def increase(self):
#         self.space[self.location] += 1
#
#     def decrease(self):
#         self.space[self.location] -= 1
#
#     def can_loop(self) -> bool:
#         if self.space[self.location] == 0:
#             return False
#         else:
#             return True
#
