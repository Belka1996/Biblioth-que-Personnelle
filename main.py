# Projet Bibliothèque Personnelle
# Auteur : Belkacem Medjkoune

import json
import os

FICHIER_JSON = "bibliotheque.json"


def charger_bibliotheque():
    if os.path.exists(FICHIER_JSON):
        with open(FICHIER_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def sauvegarder_bibliotheque(bibliotheque):
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(bibliotheque, f, indent=4, ensure_ascii=False)


def generer_id(bibliotheque):
    if not bibliotheque:
        return 1
    return max(livre["ID"] for livre in bibliotheque) + 1


def afficher_livres(bibliotheque):
    if not bibliotheque:
        print("📚 La bibliothèque est vide.")
        return
    for livre in bibliotheque:
        statut = "✅ Lu" if livre["Lu"] else "❌ Non lu"
        print(f'[{livre["ID"]}] {livre["Titre"]} - {livre["Auteur"]} ({livre["Année"]}) - {statut}')
        if livre["Lu"]:
            print(f"  📌 Note: {livre['Note']}/10")
            print(f"  💬 Commentaire: {livre.get('Commentaire', '')}")


def ajouter_livre(bibliotheque):
    titre = input("Titre: ")
    auteur = input("Auteur: ")
    annee = input("Année de publication: ")
    try:
        annee = int(annee)
        livre = {
            "ID": generer_id(bibliotheque),
            "Titre": titre,
            "Auteur": auteur,
            "Année": annee,
            "Lu": False,
            "Note": None,
            "Commentaire": ""
        }
        bibliotheque.append(livre)
        print("✅ Livre ajouté.")
    except ValueError:
        print("❌ Année invalide.")


def supprimer_livre(bibliotheque):
    try:
        id_livre = int(input("ID du livre à supprimer: "))
        for livre in bibliotheque:
            if livre["ID"] == id_livre:
                bibliotheque.remove(livre)
                print("🗑️ Livre supprimé.")
                return
        print("❌ Livre non trouvé.")
    except ValueError:
        print("❌ ID invalide.")


def rechercher_livre(bibliotheque):
    mot_cle = input("Mot-clé (titre ou auteur): ").lower()
    resultats = [livre for livre in bibliotheque if mot_cle in livre["Titre"].lower() or mot_cle in livre["Auteur"].lower()]
    afficher_livres(resultats)


def marquer_lu(bibliotheque):
    try:
        id_livre = int(input("ID du livre lu: "))
        for livre in bibliotheque:
            if livre["ID"] == id_livre:
                livre["Lu"] = True
                note = input("Note sur 10 (facultatif): ")
                commentaire = input("Commentaire (facultatif): ")
                try:
                    livre["Note"] = int(note) if note else None
                except ValueError:
                    livre["Note"] = None
                livre["Commentaire"] = commentaire
                print("📘 Livre marqué comme lu.")
                return
        print("❌ Livre non trouvé.")
    except ValueError:
        print("❌ ID invalide.")


def afficher_filtre(bibliotheque, lu=True):
    filtres = [livre for livre in bibliotheque if livre["Lu"] == lu]
    afficher_livres(filtres)


def trier_livres(bibliotheque):
    critere = input("Trier par (annee/auteur/note): ").lower()
    if critere in ["annee", "auteur", "note"]:
        livres_tries = sorted(bibliotheque, key=lambda x: x.get(critere) or "")
        afficher_livres(livres_tries)
    else:
        print("❌ Critère invalide.")


def menu():
    print("\n📚 MENU BIBLIOTHÈQUE")
    print("1. Afficher tous les livres")
    print("2. Ajouter un livre")
    print("3. Supprimer un livre")
    print("4. Rechercher un livre")
    print("5. Marquer un livre comme lu")
    print("6. Afficher livres lus")
    print("7. Afficher livres non lus")
    print("8. Trier les livres")
    print("9. Quitter")


def main():
    bibliotheque = charger_bibliotheque()

    while True:
        menu()
        choix = input("Votre choix: ")

        if choix == "1":
            afficher_livres(bibliotheque)
        elif choix == "2":
            ajouter_livre(bibliotheque)
        elif choix == "3":
            supprimer_livre(bibliotheque)
        elif choix == "4":
            rechercher_livre(bibliotheque)
        elif choix == "5":
            marquer_lu(bibliotheque)
        elif choix == "6":
            afficher_filtre(bibliotheque, lu=True)
        elif choix == "7":
            afficher_filtre(bibliotheque, lu=False)
        elif choix == "8":
            trier_livres(bibliotheque)
        elif choix == "9":
            sauvegarder_bibliotheque(bibliotheque)
            print("👋 Au revoir !")
            break
        else:
            print("❌ Choix invalide.")


if __name__ == "__main__":
    main()
