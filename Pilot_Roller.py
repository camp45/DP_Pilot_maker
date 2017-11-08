# Dawn Patrol Pilot Creater
import random
import mimesis



def pilot_nationality_detail(nationality):
    nationality_table = {'american':{2:['DE', 'MD', 'NJ', 'NY', 'PA', 'VA'],
                                    3:['CT', 'MA', 'ME', 'NH', 'RI', 'VT'],
                                    4:['ID', 'MT', 'NV', 'OR', 'WA', 'WY'],
                                    5:['AL', 'FL', 'GA', 'MS', 'NC', 'SC'],
                                    6:['CT', 'MA', 'ME', 'NH', 'RI', 'VT'],
                                    7:['DE', 'MD', 'NJ', 'NY', 'PA', 'VA'],
                                    8:['IL', 'IN', 'MI', 'MN', 'OH', 'WI'],
                                    9:['AR', 'KY', 'LA', 'MO', 'TN', 'WV'],
                                    10:['IA', 'KS', 'NB', 'ND', 'OK', 'SD'],
                                    11:['AZ', 'CA', 'CO', 'NM', 'TX', 'UT'],
                                    12:['AZ', 'CA', 'CO', 'NM', 'TX', 'UT']},
                        'belgin':{2:'Flemish', 3:'Flemish', 4:'Flemish',
                                   5:'Flemish', 6:'Flemish', 7:'Flemish',
                                   8:'Flemish', 9:'Waloon', 10:'Waloon',
                                   11:'Waloon', 12:'Waloon'},
                        'british':{2:'Rhodesian', 3:'South African', 4:'Welsh',
                                    5:'Scottish', 6:'English', 7:'English',
                                    8:'English', 9:'Canadian', 10:'Australian/New Zealand',
                                    11:'American', 12:'Irish'},
                        'italian':{2:'Sardinia', 3:'Sicily', 4:'Piedmont', 5:'Tuscany',
                                   6:'Latium', 7:'Campania', 8:'Venezia', 9:'Lombardy',
                                   10:'Apulia', 11:'Liguria', 12:'Calabria'},
                        'french':{2:'French', 3:'French', 4:'French', 5:'French',
                                  6:'French', 7:'French', 8:'French', 9:'French',
                                  10:'sub', 11:'American',
                                  12:{2:'Montenegro/Luxemborg', 3:'Norway/Danish',
                                      4:'Spain(N)', 5:'Russia', 6:'Italy', 7:'Serbia',
                                      8:'Romania', 9:'Portugal', 10:'Norway(N)',
                                      11:'Sweden/Switzerland', 12:'Japan/China'}},
                        'german':{2:'Prussian', 3:'Prussian', 4:'Saxon', 5:'Prussian',
                                  6:'Bavarian', 7:'Saxon', 8:'Wurttemberger', 9:'Prussian',
                                  10:'Bavarian', 11:'Wurttemberger', 12:'Prussian'},
                        'austro-hungarian': {2: 'Czech', 3: 'Slovakian', 4: 'Croatian',
                                            5: 'Magyar (Hungarian)', 6: 'Austrian', 7: 'Austrian',
                                            8: 'Austrian', 9: 'Magyar (Hungarian)', 10: 'Bosnian',
                                            11: 'Slovene', 12: 'Czech'}}

    roll_1 = int(random.uniform(1, 7))+int(random.uniform(1, 7))
    if nationality.lower() == 'american':
        return nationality_table[nationality.lower()][roll_1][int(random.uniform(0,6))]

    elif nationality.lower() == 'french':

        if roll_1 == 12:
            return nationality_table[nationality.lower()][roll_1][int(random.uniform(1,7))]
        else:
            return nationality_table[nationality.lower()][roll_1]
    else:
        return nationality_table[nationality.lower()][roll_1]


def pilot_rank(nationality):
    ranks = {'french':{1:'Sergent', 2:'Adjudant', 3:'Sous-Lieutenant', 4:'Sous-Lieutenant', 5:'Lieutenant', 6:'Lieutenant'},
             'belgin':{1:'Sergent', 2:'Adjudant', 3:'Sous-Lieutenant', 4:'Sous-Lieutenant', 5:'Lieutenant', 6:'Lieutenant'},
             'american':{1:'2nd Lieutenant', 2:'2nd Lieutenant', 3:'Lieutenant', 4:'Lieutenant', 5:'Lieutenant', 6:'Lieutenant'},
             'italian':{1:'Sergente', 2:'Sergente', 3:'Sottotenente', 4:'Sottotenente', 5:'Tenente', 6:'Tenente'},
             'british':{1:'2nd Lieutenant', 2:'2nd Lieutenant', 3:'Lieutenant', 4:'Lieutenant', 5:'Lieutenant', 6:'Captian'},
             'austro-hungarian':{1:'Feldwebel', 2:'Feldwebel', 3:'Feldwebel', 4:'Leutnant', 5:'Leutnant', 6:'Leutnant'},
             'german':{1:'Unteroffizier', 2:'Vizefeldwebel', 3:'Vizefeldwebel', 4:'Leutnant', 5:'Leutnant', 6:'Leutnant',}}
    return ranks[nationality.lower()][int(random.uniform(1,7))]


def pilot_name(nationality):
    nationality_conversion = {'american': 'en', 'belgin': 'nl-be', 'british': 'en-gb', 'italian': 'it',
                              'french': 'fr', 'german': 'de', 'austro-hungarian': 'de-at'}
    nat = nationality_conversion[nationality.lower()]
    return mimesis.Personal(nat).full_name(gender='male')



def main():
    print('Welcome to Dawn Patrol Pilot Roller.\n')
    while True:
        print('Menu'.center(20,'-'))
        main_menu = ['Fetch Squadron', 'Save Squadron', 'Roll New Squadron', 'Roll Single Pilot',
                     'Show Current Squadron', 'Exit']
        for i in main_menu:
            print('[' + str(main_menu.index(i)+1) + ']' + i)
        user_input = input('Command:')
        if user_input.isalnum():
            if user_input.lower() == main_menu[0].lower() or user_input == '1':
                print('Fetching Squadron', end='\n\n')
            elif user_input.lower() == main_menu[1].lower() or user_input == '2':
                print('Saving Squadron', end='\n\n')
            elif user_input.lower() == main_menu[2] or user_input == '3':
                print('Rolling New Squadron', end='\n\n')
            elif user_input.lower() == main_menu[3] or user_input == '4':
                print('Rolling Single Pilot', end='\n\n')
                nat = input('Pilot Nationality?:')
                print(pilot_rank(nat) + ' ' + pilot_name(nat) + ' ' + 'from ' + pilot_nationality_detail(nat))
            elif user_input.lower() == main_menu[4] or user_input == '5':
                print('Showing Current Squadron', end='\n\n')
            elif user_input.lower() == main_menu[5] or user_input == '6':
                print('Exiting', end='\n\n')
                exit()
            else:
                print('Enter a valid option.', end='\n\n')
        else:
            print('Enter a valid option.', end='\n\n')




if __name__ == '__main__':
    main()
    




