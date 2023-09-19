length = int(input())
width = int(input())
height = int(input())
percent = int(input())

space = length * width * height
space_litres = space / 1000
used_space = 17 / 100

space_litres_remaining = space_litres * (1 - (17 / 100))

print(space_litres_remaining)
