import random

def roll_d(n):
    return random.randint(1, n)

def roll_d4():
    return roll_d(4)

def roll_d6():
    return roll_d(6)

def roll_d8():
    return roll_d(8)

def roll_d10():
    return roll_d(10)

def roll_d12():
    return roll_d(12)

def roll_d20():
    return roll_d(20)

def roll_d100():
    return roll_d(100)

def roll_dice(n, d):
    return sum([roll_d(d) for _ in range(n)])

def roll_from_string(s):
    if s == "once":
        return 1
    d, n = s.split("d")
    return roll_dice(int(d), int(n))

def parse_money_line(line):
    # Example line format:
    # 31–60	–	6d6 x 10 (210)	–	2d6 x 10 (70)	–
    copper = 0
    silver = 0
    electrum = 0
    gold = 0
    platinum = 0
    
    # Split the line by tabs
    columns = line.split("\t")
    
    # Parse copper
    if columns[1] != "–":
        if "x" in columns[1]:
            copper = roll_dice(int(columns[1].split("d")[0]), int(columns[1].split("d")[1].split(" ")[0])) * int(columns[1].split("x")[1].split(" ")[1])
        else:
            copper = roll_dice(int(columns[1].split("d")[0]), int(columns[1].split("d")[1].split(" ")[0]))
        
    # Parse silver
    if columns[2] != "–":
        if "x" in columns[2]:
            silver = roll_dice(int(columns[2].split("d")[0]), int(columns[2].split("d")[1].split(" ")[0])) * int(columns[2].split("x")[1].split(" ")[1])
        else:
            silver = roll_dice(int(columns[2].split("d")[0]), int(columns[2].split("d")[1].split(" ")[0]))
            
    # Parse electrum
    if columns[3] != "–":
        if "x" in columns[3]:
            electrum = roll_dice(int(columns[3].split("d")[0]), int(columns[3].split("d")[1].split(" ")[0])) * int(columns[3].split("x")[1].split(" ")[1])
        else:
            electrum = roll_dice(int(columns[3].split("d")[0]), int(columns[3].split("d")[1].split(" ")[0]))
        
    # Parse gold
    if columns[4] != "–":
        if "x" in columns[4]:
            gold = roll_dice(int(columns[4].split("d")[0]), int(columns[4].split("d")[1].split(" ")[0])) * int(columns[4].split("x")[1].split(" ")[1])
        else:
            gold = roll_dice(int(columns[4].split("d")[0]), int(columns[4].split("d")[1].split(" ")[0]))
        
    # Parse platinum
    if columns[5] != "–" and columns[5] != "–\n":
        if "x" in columns[5]:
            platinum = roll_dice(int(columns[5].split("d")[0]), int(columns[5].split("d")[1].split(" ")[0])) * int(columns[5].split("x")[1].split(" ")[1])
        else:
            platinum = roll_dice(int(columns[5].split("d")[0]), int(columns[5].split("d")[1].split(" ")[0]))
        
    return (copper, silver, electrum, gold, platinum)

def generate_gems(dice, value):
    print (f"Generating gems with dice: {dice} and value: {value}")
    roll = roll_from_string(dice)
    gems = []
    
    with open(f"../tables/gems_{value}gp.txt") as f:
        lines = f.readlines()
        for _ in range(roll):
            # Add random line to gems
            gems.append(random.choice(lines).split("\t")[1].strip())
            
    return gems

def generate_art_objects(dice, value):
    print (f"Generating art objects with dice: {dice} and value: {value}")
    roll = roll_from_string(dice)
    art_objects = []
    
    with open(f"../tables/art_objects_{value}gp.txt") as f:
        lines = f.readlines()
        for _ in range(roll):
            # Add random line to art_objects
            art_objects.append(random.choice(lines).split("\t")[1].strip())
            
    return art_objects

def parse_gems_or_art_objects_line(line):
    # Example line format:
    # 2d6 (7) 50 gp gems
    # 2d4 (5) 25 gp art objects
    gems = []
    art_objects = []
    
    if line == "–":
        return (gems, art_objects)
    
    # Split the line by tabs
    columns = line.split(" ")
    
    # Parse gems
    if "gems" in columns[4]:
        gems = generate_gems(columns[0], columns[2])
    elif "art" in columns[4]:
        art_objects = generate_art_objects(columns[0], columns[2])
        
    return (gems, art_objects)

def roll_on_magic_item_table(times, table):
    print(f"Rolling {times} times on table {table}")
    
    magic_items = []
    
    with open(f"../tables/table_{table}.txt") as f:
        lines = f.readlines()
        for _ in range(times):
            roll = roll_d100()
            print(f"Rolled: {roll}")
            for line in lines:
                if line.split("\t")[0] == "-":
                    continue
                if "–" not in line:
                    min_roll = int(line.split("\t")[0])
                    max_roll = int(line.split("\t")[0])
                else:
                    min_roll = int(line.split("\t")[0].split("–")[0])
                    max_roll = int(line.split("\t")[0].split("–")[1])
                    
                if roll >= min_roll and roll <= max_roll:
                    magic_items.append(line.split("\t")[1].strip())
                    if "(roll d" in line:
                        # We got one of those pesky "roll dX" ones
                        versions = []
                        # Get dice to roll
                        dice = line.split("roll d")[1].split(" )")[0].split(")")[0]
                        roll = roll_d(int(dice))
                        # Read all the next lines starting with "-"
                        for subline in lines[lines.index(line):]:
                            if subline.split("\t")[0] == "-":
                                if "–" not in subline:
                                    min_roll = int(subline.split("\t")[1].split(":")[0])
                                    max_roll = int(subline.split("\t")[1].split(":")[0])
                                else:
                                    min_roll = int(subline.split("\t")[1].split("–")[0])
                                    max_roll = int(subline.split("\t")[1].split("–")[1].split(":")[0])
                                    
                                if roll >= min_roll and roll <= max_roll:
                                    versions.append(subline.split("\t")[1].split(":")[1].strip())
                                    
                        magic_items[-1] = f"{magic_items[-1].split('(')[0].strip()} ({versions[0]})"
                                                
                    break
        
    return magic_items

def parse_magic_items_line(line):
    # Example line format:
    # Roll 1d4 times on Magic Item Table B.\n    
    magic_items = []
    
    if line == "–" or line == "–\n":
        return magic_items
    
    times = roll_from_string(line.split(" ")[1])
    if line.split(" ")[1] == "once":
        table = line.split(" ")[6].split(".")[0]    
    else:
        table = line.split(" ")[7].split(".")[0]
    
    magic_items = roll_on_magic_item_table(times, table)
    
    if "and" in line:
        times = roll_from_string(line.split("and")[1].split(" ")[1])
        table = line.split(" ")[10].split(".")[0]
        magic_items += roll_on_magic_item_table(times, table)
    
    return magic_items
