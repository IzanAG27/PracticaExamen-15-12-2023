def calculate_score(set):
    score_A, score_B = 0, 0
    serve = 'A'
    for point in set:
        if point == serve:
            if serve == 'A':
                score_A += 1
            else:
                score_B += 1
        else:
            serve = point
        if max(score_A, score_B) >= 9 and abs(score_A - score_B) >= 2:
            break
    return score_A, score_B


def print_score(score_A, score_B):
    print(f'{score_A}-{score_B}')


def squash_score(points):
    sets = points.split('F')[:-1]
    for set in sets:
        score_A, score_B = calculate_score(set)
        print_score(score_A, score_B)


num_games = int(input())
for _ in range(num_games):
    points = input()
    squash_score(points)
