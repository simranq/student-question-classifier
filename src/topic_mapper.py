def get_topic(subject):

    animals = ["duck","elephant","kangaroo","leopard","otter","penguin","polar_bear","turtle","beetle","Gray_Wolf"]
    countries = ["Egypt","Canada","Finland","Ghana","Indonesia","Qatar","Romania","Singapore","Uruguay","Liechtenstein"]
    scientists = ["Isaac_Newton","Amedeo_Avogadro","Alessandro_Volta","Henri_Becquerel","Anders_Celsius","James_Watt"]
    presidents = ["Abraham_Lincoln","Calvin_Coolidge","Gerald_Ford","James_Monroe","John_Adams","Theodore_Roosevelt","Ulysses_S._Grant","Woodrow_Wilson","Grover_Cleveland","Millard_Fillmore"]

    if subject in animals:
        return "animal"
    elif subject in countries:
        return "country"
    elif subject in scientists:
        return "science"
    elif subject in presidents:
        return "politics"
    else:
        return "general"
