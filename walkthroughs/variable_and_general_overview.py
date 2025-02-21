# Variable Types (Data Structures):
    # Integers (int): Whole numbers (3, 4, 9) can be negative
    # Decimals (float): Decimal numbers (-.3, .34, 3.4) can be negative as well
    # Strings (str): Text data ("This is a string", 'This is also a string')
    # Booleans (bool): True or False values (bool_var: bool = 1 == 2)
    # Lists (list): Ordered set of items, ([1, 2, 3])
    # Dictionary (dict): Key-value pairs ({"name": "Tanner"})

# Keyboard Shortcuts:
    # CMD arrow key -> send you to the front or end of a line (lef and right) and top or bottom of a page (up and down)
    # OPT arrow key (left and right) -> skip over each word at a time
    # CMD j -> open and close your bottom console with a terminal
    # CMD b -> open and close your file directory
    # CMD + OPT + s -> save all files (unsaved files have a white dot next to their tab)

# using a function called type() - This will help us be able to check a variable's type at any moment

# Note: variables are like Pokemon! They each will have a type. the type is int, or bool, or float, etc, just like
    # in pokemon we have Fire, Water, Grass, etc

# Syntax of a funciton:
    # def -> I am declaring that what is about to come is a function
    # name of function -> typcially follow the standard of having "_"s between words (this is known as "snake case")
    # You must have "()" -> This is a reception point for variables or other objects that may be required to run this funciton.
        # often what is found within these () are called "Parameters"
        # Think of a car
def variable_hunt():
    # The syntax of declaring a variable is as follows:
        # simply put the name of the variable: response
        # Next you want to declare what type the variable is: response: str
        # finally you set the variable equal to something: response: str = "Test Response"

    # floats can hold int, but int cannot hold floats
    age: int = 9
    height: float = 5.9
    name: str = "Tanner"
    is_student: bool = True
    # This grades variable is a list of int
    grades: list[int] = [90, 105, 93]

    grades_dict: dict = {
        "name": name,
        "grades": grades, 
        "is_student": is_student
        }

    # print all of the variables and their types
    # print -> it will display what is found in the parethensis to the terminal
    print(f"age is a {type(age)} type")
    print(f"height is a {type(height)} type")
    print(f"name is a {type(name)} type")
    print(f"is_student is a {type(is_student)} type")
    print(f"grades is a {type(grades)} type")
    print(f"Is {grades_dict['name']} a student? {grades_dict['is_student']}. They have the grades as follows: {grades_dict['grades']}")


# magic syntax so that your computer knows when you run this file, it needs to run only the things found UNDER this line of code
if __name__ == "__main__":
    # Whenever we place a function, we refer to this as "Calling" the function
    variable_hunt()