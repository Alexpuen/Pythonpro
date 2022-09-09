def run():
    Dragon = {"Dragonite", "Altaria", "Salamance", "Latios", "Latias", "Rayquaza", "Gible", "Gabite", "Garchomp", "Dragapult"}
    Volador = {"Charizard", "Zubat", "Doduo", "Articuno", "Dragonite", "Salamance", "Altaria"}

    pokemon = Dragon | Volador
    print(pokemon)

    pokemon_2 = Dragon & Volador
    print(pokemon_2)

    pokemon_3 = Dragon - Volador
    print(pokemon_3)

    pokemon_4 = Volador - Dragon
    print(pokemon_4)

    pokemon_5 = Dragon ^ Volador
    print(pokemon_5)




if __name__ == "__main__":
    run()