# Dawn Patrol Pilot Creator
import random
import mimesis
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os



class Pilot(object):
    """Pilot class: Holds all data related to the pilot"""

    def __init__(self, pilot_log):
        self.status = pilot_log['Status']
        self.pilot_id = pilot_log['Pilot ID']
        self.rank = pilot_log['Rank']
        self.name = pilot_log['Name']
        self.allegiance = pilot_log['Allegiance']
        self.nationality = pilot_log['Nationality']
        self.plane_group = pilot_log['Plane Group']
        self.missions = pilot_log['Missions']
        self.kills = pilot_log['Kills']
        self.date_created = pilot_log['Date Created']
        self.date_reported_killed = pilot_log['Date Reported Killed']
        self.kill_log = pilot_log['Kill Log']


    def addKill(self):
        self.kills += 1
        self.kill_log.append(input('Plane downed?:'))

    def addMission(self):
        self.missions += 1


def pilot_nationality_detail(nationality):
    nationality_table = {'american': {2: ['DE, USA', 'MD, USA', 'NJ, USA', 'NY, USA', 'PA, USA', 'VA, USA'],
                                      3: ['CT, USA', 'MA, USA', 'ME, USA', 'NH, USA', 'RI, USA', 'VT, USA'],
                                      4: ['ID, USA', 'MT, USA', 'NV, USA', 'OR, USA', 'WA, USA', 'WY, USA'],
                                      5: ['AL, USA', 'FL, USA', 'GA, USA', 'MS, USA', 'NC, USA', 'SC, USA'],
                                      6: ['CT, USA', 'MA, USA', 'ME, USA', 'NH, USA', 'RI, USA', 'VT, USA'],
                                      7: ['DE, USA', 'MD, USA', 'NJ, USA', 'NY, USA', 'PA, USA', 'VA, USA'],
                                      8: ['IL, USA', 'IN, USA', 'MI, USA', 'MN, USA', 'OH, USA', 'WI, USA'],
                                      9: ['AR, USA', 'KY, USA', 'LA, USA', 'MO, USA', 'TN, USA', 'WV, USA'],
                                      10: ['IA, USA', 'KS, USA', 'NB, USA', 'ND, USA', 'OK, USA', 'SD, USA'],
                                      11: ['AZ, USA', 'CA, USA', 'CO, USA', 'NM, USA', 'TX, USA', 'UT, USA'],
                                      12: ['AZ, USA', 'CA, USA', 'CO, USA', 'NM, USA', 'TX, USA', 'UT, USA']},
                         'belgin': {2: 'Flanders, Belgium', 3: 'Flanders, Belgium', 4: 'Flanders, Belgium',
                                    5: 'Flanders, Belgium', 6: 'Flanders, Belgium', 7: 'Flanders, Belgium',
                                    8: 'Flanders, Belgium', 9: 'Wallonia, Belgium', 10: 'Wallonia, Belgium',
                                    11: 'Wallonia, Belgium', 12: 'Wallonia, Belgium'},
                         'british': {2: 'Rhodesia', 3: 'South Africa', 4: 'Wales',
                                     5: 'Scotland', 6: 'England', 7: 'England',
                                     8: 'England', 9: 'Canada', 10: 'Australia/New Zealand',
                                     11: 'America', 12: 'Ireland'},
                         'italian': {2: 'Sardinia', 3: 'Sicily', 4: 'Piedmont', 5: 'Tuscany',
                                     6: 'Latium', 7: 'Campania', 8: 'Venezia', 9: 'Lombardy',
                                     10: 'Apulia', 11: 'Liguria', 12: 'Calabria'},
                         'french': {2: 'France', 3: 'France', 4: 'France', 5: 'France',
                                    6: 'France', 7: 'France', 8: 'France', 9: 'France',
                                    10: 'sub', 11: 'America',
                                    12: {2: 'Montenegro/Luxemborg', 3: 'Norway/Danish',
                                         4: 'Spain(N)', 5: 'Russia', 6: 'Italy', 7: 'Serbia',
                                         8: 'Romania', 9: 'Portugal', 10: 'Norway(N)',
                                         11: 'Sweden/Switzerland', 12: 'Japan/China'}},
                         'german': {2: 'Prussian', 3: 'Prussian', 4: 'Saxon', 5: 'Prussian',
                                    6: 'Bavarian', 7: 'Saxon', 8: 'Wurttemberger', 9: 'Prussian',
                                    10: 'Bavarian', 11: 'Wurttemberger', 12: 'Prussian'},
                         'austro-hungarian': {2: 'Czech', 3: 'Slovakian', 4: 'Croatian',
                                              5: 'Magyar (Hungarian)', 6: 'Austrian', 7: 'Austrian',
                                              8: 'Austrian', 9: 'Magyar (Hungarian)', 10: 'Bosnian',
                                              11: 'Slovene', 12: 'Czech'}}

    roll_1 = int(random.uniform(1, 7)) + int(random.uniform(1, 7))
    if nationality.lower() == 'american':
        return nationality_table[nationality.lower()][roll_1][int(random.uniform(0, 6))]

    elif nationality.lower() == 'french':

        if roll_1 == 12:
            return nationality_table[nationality.lower()][roll_1][int(random.uniform(1, 7))]
        else:
            return nationality_table[nationality.lower()][roll_1]
    else:
        return nationality_table[nationality.lower()][roll_1]


