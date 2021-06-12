import time as time
import math as math
import random

print("Hello, welcome to the ultimate super fun game!")
time.sleep(0.7)
name = input("What is your name? ")
opponent = input("What would you like your opponent to be called? ")
print("-----------------------------")
helpchoice = str(input("Do you know how atk/spatk and def/spdef works? [Y/N] "))
if helpchoice == "N" or helpchoice == "n":
  time.sleep(1)
  print("There are two types of attacks, attack and special attack.")
  time.sleep(3)
  print("When calculating damage dealt by a normal attack, the opponent's defense stat is used.")
  time.sleep(4.5)
  print("However, when calculating damage dealt by a special attack, the opponent's special defense stat is used.")
else:
  print("Great! Moving on...")

time.sleep(0.5)
print("Remember, the user with the greater speed stat goes first / this may determine the winner in certain matches.")
time.sleep(1)
print("-----------------------------")
user_hp = random.randint(150, 250)
user_atk = random.randint(50, 150)
user_spatk = random.randint(50, 250-user_atk)
user_def = random.randint(50, 150)
user_spdef = random.randint(50, 250-user_def)
user_spd = random.randint(50, 325 - user_hp)

print(name + "'s stats are: ")
print("HEALTH: ", user_hp)
print("ATTACK: ", user_atk)
print("SPECIAL ATTACK: ", user_spatk)
print("DEFENSE: ", user_def)
print("SPECIAL DEFENSE: ", user_spdef)
print("SPEED: ", user_spd)
print("-----------------------------")

time.sleep(0.7)
op = input("Which difficulty would you like? You can choose Easy, Normal, or Hard. [E/N/H] ")

while op != "E" and op != "e" and op != "N" and op != "n" and op != "H" and op != "h":
  print("That's not a valid difficulty setting!")
  time.sleep(0.3)
  op = input("Which difficulty would you like? You can choose Easy, Normal, or Hard. [E/N/H] ")

if op == 'E' or op == 'e':
  op_hp = random.randint(200, 275)
  op_atk = random.randint(100, 195)
  op_spatk = random.randint(100, 295 - op_atk)
  op_def = random.randint(100, 175)
  op_spdef = random.randint(100, 275 - op_def)
  op_spd = random.randint(100, 350 - op_hp)
elif op == 'N' or op == 'n':
  op_hp = random.randint(230, 305)
  op_atk = random.randint(130, 225)
  op_spatk = random.randint(130, 355 - op_atk)
  op_def = random.randint(130, 225)
  op_spdef = random.randint(130, 355 - op_def)
  op_spd = random.randint(130, 330 - (op_hp /2))
elif op == 'H' or op == 'h':
  op_hp = random.randint(260, 335)
  op_atk = random.randint(160, 255)
  op_spatk = random.randint(160, 415 - op_atk)
  op_def = random.randint(160, 255)
  op_spdef = random.randint(160, 415 - op_def)
  op_spd = random.randint(160, 360 - (op_hp /2))

if op == 'E' or op == 'e':
  pt_remaining = 200  
elif op == 'N' or op == 'n':
  pt_remaining = 235
elif op == 'H' or op == 'h':
  pt_remaining = 300

print("You can put up to 100 points for each stat")
print("You have " + str(pt_remaining) + " points left.")
time.sleep(1)
user_hp_pt = int(input("How many points would you like to spend on health? "))

while user_hp_pt < 0:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_hp_pt = int(input("How many points would you like to spend on health? "))

while user_hp_pt > 100:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_hp_pt = int(input("How many points would you like to spend on health? "))

user_hp = user_hp + user_hp_pt

pt_remaining = pt_remaining - user_hp_pt
print("You have " + str(pt_remaining) + " points left.")


time.sleep(1)
user_atk_pt = int(input("How many points would you like to spend on attack? "))

while user_atk_pt > pt_remaining:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_atk_pt = int(input("How many points would you like to spend on attack? "))

while user_atk_pt < 0:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_atk_pt = int(input("How many points would you like to spend on attack? "))

while user_atk_pt > 100:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_atk_pt = int(input("How many points would you like to spend on attack? "))

user_atk = user_atk + user_atk_pt

pt_remaining = pt_remaining - user_atk_pt
print("You have " + str(pt_remaining) + " points left.")


