

class Map:

    def __init__(self, countries_dict: dict):
        self.countries = countries_dict

    def get_border_countries(self, country_name):
        return self.countries[country_name]


AMERIQUE_DU_SUD = Map({
        'Colombie': ['Equateur', 'Venezuela', 'Brésil'],
        'Venezuela': ['Colombie', 'Guyana', 'Brésil'],
        'Guyana': ['Venezuela', 'Suriname', 'Brésil'],
        'Suriname': ['Guyana', 'France', 'Brésil'],
        'France': ['Suriname', 'Brésil'],
        'Equateur': ['Colombie', 'Pérou'],
        'Pérou': ['Equateur', 'Colombie', 'Brésil', 'Bolivie', 'Chili'],
        'Brésil': ['Colombie', 'Venezuela', 'Guyana', 'Suriname', 'France', 'Pérou', 'Bolivie', 'Paraguay', 'Argentine', 'Uruguay'],
        'Bolivie': ['Pérou', 'Brésil', 'Paraguay', 'Argentine', 'Chili'],
        'Paraguay': ['Bolivie', 'Brésil', 'Argentine'],
        'Chili': ['Pérou', 'Bolivie', 'Argentine'],
        'Argentine': ['Chili', 'Bolivie', 'Paraguay', 'Brésil', 'Uruguay'],
        'Uruguay': ['Argentine', 'Brésil']
    })

EUROPE = Map({
    'Islande': [],
    'Irlande': [],
    'Pays-de-Galle': ['Angleterre'],
    'Angleterre': ['Pays-de-Galle', 'Ecosse'],
    'Ecosse': ['Angleterre'],
    'Norvège': ['Suède'],
    'Suède': ['Norvège', 'Finlande'],
    'Finlande': ['Suède', 'Russie'],
    'Russie': ['Finlande', 'Estonie', 'Lettonie', 'Biélorussie', 'Ukraine'],
    'Estonie': ['Russie', 'Lettonie'],
    'Lettonie': ['Estonie', 'Russie', 'Lituanie'],
    'Lituanie': ['Lettonie', 'Pologne'],
    'Biélorussie': ['Lettonie', 'Lituanie', 'Pologne', 'Russie', 'Ukraine'],
    'Pologne': ['Lituanie', 'Biélorussie', 'Ukraine', 'Allemagne', 'République-Tchèque', 'Slovaquie'],
    'Ukraine': ['Russie', 'Biélorussie', 'Pologne', 'Slovaquie', 'Hongrie', 'Roumanie', 'Moldavie'],
    'Moldavie': ['Ukraine', 'Roumanie'],
    'Roumanie': ['Ukraine', 'Moldavie', 'Bulgarie', 'Serbie', 'Hongrie'],
    'Bulgarie': ['Roumanie', 'Serbie', 'Macédoine', 'Grèce'],
    'Serbie': ['Hongrie', 'Roumanie', 'Bulgarie', 'Macédoine', 'Albanie', 'Monténégro', 'Bosnie', 'Croatie'],
    'Hongrie': ['Slovaquie', 'Ukraine', 'Roumanie', 'Serbie', 'Croatie', 'Slovénie', 'Autriche'],
    'Croatie': ['Hongrie', 'Slovénie', 'Serbie', 'Bosnie', 'Monténégro'],
    'Slovaquie': ['Hongrie', 'Autriche', 'République-Tchèque', 'Pologne', 'Ukraine'],
    'Bosnie': ['Croatie', 'Monténégro', 'Serbie'],
    'Monténégro': ['Bosnie', 'Serbie', 'Albanie'],
    'Macédoine': ['Albanie', 'Serbie', 'Bulgarie', 'Grèce'],
    'Grèce': ['Macédoine', 'Albanie', 'Bulgarie'],
    'Albanie': ['Monténégro', 'Serbie', 'Macédoine', 'Grèce'],
    'Slovénie': ['Hongrie', 'Autriche', 'Italie', 'Croatie'],
    'Autriche': ['Hongrie', 'Suisse', 'Italie', 'Allemagne', 'République-Tchèque', 'Slovaquie', 'Slovénie'],
    'République-Tchèque': ['Allemagne', 'Pologne', 'Slovaquie', 'Autriche'],
    'Allemagne': ['Pays-Bas', 'Belgique', 'Luxembourg', 'France', 'Pologne', 'Autriche', 'Suisse', 'République-Tchèque', 'Danemark'],
    'Suisse': ['France', 'Italie', 'Autriche', 'Allemagne'],
    'Pays-Bas': ['Belgique', 'Allemagne'],
    'Belgique': ['Pays-Bas', 'France', 'Luxembourg', 'Allemagne'],
    'France': ['Belgique', 'Allemagne', 'Suisse', 'Italie', 'Espagne', 'Luxembourg'],
    'Luxembourg': ['France', 'Allemagne', 'Belgique'],
    'Italie': ['France', 'Suisse', 'Autriche', 'Slovénie'],
    'Malte': [],
    'Chypre': [],
    'Espagne': ['Portugal', 'France'],
    'Portugal': ['Espagne'],
    'Danemark': ['Allemagne'],
})