def pilot_rank(nationality):
    ranks = {'french': {1: 'Sergent', 2: 'Adjudant', 3: 'Sous-Lieutenant', 4: 'Sous-Lieutenant', 5: 'Lieutenant',
                        6: 'Lieutenant'},
             'belgin': {1: 'Sergent', 2: 'Adjudant', 3: 'Sous-Lieutenant', 4: 'Sous-Lieutenant', 5: 'Lieutenant',
                        6: 'Lieutenant'},
             'american': {1: '2nd Lieutenant', 2: '2nd Lieutenant', 3: 'Lieutenant', 4: 'Lieutenant', 5: 'Lieutenant',
                          6: 'Lieutenant'},
             'italian': {1: 'Sergente', 2: 'Sergente', 3: 'Sottotenente', 4: 'Sottotenente', 5: 'Tenente',
                         6: 'Tenente'},
             'british': {1: '2nd Lieutenant', 2: '2nd Lieutenant', 3: 'Lieutenant', 4: 'Lieutenant', 5: 'Lieutenant',
                         6: 'Captian'},
             'austro-hungarian': {1: 'Feldwebel', 2: 'Feldwebel', 3: 'Feldwebel', 4: 'Leutnant', 5: 'Leutnant',
                                  6: 'Leutnant'},
             'german': {1: 'Unteroffizier', 2: 'Vizefeldwebel', 3: 'Vizefeldwebel', 4: 'Leutnant', 5: 'Leutnant',
                        6: 'Leutnant', }}
    return ranks[nationality.lower()][int(random.uniform(1, 7))]


def pilot_name(nationality):
    nationality_conversion = {'american': 'en', 'belgin': 'nl-be', 'british': 'en-gb', 'italian': 'it',
                              'french': 'fr', 'german': 'de', 'austro-hungarian': 'de-at'}
    nat = nationality_conversion[nationality.lower()]
    return mimesis.Personal(nat).full_name(gender='male')


def getsquad():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials/secret_client.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Squadron_test').sheet1
    return sheet.get_all_records()




def main():
    print('Welcome to Dawn Patrol Pilot Roller.\n')
    while True:
        print('Menu'.center(20, '-'))
        main_menu = ['Fetch Squadron', 'Save Squadron', 'Roll New Squadron', 'Roll Single Pilot',
                     'Show Current Squadron', 'Exit']
        for i in main_menu:
            print('[' + str(main_menu.index(i) + 1) + ']' + i)
        user_input = input('Command:')
        if user_input.isalnum():
            if user_input.lower() == main_menu[0].lower() or user_input == '1':
                print('Fetching Squadron', end='\n\n')
                squad = getsquad()
                print('There are ' + str(len(squad)) + ' pilots in the suadron.')
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
