#!/usr/bin/python3

# print("Hello, world!")


def get_festival_name(day_of_year):
    start_end_festival = [
        [152, 181, "pride"],
        [359, 359, "christmas"],
        [256, 256, "day_of_the_programmer"],
        [166, 166, "national-beer-day"],
        [103, 104, "vaisakhi"],
        # ad infinitum
    ]

    for festival in start_end_festival:
        if festival[0] <= day_of_year <= festival[1]:
            return festival[2]
    return "main"


from datetime import datetime


day_of_year_now = datetime.now().timetuple().tm_yday

logo_filename = " logo-" + get_festival_name(103) + ".svg"
print(logo_filename)
#
# for day in range(1, 366):
#     logo_filename = (
#             str(day) + " logo-" + get_festival_name(day) + ".svg"
#     )
#     print(logo_filename)
