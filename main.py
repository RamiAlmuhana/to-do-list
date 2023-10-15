def create_to_do(bestand, user_input):
    with open(bestand, "a") as file_data:
        file_data.write(f"{user_input}\n")


def show_all_to_do(bestand):
    # database = []
    with open(bestand, "r") as file_data:
        # test = file_data.readlines()
        for lines in file_data:
            print(lines)


def main():
    print("Welcome to the To-Do List app!\n"
          "1. Add something to my list\n"
          "2. Laat alle to-do list zien")
    keuze = int(input("Voer uw keuze in: "))
    bestand = "to-do_list.txt"
    if keuze == 1:
        user_input = input("Voer uw To-do list in: ")
        create_to_do(bestand, user_input)
        print(f"Uw heeft ({user_input}) toegevoegd aan uw to-do list\n")
    elif keuze == 2:
        print("Hier onder kunt u alle To-do list vinden:")
        show_all_to_do(bestand)


if __name__ == '__main__':
    main()
