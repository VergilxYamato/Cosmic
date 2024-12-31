import colorama
from colorama import Fore, Style
import webbrowser

colorama.init()

logo = (f"""
{Fore.GREEN}{Style.BRIGHT}
███████╗██╗   ██╗███╗   ██╗
██╔════╝██║   ██║████╗  ██║
█████╗  ██║   ██║██╔██╗ ██║
██╔══╝  ██║   ██║██║╚██╗██║
██║     ╚██████╔╝██║ ╚████║
╚═╝      ╚═════╝ ╚═╝  ╚═══╝
{Style.RESET_ALL}
••••••••••••••••••••••••••••••••••••••••••••••••••{Fore.YELLOW}
  {Fore.GREEN}Author       : ADITYA-NP
  {Fore.YELLOW}GitHub       : VergilxYamato
  {Fore.GREEN}Version      : 5.4
••••••••••••••••••••••••••••••••••••••••••••••••••{Fore.GREEN}""")


def main_menu():
    print(logo)
    print("1. Would You Rather Game")
    print("2. Quiz Game")
    print("3. Developer Info")
    print("4. Exit Tool")
    choice = input("Enter your choice: ")
    if choice == "1":
        would_you_rather_game()
    elif choice == "2":
        quiz_game()
    elif choice == "3":
        developer_info()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please try again.")


def would_you_rather_game():
    print("1. Start Game")
    print("2. Go Back to Main Menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        questions = [
            ("Would you rather be able to fly or be invisible?", ["Fly", "Invisible"]),
            ("Would you rather be able to speak any language or be able to play any instrument?", ["Speak any language", "Play any instrument"]),
            ("Would you rather live in the past, present, or future?", ["Past", "Present", "Future"]),
            ("Would you rather always be too hot or always be too cold?", ["Too hot", "Too cold"]),
            ("Would you rather be able to read minds or be able to control time?", ["Read minds", "Control time"]),
            ("Would you rather have unlimited money or unlimited health?", ["Unlimited money", "Unlimited health"]),
            ("Would you rather be able to teleport anywhere or be able to time travel?", ["Teleport", "Time travel"]),
            ("Would you rather be a superhero or a supervillain?", ["Superhero", "Supervillain"]),
            ("Would you rather live in a world without technology or a world without nature?", ["Without technology", "Without nature"]),
            ("Would you rather be the smartest person in the world or the funniest person in the world?", ["Smartest", "Funniest"]),
            ("Would you rather live in a world without pain or a world without fear?", ["Without pain", "Without fear"]),
            ("Would you rather be able to breathe underwater or be able to hold your breath indefinitely?", ["Breathe underwater", "Hold breath indefinitely"]),
            ("Would you rather always be early or always be late?", ["Always early", "Always late"]),
            ("Would you rather be able to talk to animals or be able to understand any language?", ["Talk to animals", "Understand any language"]),
            ("Would you rather live in a world without colors or a world without sounds?", ["Without colors", "Without sounds"]),
            ("Would you rather be able to control fire or water?", ["Control fire", "Control water"]),
            ("Would you rather live in a world without internet or a world without books?", ["Without internet", "Without books"]),
            ("Would you rather be a famous actor or a famous scientist?", ["Famous actor", "Famous scientist"]),
            ("Would you rather be able to travel to any place in the world or be able to travel to any time period?", ["Travel to any place", "Travel to any time period"]),
        ]

        for question, options in questions:
            print(question)
            if options:
                for i, option in enumerate(options, 1):
                    print(f"{i}. {option}")
            answer = input("Enter your choice: ")
            # Process the answer here (e.g., check if it's valid, provide feedback)

    elif choice == "2":
        main_menu()
    else:
        print("Invalid choice. Please try again.")

def quiz_game():
    print("1. Start")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        difficulty_menu()
    elif choice == "2":
        main_menu()
    else:
        print("Invalid choice. Please try again.")
        
def difficulty_menu():
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    choice = input("Enter your choice: ")
    if choice == "1":
        easy_quiz()
    elif choice == "2":
        medium_quiz()
    elif choice == "3":
        hard_quiz()
    else:
        print("Invalid choice. Please try again.")
        	
