

def ask_question(question, ans_a, ans_b, ans_c, ans_d, correct_ans):
    # ask a question and return True if ans is correct, else False

    print('\n' + question)
    print('a. {a}\nb. {b}\nc. {c}\nd. {d}'.format(
        a = ans_a,
        b = ans_b,
        c = ans_c,
        d = ans_d
    ))

    ans = ''
    while ans not in 'a b c d'.split():
        ans = input('\nEnter answer (a/b/c/d): ').lower()
    
    return ans == correct_ans.lower()


def change_score(correct):
    # increase the score id correct 

    global score
    
    if correct:
        print('\nCorrect answer, you get 1 point.')
        score += 1
    else:
        print('\nWrong answer, you lost 1 point.')
        score -= 1

    print('Current score: {s}'.format(
        s = score
    ))


def ask_questions(q_list):
    for q in q_list:
        res = ask_question(*q)
        change_score(res)

    print('\nFinal score: {s}'.format(
        s = score
    ))


def welcome():
    name = input('What\'s your name: ')
    print('Hello {n}, welcome to the quiz.'.format(
        n = name
    ))


questions = [
        ['What is Python?', 'A programing language', 'A plant', 'A color', 'None of the above', 'a'],
        ['What is 1 + 1?', '1', '2', '3', '4', 'b']
    ]

score = 0


def main():
    welcome()
    ask_questions(questions)

if __name__ == '__main__':
    main()