def create_to_do(bestand, user_input):
    with open(bestand, "a") as file_data:
        file_data.write(f"{user_input}\n")


def show_all_to_do(bestand):
    with open(bestand, "r") as file_data:
        counter = 0
        for lines in file_data:
            counter += 1
            print(f"{counter}. {lines}")


def delete_to_do(bestand, gebruikers_input):
    with open(bestand, "r") as file_data:
        lines = file_data.readlines()
        if gebruikers_input <= len(lines):
            del lines[gebruikers_input - 1]
        else:
            print("De lijn bestaat niet")
        with open(bestand, "w") as bestand_data:
            for line in lines:
                bestand_data.write(line)


def main():
    print("Welcome to the To-Do List app!")
    app_draait = True
    while app_draait:
        print("1. Add something to my list\n"
              "2. Laat alle to-do list zien\n"
              "3. Verwijder to-do")

        keuze = int(input("Voer uw keuze in: "))
        bestand = "to-do_list.txt"
        if keuze == 1:
            user_input = input("Voer uw To-do list in: ")
            create_to_do(bestand, user_input)
            print(f"Uw heeft ({user_input}) toegevoegd aan uw to-do list\n")
        elif keuze == 2:
            print("Hier onder kunt u alle To-do list vinden:")
            show_all_to_do(bestand)
        elif keuze == 3:
            gebruikers_input = int(input("Welke? "))
            delete_to_do(bestand, gebruikers_input)


if __name__ == '__main__':
    main()
