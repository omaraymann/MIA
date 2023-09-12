import colorama  #imported colorama to change the text colors
from colorama import Fore, Style
'''to use rich library you need to open cmd
   and type pip install rich '''
from rich.console import Console
from rich.table import Table
import math
class villains:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

class Gru(villains):
    #lists of all allowed weapns and resources and energy each one has the same index for its data and 100 means infinite time of resources
    allowed_weapons = ["freeze gun","electric prod","mega magnet","kalman missile","no weapon"]
    weapons_energy = ["50","88","92","120","0"]
    weapons_resources = [100,5,3,1,100]

    allowed_shields = ["energy projected barriergun","selective permeability","no shield"]
    shields_energy = ["20","50","0"]
    shields_resources = [100,2,100]

    weapon_damage = 0
    shield_save = 1

    weapon = ""
    shield = ""

    def __init__(self,health,energy):
        super().__init__(health,energy)

    def choose_weapon(self):
        weapons_index = [] #counts the number of allowed weapons to the villain in this round to avoid errors in the list indexing
        cntr = 0
        choice = 0
        print(Fore.LIGHTYELLOW_EX + "\nCHOOSE GRU'S WEAPON:\n", Style.RESET_ALL)
        for i in range(5):
            #prints the weapons allowed in this round based on the villain energy and resource of this weapon
            if self.energy > int(Gru.weapons_energy[i]) and Gru.weapons_resources[i] > 0:
                print(f" {cntr+1}.{Gru.allowed_weapons[i]}")
                weapons_index.append(i)     #this list should have the index of the weapons printed to the player to know which one is choosen
                cntr += 1                   
        choice = int(input(Fore.LIGHTMAGENTA_EX + "Enter your choice: "))
        print(Style.RESET_ALL)
        if choice > cntr:                            #to avoid entering a number greater than the offered choices
            self.weapon = Gru.allowed_weapons[4]     #if the user enters a greater value it means that he will play with no weapon
        else:
            self.weapon = Gru.allowed_weapons[weapons_index[choice-1]]
            Gru.weapons_resources[weapons_index[choice-1]] -= 1
        weapons_index.clear()
        Gru.weapon_energy(self)

    def weapon_energy(self):
        if self.weapon == Gru.allowed_weapons[0]:
            self.energy -= 50                         #reduces player's energy
            Gru.weapon_damage = 11                    #damage of this certain weapon
        elif self.weapon == Gru.allowed_weapons[1]:
            self.energy -= 88
            Gru.weapon_damage = 18
        elif self.weapon == Gru.allowed_weapons[2]:
            self.energy -= 92
            Gru.weapon_damage = 10
        elif self.weapon == Gru.allowed_weapons[3]:
            self.energy -= 120
            Gru.weapon_damage = 20
        else:
            Gru.weapon_damage = 0

    def choose_shield(self):
        shields_index = [] #counts the number of allowed shields to the villain in this round to avoid errors in the list indexing
        cntr = 0
        print(Fore.LIGHTYELLOW_EX + "\nCHOOSE GRU'S SHIELD:", Style.RESET_ALL)
        for i in range(3):
            if self.energy > int(Gru.shields_energy[i]) and Gru.shields_resources[i] > 0:
                print(f" {cntr+1}.{Gru.allowed_shields[i]}")
                shields_index.append(i)
                cntr += 1
        choice = int(input(Fore.LIGHTMAGENTA_EX + "Enter Your Choice: "))
        print(Style.RESET_ALL)
        if choice > cntr:  #to avoid entering a number greater than the offered choices
            self.shield = Gru.allowed_shields[2]
        else:
            self.shield = Gru.allowed_shields[shields_index[choice-1]]
            Gru.shields_resources[shields_index[choice-1]] -= 1
        shields_index.clear()
        Gru.shield_energy(self)

    def shield_energy(self):
        if self.shield == Gru.allowed_shields[0]:
            self.energy -= 20
            Gru.shield_save = 0.60
        elif self.shield == Gru.allowed_shields[1]:
            self.energy -= 50
            Gru.shield_save = 0.10
        else:
            Gru.shield_save = 1

