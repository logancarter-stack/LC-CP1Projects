#lcc combat program 1

import random as rd

print ('Welcome to training! First I need to know some things about you!')
name = input('What is your name: ')
fighter_type = int(input('What fighter type are you(fighter 1, wizard 2, rogue 3) please put the number : '))


fighter_stats= [75,40,100]
if fighter_type== 1:
    print("Here are your stats:")
    print(f"Health: {fighter_stats[0]}")
    print(f"Damage: {fighter_stats[1]}")
    print(f"Defense: {fighter_stats[2]}")

wizard_stats = [100,100,20]
if fighter_type== 2:
    print("Here are your stats:")
    print(f"Health: {wizard_stats[0]}")
    print(f"Damage: {wizard_stats[1]}")
    print(f"Defense: {wizard_stats[2]}")
rogue_stats = [50,60,10]
if fighter_type== 3:
    print("Here are your stats:")
    print(f"Health: {rogue_stats[0]}")
    print(f"Damage: {rogue_stats[1]}")
    print(f"Defense: {rogue_stats[2]}")


player_damage = rd.randint(1,20)
def battle_fighter():
 if fighter_type == '1':
  print("you are a fighter")
opdamage = rd.randint(1,20) 
totalopdamage=   + 5
     
 
fighter_health = 75

wild_attack_damage = totalopdamage * 2

wild_attack_player_damage = wild_attack_damage/2



f_attack = input(f"You are being attacked by a Dire Wolf!\nYou move first!\n\nWhat do you do?\n1. Normal Attack \n2. Wild Attack (you double the damage but you also take 50% damage) \n3. Drink a healing potion (get 9 health)\n4. Flee (50% chance of success): ")
if f_attack == "1":
    wolf_damage = rd.randint(1,20)
    print(f"You attacked the Dire Wolf you did {totalopdamage} and the Dire Wolf did {wolf_damage}")
    if wolf_damage > 75:
        print("You died! Dire Wolf wins")
        if f_attack == "2":
         print(f"You did the wild attack damage and dealt {wild_attack_damage} and you got {wild_attack_player_damage} damage")
        if wild_attack_player_damage >= 75:
            print("You die! Dire Wolf win")
        else:
            print("YOU WIN! somehow...")

    if f_attack == "3":
        new_health = fighter_health + 9
        print(f"You gained {new_health}")
        
    if f_attack == "4":
        escape_chance = rd.randint(1,2)
        if escape_chance == 1:
            print("The Dire Wolf caught upto you and you died!")
        if escape_chance == 2:
            print("You escaped! ")



def battle_wizard():
    if fighter_type == '2':
      print("you are a wizard")
    opdamage = rd.randint(1,20)
    totalopdamage = opdamage + 6
    
    
wizard_health = 100
    
wild_attack_player_damage = rd.randint(1,20)
    
wild_attack_damage = totalopdamage * 2

 
w_attack = input(f"You are being attacked by a Dire Wolf!\nYou move first!\n\nWhat do you do?\n1. Normal Attack\n2. Wild Attack (you can double the damage but you will also take damage) details:\n3. Drink a healing potion (get 9 health)\n4. Flee (50% chance of surviving): ")
if w_attack == "1":
        wolf_damage = rd.randint(1,20)
        print(f"You attacked the Dire Wolf you did {totalopdamage} and the Dire Wolf did {wolf_damage}")
        if wolf_damage >= 100:
            print("You die! Dire Wolf win")
if w_attack == "2":
        print(f"You did the wild attack damage and dealt {wild_attack_damage} and you got {wild_attack_player_damage} damage")
        if wild_attack_player_damage >= 100:
            print("You die! Dire Wolf win")
        else:
            print("YOU WIN! somehow...")
if w_attack == "3":
        new_health = wizard_health+ 9
        print(f"You gained {new_health}")

if w_attack == "4":
        escape_chance = rd.randint(1,2)
        if escape_chance == 1:
            print("The Dire Wolf caught upto you and you died!")
        if escape_chance == 2:
            print("You escaped!")


def battle_rouge():
    if fighter_type == '3':
      print("you are a rouge")
    opdamage = rd.randint(1,20)
    totalopdamage = opdamage + 4
    
    
rouge_health = 50
    
wild_attack_player_damage = totalopdamage
    
wild_attack_damage = totalopdamage * 2
    

r_attack = input(f"You are being attacked by a Dire Wolf!\nYou move first!\n\nWhat do you do?\n1. Normal Attack\n2. Wild Attack (you can double the damage but you will also take damage)\n3. Drink a healing potion (get 9 health)\n4. Flee (50% chance of surviving): ")
if r_attack == "1":
        wolf_damage = rd.randint(1,20)
        print(f"You attacked the Dire Wolf you did {totalopdamage} and the Dire Wolf did {wolf_damage}")
        if wolf_damage >= 50:
            print("You die! Dire Wolf win")
if r_attack == "2":
        print(f"You did the wild attack damage and dealt {wild_attack_damage} and you got {wild_attack_player_damage} damage")
        if wild_attack_player_damage >= 50:
            print("You die! Dire Wolf win")
        else:
            print("YOU WIN! somehow...")
if r_attack == "3":
        new_health = rouge_health + 9
        print(f"You gained {new_health}")
        print(f"But the Dire Wolf attacked you and did {totalopdamage} damage to you so you die")
if r_attack == "4":
         escape_chance = rd.randint(1,2)
         if escape_chance == 1:
            print("The Dire Wolf caught upto you and you died!")
         if escape_chance == 2:
            print("You escaped!")