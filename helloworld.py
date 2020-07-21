# A next step for "Hello World"

from time import sleep

x = 0
x_limit = 100
limit = False

while True:

    if limit:
        x -= 1

    else:
        x += 1

    if x >= x_limit:
        limit = True

    if x <= ~ x_limit + 1:
        limit = False

    print(f"Hello floor {x}!")
    sleep(1)
