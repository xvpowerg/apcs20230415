from statistics import mean
scores=[87,66,90,65,70]
score_sum = 0
counts = len(scores)
score_max = 0
score_min = 100

for i in range(counts):
    print(f"{i+1}.{scores[i]}")
    score_sum += scores[i]
    if scores[i] > score_max:
        score_max = scores[i]
    if scores[i] <  score_min:
        score_min = scores[i]

print(score_sum)
print(score_max)
print(score_min)

print(sum(scores))
print(max(scores))
print(min(scores))
print(mean(scores))
