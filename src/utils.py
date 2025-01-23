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

def parse_money_line(line):
    print(line)
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
        print(columns[1])
        if "x" in columns[1]:
            copper = roll_dice(*map(int, columns[1].split("d")[0].split(" x ")))
        else:
            copper = roll_dice(int(columns[1].split("d")[0]), int(columns[1].split("d")[1].split(" ")[0]))
        
    # Parse silver
    if columns[2] != "–":
        print(columns[2])
        if "x" in columns[2]:
            silver = roll_dice(*map(int, columns[2].split("d")[0].split(" x ")))
        else:
            silver = roll_dice(int(columns[2].split("d")[0]), int(columns[2].split("d")[1].split(" ")[0]))
            
    # Parse electrum
    if columns[3] != "–":
        print(columns[3])
        if "x" in columns[3]:
            electrum = roll_dice(*map(int, columns[3].split("d")[0].split(" x ")))
        else:
            electrum = roll_dice(int(columns[3].split("d")[0]), int(columns[3].split("d")[1].split(" ")[0]))
        
    # Parse gold
    if columns[4] != "–":
        print(columns[4])
        if "x" in columns[4]:
            gold = roll_dice(*map(int, columns[4].split("d")[0].split(" x ")))
        else:
            gold = roll_dice(int(columns[4].split("d")[0]), int(columns[4].split("d")[1].split(" ")[0]))
        
    # Parse platinum
    if columns[5] != "–" and columns[5] != "–\n":
        print(columns[5])
        if "x" in columns[5]:
            platinum = roll_dice(*map(int, columns[5].split("d")[0].split(" x ")))
        else:
            platinum = roll_dice(int(columns[5].split("d")[0]), int(columns[5].split("d")[1].split(" ")[0]))
        
    return (copper, silver, electrum, gold, platinum)