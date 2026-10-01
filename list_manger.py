# LC list manger 1
shopping_list = []
while True:

    #Write your code here
    action =input("what do you want to do: add, remove , view, exit: ")
    if action == "add":
        added_item = input("what do you want to add: ")
        shopping_list.append(added_item)
        print ("here is your list")
        print(*shopping_list )
    elif action == "remove":
        removed_item =input("what item from your list do you want to remove")
        shopping_list.remove(removed_item)
        print ("here is your list")
        print(*shopping_list )
    elif action == "view":
        print ("here is your list")
        print(*shopping_list)       
    elif action == "exit":
        break
    else:
        print('that was not an action' )