# output_numbers.py

def output_numbers(start, end):
    """
    Outputs numbers from start to end (inclusive).

    Args:
        start (int): The starting number.
        end (int): The ending number.
    """
    for num in range(start, end + 1):
        print(num)

if __name__ == "__main__":
    output_numbers(1, 100)
