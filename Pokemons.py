pokemons = {
    "pikachu": {"Type": "electric", "Level": 10},
    "charmander": {"Type": "fire", "Level": 8},
    "raichu": {"Type": "electric", "Level": 20},
}

bag = {"pocion": 3, "pokeball": 5, "superpocion": 2}


def Pokedex():
    # menu de inicio
    while True:
        try:
            n = int(
                input(
                    "\n1) Search Pokemon"
                    "\n2) Types"
                    "\n3) Backpack"
                    "\n4) Register Pokemon"
                    "\n5) Exit"
                    "\n- "
                )
            )

            if n == 1:
                searchPokemon()
            elif n == 2:
                types()

            elif n == 3:
                backpack()

            elif n == 4:
                registerPokemon()

            elif n == 5:
                print("Exiting the system.")
                break
            else:
                print("Choose one of the options.")
        except ValueError:
            print("It must be a whole number. ")


def searchPokemon():
    # Pokémon search function
    print("--- Pokémon Finder ---")
    i = input("\n Which Pokémon do you want to look for?" "\n- ").lower().strip()
    if i in pokemons:
        print("--- POKEMON FOUND --- ", f"\n{i} ")
        for j in pokemons[i]:
            print(f"{j}:", pokemons[i][j])
    else:
        print("That Pokémon was not found.")


def types():
    # funcion de tipos
    found = False
    type = input("What type of Pokémon are you looking for?" "\n- ").lower().strip()
    for i in pokemons:
        if type == pokemons[i]["Type"]:
            if not found:
                print("--- POKEMONS FOUND ---")
            found = True
            print(i)

    # in case the Pokémon type has not been found
    if not found:
        print("--- POKEMONS NOT FOUND ---")


def backpack():
    print("--- ACCESSING THE BACKPACK ---")
    if bag:
        for i in bag:
            print(f"{i}:", bag[i])
    else:
        print("There are no items in the backpack.")


def registerPokemon():
    print("--- REGISTER NEW POKEMON ---")
    new = input("nombre del nuevo pokemon").lower().strip()
    if new in pokemons:
        print("ya existe ese pokemon")

    type = input("cual es su tipo")

    nivel = int(input("cual es su nivel"))


def main():
    Pokedex()


if __name__ == "__main__":
    main()
