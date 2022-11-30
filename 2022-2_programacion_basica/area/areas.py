class Area:
    def __init__(self, sides):
        self.sides = sides

    __privateShapes = [
        {'nsides': 3, 'name': 'triángulo (o trígono)'},
        {'nsides': 4, 'name': 'cuadrilátero (o tetrágono)'},
        {'nsides': 5, 'name': 'pentágono'},
        {'nsides': 6, 'name': 'hexágono'},
        {'nsides': 7, 'name': 'heptágono'},
        {'nsides': 8, 'name': 'octógono (u octágono)'},
        {'nsides': 9, 'name': 'eneágono (o nonágono)'},
        {'nsides': 10, 'name': 'decágono'},
        {'nsides': 11, 'name': 'endecágono (o undecágono)'},
        {'nsides': 12, 'name': 'dodecágono'},
        {'nsides': 13, 'name': 'tridecágono'},
        {'nsides': 14, 'name': 'tetradecágono'},
        {'nsides': 15, 'name': 'pentadecágono'},
        {'nsides': 16, 'name': 'hexadecágono'},
        {'nsides': 17, 'name': 'heptadecágono'},
        {'nsides': 18, 'name': 'octadecágono'},
        {'nsides': 19, 'name': 'eneadecágono (o nonadecágono)'},
        {'nsides': 20, 'name': 'icoságono (o isodecágono)'},
        {'nsides': 30, 'name': 'triacontágono'},
        {'nsides': 40, 'name': 'tetracontágono'},
        {'nsides': 50, 'name': 'pentacontágono'},
        {'nsides': 60, 'name': 'hexacontágono'},
        {'nsides': 70, 'name': 'heptacontágono'},
        {'nsides': 80, 'name': 'octacontágono'},
        {'nsides': 90, 'name': 'eneacontágono (o nonacontágono)'},
        {'nsides': 100, 'name': 'hectágono'},
        {'nsides': 1000, 'name': 'chiliágono'},
        {'nsides': 10000, 'name': 'miriágono'},
        {'nsides': 100000, 'name': 'hectamiriágono'},
    ]

    def calculateArea(self, length):
        return self.sides * length

    def findShapeName(self, nSides):
        i = 0
        name = f"polígono de {self.sides} lados"
        while i < len(Area.__privateShapes):
            if Area.__privateShapes[i]['nsides'] == nSides:
                name = Area.__privateShapes[i]['name']
            i += 1
        return name

    def shapePerimeter(self, sideLength):
        if self.sides < 3:
            print('\nSe necesitan como mínimo 3 lados para formar un polígono.');
        else:
            print(
                "El perímetro de un",
                self.findShapeName(self.sides),
                "de",
                sideLength,
                "unidades por lado, será igual a",
                str(self.calculateArea(sideLength))
            )

        if self.sides == 4:
            self.calculateAreaSquare(sideLength)
    
    def calculateAreaSquare(self, sideLength):
        print("  Este cuadrilátero tiene un área de", sideLength * sideLength, "unidades cuadradas\n")


square = Area(4)
square.shapePerimeter(10)

pentagon = Area(5)
pentagon.shapePerimeter(11)

otherShape = Area(123)
otherShape.shapePerimeter(0.5)

noPolygon = Area(2)
noPolygon.shapePerimeter(7)
