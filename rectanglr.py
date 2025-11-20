from numpy.distutils.lib2def import output_def


class Rectangle:
    def area(self, length, breadth):
        return length * breadth
    def perimeter(self, length, breadth):
        return 2 * (length + breadth)
    def compare_area(self, area1, area2):
        if area1 > area2:
            return"rectangle 1 has a greater area."
        elif area1 < area2:
            return "rectangle 2 has a greater area."
        else:
            return "both rectangles have the same area."
length1 = float(input("Enter length of Rectangle 1: "))
breadth1 = float(input("Enter breadth of Rectangle 1: "))

length2 = float(input("Enter length of Rectangle 2: "))
breadth2 = float(input("Enter breadth of Rectangle 2: "))

rectangle = Rectangle()


area_rect1 = rectangle.area(length1, breadth1)
area_rect2 = rectangle.area(length2, breadth2)
perimeter_rect1 = rectangle.perimeter(length1, breadth1)
perimeter_rect2 = rectangle.perimeter(length2, breadth2)

print("\nRectangle 1:")
print("Area:", area_rect1)
print("Perimeter:", perimeter_rect1)
print("\nRectangle 2:")
print("Area:", area_rect2)
print("Perimeter:", perimeter_rect2)
area_comparison = rectangle.compare_area(area_rect1, area_rect2)
print("\n" + area_comparison)



output
#Enter length of Rectangle 1: 5
Enter breadth of Rectangle 1: 4
Enter length of Rectangle 2: 6
Enter breadth of Rectangle 2: 3

Rectangle 1:
Area: 20.0
Perimeter: 18.0

Rectangle 2:
Area: 18.0
Perimeter: 18.0

rectangle 1 has a greater area.