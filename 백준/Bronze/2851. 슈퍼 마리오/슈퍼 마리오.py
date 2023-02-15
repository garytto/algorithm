coin = []
for i in range(10):
    coin.append(int(input()))

score = 0
for j in coin:
    score += j
    if score >= 100:
        if (score - 100) > (100 - (score - j)):
            score -= j
        break
print(score)