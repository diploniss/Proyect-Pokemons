pokemons = {
    "pikachu": {"tipo": "electrico", "nivel": 10},
    "charmander": {"tipo": "fuego", "nivel": 8},
    "raichu": {"tipo": "electrico", "nivel": 20},
}


def Pokedex():
    # Start menu
    while True:
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
