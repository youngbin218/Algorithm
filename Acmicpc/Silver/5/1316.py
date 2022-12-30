n = int(input())
words = []
cnt = 0


def group_word(word):
    bag_word = {}
    prev_w = ''
    for w in word:
        if w not in bag_word:
            bag_word[w] = 1
        else:
            if prev_w != w:
                return 0
        prev_w = w
    return 1


for i in range(n):
    word = list(input())
    words.append(word)

for idx in range(n):
    cnt += group_word(words[idx])

print(cnt)
