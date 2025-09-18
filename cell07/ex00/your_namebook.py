def array_of_names(names_dict):
    full_name = []
    for first, last in names_dict.items():
        full_name = first.capitalize() + "" + last.capitalize()
        full_name = first.append(full_name)
    return full_name

persons ={ 
    "Wanchalerm":"Kawalin",
    "Pholnam": "Sakhamphan",
    "Pop": "fanta"
}

print(array_of_names(persons))