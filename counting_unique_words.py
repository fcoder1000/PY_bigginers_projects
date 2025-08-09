from collections import Counter

text = input('Write a text: \n')

counter = Counter(text.split())

for word, count in counter.items():
    print(f'{word}: {count}')