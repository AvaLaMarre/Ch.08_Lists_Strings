import os

'''
ADVENTURE GAME (4pts)
-----------------
1. Use the pseudo-code on the website to help you set up the basic move through the house program
2. Print off a physical map for players to use with your program
3. Expand your program to make it a real adventure game

'''
"Exposition Of The Game"
print("\u001b[39;1m")
print("...Welcome To The Maze...")
print("You Made Enemies With The Lord Of Your Town, They Throw You Into Maze With Winding Hallways And Locked Doors")
print("To Get Out Of The Maze Alive You Will Need To Find Your Way Through Rooms And Find" "\u001b[32;1m"+" Keys " "\u001b[39;1m"+ "To Unlock The Doors")
print("Doors Will Not Open Without Keys and Keys Can Be In Any Room")
print("To Make Your Way Through The Maze You Will Have To Find Keys To Go Through Locked Doors")
print("Doors Are Shown As | X |")
print("Will You Escape?")
print("\u001b[31;1m"+"                ___-------___")
print("         ___---               ---___")
print("       /                             \ ")
print("     /                                \ ")
print("    |  |                             | |")
print("    |  \   --__              ___-    / |")
print("   |   /  ___   \          /   ___   \  | ")
print("   |  /  /   |               /    \  \  | ")
print("   |    |  ?  \             /  ?   |    | ")
print("   |    \     |    /  \     \     /     | ")
print("    \_\  \___/    |    |     \___/   /_/ ")
print("       \_______   |/\/\|    ________/ ")
print("            |    | |   |   |  | ")
print("            |_|_-|_|_|_|_|-|__| ")
print("\u001b[39;1m")
print()
input("Enter To Continue...")

