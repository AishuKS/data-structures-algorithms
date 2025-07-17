height = [4, 1, 4, 10]
width = [6, 2, 5, 12]
length = [7, 3, 6, 32]

n = len(length)
rotations = []
cuboids = []

for i in range(n):
    cuboids.append([length[i], width[i], height[i]])

for l, w, h in cuboids:
        rotations.append([max(w, l), min(w, l), h])  # base: w x l, height: h
        rotations.append([max(h, l), min(h, l), w])  # base: h x l, height: w
        rotations.append([max(h, w), min(h, w), l])  # base: h x w, height: l
rotations.sort(reverse=True)
n = len(rotations)
maxSize = [rotations[i][-1] for i in range(n)]
result = [0] * n

for i in range(1,n):
    for j in range(i):
        if rotations[j][0] > rotations[i][0] and rotations[j][1] > rotations[i][1]:
            maxSize[i] = max(maxSize[j]+rotations[i][-1], maxSize[i])

print(max(maxSize))