
#polymorphisim is many form a method can take or have

class Retangle:
    def draw(self):
        print("drawing a rectangle")

class Rhombus:
    def draw(self):
        print("Drawing a Rhombus")

class Parallelogram:
    def draw(self):
        print("Drawig a parallelogram")

r = Retangle()
r.draw()

Rh = Rhombus()
Rh.draw()

P = Parallelogram()
P.draw()