key = 0
key2 = 0
key3 = 0
lock = -1
lock2 = -1
lock3 = -1
"Set Up Of Game,    N E S W"
room_list = []
room = ["ROOM: 0 |To the South Is A Locked Door. There Are 2 Ways You Can Go: N, S", None, 1, None, None, lock]
room_list.append(room)
room = ["ROOM: 1 |You Enter From The West, Seeing A Key Laying On The Floor You Grab It. There Is 1 Way You Can Go: W", None, None, None, 0, key]
room_list.append(room)
room = ["ROOM: 2 |You Enter The Main Part Of The Maze, There 3 Ways You Can Go: N, E, W", 0, 3, None, 4]
room_list.append(room)
room = ["ROOM: 3 |There Are 3 Ways You Can Go: E, S, W", None, 12, 9, 2]
room_list.append(room)
room = ["ROOM: 4 |There Are 3 Ways You Can Go: E, S, W", None, 2, 6, 5]
room_list.append(room)
room = ["ROOM: 5 |There Is 1 Way You Can Go: E", None, 4, None, None]
room_list.append(room)
room = ["ROOM: 6 |There Are 3 Ways You Can Go: N, S, W", 4, None, 8, 7]
room_list.append(room)
room = ["ROOM: 7 |There Is 1 Way You Can Go: E ", None, 6, None, None]
room_list.append(room)
room = ["ROOM: 8 |There Is 1 Way You Can Go: N", 6, None, None, None]
room_list.append(room)
room = ["ROOM: 9 |There Are 3 Ways You Can Go: N, S, W", 3, None, 11, 10]
room_list.append(room)
room = ["ROOM: 10 |There Is 1 Way You Can Go: E", None, 9, None, None]
room_list.append(room)
room = ["ROOM: 11 |There Is 1 Way You Can Go: N", 9, None, None, None]
room_list.append(room)
room = ["ROOM: 12 |There Are 3 Ways You Can Go: E, S, W", None, 13, 17, 3]
room_list.append(room)
room = ["ROOM: 13 |There Are 2 Ways You Can Go: S, W", None, None, 14, 12]
room_list.append(room)
room = ["ROOM: 14 |There Are 3 Ways You Can Go: N, S, W", 13, None, 15, 16]
room_list.append(room)
room = ["ROOM: 15 |There Is 1 Way You Can Go: E", None, 14, None, None]
room_list.append(room)
room = ["ROOM: 16 |There Is 1 Way You Can Go: N", 14, None, None, None]
room_list.append(room)
room = ["ROOM: 17 |There Are 3 Ways You Can Go: N, S, W", 12, None, 19, 18]
room_list.append(room)
room = ["ROOM: 18 |There Is 1 Way You Can Go: E", None, 17, None, None]
room_list.append(room)
room = ["ROOM: 19 |There Are 2 Ways You Can Go: N, S", 17, None, 20, None]
room_list.append(room)
room = ["ROOM: 20 |There Are 3 Ways You Can Go: N, E, S", 19, 21, 29, None]
room_list.append(room)
room = ["ROOM: 21 |There Are 2 Ways You Can Go: S, W", None, None, 22, 20]
room_list.append(room)
room = ["ROOM: 22 |There Are 2 Ways You Can Go: N, S", 21, None, 23, None]
room_list.append(room)
room = ["ROOM: 23 |There Are 3 Ways You Can Go: N, S, W", 22, None, 24, 26]
room_list.append(room)
room = ["ROOM: 24 |There Are 2 Ways You Can Go: N, W", 23, None, None, 25]
room_list.append(room)
room = ["ROOM: 25 |Seeing A Key Laying On The Floor You Grab It. There Is 1 Way You Can Go: E", None, 24, None, None, key3]
room_list.append(room)
room = ["ROOM: 26 |There Are 2 Ways You Can Go: E, W", None, 23, None, 27]
room_list.append(room)
room = ["ROOM: 27 |There Are 2 Ways You Can Go: E, S", None, 26, 28, None]
room_list.append(room)
room = ["ROOM: 28 |There Is 1 Way You Can Go: N", 27, None, None, None]
room_list.append(room)
room = ["ROOM: 29 |There Are 2 Ways You Can Go: N, S", 20, None, 30, None]
room_list.append(room)
room = ["ROOM: 30 |There Are 2 Ways You Can Go: N, E", 31, 29, None, None]
room_list.append(room)
room = ["ROOM: 31 |There Are 2 Ways You Can Go: S, W", None, None, 30, 32]
room_list.append(room)
room = ["ROOM: 32 |There Are 2 Ways You Can Go: E, W", None, 31, None, 33]
room_list.append(room)
room = ["ROOM: 33 |There Are 4 Ways You Can Go: N, E, S, W", 34, 32, 38, 35]
room_list.append(room)
room = ["ROOM: 34 |There Is 1 Way You Can Go: S", None, None, 33, None]
room_list.append(room)
room = ["ROOM: 35 |There Are 2 Ways You Can Go: N, E", 36, 33, None, None]
room_list.append(room)
room = ["ROOM: 36 |There Are 2 Ways You Can Go: N, S", 37, None, 35, None]
room_list.append(room)
room = ["ROOM: 37 |Seeing A Key Laying On The Floor You Grab It. There Is 1 Way You Can Go: S", None, None, 36, None, key3]
room_list.append(room)
room = ["ROOM: 38 |To the South Is A Locked Door. There Are 2 Ways You Can Go: N, S", 33, None, None, None, lock2]
room_list.append(room)
room = ["ROOM: 39 |There Are 2 Ways You Can Go: N, E", 38, 40, None, None]
room_list.append(room)
room = ["ROOM: 40 |There Are 2 Ways You Can Go: N, W ", 41, None, None, 39]
room_list.append(room)
room = ["ROOM: 41 |There Are 2 Ways You Can Go: N, S ", 42, None, 40, None]
room_list.append(room)
room = ["ROOM: 42 |There Are 2 Ways You Can Go: N, S", 43, None, 41, None]
room_list.append(room)
room = ["ROOM: 43 |There Are 2 Ways You Can Go: E, S", None, 44, 42, None]
room_list.append(room)
room = ["ROOM: 44 |There Are 2 Ways You Can Go: S, W ", None, None, 45, 43]
room_list.append(room)
room = ["ROOM: 45 |There Are 2 Ways You Can Go: N, S", 44, None, 47, None]
room_list.append(room)
room = ["ROOM: 46 |There Is 1 Way You Can Go: E", None, 47, None, None]
room_list.append(room)
room = ["ROOM: 47 |There Are 3 Ways You Can Go: N, E, W ", 45, 48, None, 46]
room_list.append(room)
room = ["ROOM: 48 |To the South Is A Locked Door. There Are 2 Ways You Can Go: S, W", None, None, None, 47, lock3]
room_list.append(room)
'''Room 49'''
room = ["ROOM: ? |Your See The Light At The End Of The Tunnel, You Won: "]
room_list.append(room)

