# A next step for "Hello World"

from time import sleep

x = 0
x_limit = 10
limit = False

while True:
    print(f"Hello, {x}! Limit is currently {limit}")

    if x >= x_limit:
        limit = True

    if x <= ~ x_limit + 1:
        limit = False

    if limit is True:
        x -= 1
    else:
        x += 1

    sleep(0.5)