def easy_quiz():
    print("Easy Quiz:")
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is the largest country in the world by land area?", "Russia"),
        ("What is the smallest country in the world?", "Vatican City"),
        ("What is the tallest mountain in the world?", "Mount Everest"),
        ("What is the largest ocean in the world?", "Pacific Ocean"),
        ("What is the national animal of India?", "Tiger"),
        ("What is the national bird of the United States?", "Bald Eagle"),
        ("What is the capital of Australia?", "Canberra"),
        ("What is the currency of Japan?", "Yen"),
        ("What is the largest desert in the world?", "Sahara Desert"),
        ("What is the longest river in the world?", "Nile River"),
        ("What is the largest freshwater lake in the world?", "Lake Superior"),
        ("What is the hottest continent on Earth?", "Africa"),
        ("What is the coldest continent on Earth?", "Antarctica"),
        ("What is the largest country in South America?", "Brazil"),
        ("What is the capital of Canada?", "Ottawa"),
        ("What is the national language of Brazil?", "Portuguese"),
        ("What is the national sport of India?", "Cricket"),
        ("What is the capital of Egypt?", "Cairo"),
        ("What is the largest country in Africa?", "Algeria")
    ]

    score = 0
    for question, answer in questions:
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The answer is:", answer)

    print("Your score:", score, "/", len(questions))
    
def medium_quiz():
    print("Medium Quiz:")
    questions = [
        ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
        ("What is the capital of Australia?", "Canberra"),
        ("What is the largest organ in the human body?", "Liver"),
        ("What is the chemical symbol for gold?", "Au"),
        ("In which year did World War II end?", "1945"),
        ("What is the largest country in South America?", "Brazil"),
        ("What is the national animal of India?", "Tiger"),
        ("What is the national bird of the United States?", "Bald Eagle"),
        ("What is the capital of Canada?", "Ottawa"),
        ("What is the national language of Brazil?", "Portuguese"),
        ("What is the national sport of India?", "Cricket"),
        ("What is the capital of Egypt?", "Cairo"),
        ("What is the largest country in Africa?", "Algeria"),
        ("What is the capital of Germany?", "Berlin"),
        ("What is the currency of Japan?", "Yen"),
        ("What is the largest desert in the world?", "Sahara Desert"),
        ("What is the longest river in the world?", "Nile River"),
        ("What is the largest freshwater lake in the world?", "Lake Superior"),
        ("What is the hottest continent on Earth?", "Africa"),
        ("What is the coldest continent on Earth?", "Antarctica")
    ]

    score = 0
    for question, answer in questions:
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The answer is:", answer)

    print("Your score:", score, "/", len(questions))

def hard_quiz():
    print("Hard Quiz:")
    questions = [
        ("What is the largest country in North America by land area?", "Canada"),
        ("What is the national animal of Australia?", "Kangaroo"),
        ("What is the national bird of Mexico?", "Golden Eagle"),
        ("What is the capital of New Zealand?", "Wellington"),
        ("What is the currency of South Korea?", "South Korean Won"),
        ("What is the second largest desert in the world?", "Gobi Desert"),
        ("What is the second longest river in the world?", "Amazon River"),
        ("What is the deepest lake in the world?", "Lake Baikal"),
        ("What is the driest place on Earth?", "Dry Valleys, Antarctica"),
        ("What is the highest mountain in Africa?", "Mount Kilimanjaro"),
        ("What is the largest country in Oceania?", "Australia"),
        ("What is the capital of South Africa?", "Pretoria"),
        ("What is the national language of Spain?", "Spanish"),
        ("What is the national sport of Pakistan?", "Cricket"),
        ("What is the capital of Russia?", "Moscow"),
        ("What is the largest country in Europe by land area?", "Russia")
    ]

    score = 0
    for question, answer in questions:
        print(question)
        user_answer = input("Your answer: ")
        if user_answer.lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The answer is:", answer)

    print("Your score:", score, "/", len(questions))

def developer_info():
        print("Developer Info:")
        print("Name: Aditya Chapagai")
        print("GitHub: VergilxYamato")
        print("Youtube: ADITYA-NP")
        print("Instagram: aditya_chapagai")
        print("Email: adityachapagai@gmail.com")
        print("Number: 9709412405")
        print("Call me if you are a girl")

if __name__ == "__main__":
    main_menu()
