def square(x):
    return x * x


def cube(x):
    return x * x * x

# f = square
#
# print(square)
# print(f(5))


def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])
cubes = my_map(cube, [1, 2, 3, 4, 5])

print("SQUARES", squares)
print("CUBES", cubes)
