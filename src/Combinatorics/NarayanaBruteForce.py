def next_permutation(sequence, compare):
    count = len(sequence)
    i = count
    while True:
        if i < 2:
            return False
        i -= 1
        if compare(sequence[i - 1], sequence[i]):
            break
    j = count
    while j > i and not compare(sequence[i - 1], sequence[j - 1]):
        j -= 1
    sequence[i - 1], sequence[j - 1] = sequence[j - 1], sequence[i - 1]
    j = count
    while i < j - 1:
        j -= 1
        sequence[i], sequence[j] = sequence[j], sequence[i]
        i += 1
    return True

def greater(value_0, value_1):
    return value_0 > value_1

count = int(input());
sequence = list(range(1, count + 1))
permutation_found = True
while permutation_found:
    print(sequence)
    permutation_found = next_permutation(sequence, less)