# proketi.py
# meal planner / ruokalistasuunnitelija

def lisaa_resepti(reseptit):
    nimi = input("Anna reseptin nimi: ")
    ainesosat = input("Anna ainesosat pilkulla erotettuna: ").split(",")
    reseptit[nimi] = ainesosat
    print(f"Resepti '{nimi}' lisätty.\n")

def nayta_reseptit(reseptit):
    if not reseptit:
        print("Ei reseptejä tallennettuna.\n")
        return
    for nimi, ainesosat in reseptit.items():
        print(f"Resepti: {nimi}")
        print("Ainesosat:")
        for ainesosa in ainesosat:
            print(f"- {ainesosa.strip()}")
        print("\n")

def luo_ruokalista(reseptit):
    ruokalista = []
    print("Syötä viikon päivät (maanantai, tiistai, ...). Kirjoita 'valmis' lopettaaksesi.")
    while True:
        paiva = input("Anna päivän nimi (tai 'valmis' lopettaaksesi): ")
        if paiva.lower() == 'valmis':
            break
        if paiva:
            resepti = input(f"Anna resepti {paiva}ksi: ")
            if resepti in reseptit:
                ruokalista.append((paiva, resepti))
            else:
                print("Reseptiä ei löytynyt. Yritä uudelleen.")
    return ruokalista

def nayta_ostoslista(ruokalista, reseptit):
    ostoslista = []
    for paiva, resepti in ruokalista:
        ostoslista.extend(reseptit[resepti])
    ostoslista = [ainesosa.strip() for ainesosa in set(ostoslista)]
    print("Ostoslista:")
    for ainesosa in ostoslista:
        print(f"- {ainesosa}")
    print("\n")

def main():
    reseptit = {}
    ruokalista = []
    
    while True:
        print("Valitse toiminto:")
        print("1. Lisää resepti")
        print("2. Näytä reseptit")
        print("3. Luo ruokalista")
        print("4. Näytä ostoslista")
        print("5. Lopeta")
        
        valinta = input("Syötä valinta (1/2/3/4/5): ")
        
        if valinta == "1":
            lisaa_resepti(reseptit)
        elif valinta == "2":
            nayta_reseptit(reseptit)
        elif valinta == "3":
            ruokalista = luo_ruokalista(reseptit)
        elif valinta == "4":
            nayta_ostoslista(ruokalista, reseptit)
        elif valinta == "5":
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")

if __name__ == "__main__":
    main()