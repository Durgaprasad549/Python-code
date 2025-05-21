'''s With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]

Output: (examples)

1) input a = 1, then output: 1

2) input a = 2, then output: 1,3

3) input a = 3, then output: 1, 3, 5

4) input a = 4, then output: 1, 3, 5, 7

5) input a = x, then output: 1, 3, 5, 7, .......'''

def generate_oddseries(n: int):
    
    return [str(2*i + 1) for i in range(n)]

if __name__ == "__main__":
    try:
        a = int(input("Enter a positive integer: "))
        if a < 1:
            raise ValueError("Input must be a positive integer.")
        series = generate_oddseries(a)
        print(", ".join(series))
    except Exception as e:
        print(f"Error: {e}")

