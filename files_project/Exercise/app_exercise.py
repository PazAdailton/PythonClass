"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

open_questions = open('questions.txt', 'r')
read_questions = open_questions.readlines()
open_questions.close()

asks = []
answers_txt = []

for linha in read_questions:
    ask = linha.split("=")[0] + "="
    answer = linha.split("=")[1].strip()
    asks.append(ask)
    answers_txt.append(answer)

answers_user = []
for ask in asks:
    input_answer = input(f"{ask}")
    try:
        answer_user = int(input_answer)
        answers_user.append(answer_user)
    except ValueError:
        print('Enter correct number')
        break

if len(answers_user) != len(asks):
    print("You did not answer all questions.")
    exit()

rights = 0

for i in range(len(asks)):
    if answers_user[i] == int(answers_txt[i]):
        rights += 1

answer_format = f"Your final score is {rights}/{len(asks)}."
open_result_txt = open('result.txt', 'w')
write_result_txt = open_result_txt.write(answer_format)
open_result_txt.close()




''''
# read from questions.txt and append each line into a list
questions = open("questions.txt", "r")  # read from questions.txt
 
# read all lines and get rid of line break for each line, then append each stripped line to a list
question_list = [line.strip() for line in questions]
questions.close()
 
score = 0  # initialize score
total = len(question_list)  # set total score
 
for line in question_list:
    # split equation with `=` into question and answer
    q, a = line.split("=")
 
    # print question and wait for user to input their answer
    ans = input(f"{q}=")
 
    if a == ans:  # if user input matches answer
        score += 1  # increase score
 
result = open("result.txt", "w")  # open result.txt
# write final score to result.txt
result.write(f"Your final score is {score}/{total}.")
result.close()



'''




