n = int(input())

card = [i for i in range(1, n + 1)]

while len(card) > 1:
    print(card.pop(0), end=' ')
    top = card.pop(0)
    card.append(top)

print(card[0])
