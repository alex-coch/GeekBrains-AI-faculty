class Stationary:

    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f'Just start drawing! {self.title}')


class Pen(Stationary):
    def draw(self):
        print(f'Just start drawing with Pen! {self.title}')


class Pencil(Stationary):
    def draw(self):
        print(f'Just start drawing with Pencil! {self.title}')


class Marker(Stationary):
    def draw(self):
        print(f'Just start drawing with Marker! {self.title}')

stat = Stationary()
stat.draw()

mark = Marker()
pen = Pencil()

mark.draw()
pen.draw()
