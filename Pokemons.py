pokemons = {
    "pikachu": {"Type": "electric", "Level": 10},
    "charmander": {"Type": "fire", "Level": 8},
    "raichu": {"Type": "electric", "Level": 20},
}


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
    print("--- SEARCHING BACKPACK ---")


def registerPokemon():
    print("--- SEARCHING TYPES ---")


def main():
    Pokedex()


if __name__ == "__main__":
    main()
