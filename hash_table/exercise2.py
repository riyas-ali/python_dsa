word_count = {}
with open("poem.txt", "r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            tokan = token.replace('\n', '')
            if tokan in word_count:
                word_count[tokan] += 1
            else:
                word_count[tokan] = 1
print(word_count)
print(word_count['diverged'])
print(word_count['in'])
print(word_count['I'])