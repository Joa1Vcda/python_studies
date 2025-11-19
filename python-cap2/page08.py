"""getter-@property"""


class Pencil:
    def __init__(self, color):
        self.color = color

    @property
    def get_color(self):
        return self.color

    # def get_color_2(self):
    #     return self.color


pencil = Pencil("Blue")
# print(pencil.get_color_2())
print(pencil.color)
