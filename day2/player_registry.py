"""
1- Add Player
2- Show Players
3- Exit
"""

player_list = []

while True:
    print("""-----------------------------------
    1- Add Player
    2- Show Players
    3- Exit
          -----------------------------------""")

    choice = input("Enter your choice:")

    if choice == "1":
        player = input("Enter player name:")
        player_list.append(player)

    elif choice == "2":
        if len(player_list) == 0:
            print("No players added yet.")
        else:
            for i in range(len(player_list)):
                print(i,player_list[i])

    elif choice == "3":
        print("The program has ended.")
        break

    else:
        print("invalid choice")