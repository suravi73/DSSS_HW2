import random

def generate_random_no(min, max):
    """
    Random integer.
    """
    return random.randint(min, max) # Returns: A random integer within the specified range.


def select_operator():
    return random.choice(['+', '-', '*']) #  Returns: str: randomly selected operator.


def calculate(num1, num2, operator): # Generate a math problem and calculate the answer.
   
    problem = f"{num1} {operator} {num2}"
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-': 
        answer = num1 - num2
    else: 
        answer = num1 * num2
    return problem, answer      # Returns:  A tuple containing the math problem string and the calculated answer.

def math_quiz():
    score = 0 # Initialize the score variable to 0
    t_q = 3 # The total number of quiz questions 

    print(f" \n Welcome to the Math Quiz Game! \n ")
    print(f" You will be presented with math problems, and \n you need to provide the correct answers.")

    for _ in range (t_q):
        # Generate random numbers and operator using generate_random_no() and select_operator()
        num_1 = generate_random_no(1, 10); 
        num_2 = generate_random_no(1, 5); 
        o = select_operator()

        # Generate the problem and answer using calculate()
        PROBLEM, ANSWER = calculate(num_1, num_2, o)  
        
        # Display the quiz problem to the user
        print(f"\nQuestion: {PROBLEM}")

        # Get the user's answer
        useranswer = input("Your answer: ") 
        useranswer = int(useranswer)

        # Check if the user's answer is correct
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1  # Increment the score by 1 for a correct answer
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")
            
    # Display the final score at the end of the quiz
    print(f"\nGame over! Your score is: {score}")

if __name__ == "__main__":
    math_quiz()
