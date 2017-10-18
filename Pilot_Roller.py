    print('')
# Dawn Patrol Pilot Creater
import random




def pilot_nationality_detail(nationality):
    roll = int(random.uniform(2,13))
    american = {2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:"", 9:"", 10:"", 11:"", 12:""}
    belgin = {2:"Flemish", 3:"Flemish", 4:"Flemish", 5:"Flemish", 6:"Flemish", 7:"Flemish",
              8:"Flemish", 9:"Waloon", 10:"Waloon", 11:"Waloon", 12:"Waloon"}
    british = {2:"Rhodesian", 3:"South African", 4:"Welsh", 5:"Scottish", 6:"English",
               7:"English", 8:"English", 9:"Canadian", 10:"Australian/New Zealand", 11:"American", 12:"Irish"}
    italian = {2:"Sardinia", 3:"Sicily", 4:"Piedmont", 5:"Tuscany", 6:"Latium", 7:"Campania",
               8:"Venezia", 9:"Lombardy", 10:"Apulia", 11:"Liguria", 12:"Calabria"}
    french = {2:"French", 3:"French", 4:"French", 5:"French", 6:"French", 7:"French", 8:"French",
              9:"French", 10:"sub", 11:"American", 12:"sub"}
    lesser_allies = {2:"Montenegro/Luxemborg", 3:"Norway/Danish", 4:"Spain(N)", 5:"Russia",
                     6:"Italy", 7:"Serbia", 8:"Romania", 9:"Portugal", 10:"Norway(N)", 11:"Sweden/Switzerland", 12:"Japan/China"}
    german = {2:"Prussian", 3:"Prussian", 4:"Saxon", 5:"Prussian", 6:"Bavarian", 7:"Saxon", 8:"Wurttemberger",
              9:"Prussian", 10:"Bavarian", 11:"Wurttemberger", 12:"Prussian"}
    austro-hungarian = {2:"Czech", 3:"Slovakian", 4:"Croatian", 5:"Magyar (Hungarian)", 6:"Austrian", 7:"Austrian",
                        8:"Austrian", 9:"Magyar (Hungarian)", 10:"Bosnian", 11:"Slovene", 12:"Czech"}




