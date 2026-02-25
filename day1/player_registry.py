name = input("Enter the name of the player:")
surname = input("Enter the surname of the player:")
age = int(input("Enter the age of the player:"))
team = input("Enter the team of the player:")

informations = [name,surname,age,team]

print("Player information:\nName:{}\nSurname:{}\nAge:{}\nTeam:{}"
      .format(informations[0],informations[1],informations[2],informations[3]))