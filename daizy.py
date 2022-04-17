def get_cans():
    cans = []

    input_total_cans = int(input("How many cans do you have? "))
    for can in range(input_total_cans):
        input_can_name = input("What is the name of the can? ")
        cans.append(input_can_name)

    for count, can in enumerate(cans):
        print(count+1, can)

    input_get_can = int(input("Which can do you want to get? "))-1
    print("You got", cans[input_get_can])

# cans = input("name 5 cans in your cupboard:")


# get_cans()

def cat(legs, name):
    legs = legs-1
    return name + " has " + str(legs) + " legs"
    return f"{name} has {legs} legs"
#
# house_of_cats = [
#                  [4, "Garfield"],
#                  [5, "Tom"],
#                  [3, "Puss in Boots"],
#                  [5, "Socks"],
#                  ]
# for this_cat in house_of_cats:
#     print(cat(this_cat[0], this_cat[1]))

legs = input("How many legs does your cat have? ")
name = input("What is its name? ")
print(cat(int(legs), name))
lopped_cat = cat(int(legs), name)
print(lopped_cat/2)