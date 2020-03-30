# max 30 levels to print towers OK on my laptop(huawei). It will perform (2^level - 1) recursive calls
levels_total = 5

tower1 = [x for x in range(levels_total, 0, -1)]
tower2 = list()
tower3 = list()


def print_gap():
    for x in range(4):
        print(' ', end='')


def print_stars(number):
    for x in range(number):
        print('*', end='')


def print_spaces(number):
    for x in range(number):
        print(' ', end='')


def print_ground():
    for x in range(199):
        print('%', end='')
    print()


def print_tower_level(tower, level):
    stars = 0
    if len(tower) >= level:
        stars = tower[level - 1]
    spaces = 30 - stars
    print_spaces(spaces)
    print_stars(stars)
    print('|' if stars == 0 else '*', end="")
    print_stars(stars)
    print_spaces(spaces)


def print_towers():
    print(tower1)
    print(tower2)
    print(tower3)
    global levels_total
    for level in range(levels_total, 0, -1):
        print_gap()
        print_tower_level(tower1, level)
        print_gap()
        print_tower_level(tower2, level)
        print_gap()
        print_tower_level(tower3, level)
        print()
    print_ground()


call_counter = 1


def move_plates(levels, from_tower, to_tower, helper_tower):
    global call_counter
    if levels < 1:
        return
    if levels == 1:
        to_tower.append(from_tower.pop())
        print('Call:', call_counter)
        call_counter += 1
        print_towers()
        return
    move_plates(levels - 1, from_tower, helper_tower, to_tower)
    to_tower.append(from_tower.pop())
    print('Call:', call_counter)
    call_counter += 1
    print_towers()
    move_plates(levels - 1, helper_tower, to_tower, from_tower)


print('Before:')
print_towers()

move_plates(len(tower1), tower1, tower3, tower2)
