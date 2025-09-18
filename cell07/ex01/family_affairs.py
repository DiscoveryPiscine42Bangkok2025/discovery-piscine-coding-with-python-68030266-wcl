def popfanta(family):
    return list(filter(lambda name: family[name] == "pop", family.keys()))

dupont_family = {
    "Wanchalerm":"Kawalin",
    "Pholnam": "Sakhamphan",
    "Pop": "fanta"
}
print(popfanta(dupont_family))