import time

def get_user_answer():
    try:
        return int(input("Your answer (1-4): "))
    except ValueError:
        return None

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")
        return 0

def quiz_game():
    score = 0

    print("1. What is the capital of France?")
    print("1. Berlin\n2. Paris\n3. Madrid\n4. Rome")
    user_answer = get_user_answer()
    score += check_answer(user_answer, 2)

    print("2. Which of the following is not a programming language?")
    print("1. Python\n2. Java\n3. HTML\n4. C++")
    user_answer = get_user_answer()
    score += check_answer(user_answer, 3)

    print("3. What is the output of 2 + 2 in Python?")
    print("1. 3\n2. 4\n3. 22\n4. None of the above")
    user_answer = get_user_answer()
    score += check_answer(user_answer, 2)

    print(f"Quiz finished! Your final score is {score}\n")

if __name__ == "__main__":
    print("\n\nWelcome To My quiz Game\n\n")
    print("\nThe Rules Are Simple There are 3 question if answer is Correct one point is given there is no Negative Marking\n\n")
    time.sleep(5)
    quiz_game()
