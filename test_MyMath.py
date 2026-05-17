from MyMath import myArea, myvolume, mycondition

def test_myArea():
    # Проверяем площадь прямоугольника (5 * 4 = 20)
    assert myArea("rectangle", 5, 4, 0, 0) == 20
    # Проверяем площадь квадрата (3^2 = 9)
    assert myArea("square", 3, 0, 0, 0) == 9

def test_myvolume():
    # Проверяем объем куба (3^3 = 27)
    assert myvolume("cube", 3, 0, 0, 0) == 27
    # Проверяем объем кубоида (2 * 3 * 4 = 24)
    assert myvolume("cuboid", 2, 3, 4, 0) == 24

def test_mycondition():
    # Проверяем теорему Пифагора (3^2 + 4^2 = 5^2). 
    # Функция возвращает 1, если это пифагорова тройка.
    assert mycondition("Pythagorean Triplet Checker", 3, 4, 5, 0) == 1
    # Если не тройка, возвращает 2.
    assert mycondition("Pythagorean Triplet Checker", 1, 2, 3, 0) == 2
