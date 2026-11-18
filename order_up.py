#lc order up 1
def welcome():#welcome statement
    print("Welcome to the world's grossest resturant.")

#setting up the menu

menu={
    "Main": {
        "booger":6,
        "hot DOG":6,
        "burriTOE":5,
        "SANDwitch":5
    },
    "Drinks" :{
        "Coke and men toes":3,
        "minty orange juice":3,
        "ketchup and mustard":3,
        "Chick-Fil-A sauce":4
    },
    "Sides" : {
        "french thighs":2,
        "sonion rings" :2,
        "mac and knees" :3,
        "mashed potaTOEs": 1

    }
}
welcome()


for category, items in menu.items():
    print(f"{category.upper()}")

    for item, price in items.items():
      print(f" - {item}: ${price}")

def get_valid_item(prompt_text, allowed_categories):
  while True:
    choice = input(prompt_text)
    for cat in allowed_categories:
      if choice in menu[cat]:
        return choice
    print("try again wrong input")

def order():
  order = []
  order.append(get_valid_item("\nSelect a Drink: ", ["Drinks"]))
  order.append(get_valid_item("\nSelect a Main Course : ", ["Main"]))
  order.append(get_valid_item("\nSelect your 1st Side Dish: ", ["Sides"]))
  order.append(get_valid_item("\nSelect your 2nd Side Dish: ", ["Sides"]))

  #placing order
  while True:
    choice = input("\nWhat else do you want? (type 'done' to finish): ")
    if choice.lower() == "done":
      break

    found = False
    for items in menu.values():
      if choice in items:
        found = True

    if found:
      order.append(choice)
    else:
      print("Try again wrong input")
  return order
#endregion





