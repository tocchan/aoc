import io
import re
import sys
import time
from collections import defaultdict
from copy import deepcopy


import aoc
from utils import time_func

# config
INPUT_FILE = 'day21.input.txt';
REMOVE_LINE_BREAKS = True


# read input
input_sets = aoc.ImportInput(INPUT_FILE, REMOVE_LINE_BREAKS)

foods = []
allergens = []
for input_set in input_sets:
    food_list, allergy_list = input_set.split('(')
    food_list = food_list.strip().split(' ')
    allergy_list = allergy_list[9:-1].split(', ')

    foods.append(set(food_list))
    allergens.append(set(allergy_list))

input_count = len(foods)

# implementation
@time_func
def part01():
    # so, what we're going to do is create 'sets' of foods that share lists
    allergen_map = defaultdict(set)
    total_food_set = set()

    for i in range(input_count):
        allergen_set = allergens[i]
        food_set = foods[i]
        total_food_set = total_food_set.union(food_set)

        for allergen in allergen_set:
            if allergen not in allergen_map:
                allergen_map[allergen] = food_set
            else:
                cur = allergen_map[allergen]
                allergen_map[allergen] = cur.intersection(food_set)

    allergy_food_set = set()
    for key in allergen_map:
        allergen_set = allergen_map[key]
        allergy_food_set = allergy_food_set.union(allergen_set)

    count = 0
    safe_foods = total_food_set - allergy_food_set
    for food_set in foods:
        count += len(food_set.intersection(safe_foods))

    print(f'part01 answer: {count}')
# end part01


@time_func
def part02():
    pass
# end part02


# run the parts
part01()
part02()

