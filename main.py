# proketi.py
# meal planner / ruokalistasuunnitelija

# meal_planner.py

# Reseptien tallentaminen sanakirjaan, jossa avain on reseptin nimi ja arvo on lista ainesosista
recipes = {}

# Viikoittaisen ruokalistan tallentaminen sanakirjaan, jossa avain on viikonpäivä ja arvo on reseptin nimi
meal_plan = {}

def add_recipe():
    """
    Funktio uuden reseptin lisäämiseen.
    Pyytää käyttäjältä reseptin nimen ja ainesosat, ja tallentaa ne recipes-sanakirjaan.
    """
    name = input("Anna reseptin nimi: ")  # Pyydetään käyttäjää syöttämään reseptin nimi
    ingredients = input("Anna ainesosat pilkulla erotettuna: ").split(",")  # Pyydetään ainesosat pilkulla erotettuna ja jaetaan ne listaksi
    recipes[name] = [ingredient.strip() for ingredient in ingredients]  # Tallennetaan reseptin nimi ja ainesosat sanakirjaan
    print(f"Resepti '{name}' lisätty.")  # Tulostetaan vahvistusviesti

def show_recipes():
    """
    Funktio kaikkien reseptien näyttämiseen.
    Tulostaa kaikki tallennetut reseptit ja niiden ainesosat.
    """
    if not recipes:  # Tarkistetaan, onko recipes-sanakirja tyhjä
        print("Ei reseptejä tallennettuna.")  # Jos tyhjä, tulostetaan ilmoitus
    else:
        for name, ingredients in recipes.items():  # Käydään läpi kaikki reseptit
            print(f"Resepti: {name}\nAinesosat:")  # Tulostetaan reseptin nimi
            for ingredient in ingredients:  # Käydään läpi reseptin ainesosat
                print(f"- {ingredient}")  # Tulostetaan kukin ainesosa

def create_meal_plan():
    """
    Funktio viikoittaisen ruokalistan luomiseen.
    Pyytää käyttäjältä viikonpäivät ja niille valitut reseptit, ja tallentaa ne meal_plan-sanakirjaan.
    """
    print("Syötä viikon päivät (maanantai, tiistai, ...). Kirjoita 'valmis' lopettaaksesi.")  # Ohjeistaa käyttäjää
    while True:
        day = input("Anna päivän nimi (tai 'valmis' lopettaaksesi): ").lower()  # Pyydetään käyttäjältä päivän nimi
        if day == "valmis":  # Jos käyttäjä kirjoittaa 'valmis', lopetetaan syöttö
            break
        if day in meal_plan:  # Jos päivä on jo meal_plan-sanakirjassa, ilmoitetaan siitä
            print(f"Päivälle {day} on jo suunniteltu resepti.")
            continue
        recipe = input(f"Anna resepti {day}ksi: ")  # Pyydetään käyttäjältä reseptin nimi
        if recipe in recipes:  # Tarkistetaan, onko resepti olemassa recipes-sanakirjassa
            meal_plan[day] = recipe  # Tallennetaan resepti meal_plan-sanakirjaan
            print(f"Ruokalista päivitetty: {day} -> {recipe}")  # Tulostetaan vahvistusviesti
        else:
            print(f"Reseptiä '{recipe}' ei löydy. Lisää resepti ensin.")  # Jos reseptiä ei löydy, ilmoitetaan siitä

def show_shopping_list():
    """
    Funktio ostoslistan näyttämiseen.
    Generoi ja tulostaa ostoslistan viikoittaisen ruokalistan ainesosien perusteella.
    """
    shopping_list = {}  # Luodaan tyhjä sanakirja ostoslistalle
    for day, recipe in meal_plan.items():  # Käydään läpi viikoittainen ruokalista
        for ingredient in recipes[recipe]:  # Käydään läpi kunkin reseptin ainesosat
            if ingredient in shopping_list:  # Jos ainesosa on jo ostoslistassa, kasvatetaan määrää
                shopping_list[ingredient] += 1
            else:
                shopping_list[ingredient] = 1  # Jos ainesosa ei ole ostoslistassa, lisätään se
    if not shopping_list:  # Jos ostoslista on tyhjä, ilmoitetaan siitä
        print("Ostoslista on tyhjä.")
    else:
        print("Ostoslista:")  # Tulostetaan otsikko
        for ingredient, count in shopping_list.items():  # Käydään läpi ostoslista
            print(f"- {ingredient} ({count} kpl)")  # Tulostetaan kukin ainesosa ja sen määrä

def main():
    """
    Pääfunktio, joka sisältää sovelluksen päävalikon ja käyttäjän valintojen käsittelyn.
    """
    while True:
        print("\nValitse toiminto:")  # Tulostetaan valikko
        print("1. Lisää resepti")
        print("2. Näytä reseptit")
        print("3. Luo ruokalista")
        print("4. Näytä ostoslista")
        print("5. Lopeta")

        choice = input("Syötä valinta (1/2/3/4/5): ")  # Pyydetään käyttäjän valinta

        if choice == "1":  # Jos valinta on 1, kutsutaan add_recipe-funktiota
            add_recipe()
        elif choice == "2":  # Jos valinta on 2, kutsutaan show_recipes-funktiota
            show_recipes()
        elif choice == "3":  # Jos valinta on 3, kutsutaan create_meal_plan-funktiota
            create_meal_plan()
        elif choice == "4":  # Jos valinta on 4, kutsutaan show_shopping_list-funktiota
            show_shopping_list()
        elif choice == "5":  # Jos valinta on 5, lopetetaan ohjelma
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")  # Jos valinta ei ole kelvollinen, ilmoitetaan siitä

if __name__ == "__main__":
    main()  # Kutsutaan pääfunktiota, jos tiedosto ajetaan suoraan
