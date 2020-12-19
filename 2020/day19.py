import io
import re
import sys
import time
from copy import deepcopy

import aoc
from utils import time_func

# config
INPUT_FILE = 'day19.input.txt';
REMOVE_LINE_BREAKS = True


# read input
file_text = ""
with open(INPUT_FILE, 'r') as input_file:
    file_text = input_file.read()

lines = file_text.splitlines(False)
rule_texts = []
inputs = []

line_count = len(lines)
line_idx = 0
longest_line = 0
while line_idx < line_count:
    line = lines[line_idx]
    if not line:
        break;
    rule_texts.append(line)
    line_idx += 1

line_idx += 1
while line_idx < line_count:
    line = lines[line_idx]
    inputs.append(line)
    longest_line = max(len(line), longest_line)
    line_idx += 1

def to_sequence(text_val):
    if text_val.isdigit():
        return int(text_val)
    else:
        return text_val.replace('"', '')

rules = {}
a_rule = -1
b_rule = -1

rule_texts.append('8: 42 | 42 8')
rule_texts.append('11: 42 31 | 42 11 31')
for rule_text in rule_texts:
    key, branches = rule_text.split(':', 1)
    ikey = int(key)
    branches = branches.split('|')

    rule_seq = []
    for branch in branches:
        sequence = [to_sequence(s) for s in branch.strip().split(' ')]
        if sequence == ['a']:
            a_rule = ikey
        elif sequence == ['b']:
            b_rule = ikey
        rule_seq.append(sequence)

    rules[ikey] = rule_seq


# implementation

def permute(set0, set1, max_len):
    if len(set0) == 0:
        return set1
    elif len(set1) == 0:
        return set0

    values = []
    for i in set0:
        for j in set1:
            new_item = i + j
            if len(new_item) <= max_len and new_item not in values:
                values.append(new_item)
    return values


# rules is a map to potential sequences
# inputs are the inputs at the bottom of the file
def generate_sequences(key, max_len):
    sequences = rules[key]
    values = []
    if max_len <= 0:
        return values

    for sequence in sequences:
        options = []
        cnt = 0
        seq_len = len(sequence)
        for item in sequence:
            if isinstance(item, int):
                next_sequences = generate_sequences(item, max_len - (seq_len - 1))
                options = permute(options, next_sequences, max_len)
            else:
                options = permute(options, [item], max_len)
            cnt += 1

        values += options

    return values


def rule_is_valid(seq, rule_seq):
    if len(seq) < len(rule_seq):
        return False

    # try all combinations of the following rules
    # if there is only one rule, fall down to it
    seq_len = len(seq)
    rule_count = len(rule_seq)
    if rule_count == 1:
        return sequence_is_valid(rule_seq[0], seq)

    # if there are multiple rules, try every possible split of our input
    max_len = seq_len - (rule_count - 1)
    for i in range(1, max_len + 1):
        if sequence_is_valid(rule_seq[0], seq[:i]) and rule_is_valid(seq[i:], rule_seq[1:]):
            return True
    return False


def sequence_is_valid(key, seq):
    if not isinstance(key, int):
        return key == seq

    # empty string means done
    if not seq:
        return False

    # okay, split my sequence evenly over the search space
    rule = rules[key]
    for rule_seq in rule:
        if rule_is_valid(seq, rule_seq):
            return True
    return False





# valid_sequences = generate_sequences(0, longest_line)
# print(f'Sequences Generated: {len(valid_sequences)}')

# valid_map = {}
# for item in valid_sequences:
#    valid_map[item] = True

@time_func
def part01():
    count = 0
    total = len(inputs)
    for i, seq in enumerate(inputs):
        print(f'Checking sequence {i + 1}/{total}: {seq}')
        if sequence_is_valid(0, seq):
            print('-passed')
            count += 1
        else:
            print('-failed')

    print(f'part01 answer: {count}')
# end part01


@time_func
def part02():
    pass
# end part02


# run the parts
part01()
part02()

