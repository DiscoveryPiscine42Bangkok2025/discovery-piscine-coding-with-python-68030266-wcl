def famous_births(figures):
    sorted_figures = sorted(figures.value(), key=lambda x:x["date_of_birth"])
    for persons in sorted_figures:
        print(f"{persons['name']} -{persons['date_of_birth']}")

scientists:  {
    "a":{"name": "b", "date_of_birth":"3333"},
    "c":{"name": "d", "date_of_birth":"6666"},
    "e":{"name": "f", "date_of_birth":"1000"},
    "g":{"name": "h", "date_of_birth":"2006"},
}

famous_births(scientists)