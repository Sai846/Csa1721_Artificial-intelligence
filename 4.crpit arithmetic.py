from itertools import permutations

def solve_cryptarithmetic(puzzle):
    words = puzzle.split()
    unique_chars = set("".join(words))
    if len(unique_chars) > 10:
        print("Invalid puzzle: More than 10 unique characters.")
        return

    for perm in permutations("0123456789", len(unique_chars)):
        mapping = dict(zip(unique_chars, perm))
        if "0" in mapping.values() and any(mapping[word[0]] == "0" for word in words):
            continue

        expression = " ".join("".join(mapping[char] for char in word) for word in words)
        if eval(expression.replace(" ", "")):  # Removing spaces before evaluation
            print("Solution found:")
            for word in words:
                print(word, "=", "".join(mapping[char] for char in word))
            return

    print("No solution found.")

# Example usage:
puzzle = "SEND + MORE = MONEY"
solve_cryptarithmetic(puzzle)
