pokemons = {
    "pikachu": {"type": "electric", "level": 10},
    "charmander": {"type": "fire", "level": 8},
    "raichu": {"type": "electric", "level": 20},
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
                search_pokemon()
            elif n == 2:
                pokemon_type()

            elif n == 3:
                backpack()

            elif n == 4:
                pokemon_register()

            elif n == 5:
                print("Exiting the system.")
                break
            else:
                print("Choose one of the options.")
        except ValueError:
            print("It must be a whole number.")


def search_pokemon():
    # Pokémon search function
    print("--- Pokémon Finder ---")
    search = input("\n Which Pokémon do you want to look for?" "\n- ").lower().strip()
    if search in pokemons:
        print("--- POKEMON FOUND --- ", f"\n{search} ")
        for value in pokemons[search]:
            print(f"{value}:", pokemons[search][value])
    else:
        print("That Pokémon was not found.")


def pokemon_type():
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


def pokemon_register():
    print("--- REGISTER NEW POKEMON ---")
    while True:
        name = input("Name of the new Pokémon" "\n- ").lower().strip()
        if name in pokemons:
            print("This Pokémon is already registered.")
            continue
        elif name == "":
            print("Enter a name.")
            continue
        while True:
            type = input("What type is the Pokémon?" "\n- ").lower().strip()
            if type == "":
                print("Enter the Pokémon type.")
                continue
            break
        while True:
            try:
                level = int(input("What is the Pokémon's level?" "\n- "))
            except ValueError:
                print("It must be a whole number.")
                continue
            break
        break
    pokemons[name] = {"type": type, "level": level}
    print("Pokemon registered successfully")


def main():
    Pokedex()


if __name__ == "__main__":
    main()
