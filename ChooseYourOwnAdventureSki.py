while True:
    answer = input("Would you like to play the ski adventure game? (yes/no)").lower().strip()

    if answer == 'yes':
        name = input("What is your character's name?")
        health = 10
        intox = 0
        print(f'{name} is going skiing today. Hopefully you can make it through the whole day!\n')
        breakfast = input('What is your choice of breakfast beverage, Coffee or Fireball?\n').lower().strip()
        if breakfast == 'coffee':
            print('Energized and ready for the day, and a bowel movement.\n')
            health += 1
        elif breakfast == 'fireball':
            print('You feel the hangover disappearing, LETS GO!\n')
            intox += 1
        else:
            print('Not fireball OR coffee, alright weird choice??\n')

        stretchQ = input('Liam is looking for his lunch so you have 5 minutes before we leave. Do you stretch or smoke?\n').lower().strip()
        if stretchQ == 'stretch':
            print('You feel nimble!\n')
            health += 1
        elif stretchQ == 'smoke':
            print('Any stress is all gone. Chill day ahead.\n')
            intox += 1
        else:
            print('neither? aight\n')

        firstRun = input('First run of the day do you opt for:\n (1) huckleberry and a slow warm up \n (2) A fast North Road to get the legs burning \n Enter 1 or 2:')
        if firstRun == '1':
            print('A smart call! Great first run and the legs are nice and stretched!\n')
            run = input('On the next run you can choose a green, blue or black run! How skilled are you feeling? (green/blue/black)').lower().strip()
            if run == 'green':
                    bear = input('Your green run is going nice and slow until you see a bear ahead on the trail!! Do you stop and wait or shred past? (stop/shred)').lower().strip()
                    if bear == 'shred':
                        print('You continue riding and pop a 360 as you pass the bear. The bear looks impressed and begins to clap! You Win!!')

                    else:
                        print('The bear says "Wow, are you scared? Just cause I\'m a bear you think I\'m evil? Not cool bro!" The bear eats you and you lose! ')

            elif run == 'blue':
                    if intox > 3:
                        print('You are feeling a little drunk and catch your edge. You tumble down the hill and lay in the bottom in a heap of gear. You lose!')
                    else:
                        print('That run was a little harder than you expected, good thing you haven\'t been drinking!')
                        lift = input('Standing in the lift line you can either ride up with a cute ski girl, or a mountain patroller. (girl/patroller)').strip().lower()
                        if lift == 'girl':
                            print('You have a great chat with this snow bunny on the ride up. You are distracted trying to get her number and drop your helmet and gloves off the lift. YOU LOSE!')
                        elif lift == 'patroller':
                            flask = input('The man in the red jacket and great stache introduces himself as patroller Nick. Do you offer him your flask? (yes/no)').strip().lower()
                            if flask == 'no':
                                print('Good thinking! He tells you about a dangerous run to avoid due to rocks. YOU WIN!')
                            else:
                                print(f'\"Sorry {name} you can\'t drink on the lift, I\'m gonna have to take your pass!\" -Nick YOU LOSE!')
                        else:
                            print('You are distracted trying to decide and the chair hits you in the calves. You get drug along the loading ramp and everyone laughs, YOU LOSe')
            else:
                    print('You go down a black diamond run! Your skis cross after you hit a rock!! You wipe out and your day is over. You lose!')
        elif firstRun == '2':
            print('Little ambitious! You crash into a tree before you can remember how skiing works! Ouch!\n')
            health -= 5
            afterCrash = input('First crash of the day. Do you \n (1) Go straight to the pub to refuel \n (2) Take the second run easier \n Enter 1 or 2')
            if afterCrash == '1':
                print('That beer totally makes the pain go away!\n')
                print('You spend the afternoon drinking in the pub and forget about skiing. Some might consider that a win?!?')
                intox += 1
            elif afterCrash == '2':
                print('Knee feels a little better after that second run.')
                health += 2
                park = input('You ride into the terrain park and can either choose the jump line or a box and rail. (jump/rail)').strip().lower()
                if park == 'jump':
                    print('You spread eagle all three jumps in a row. Some kid on the lift cheers. You are the king of the mountain, YOU WIN!')
                elif park == 'rail':
                    print('You kill it on the box but slip out on the rail and taco over it. You might lose you lunch! YOU LOSE')
                else:
                    print('You ride through the park without hitting any features. The park rats yell and embarrass you. You feel weak, GAME OVER, YOU LOSE!')
            else:
                print('invalid entry, you lose lol!')
        else:
            print('Do you know what the first run is meant to be for?\n')

    else:
        print("That's too bad!")
        break