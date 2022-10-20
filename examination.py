def main():
    file_solution = open('student_solution.txt', 'r')
    file_grade = open('grade_result.txt', 'r')
    grade = []
    grade_user = []
    for i in file_solution:
        i = i.rstrip('\n')
        grade.append(i)
    print(grade)
    for i in file_grade:
        i = i.rstrip('\n')
        grade_user.append(i)
    print(grade_user)
    ball = 0
    question = []
    for num in range(20):
        if grade[num] != grade_user[num]:
            ball += 1
            question.append(num + 1)
    if ball > 5:
        print(f" You didn't pass the exam. You do error in answer: {question} ")
    else:
        print(f'You do {ball} error')
        print(f'You do error in answer: {question}')


if __name__ == '__main__':
    main()
