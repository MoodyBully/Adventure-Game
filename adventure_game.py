import time
import random
import sys
weapons = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("\nIt's a cold and rainy night as you "
                "sleep soundly in your bed.")
    print_pause("\nYou slowly awake in the middle of the night...")
    print_pause("\nfrom the sound of three subtle taps.")
    print_pause("\nOddly, the echoing sound of each tap seem to come from "
                "three different places in your bedroom.")
    print_pause("\nThe first tap echoes from the closet.")
    print_pause("\nThe second tap echoes from underneath your the bed.")
    print_pause("\nThe third tap echoes from the mirror on your dresser.")


def closet():
    print_pause("\nYou walk to the closet and slowly open the door.")
    if "cape" in weapons:
        print_pause("\nYou have aquired the Cape of Courage from the slain "
                    "Closet Monster, "
                    "there is nothing more to do here.")
        lucky_coin()
    else:
        print_pause("\nThe monster in the closet suddenly jumps out and "
                    "lunges right at you.")
        while True:
            respond_closet = input("\nDo you (1) scream in fear or "
                                   "(2) stand tall?\n")
            if respond_closet == '1':
                print_pause("\n'Ahhh!!' you shout in fear.")
                print_pause("\nConsequently, fear only makes the "
                            "Closet Monster angier and stronger.")
                print_pause("\nYou sprint back to your bed hiding "
                            "under the covers.")
                lucky_coin()
            elif respond_closet == '2':
                print_pause("\nSuddenly, you build the courage to "
                            "stand tall and stare down the Closet Monster.")
                print_pause("\nThe Closet Monster weakens and surrenders "
                            "to your display of courage.")
                print_pause("\nYou are rewarded with the Closet Monster's "
                            "Cape of Courage.")
                weapons.append("cape")
                lucky_coin()
            else:
                print_pause("\nI'm afraid there are only two "
                            "options here...")


def under_bed():
    print_pause("\nYou slowly pull up the hanging covers to peep "
                "underneath your bed.")
    if "t-shirt" in weapons:
        print_pause("\nYou have aquired the T-shirt of Truth from the slain "
                    "Bed Bug, there is nothing more to do here.")
        lucky_coin()
    else:
        print_pause("\nThe monster, a giant Bed Bug, slithers from "
                    "underneath the bed and attempts to coil "
                    "itself around your body.")
        while True:
            respond_bed = input("\nDo you (1) scream in fear or (2) "
                                "show your strength?\n")
            if respond_bed == '1':
                print_pause("\nThe Bed Bug is strengthened by your fear "
                            "and squeezes around your body tighter.")
                print_pause("\nYou pass out from the monster's tight grip "
                            "as it returns you to your bed.")
                print_pause("\nYou soon awaken.")
                lucky_coin()
            elif respond_bed == '2':
                print_pause("\nYou utilize all of your strength to break "
                            "from the Bed Bug's coiling grip as it "
                            "then retreats.")
                print_pause("\nYou are now rewarded with the Bed Bug's "
                            "T-shirt of Truth displaying a large 'T' across "
                            "your chest.")
                weapons.append("t-shirt")
                lucky_coin()
            else:
                print_pause("\nI'm afraid there are only two "
                            "options here...")


def mirror():
    print_pause("\nYou make your way toward the dresser and "
                "peer into the mirror.")
    print_pause("\nIn place of your own reflection, you see the HORRIFIC "
                "MIRROR MONSTER!!!")
    print_pause("\nImmediately, with its long claws extended, "
                "the Mirror Monster reaches out and grabs you!")
    while True:
        respond_mirror = input("\nDo you want to (1) scream in fear or (2) "
                               "fight?\n")
        if respond_mirror == '2':
            if "cape" in weapons:
                print_pause("\nQuickly, with your Cape of Courage you "
                            "cover the Mirror Monster's dreadful face.")
                print_pause("\nThis temporaly blinds the monster but you "
                            "still need the T-shirt of Truth!")
                if "t-shirt" in weapons:
                    print_pause("\nFortunately you aquired the T-shirt "
                                "of Truth after defeating the Bed Bug.")
                    print_pause("\nBlinded by the cape the Mirror Monster "
                                "frantically lashes for you.")
                    print_pause("\nIts long claws graze the 'T' on "
                                "your T-shirt of Truth.")
                    print_pause("\nThis causes the Mirror Monster to "
                                "desinigrate into the air revealing "
                                "your true self in the mirror.")
                    print_pause("\nYou have defeated all three monsters "
                                "and can return to your bed in peace.")
                    play_again()
                else:
                    print_pause("\nWithout the T-shirt of Truth you "
                                "are forced to retreat to your bed.")
                    lucky_coin()
            else:
                print_pause("\nYou are not yet equipped to defeat "
                            "the Mirror Monster.")
                print_pause("\nGo back to bed!")
                lucky_coin()
        elif respond_mirror == '1':
            print_pause("\nYou attempt to scream but no sound "
                        "comes from your mouth as you are frozen "
                        "with fear.")
            print_pause("\nYou shamefully run back to your bed "
                        "and hide under the covers.")
            lucky_coin()
        else:
            print_pause("\nI'm afraid there are only two options here...")


def lucky_coin():
    print_pause("\nYou bring out your lucky coin to decide your next move.")
    print_pause("\n'Heads' the closet, 'Tails' under the bed.")
    coin = random.choice(["heads", "tails", "put_away"])
    if coin == 'heads':
        print("\nHeads it is...")
        closet()
    elif coin == 'tails':
        print("\nTails it is...")
        under_bed()
    elif coin == 'put_away':
        print("\nRather than leaving it to chance you decide to head "
              "straight to the mirror.")
        mirror()


def play_again():
    while True:
        play_again = input("\nDo you want to play again? (y/n)\n")
        if play_again == 'y':
            print_pause("\nGood luck...")
            weapons.clear()
            adventure_game()
        elif play_again == 'n':
            print_pause("\nVery well. Go ahead and 'tap' your way on out "
                        "of this game, but before you go...\n")
            print_pause("\n\n\n\nJust before falling back to sleep, "
                        "your mom peeps into your room "
                        "to check on you.")
            print_pause("\nSeeing that all is well, she steps back "
                        "closing the door behind her.")
            print_pause("\nBefore the door shuts, she whispers...")
            print_pause("\ntap...tap...tap...you win.\n")
            sys.exit()
        else:
            print_pause("\nI'm sorry, but I do not understand.")


def adventure_game():
    intro()
    lucky_coin()
adventure_game()
