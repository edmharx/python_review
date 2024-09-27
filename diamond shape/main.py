#ask the width size
#only integer number must be accepted
# create the function
#upper first -  same as to how to create a pyramid
#lower part next - create a inverse pyramid

width = int(input("Type the desired width of the diamond"))

def print_diamond(width):
        if width % 2 == 0:
            print("Please provide an odd integer")
        elif width < 0:
            print("Type positive odd integer")
        else:
            for i in range(width // 2 + 1):
                print(' ' * (width // 2 - i),end = '')
                print('*' * (2 * i + 1))

print_diamond(width)