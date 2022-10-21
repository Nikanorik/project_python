def main():
    score1 = int(input('Enter score1: '))
    score2 = int(input('Enter score2: '))
    score3 = int(input('Enter score3: '))
    score4 = int(input('Enter score4: '))
    score5 = int(input('Enter score5: '))
    average_score = calc_average(score1,score2,score3,score4,score5)
    print(f'Score\tGrade')
    print(f'{score1}\t\t{determine_grade(score1)}')
    print(f'{score2}\t\t{determine_grade(score2)}')
    print(f'{score3}\t\t{determine_grade(score3)}')
    print(f'{score4}\t\t{determine_grade(score4)}')
    print(f'{score5}\t\t{determine_grade(score5)}')
    print(f'Average grade = {calc_average(score1,score2,score3,score4,score5)}')
    print(f'Average grade average score = {determine_grade(average_score)}')
def calc_average(s1,s2,s3,s4,s5):
    return  (s1+s2+s3+s4+s5)/5
def determine_grade(score):
    if score>=90:
        return 'A'
    elif 80<score<=89:
        return 'B'
    elif 65<score<=79:
        return 'C'
    else:
        return 'D'
main()









