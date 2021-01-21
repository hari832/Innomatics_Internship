if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores=student_marks[query_name]
    total=sum(student_marks[query_name])
    ave=total/len(query_scores)
    print("%.2f"%ave)
