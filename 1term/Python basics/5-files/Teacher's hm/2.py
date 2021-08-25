with open('2.txt', 'r', encoding='utf-8') as f:
    usefulness = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов ' for line, count in enumerate(f, 1)]
    print(*usefulness, f'всего строк - {len(usefulness)}.', sep='\n')


lines_n = 0
words_n = 0
f = open('2.txt', 'r')
for line in f:
    lines_n += 1
    words = line.split()
    words_n += len(words)
f.close()
print(lines_n)
print(words_n)