currentRoom = 0
done = False
turns = 0
wall = 0
"Actual Game"
while not done:
    print("")
    print(room_list[currentRoom][0])
    if len(room_list[currentRoom]) < 2:
        done = True
        print("As You Rise Up The Staircase You Feel The Sun Hit Your Face...")
        print()
        print()
        break
    if len(room_list[currentRoom]) > 5:
        if lock > -1:
            room_list[0] = ["ROOM: 0 |With The Key The Door Opens. There Are 2 Ways You Can Go: N, S", None, 1, 2, None]
        if lock2 > -1:
            room_list[38] = ["ROOM: 38 |With The Key The Door Opens, There Are 2 Ways You Can Go: N, S", 33, None, 39, None]
        if lock3 > -1:
            room_list[48] = ["ROOM: 48 |With The Key The Door Opens, There Are 2 Ways You Can Go: S, W", None, None, 49, 47]
        if currentRoom == 1:
            lock += 1
            key += 1
            print("Obtained " + "\u001b[32;1m" "Key 1" + "\u001b[39;1m" + " To Lock One")
            room_list[1] = ["ROOM: 1 |Key Room, Key Is Gone", None, None, None, 0]
            room_list[0] = ["ROOM: 0 | With The Key The Door Opens", None, 1, 2, None]
        if currentRoom == 25:
            if key2 == 0:
                lock2 += 1
                key2 += 1
                print("Obtained " + "\u001b[32;1m" "Key 2" + "\u001b[39;1m" + " To Lock Two")
                room_list[25] = ["ROOM: 25 |Room Description, key", None, 24, None, None, key2]
                room_list[38] = ["ROOM: 0 | With The Key The Door Opens", None, 1, 2, None]
        if currentRoom == 37:
            lock3 += 1
            key3 += 1
            print("Obtained " + "\u001b[32;1m" "Key 3" + "\u001b[39;1m" + " To Lock Three")
            room_list[37] = ["ROOM: 37 |Room Description, key", None, None, 36, None, key3]
            room_list[48] = ["ROOM: 48 |With The Key The Door Opens, There Are 2 Ways You Can Go: S, W", None, None, 49, 47]

    direction = input("What Direction Do You Want To Go?:")

    if direction.lower() == "north" or direction.lower() == "n":
        nextRoom = room_list[currentRoom][1]
        if nextRoom is None:
            print("You Cant Go North, Try Again. Its Either A Wall Or The Way Is Locked,")
            wall += 1
        else:
            currentRoom = nextRoom
            print("You Go North")
            turns += 1
    elif direction.lower() == "east" or direction.lower() == "e":
        nextRoom = room_list[currentRoom][2]
        if nextRoom is None:
            print("You Cant Go East, Try Again. Its Either A Wall Or The Way Is Locked,")
            wall += 1
        else:
            currentRoom = nextRoom
            print("You Go East")
            turns += 1
    elif direction.lower() == "south" or direction.lower() == "s":
        nextRoom = room_list[currentRoom][3]
        if nextRoom is None:
            print("You Cant Go South, Try Again. Its Either A Wall Or The Way Is Locked,")
            wall += 1
        else:
            currentRoom = nextRoom
            print("You Go South")
            turns += 1
    elif direction.lower() == "west" or direction.lower() == "w":
        nextRoom = room_list[currentRoom][4]
        if nextRoom is None:
            print("You Cant Go West, Try Again. Its Either A Wall Or The Way Is Locked,")
            wall += 1
        else:
            currentRoom = nextRoom
            print("You Go West")
            turns += 1
    elif direction.lower() == "quit" or direction.lower() == "q":
        done = True
        break
    else:
        print("Sorry This Command Does Not Exist, Try Again. Type N, E, S, W, or Q")

print()
print("Stepping Out Of The Tunnel You Feel The Sun Against Your Face")
print("Your Free..")
print()
print("You Passed Through", turns, "Rooms")
print("You Ran Into ", wall, )
