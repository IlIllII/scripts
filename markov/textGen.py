import random


PREFIX_LENGTH = 2
NUM_WORDS = 100
FILENAME = "text.txt"
NONWORD = "\n"


def make_starting_prefix_array(n: int = PREFIX_LENGTH) -> list:
    return [NONWORD] * n


def make_key(*args) -> str:
    return "".join(args)


def construct_prefix_map(filename: str) -> dict:
    prefix_map = dict()
    prefixes = make_starting_prefix_array()
    with open(filename) as f:
        for line in f.readlines():
            words = line.split()
            for word in words:
                prefix_map[make_key(*prefixes)] = prefix_map.get(make_key(*prefixes), []) + [word]
                prefixes[:-1] = prefixes[1:]
                prefixes[-1] = word
    prefix_map[make_key(*prefixes)] = prefix_map.get(make_key(*prefixes), []) + [NONWORD]
    return prefix_map


def generate_text(n: int, prefix_map: dict) -> None:
    prefixes = make_starting_prefix_array()
    for _ in range(n):
        suffixes = prefix_map[make_key(*prefixes)]
        word = random.choice(suffixes)
        print(word, end=" ")
        if word == NONWORD:
            prefixes = make_starting_prefix_array()
        prefixes[:-1] = prefixes[1:]
        prefixes[-1] = word


if __name__ == "__main__":
    prefix_map = construct_prefix_map(FILENAME)
    generate_text(NUM_WORDS, prefix_map)