class Vector(villains):
    allowed_weapons = ["laser blasters","plasma grenades","sonic resonance cannon","no weapon"]
    weapons_energy = ["40","56","100","0"]
    weapons_resources = [100,8,3,100]

    allowed_shields = ["energy net trap","quantum deflector","no shield"]
    shields_energy = ["15","40","0"]
    shields_resources = [100,3,100]

    weapon_damage = 1
    shield_save = 0

    weapon = ""
    shield = ""

    def __init__(self,health,energy):
        super().__init__(health,energy)

    def choose_weapon(self):
        weapons_index = [] #counts the number of allowed weapons to the villain in this round to avoid errors in the list indexing
        cntr = 0
        print(Fore.LIGHTYELLOW_EX + "\nCHOOSE VECTOR'S WEAPON:\n", Style.RESET_ALL)
        for i in range(4):
            if self.energy > int(Vector.weapons_energy[i]) and Vector.weapons_resources[i] > 0:
                print(f" {cntr+1}.{Vector.allowed_weapons[i]}")
                weapons_index.append(i)
                cntr += 1
        choice = int(input(Fore.LIGHTMAGENTA_EX + "Enter Your Choice: "))
        print(Style.RESET_ALL)
        if choice > cntr:  #to avoid entering a number greater than the offered choices
            self.weapon =Vector.allowed_weapons[4]
        else:
            self.weapon = Vector.allowed_weapons[weapons_index[choice-1]]
            Vector.weapons_resources[weapons_index[choice-1]] -= 1
        weapons_index.clear()
        Vector.weapon_energy(self)

    def weapon_energy(self):
        if self.weapon == Vector.allowed_weapons[0]:
            self.energy -= 40
            Vector.weapon_damage = 8
        elif self.weapon == Vector.allowed_weapons[1]:
            self.energy -= 56
            Vector.weapon_damage = 13
        elif self.weapon == Vector.allowed_weapons[2]:
            self.energy -= 100
            Vector.weapon_damage = 22
        else:
            Vector.weapon_damage = 0

    def choose_shield(self):
        shields_index = [] #counts the number of allowed shields to the villain in this round to avoid errors in the list indexing
        cntr = 0
        print(Fore.LIGHTYELLOW_EX + "\nCHOOSE VECTOR'S SHIELD:", Style.RESET_ALL)
        for i in range(3):
            if self.energy > int(Vector.shields_energy[i]) and Vector.shields_resources[i] > 0:
                print(f" {cntr+1}.{Vector.allowed_shields[i]}")
                shields_index.append(i)
                cntr += 1
        choice = int(input(Fore.LIGHTMAGENTA_EX + "Enter Your Choice: "))
        print(Style.RESET_ALL)
        if choice > cntr:  #to avoid entering a number greater than the offered choices
            self.shield = Vector.allowed_shields[2]
        else:
            self.shield = Vector.allowed_shields[shields_index[choice-1]]
            Vector.shields_resources[shields_index[choice-1]] -= 1
        shields_index.clear()
        Vector.shield_energy(self)

    def shield_energy(self):
        if self.shield == Vector.allowed_shields[0]:
            self.energy -= 15
            Vector.shield_save = 0.68
        elif self.shield == Vector.allowed_shields[1]:
            self.energy -= 40
            Vector.shield_save = 0.20
        else:
            Vector.shield_save = 1

def damage():
    #case 1 reduce vector's health by 20 and ignores his shield
    if villain_1.weapon == "kalman missile":             
       villain_1.health -= villain_1.shield_save * villain_2.weapon_damage
       villain_2.health -= 20
    #case2 reduce gru's health by 80% of the actual reduction 
    elif villain_1.weapon == "mega magnet":
        villain_1.health -= villain_1.shield_save * villain_2.weapon_damage * 0.8
        villain_2.health -= villain_2.shield_save * villain_1.weapon_damage
    #general case reduce the health by multiplying the sheild save percentage with the opponent's weapon damage
    else:
        villain_1.health -= (villain_1.shield_save * villain_2.weapon_damage)
        villain_2.health -= (villain_2.shield_save * villain_1.weapon_damage)

def villian_info_display(gru_energy,vector_energy,gru_health,vector_health):
   console = Console()

    #to prevent printing negative values in the last round display 
   if gru_energy < 0:
       gru_energy = 0
   if vector_energy < 0: 
       vector_energy = 0
   if gru_health < 0:
       gru_health = 0
   if vector_health < 0:
       vector_health = 0

    #to indicate the color of health and energy
   gru_health_color = "[green]"
   if gru_health < 50:
        gru_health = "[red]"
   vector_health_color = "[green]"
   if vector_health < 50:
       vector_health_color = "[red]"
   gru_energy_color = "[green]"
   if gru_energy < 200:
       gru_energy_color = "[red]"
   vector_energy_color = "[green]"
   if vector_energy < 200:
       vector_energy_color = "[red]"

    #editing the bar graph
   bar_graph = Table(show_header=True, show_footer=False, show_lines=True)
   bar_graph.add_column("[blue]" + "Villain")
   bar_graph.add_column("[blue]" + "Energy")
   bar_graph.add_column("[blue]" + "Health")
   bar_graph.add_column("[blue]" + "Health Bar")
   
   bar_graph.add_row("[black]" + "GRU",gru_energy_color + f"{gru_energy}",gru_health_color + f"{gru_health}" , gru_health_color +  "▐" * (int(gru_health) // 10))
   bar_graph.add_row("[black]" + "VECTOR",vector_energy_color + f"{vector_energy}",vector_health_color + f"{round(float(vector_health),2)}", vector_health_color + "▐" * (int(vector_health) // 10))

   console.print(bar_graph) #print the bar graph

villain_1 = Gru(100,500)    #create two villians objects
villain_2 = Vector(100,500)

while villain_1.health > 0 and villain_2.health > 0 :
    villian_info_display(villain_1.energy,villain_2.energy,villain_1.health,villain_2.health)
    villain_1.choose_weapon()
    villain_1.choose_shield()
    villain_2.choose_weapon()
    villain_2.choose_shield()
    damage()
    if villain_1.energy < 50 and villain_2.energy < 40:    #both villains cannot use weapons
        print(Fore.LIGHTGREEN_EX + "\n♦♦♦ DEFEAT ♦♦♦")
        villian_info_display(villain_1.energy,villain_2.energy,villain_1.health,villain_2.health)
        break

if villain_1.health == 0 :
    print(Fore.LIGHTGREEN_EX + "\n♦♦♦ THE WINNER IS VECTOR ♦♦♦")
elif villain_2.health == 0:
    print(Fore.LIGHTGREEN_EX + "\n♦♦♦ THE WINNER IS GRU ♦♦♦")