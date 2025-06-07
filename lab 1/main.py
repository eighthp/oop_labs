from point2d import Point2D
from vector2d import Vector2D

def main():
    # Создаём точки
    p1 = Point2D(30, 40)
    p2 = Point2D(120, 200)

    print("Точки:")
    print(f"p1 = {p1}")  # Point2D(30, 40)
    print(f"p2 = {p2}")  # Point2D(120, 200)
    print(f"p1 == p2? {p1 == p2}")  # False

    # Создаём векторы
    v1 = Vector2D(5, 12)
    v2 = Vector2D.from_points(p1, p2)

    print("\nВекторы:")
    print(f"v1 = {v1}")  # Vector2D(5, 12)
    print(f"v2 = {v2}")  # Vector2D(90, 160)
    print(f"Длина v1: {abs(v1):.1f}")  # 13.0

    print("\nОперации с векторами:")
    print(f"v1 + v2 = {v1 + v2}")  # Vector2D(95, 172)
    print(f"v2 - v1 = {v2 - v1}")  # Vector2D(85, 148)
    print(f"v1 * 3 = {v1 * 3}")    # Vector2D(15, 36)
    print(f"v2 / 2 = {v2 / 2}")    # Vector2D(45, 80)

    print("\nСкалярное произведение:")
    print(f"v1 · v2 = {v1.dot(v2)}")  # 5*90 + 12*160 = 450 + 1920 = 2370

    print("\nВекторное произведение:")
    print(f"v1 × v2 = {v1.cross(v2)}")  # 5*160 - 12*90 = 800 - 1080 = -280

if __name__ == "__main__":
    main()