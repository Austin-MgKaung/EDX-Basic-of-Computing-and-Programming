def main():
    print('Please enter two numbers, on two separate lines:')
    num1 = input()
    num2 = input()
    sum = num1 + num2
    print(type(sum))
    print(sum)
    sum_1 = int(num1) + int(num2)
    print(type(sum_1))
    print(sum_1)
    output_sentence = f' {num1} + {num2} = {sum_1}'
    print(output_sentence)
    print('abc', 'def', 'ghi')
    print('abc', 3, 'def', 6, "ghi")


if __name__ == "__main__":
    main()
