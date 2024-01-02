import random
import argparse
from termcolor import colored
from termcolor import cprint

def print_cat(mood):
    cats = {
        'happy': r'''
         /\_/\
        ( o.o )
         > ^ <
        ''',
        'cross_eyed': r'''
         /\_/\
        ( x.x )
         > ^ <
        ''',
        'bored': r'''
         /\_/\
        ( -.- )
         >   <
        ''',
        'angry': r'''
         /\_/\
        ( >_< )
         >   <
        '''
    }
    print(cats[mood])

def generate_multiplication_table(number, range_limit):
    table = []
    for i in range(1, range_limit + 1):
        table.append(f"{number} x {i} = {number * i}")
    return table

def list_multiplication_tables_to_file(filename, range_limit, num_tables):
    with open(filename, 'w') as file:
        for number in range(1, num_tables + 1):
            table = generate_multiplication_table(number, range_limit)
            file.write(f"{number} times table (to {range_limit}):\n")
            for line in table:
                file.write(f"{line}\n")
            file.write("\n")

def quiz_multiplication_tables(range_limit, total_questions, metrics_file):
    print(f"Welcome to Marta's Multiplication Table Quiz (Up to {range_limit}): (-h for help)\n")
    correct_answers = 0
    total_questions_asked = 0
    score_details = {str(i): {'correct': 0, 'questions_asked': 0} for i in range(1, range_limit + 1)}
    current_difficulty = range_limit  # Start with the highest difficulty
    
    while total_questions_asked < total_questions:
        number = random.randint(1, current_difficulty)
        table = generate_multiplication_table(number, range_limit)
        question = random.choice(table)
        
        #print(f"What is {question.split('=')[0]}?")
        #cprint(f"What is {question.split('=')[0]}?", attrs=['bold'])
        print(f"What is \033[1m{question.split('=')[0]}?\033[0m")
        user_answer = input("Your Answer: ")
        
        expected_answer = question.split('=')[1].strip()
        if user_answer == expected_answer:
            #print("Correct!\n")
            print(colored("Correct!\n", "green"))
            correct_answers += 1
            score_details[str(number)]['correct'] += 1
        else:
            #print(f"Wrong! The correct answer is {expected_answer}\n")
            print(colored(f"Wrong! The correct answer is \033[1m{expected_answer}\033[0m\n", "red"))
            learncounter = 0
            while(learncounter < 3):
                learncounter +=1
                print(f"\tagain - \033[1m{question.split('=')[0]}?\033[0m")
                user_answer = input("\tYour Answer: ")
                expected_answer = question.split('=')[1].strip()
                if user_answer != expected_answer:
                    print(colored(f"\tWrong! It's \033[1m{expected_answer}\033[0m\n", "red"))
                    learncounter =0
            print("\n")
        
        # Update score details
        score_details[str(number)]['questions_asked'] += 1
        
        # Increment the total questions asked
        total_questions_asked += 1
        
        # Adjust difficulty based on performance after every question
        if correct_answers / total_questions_asked >= 0.6:
            current_difficulty = min(range_limit, current_difficulty + 1)
        else:
            current_difficulty = max(2, current_difficulty - 1)


        score_percentage = (correct_answers / total_questions) * 100
        # Debugging: Print current difficulty
        if(args.debug !=0):
            print(f"Current Difficulty: {current_difficulty}/{range_limit} (correct answers: {correct_answers}, total questions asked: {total_questions_asked} total questions {total_questions})\n")
    
    print(f"You got {correct_answers} out of {total_questions} questions correct!")
    final_score = (correct_answers / total_questions) * 100
    print(f"Your final score: {final_score:.2f}%\n")
    
    # Display a cat based on performance
    if score_percentage >= 80: print_cat('happy')
    elif score_percentage >= 50: print_cat('bored')
    elif score_percentage >= 20: print_cat('cross_eyed')
    else: print_cat('angry')

    # Append score details to the specified metrics file
    with open(metrics_file, 'a') as score_file:
        score_file.write("Test Summary:\n")
        score_file.write(f"Total Questions: {total_questions}\n")
        score_file.write(f"Final Score: {final_score:.2f}%\n")
        score_file.write("Multiplication Table Learning Metrics:\n")
        for table_number, details in score_details.items():
            questions_asked = details['questions_asked']
            correct = details['correct']
            percentage = (correct / questions_asked) * 100 if questions_asked > 0 else 0
            score_file.write(f"Table {table_number}: {percentage:.2f}% correct ({correct}/{questions_asked} questions)\n")
        score_file.write("\n")
        score_file.write("\n")  # Add an extra newline to separate summaries for different tests

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Multiplication Table Quiz and Table Generator')
    parser.add_argument('-s', '--save', help='Save multiplication tables to a text file (e.g., multiplication_tables.txt)')
    parser.add_argument('-r', '--range', type=int, default=10, help='Number of entries in each table and number of tables')
    parser.add_argument('-n', '--total-questions', type=int, default=10, help='Total number of questions in the quiz')
    parser.add_argument('-m', '--metrics-file', default='score_details.txt', help='File to save learning metrics')
    parser.add_argument('-d', '--debug', type=int, default=0, help='Print extra info during the quiz')
    
    args = parser.parse_args()
    
    if args.save:
        list_multiplication_tables_to_file(args.save, args.range, args.range)
        print(f"{args.range} multiplication tables (up to {args.range} entries each) saved to {args.save}")
    else:
        quiz_multiplication_tables(args.range, args.total_questions, args.metrics_file)
