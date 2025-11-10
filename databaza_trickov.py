import sqlite3

conn = sqlite3.connect("databaza_trickov.db")
cur = conn.cursor()

def add_trick(name, type, diff):
    cur.execute('''INSERT INTO tricks (trick_name, trick_type, trick_difficulty)''')

while True:
    print(
        "Add trick: A\n" \
        "View tricks: V\n" \
        "Delete trick: D\n" \
        "Update trick: U\n" \
        "Close: C")
    choice = input("Type in your choice: ")

    if choice == "A" or choice == "a":
        trick_name = input("Trick name: ")
        trick_type = input("Trick type: ")
        trick_difficulty = input("Trick difficulty: ")

        

cur.close()
conn.close()