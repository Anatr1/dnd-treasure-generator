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
            if "–" not in line:
                min_roll = int(line.split("\t")[0])
                max_roll = int(line.split("\t")[0])
            else:
                min_roll = int(line.split("\t")[0].split("–")[0])
                max_roll = int(line.split("\t")[0].split("–")[1])
                
            if roll >= min_roll and roll <= max_roll:
                copper, silver, electrum, gold, platinum = utils.parse_money_line(line)
                
                print(f"\tCopper: {copper}")
                print(f"\tSilver: {silver}")
                print(f"\tElectrum: {electrum}")
                print(f"\tGold: {gold}")
                print(f"\tPlatinum: {platinum}")
                
                if save_to_file:
                    with open("../generated_treasures.txt", "a") as f:
                        now = time.strftime("%c")
                        f.write(f"Treasure generated on: {now} from a single treasure table of CR {cr}\n")
                        f.write(f"\tCopper: {copper}\n")
                        f.write(f"\tSilver: {silver}\n")
                        f.write(f"\tElectrum: {electrum}\n")
                        f.write(f"\tGold: {gold}\n")
                        f.write(f"\tPlatinum: {platinum}\n")
                        
                break
        

def generate_hoard(cr, save_to_file=False):
    print("Hoard")
    if cr <= 4:
        table = "0_4"
    elif cr <= 10:
        table = "5_10"
    elif cr <= 16:
        table = "11_16"
    else:
        table = "17+"
        
    # Read the file
    with open(f"../tables/treasure_hoard_{table}.txt") as f:
        lines = f.readlines()
        copper, silver, electrum, gold, platinum = utils.parse_money_line(lines[0])
        roll = utils.roll_d100()
        print(f"Rolled: {roll}")
        for line in lines[2:]:
            # Parse first column
            if "–" not in line:
                min_roll = int(line.split("\t")[0])
                max_roll = int(line.split("\t")[0])
            else:
                min_roll = int(line.split("\t")[0].split("–")[0])
                max_roll = int(line.split("\t")[0].split("–")[1])
                
            if roll >= min_roll and roll <= max_roll:                
                print(f"\tCopper: {copper}")
                print(f"\tSilver: {silver}")
                print(f"\tElectrum: {electrum}")
                print(f"\tGold: {gold}")
                print(f"\tPlatinum: {platinum}")
                
                gems, art_objects = utils.parse_gems_or_art_objects_line(line.split("\t")[1])
                print("Gems:")
                for gem in gems:
                    print("\t" + gem)
                print("Art objects:")
                for art_object in art_objects:
                    print("\t" + art_object)
                    
                magic_items = utils.parse_magic_items_line(line.split("\t")[2])
                print("Magic items:")
                for magic_item in magic_items:
                    print("\t" + magic_item)
                
                if save_to_file:
                    with open("../generated_treasures.txt", "a") as f:
                        now = time.strftime("%c")
                        f.write(f"Treasure generated on: {now} from a hoard table of CR {cr}\n")
                        f.write(f"Money:\n")
                        f.write(f"\tCopper: {copper}\n")
                        f.write(f"\tSilver: {silver}\n")
                        f.write(f"\tElectrum: {electrum}\n")
                        f.write(f"\tGold: {gold}\n")
                        f.write(f"\tPlatinum: {platinum}\n\n")
                        f.write("Gems:\n")
                        for gem in gems:
                            f.write(f"\t{gem}\n")
                        f.write("\nArt objects:\n")
                        for art_object in art_objects:
                            f.write(f"\t{art_object}\n")
                        f.write("\nMagic items:\n")
                        for magic_item in magic_items:
                            f.write(f"\t{magic_item}\n")
            
                break

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
        generate_single_treasure(cr, save_to_file=True)
    else:
        generate_hoard(cr)
        


if __name__ == "__main__":
    main()