time.sleep(1)
user_spatk_pt = int(input("How many points would you like to spend on special attack? "))

while user_spatk_pt > pt_remaining:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_spatk_pt = int(input("How many points would you like to spend on special attack? "))

while user_spatk_pt < 0:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_spatk_pt = int(input("How many points would you like to spend on special attack? "))

while user_spatk_pt > 100:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_spatk_pt = int(input("How many points would you like to spend on special attack? "))

user_spatk = user_spatk + user_spatk_pt

pt_remaining = pt_remaining - user_spatk_pt
print("You have " + str(pt_remaining) + " points left.")


time.sleep(1)
user_def_pt = int(input("How many points would you like to spend on defense? "))

while user_def_pt > pt_remaining:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_def_pt = int(input("How many points would you like to spend on defense? "))

while user_def_pt < 0:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_def_pt = int(input("How many points would you like to spend on defense? "))

while user_def_pt > 100:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_def_pt = int(input("How many points would you like to spend on defense? "))

user_def = user_def + user_def_pt

pt_remaining = pt_remaining - user_def_pt
print("You have " + str(pt_remaining) + " points left.")


time.sleep(1)
user_spdef_pt = int(input("How many points would you like to spend on special defense? "))

while user_spdef_pt > pt_remaining:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_spdef_pt = int(input("How many points would you like to spend on special defense? "))

while user_spdef_pt < 0:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_spdef_pt = int(input("How many points would you like to spend on special defense? "))

while user_spdef_pt > 100:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_spdef_pt = int(input("How many points would you like to spend on special defense? "))

user_spdef = user_spdef + user_spdef_pt

pt_remaining = pt_remaining - user_spdef_pt
print("You have " + str(pt_remaining) + " points left.")


time.sleep(1)
user_spd_pt = int(input("How many points would you like to spend on speed? "))

while user_spd_pt > pt_remaining:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_spd_pt = int(input("How many points would you like to spend on speed? "))

while user_spd_pt < 0:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_spd_pt = int(input("How many points would you like to spend on speed? "))

while user_spd_pt > 100:
  print("That is an invalid number. Try again.")
  
  
  time.sleep(1)
  user_spd_pt = int(input("How many points would you like to spend on speed? "))

user_spd = user_spd + user_spd_pt

time.sleep(2)
print("-----------------------------")
print(name + "'s stats are: ")
print("HEALTH: ", user_hp)
print("ATTACK: ", user_atk)

print("SPECIAL ATTACK: ", user_spatk)
print("DEFENSE: ", user_def)
print("SPECIAL DEFENSE: ", user_spdef)
print("SPEED: ", user_spd)

print("-----------------------------")
print(opponent + "'s stats are: ")
print("HEALTH: ", op_hp)
print("ATTACK: ", op_atk)
print("SPECIAL ATTACK: ", op_spatk)
print("DEFENSE: ", op_def)
print("SPECIAL DEFENSE: ", op_spdef)
print("SPEED: ", op_spd)
time.sleep(1)
print("-----------------------------")
print("A means an (A)ttack move while S means a (S)pecial Attack move")

