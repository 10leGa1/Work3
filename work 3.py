import math

class GeometryFigure:
    def area(self):
        pass
    
    def perimeter(self):
        pass

class Ellipse(GeometryFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def area(self):
        return math.pi * self.a * self.b
    
    def perimeter(self):
        return 2 * math.pi * math.sqrt((self.a ** 2 + self.b ** 2) / 2)

class Square(GeometryFigure):
    def __init__(self, a):
        self.a = a
        
    def area(self):
        return self.a * self.a
    
    def perimeter(self):
        return 4 * self.a

class Trapezoid(GeometryFigure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        
    def area(self):
        return 0.5 * (self.a + self.b) * math.sqrt(self.c ** 2 - ((self.b - self.a) ** 2 + self.c ** 2 - self.d ** 2) / (2 * (self.b - self.a)))
    
    def perimeter(self):
        return self.a + self.b + self.c + self.d

def main():
    print("Выберите геометрическую фигуру:")
    print("1. Эллипс")
    print("2. Площадь")
    print("3. Трапеция")
    
    choice = input("Введите свой выбор (1/2/3): ")
    
    if choice == "1":
        a = float(input("Введите главную ось эллипса: "))
        b = float(input("Введите малую ось эллипса: "))
        
        ellipse = Ellipse(a, b)
        print("Площадь эллипса: ", ellipse.area())
        print("Периметр эллипса: ", ellipse.perimeter())
    elif choice == "2":
        a = float(input("Введите длину стороны квадрата: "))
        
        square = Square(a)
        print("Площадь квадрата: ", square.area())
        print("Периметр площади: ", square.perimeter())
    elif choice == "3":
        a = float(input("Введите длину верхней стороны трапеции: "))
        b = float(input("Введите длину нижней стороны трапеции: "))
        c = float(input("Введите высоту трапеции: "))
        d = float(input("Введите высоту наклона трапеции: "))
        
        trapezoid = Trapezoid(a, b, c, d)
        print("Площадь трапеции: ", trapezoid.area())
        print("Периметр трапеции: ", trapezoid.perimeter())

if __name__ == "__main__":
    main()
