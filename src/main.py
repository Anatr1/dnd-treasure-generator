import os
import sys
import utils
import time



def generate_single_treasure(cr, save_to_file=False):
    print("Single treasure")
    if cr <= 4:
        table = "0_4"
    elif cr <= 10:
        table = "5_10"
    elif cr <= 16:
        table = "11_16"
    else:
        table = "17+"
        
    # Read the file
    with open(f"../tables/single_treasure_{table}.txt") as f:
        lines = f.readlines()
        roll = utils.roll_d100()
        print(f"Rolled: {roll}")
        for line in lines:
            # Parse first column
            min_roll = int(line.split("\t")[0].split("–")[0])
            max_roll = int(line.split("\t")[0].split("–")[1])
            if roll >= min_roll and roll <= max_roll:
                copper, silver, electrum, gold, platinum = utils.parse_money_line(line)
                
                print(f"Copper: {copper}")
                print(f"Silver: {silver}")
                print(f"Electrum: {electrum}")
                print(f"Gold: {gold}")
                print(f"Platinum: {platinum}")
                
                if save_to_file:
                    with open("../generated_treasures.txt", "wa") as f:
                        now = time.strftime("%c")
                        f.write(f"Treasure generated on: {now} from a single treasure table of CR {cr}\n")
                        f.write(f"\tCopper: {copper}\n")
                        f.write(f"\tSilver: {silver}\n")
                        f.write(f"\tElectrum: {electrum}\n")
                        f.write(f"\tGold: {gold}\n")
                        f.write(f"\tPlatinum: {platinum}\n")
        

def main():
    print("Enter challenge rating: ")
    cr = int(input())
    
    # Sanity check
    while cr < 0:
        print("Invalid input")
        cr = int(input())
        
    print("Single treasure or hoard? (s/h)")
    treasure_type = input()
    
    # Sanity check
    while treasure_type != "s" and treasure_type != "h":
        print("Invalid input")
        treasure_type = input()
        
    if treasure_type == "s":
        generate_single_treasure(cr)
    #else:
        #generate_hoard(cr)
        







if __name__ == "__main__":
    main()