def notes():
    """
    multi line comment
    This is special because if you put it right beneath a function it wil act as a descriptor of the function.
    """
    # single line comment
    pass

# tuple is like a list, but it cant be changed at all. and its represented with tuple_var_1 = (variable1, variable2)

def convert_temperatures(temp: float, unit: str) -> tuple[float | None, str]:
    """
    Objective:
        Convert temperature betweeen Celsius and Fahrenheit

    What it needs to run:
        Params:
            temp (float): The temperature value to convert
            unit (str): 'C' for Celsius to Fahrenheit. 'F' for Fahrenheit to Celsius

    What it returns:
        Returns:
            tuple()
            float: The converted Temperature
            str: Error messge if input is invalid, or a str of information

    """

    # This is called a try-except block

    try:
        # do what is found here
        # declare your variables for use with type
        checked_temp: float = float(temp)
        result: float

        # convert based on unit
        # .upper() convert the string to uppercase
        # == -> comparison operator that asks if left side is equal to right side
        if unit.upper() == "C":
            # Celsius to Fahrenheit
            # * -> multiplication
            result = (checked_temp * 9/5) + 32
            return round(result, 2), f"{checked_temp}C => {round(result, 2)}F" 
        elif unit.upper() == "F":
            # Fahrenheit to Celsius
            result = (checked_temp - 32) * 5/9
            return round(result, 2), f"{checked_temp}F => {round(result, 2)}C"
        else:
            # You cannot have double quotes in double quotes or single quotes in single quotes
            # you can only have single quotes in double quotes and vice versa
            return None, "Invalid unit: Use 'C' or 'F'"
        
    except Exception as e:
        # and if there is any type of error or issue, then run this code here
        # f"" -> This is known as an f string; what it does is it allows you to insert variables into a string
        return None, f"Invalid temperature value! Please enter a number. The offical error thrown was: {e}"
    
def main():
    # display a welcome message
    print("Welcome to the Temperature Converter 3000\n\n")
    try:
        # gather inputs. 1. temp input 2. the unit input
        temp_input: float = float(input("Enter temperature value:\t"))
        unit_input: str = input("Enter unit (C for Celsius, F for Fahrenheit):\t")
    except Exception as e:
        print(e)
        return None

    result, message = convert_temperatures(temp_input, unit_input)
    print(result)
    print(message)

if __name__ == "__main__":
    # run the interactive terminal app
    main()