if user_spd > op_spd:
  while user_hp > 0 and op_hp > 0:
    crt = random.randint(1, 100)
    if crt > 75:
      power = 1.5
    elif crt < 22:
      power = 0.5
    else:
      power = 1
    user_move = str(input("Which type of move would you like to do? [A/S] "))
    if user_move == "A":
      user_damage = math.floor((((((20) * 75 *user_atk) / (50 * op_def)) +2) * power ) * random.uniform(0.85, 1.15))
    else: 
      user_damage = math.floor((((((20) * 75 *user_spatk) / (50 * op_spdef)) +2) * power ) * random.uniform(0.85, 1.15))
    crt2 = random.randint(1, 100)
    if crt2 > 75:
      power2 = 1.5
    elif crt2 < 22:
      power2 = 0.5
    else:
      power2 = 1
    choose = random.randint(1, 100)
    if choose < 50:
      op_damage = math.floor((((((20) * 75 *op_atk) / (50 * user_def)) +2) * power2 ) * random.uniform(0.85, 1.15))
    else: 
      op_damage = math.floor((((((20) * 75 *op_spatk) / (50 * user_spdef)) +2) * power2 ) * random.uniform(0.85, 1.15))
    miss = random.randint(1, 100)
    miss2 = random.randint(1, 100)
    if miss > 90:
      user_damage = 0
    if miss2 > 90:
      op_damage = 0


    op_hp = op_hp - user_damage
    user_hp = user_hp - op_damage
    time.sleep(0.3)
    if power > 1.2 and miss <= 90:
      print("Critical Damage!!!")
    if miss > 90:
      print("Your attack missed!")
    print("You have dealt",str(user_damage), "damage!")
    time.sleep(0.3)
    if power < 0.7 and miss <= 90:
      print("It wasn't very effective...")
    print(opponent + "'s health is now", op_hp, ".")
    print(" ")
    time.sleep(0.3)
    if op_hp < 0:
      print("Congrats " + name + "! You won the game!")
      exit()
    if power2 > 1.2 and miss2 <= 90:
      print("Critical Damage!!!")
    if miss2 > 90:
      print(opponent + "'s attack missed!")
    print(opponent + " has dealt",str(op_damage), "damage!")
    time.sleep(0.3)
    if power2 < 0.7 and miss2 <= 90:
      print("It wasn't very effective...")
    print("Your health is now", user_hp, ".")
    time.sleep(0.5)
    print("-----------------------------")
    
#implement moves
#6 moves
#attackstat
#learn moves before fighting



else:
  while user_hp > 0 and op_hp > 0:
    crt = random.randint(1, 100)
    if crt > 75:
      power = 1.5
    elif crt < 22:
      power = 0.5
    else:
      power = 1
    user_move = str(input("Which type of move would you like to do? [A/S] "))
    if user_move == "A":
      user_damage = math.floor((((((20) * 75 *user_atk) / (50 * op_def)) +2) * power ) * random.uniform(0.85, 1.15))
    else: 
      user_damage = math.floor((((((20) * 75 *user_spatk) / (50 * op_spdef)) +2) * power ) * random.uniform(0.85, 1.15))
    crt2 = random.randint(1, 100)
    if crt2 > 75:
      power2 = 1.5
    elif crt2 < 22:
      power2 = 0.5
    else:
      power2 = 1
    choose = random.randint(1, 100)
    if choose < 50:
      op_damage = math.floor((((((20) * 75 *op_atk) / (50 * user_def)) +2) * power2 ) * random.uniform(0.85, 1.15))
    else: 
      op_damage = math.floor((((((20) * 75 *op_spatk) / (50 * user_spdef)) +2) * power2 ) * random.uniform(0.85, 1.15))
    miss = random.randint(1, 100)
    miss2 = random.randint(1, 100)
    if miss > 90:
      user_damage = 0
    if miss2 > 90:
      op_damage = 0
    user_hp = user_hp - op_damage
    op_hp = op_hp - user_damage
    time.sleep(0.3)
    if power2 > 1.2 and miss2 <= 90:
      print("Critical Damage!!!")
    if miss2 > 90:
      print(opponent + "'s attack missed!")
    print(opponent + " has dealt",str(op_damage), "damage!")
    time.sleep(0.3)
    if power2 < 0.7 and miss2 <= 90:
      print("It wasn't very effective...")
    print("Your health is now", user_hp, ".")
    time.sleep(1)
    if user_hp < 0:
      print("Oof, you lost. Better luck next time!")
      exit()
    print(" ")
    time.sleep(0.3)
    if power > 1.2 and miss <= 90:
      print("Critical Damage!!!")
    if miss > 90:
      print("Your attack missed!")
    print("You have dealt",str(user_damage), "damage!")
    time.sleep(0.3)
    if power < 0.7 and miss <= 90:
      print("It wasn't very effective...")
    print(opponent + "'s health is now", op_hp, ".")
    time.sleep(0.5)
    print("-----------------------------")




if user_hp > op_hp:
  print("Congrats " + name + "! You won the game!")
else:
  print("Oof, you lost. Better luck next time!")
'''
class Character:
  def __init__(self, name, health, atk_points, spatk_points, def_points, spdef_points, spd_points,  moves):
    self.name = name
    self.health = health
    self.atk_points = atk_points
    self.spatk_points = spatk_points
    self.def_points = def_points
    self.spdef_points = spdef_points
    self.spd_points = spd_points
    self.moves = moves
    moves = []
'''