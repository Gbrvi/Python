def relation_to_luke(name):

    dicionario = {
        'Darth Vader' : 'father',
        'Leia' : 'sister', 
        'Han' : 'brother in law', 
        'R2D2' : 'droid',
    }

    return 'Luke, I am your {}'.format(dicionario[name])



print(relation_to_luke('Darth Vader'))