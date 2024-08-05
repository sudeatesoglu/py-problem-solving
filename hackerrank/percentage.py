# https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    query_scores = student_marks[query_name]

    query_score_sum = 0
    for score in query_scores:
        query_score_sum += score

    query_score_average = query_score_sum / len(query_scores)

    print('%.2f' % query_score_average)
