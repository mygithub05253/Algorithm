number = int(input())

for _ in range(number):
    string = list(input())
    score = 0
    final_score = 0

    for i in range(len(string)):
        if string[i] == "O":
            score += 1
            final_score += score
        else:
            score = 0

    print(final_score)