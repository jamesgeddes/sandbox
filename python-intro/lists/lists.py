# the new concept for you this week is...
# *Lists*
# sometimes we might want to store many values in a variable, called a list. a list can contain any data, including numbers, strings and even other lists, which is called a nested list. Given infinite memory, you could have infinitely nested lists - a list in a list in a list (forever). For example, sometimes we might have a value that hard to calculate, so it would be more efficient to store and retrieve it, than to re-calculate it each time. Side note, some other programming languages also call this an array.
#
# *Challenge*
# - generate a list of the first 1000000 prime numbers
# - using an infinite loop to request user input, output the nth value in the list

# Initialize a list
# primes = []
# for possible_prime in range(0, 10000000):
#
#     # Assume number is prime until shown it is not.
#     is_prime = True
#     for num in range(2, possible_prime):
#         if possible_prime % num == 0:
#             is_prime = False
#
#     if is_prime:
#         primes.append(possible_prime)
#
# while True:
#     user_selection = input("Select a prime: ")
#     user_selection = int(user_selection)
#
#     print("Prime number " + str(user_selection) + " is: " + str(primes[user_selection]))



### basic value check
# can_names = []
# can_count = int(input("How many cans do you have in your cupboard? "))
#
# for can in range(can_count):
#     can_names.append(input("Can " + str(can+1) + " name: "))
#
# while True:
#     user_can = int(input("Which can number do you want? "))
#
#     if user_can > can_count:
#         print("I don't have that many cans")
#     elif user_can < 1:
#         print("No *can* do!")
#     else:
#         print("Here is your " + can_names[user_can-1])


### Catch errors! ###
# while True:
#     user_input = input("Data: ")
#     try:
#         user_input = int(user_input)
#     except ValueError:
#         print("Need an integer")
#     except:
#         print("Something went wrong")


### with try-except
# can_names = []
# while True:
#     can_count = input("How many cans do you have in your cupboard? ")
#     try:
#         can_count = int(can_count)
#     except ValueError:
#         print("Need an integer")
#     else:
#         break
#
# for can in range(can_count):
#     can_names.append(input("Can " + str(can + 1) + " name: "))
#
# print("\n\nThanks! I got all your cans!\n\n")
# print("Enter x at any time to exit.")
# while True:
#     user_can = input("Which can number do you want? ")
#
#     if user_can == "x":
#         print("Good bye!")
#         raise SystemExit
#
#     try:
#         user_can = int(user_can)
#     except ValueError:
#         print("Need an integer\n")
#         continue
#     except:
#         print("uncaught exception: Something went wrong\n")
#         continue
#     if user_can > can_count:
#         print("I don't have that many cans\n")
#     elif user_can < 1:
#         print("No *can* do!\n")
#     else:
#         print("Here is your " + can_names[user_can - 1] + "\n")

### look up index
# can_names = []
# while True:
#     can_count = input("How many cans do you have in your cupboard? ")
#     try:
#         can_count = int(can_count)
#     except ValueError:
#         print("Need an integer")
#     else:
#         break
#
# for can in range(can_count):
#     can_names.append(input("Can " + str(can + 1) + " name: "))
#
# print("\n\nThanks! I got all your cans!\n\n")
# print("Enter x at any time to exit.")
# while True:
#     user_can = input("Which can do you want? ")
#
#     if user_can == "x":
#         print("Good bye!")
#         raise SystemExit
#     try:
#         print("Your " + user_can + " can is at position " + str(can_names.index(user_can)) + "\n")
#     except ValueError:
#         print("You don't have that can, please try again\n")
#     except:
#         print("Unhandled exception")


## both index and search with error handling


def lookup_index(names, value: int):
    try:
        return names[value]
    except IndexError:
        return -1


def lookup_value(names: list, value: str):
    try:
        return names.index(value)
    except ValueError:
        return -1


def is_int(value):
    try:
        out = int(value)
        return [True, out]
    except:
        return [False, value]


def get_int():
    while True:
        count = input("Integer: ")
        try:
            can_count = int(count)
            return can_count
        except ValueError:
            print("Need an integer")


def tubby_bi_bi():
    confirm = input("Are you sure? y/n: ")
    if confirm == "y":
        print("Good bye!")
        raise SystemExit
    else:
        return 0


def main():
    can_names = []
    print("How many cans do you have in your cupboard?")
    can_count = get_int()
    for can in range(can_count):
        can_names.append(input("Can " + str(can + 1) + " name: "))

    print("\n\nThanks! I got all your cans!\n\n")
    print("\n\nPlease tell me which can you would like.\nEnter x at any time to exit.")
    while True:
        user_can = input("Can: ")

        if user_can == "x":
            tubby_bi_bi()
            print("\n")
            continue

        can = is_int(user_can)
        if can[0] is True:
            if can[1] <= 0:
                print("Please enter a positive position number\n")
                continue
            this_can_name = lookup_index(can_names, can[1] - 1)
            if this_can_name == -1:
                print("I don't have that many cans" + "\n")
            else:
                print("Your can in position " + str(can[1]) + " is " + str(this_can_name) + "\n")

        if can[0] is False:
            this_can_index = lookup_value(can_names, can[1])
            if this_can_index == -1:
                print("I don't have that can" + "\n")
            else:
                print("Your can of " + str(can[1]) + " is in position " + str(this_can_index + 1) + "\n")


main()
