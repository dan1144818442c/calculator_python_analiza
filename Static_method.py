
class method:

    @staticmethod
    def chek_ang_get_digit(num):
        while (True):
            try:
                return float(num)
            except:
                num = input(f"must enter num {num} is nut a num ")




    @staticmethod
    def print_main_menu():
        print("\n--- Shape Manager ---")
        print("1. Show all shapes")
        print("2. Add a new shape")
        print("3. Select shape and display details")
        print("4. Perform operation between shapes")
        print("0. Exit")
    @staticmethod
    def print_shape_menu():
        print("\nChoose shape type to add:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Hexagon")
        print("0. Cancel")

    @staticmethod
    def add_shape(shapes : list):
        from Square_Class import Square
        from class_Rectangle import Rectangle
        from Triangle_Class import Triangle
        from Circle_class import Circle
        from class_Regular_Hexagon import Regular_Hexagon
        method.print_shape_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            side = input("Enter side length: ")
            high = input("Enter high length:")
            shapes.append(Square(side , high))
            print("Square added.")

        elif choice == "2":
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            shapes.append(Rectangle(width, height))
            print("Rectangle added.")

        elif choice == "3":
            base = input("Enter base: ")
            height = input("Enter height: ")
            shapes.append(Triangle(base, height))
            print("Triangle added.")

        elif choice == "4":
            radius = input("Enter radius: ")
            shapes.append(Circle(radius))
            print("Circle added.")

        elif choice == "5":
            side = input("Enter side length: ")
            shapes.append(Regular_Hexagon(side))
            print("Hexagon added.")

        elif choice == "0":
            print("Cancelled.")
        else:
            print("Invalid choice.")
    @staticmethod
    def show_shapes(shapes):
        if not shapes:
            print("No shapes in the list.")
            return
        print("\n--- Shapes List ---")
        for idx, shape in enumerate(shapes):
            print(f"{idx + 1}. {shape}")
    @staticmethod
    def select_and_display_shape(shapes):
        if not shapes:
            print("No shapes to display.")
            return
        method.show_shapes(shapes)
        try:
            index = int(input("Enter shape number to view details: ")) - 1
            shape = shapes[index]
            print("\n--- Shape Details ---")
            print(shape)

        except:
            print("Invalid index.")

    @staticmethod
    def perform_operation(shapes):
        if len(shapes) < 2:
            print("You need at least two shapes to perform operations.")
            return

        method.show_shapes(shapes)

        try:
            idx1 = int(input("Enter number of first shape: ")) - 1
            idx2 = int(input("Enter number of second shape: ")) - 1

            s1 = shapes[idx1]
            s2 = shapes[idx2]

            print("\nChoose operation:")
            print("1. Add (Area1 + Area2)")
            print("2. Subtract (Area1 - Area2)")
            print("3. Compare Equal (==)")
            print("4. Greater Than (>)")

            op = input("Enter your choice: ")

            if op == "1":
                print(f"Result: {s1 + s2}")

            elif op == "2":
                print(f"Result: {s1 - s2}")

            elif op == "3":
                print("Shapes are equal." if s1 == s2 else "Shapes are not equal.")

            elif op == "4":
                print("First shape is greater." if s1 > s2 else "First shape is not greater.")

            else:
                print("Invalid operation choice.")

        except (ValueError, IndexError):
            print("Invalid index or input.")

    @staticmethod
    def main(shapes):
        while True:
            method.print_main_menu()
            option = input("Choose an option: ")

            if option == "1":
                method.show_shapes(shapes)
            elif option == "2":
                method.add_shape(shapes)
            elif option == "3":
                method.select_and_display_shape(shapes)
            elif option == "4":
                method.perform_operation(shapes)
            elif option == "0":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")




