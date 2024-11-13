# function_arguments.py
# This program demonstrates various types of function arguments in Python.

# 1. Positional Arguments
def greet(name, message):
    """
    Greet the user with a message.
    :param name: Name of the person
    :param message: Greeting message
    """
    print(f"{message}, {name}!")

# 2. Keyword Arguments
def display_info(name, age):
    """
    Display name and age using keyword arguments.
    :param name: Name of the person
    :param age: Age of the person
    """
    print(f"Name: {name}")
    print(f"Age: {age}")

# 3. Default Arguments
def describe_pet(pet_name, pet_type="dog"):
    """
    Describe a pet with a default type.
    :param pet_name: Name of the pet
    :param pet_type: Type of the pet (default is "dog")
    """
    print(f"I have a {pet_type} named {pet_name}.")

# 4. Variable-Length Arguments (*args)
def list_fruits(*fruits):
    """
    List out multiple fruits.
    :param fruits: Variable-length argument list of fruits
    """
    print("Fruits:")
    for fruit in fruits:
        print(f"- {fruit}")

# 5. Variable-Length Keyword Arguments (**kwargs)
def describe_person(**details):
    """
    Describe a person with various attributes.
    :param details: Dictionary of personal attributes (e.g., name, age, city)
    """
    print("Person Details:")
    for key, value in details.items():
        print(f"{key.capitalize()}: {value}")


# Main program to call the functions with various argument types
def main():
    # 1. Positional Arguments
    greet("Alice", "Hello")

    # 2. Keyword Arguments
    display_info(age=25, name="Bob")

    # 3. Default Arguments
    describe_pet("Buddy")         # Uses default pet_type
    describe_pet("Whiskers", "cat")  # Overrides default pet_type

    # 4. Variable-Length Arguments
    list_fruits("Apple", "Banana", "Cherry", "Date")

    # 5. Variable-Length Keyword Arguments
    describe_person(name="Charlie", age=30, city="New York", hobby="painting")


# Run the main function
if __name__ == "__main__":
    main()