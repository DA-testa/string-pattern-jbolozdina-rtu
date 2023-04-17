# python3

def read_input():
    choice = input().strip()
    if choice == 'F':
        with open("tests/" + input(), 'r') as file:
            pattern, text = file.readlines()
    else:
        pattern = input().strip()
        text = input().strip()

    return (pattern.rstrip(), text.rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def rabin_karp(pattern, text):
    p = 1000000007 # large prime number
    x = 263 # random number
    result = []

    p_hash = 0
    t_hash = 0
    h = 1

    for _ in range(len(pattern) - 1):
        h = (h * x) % p

    for i in range(len(pattern)):
        p_hash = (x * p_hash + ord(pattern[i])) % p
        t_hash = (x * t_hash + ord(text[i])) % p

    for i in range(len(text) - len(pattern) + 1):
        if p_hash == t_hash and text[i:i+len(pattern)] == pattern:
            result.append(i)
        if i < len(text) - len(pattern):
            t_hash = (t_hash - ord(text[i]) * h) % p
            t_hash = (t_hash * x + ord(text[i + len(pattern)])) % p
            t_hash = (t_hash + p) % p

    return result

def get_occurrences(pattern, text):
    return rabin_karp(pattern, text)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
