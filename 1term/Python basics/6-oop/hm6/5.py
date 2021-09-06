class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Painting runs')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Painting by pen {self.title} runs')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Painting by pencil {self.title} runs')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Painting by  handle {self.title} runs')


pen = Pen('pen1')
pencil = Pencil('pencil2')
handle = Handle('handle3')

pen.draw()
pencil.draw()
handle.draw()
