import random

def play_game():
    choices = ["stone", "scissor", "paper"]
    
    print("Гра: Камінь, ножиці, папір")
    print("Доступні варіанти: stone, scissor, paper")
    print("Для виходу введіть 'q'\n")
    
    while True:
        user_choice = input("Ваш хід (stone/scissor/paper): ").strip().lower()
        
        if user_choice == 'q':
            print("Вихід з гри. До побачення!")
            break
            
        if user_choice not in choices:
            print("Помилка: Неправильний вибір. Спробуйте ще раз.\n")
            continue
            
        computer_choice = random.choice(choices)
        print(f"Комп'ютер обрав: {computer_choice}")
        
        if user_choice == computer_choice:
            print("Нічия!\n")
        elif (
            (user_choice == "stone" and computer_choice == "scissor") or
            (user_choice == "scissor" and computer_choice == "paper") or
            (user_choice == "paper" and computer_choice == "stone")
        ):
            print("Вітаю! Ви перемогли!\n")
        else:
            print("Комп'ютер переміг!\n")

if __name__ == "__main__":
    play_game()