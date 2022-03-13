import random
import sys

# random.choice -> świetna funkcja
# list(dict) -> zwraca liste kluczy słownika; skrót od list(ids.keys())🤔

ids = {
    "en": {
        "boys": [
            "Oliver", "Harry", "George", "Noah", "Jack", "Jacob", "Leo", "Oscar", "Charlie", "Muhammad"
        ],
        "girls": [
            "Olivia", "Amelia", "Isla", "Ava", "Emily", "Isabella", "Mia", "Poppy", "Ella", "Lily"
        ],
        "lnames": [
            "Jones", "Taylor", "Williams", "Brown", "White", "Harris", "Martin", "Davies", "Wilson", "Cooper", "Evans", "King", "Thomas", "Baker", "Green", "Wright", "Johnson", "Edwards", "Clark", "Roberts", "Robinson", "Hall", "Lewis", "Clarke", "Young", "Davis", "Turner", "Hill", "Phillips", "Collins", "Allen", "Moore", "Thompson", "Carter", "James", "Knight", "Walker", "Wood", "Hughes", "Parker", "Ward", "Bennett", "Cook", "Webb", "Bailey", "Scott", "Jackson", "Lee", "Cox"
        ]
    },
    "pl": {
        "boys": [
            "Piotr", "Krzysztof", "Andrzej", "Jan", "Stanisław", "Tomasz", "Paweł",
            "Marcin", "Michał", "Marek", "Grzegorz", "Józef", "Łukasz", "Adam",
            "Zbigniew", "Jerzy", "Tadeusz", "Mateusz", "Dariusz", "Mariusz",
            "Wojciech", "Ryszard", "Jakub", "Henryk", "Robert", "Rafał",
            "Kazimierz", "Jacek", "Maciej", "Kamil", "Janusz", "Igor"
        ],
        "girls": [
            "Anna", "Maria", "Katarzyna", "Małgorzata", "Agnieszka", "Barbara",
            "Krystyna", "Ewa", "Elżbieta", "Zofia", "Teresa", "Magdalena",
            "Joanna", "Janina", "Monika", "Danuta", "Jadwiga", "Aleksandra",
            "Halina", "Irena", "Beata", "Marta", "Dorota", "Helena", "Karolina",
            "Grażyna", "Jolanta", "Iwona", "Marianna", "Natalia"
        ],
        "lnames": [
            "Nowak", "Kowalski", "Lewandowski", "Kowalczyk", "Kamiński",
            "Zieliński", "Szymański", "Jankowski", "Wojciechowski", "Kwiatkowski",
            "Kaczmarek", "Mazur", "Krawczyk", "Piotrowski", "Grabowski",
            "Nowakowski", "Michalski", "Adamczyk", "Nowicki", "Dudek", "Wieczorek",
            "Majewski", "Olszewski", "Jaworski", "Pawlak", "Malinowski", "Walczak",
            "Witkowski", "Rutkowski", "Michalak", "Sikora", "Ostrowski", "Baran",
            "Szewczyk", "Duda", "Tomaszewski", "Pietrzak", "Marciniak", "Zalewski",
            "Jakubowski", "Zawadzki", "Jasiński", "Sadowski", "Chmielewski",
            "Borkowski", "Czarnecki", "Sawicki", "Kubiak", "Maciejewski",
            "Urbański", "Kucharski", "Szczepański", "Wilk", "Lis", "Mazurek",
            "Kalinowski", "Wysocki", "Adamski", "Wasilewski", "Sobczak",
            "Andrzejewski", "Czerwiński", "Cieślak", "Zakrzewski", "Sikorski",
            "Krajewski", "Szymczak", "Szulc", "Gajewski", "Baranowski",
            "Laskowski", "Makowski", "Brzeziński", "Przybylski", "Borowski",
            "Nowacki", "Chojnacki", "Domański", "Ciesielski", "Krupa",
            "Szczepaniak", "Kaczmarczyk", "Kowalewski", "Leszczyński", "Lipiński",
            "Kozak", "Kania", "Urbaniak", "Mucha", "Kowalik", "Tomczak",
            "Czajkowski", "Markowski", "Nawrocki", "Janik", "Brzozowski",
            "Markiewicz", "Wawrzyniak", "Jarosz", "Tomczyk"
        ],
    },
    "es": {
        "boys": [
            "Lucas", "Hugo", "Martín", "Daniel", "Pablo", "Airam", "Aday", "Yerai",
            "Jonay", "Beneharo", "Ayoze", "Nauzet", "Rayco", "Anxo", "Iago",
            "Brais", "Xosé", "Markel", "Jon", "Ander", "Oier", "Iker", "Unai",
            "Mikel", "Marc", "Alex", "Eric", "Pol", "Pau", "Biel", "Hugo", "Arna",
            "Didac", "Mohamed", "Adam", "Rayan", "Bilal", "Ibrahim"
        ],
        "girls": [
            "Lucía", "Sofía", "María", "Martina", "Paula", "Naira", "Idaira",
            "Yurena", "May", "Adassa", "Dácil", "Guacimara", "Chaxiraxi", "Antía",
            "Iria", "Noa", "Uxía", "Nerea", "Ane", "June", "Irati", "Nahia",
            "Nora", "Izaro", "Uxue", "Itziar", "Salma", "Malak", "Lina", "Yasmin",
            "Sara", "Amira"
        ],
        "lnames": [
            "Garcia", "Rodriguez", "Gonzalez", "Fernandez", "Lopez", "Martinez", "Sanchez", "Perez", "Gomez", "Martin", "Jimenez", "Ruiz", "Hernandez", "Diaz", "Moreno", "Muñoz", "Alvarez", "Romero", "Alonso", "Gutierrez", "Navarro", "Torres", "Dominguez", "Ramos", "Vazquez", "Gil", "Ramirez", "Serrano", "Blanco", "Molina", "Morales", "Suarez", "Ortega", "Delgado", "Castro", "Ortiz", "Rubio", "Marin", "Sanz", "Iglesias", "Medina", "Nuñez", "Garrido", "Castillo", "Cortes", "Lozano", "Guerrero", "Santos", "Cano", "Prieto", "Cruz", "Mendez", "Calvo", "Vidal", "Gallego", "Herrera", "Cabrera", "Flores", "Peña", "Leon", "Marquez", "Campos", "Vega", "Fuentes", "Carrasco", "Diez", "Reyes", "Caballero", "Nieto", "Pascual", "Aguilar", "Santana", "Herrero", "Ferrer", "Lorenzo", "Gimenez", "Hidalgo", "Montero", "Ibañez", "Santiago", "Mora", "Vicente", "Vargas", "Arias", "Duran", "Benitez", "Carmona", "Crespo", "Pastor", "Soto", "Soler"
        ],
    }
}


def get_name(names):
    return random.choice(names)


nationality = random.choice(list(ids.keys()))  # lostujemy narodowść
if len(sys.argv) == 2:  # jeżeli akurat podalismy argument do skryptu to weźmy tą narodowść
    # sprawdźmy czy się nie pomyliliśmy
    if sys.argv[1] in set(ids.keys()):
        nationality = sys.argv[1]

gender = random.choice(["boys", "girls"])

fname = get_name(ids[nationality][gender])
lname = get_name(ids[nationality]["lnames"])

print(f'{fname} {lname}')
