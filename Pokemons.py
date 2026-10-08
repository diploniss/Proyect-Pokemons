pokemons = {
    "pikachu": {"tipo": "electrico", "nivel": 10},
    "charmander": {"tipo": "fuego", "nivel": 8},
    "raichu": {"tipo": "electrico", "nivel": 20},
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
                print("saliendo del sistema")
                break
            else:
                print("Elije una de las opciones")
        except ValueError:
            print("Tiene que ser un numero entero ")


def searchPokemon():
    print("--- SEARCHING POKEMONS ---")


def types():
    print("--- SEARCHING TYPES ---")


def backpack():
    print("--- SEARCHING BACKPACK ---")


def registerPokemon():
    print("--- SEARCHING TYPES ---")
