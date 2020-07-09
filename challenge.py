import math


def square_area(side):
    """Returns the area of a square"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return side ** 2


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (1/2) * base * height


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (1/2) * diagonal_1 * diagonal_2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (1/2) * (base_minor + base_major) * height


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    # You have to code here
    # REMEMBER: Tests first!!!
    return (1/2) * perimeter * apothem


def circumference_area(radius):
    """Returns the area of a circumference"""
    # You have to code here
    # REMEMBER: Tests first!!!
    # Use math.pi for π value
    return math.pi * (radius ** 2)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            # Initialize the needed values for the tests
            self.circles = {
                12.56637061 : 2,
                50.26548245 : 4,
                113.09733552: 6,
                201.06192982: 8
                }
            self.polygons = { #Note: Those polygons are pentagons
                6.88190960 : (10,1.37638192),
                27.52763840 : (20,2.75276384),
                61.93718642 : (30,4.12914576),
                110.1105536 : (40,5.50552768)
                }
            self.trapezoids = {
                3 : (2,4,1),
                18 : (4,8,3),
                45 : (6,12,5),
                84 : (8,16,7)
                }
            self.rhombuses = {
                4 : (2,4),
                16 : (4,8),
                36 : (6,12),
                64 : (8,16)
                }
            self.triangles = {
                10 : (5,4),
                40 : (10,8),
                90 : (15,12),
                160 : (20,16)
                }
            self.rectangles = {
                2 : (1,2),
                15 : (3,5),
                104 : (8,13),
                320 : (20,16)
                }
            self.squares = {
                4 : 2,
                9 : 3,
                16 : 4,
                25 : 5
                }
        def test_square_area(self):
             for key, value in self.squares.items():
                self.assertEqual(True, 
                math.isclose(key, square_area(value)),
                'Please, check square_area func')

        def test_rectangle_area(self):
             for key, value in self.rectangles.items():
                self.assertEqual(True, 
                math.isclose(key, rectangle_area(value[0], value[1])),
                'Please, check rectangle_area func')

        def test_triangle_area(self):
             for key, value in self.triangles.items():
                self.assertEqual(True, 
                math.isclose(key, triangle_area(value[0], value[1])),
                'Please, check triangle_area func')

        def test_rhombus_area(self):
             for key, value in self.rhombuses.items():
                self.assertEqual(True, 
                math.isclose(key, rhombus_area(value[0], value[1])),
                'Please, check rhombus_area func')

        def test_trapezoid_area(self):
             for key, value in self.trapezoids.items():
                self.assertEqual(True, 
                math.isclose(key,trapezoid_area(value[0], value[1], value[2])),
                'Please, check trapezoid_area func')

        def test_regular_polygon_area(self):
            for key, value in self.polygons.items():
                self.assertEqual(True, 
                math.isclose(key,regular_polygon_area(value[0], value[1])),
                'Please, check regular_polygon_area func')

        def test_circumference_area(self):
            for key, value in self.circles.items():
                self.assertEqual(True, 
                math.isclose(key,circumference_area(value)),
                'Please, check circumference_area function')

        def tearDown(self):
            del(self.circles)
            del(self.polygons)
            del(self.trapezoids)
            del(self.rhombuses)
            del(self.triangles)
            del(self.rectangles)
            del(self.squares)

    unittest.main()
