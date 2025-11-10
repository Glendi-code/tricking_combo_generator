import sqlite3

conn = sqlite3.connect("databaza_trickov.db")
cur = conn.cursor()

def add_trick(name, typ, diff):
    cur.execute('''INSERT INTO tricks (trick_name, trick_type, trick_difficulty) VALUES (?, ?, ?)''', (name, typ, diff))
    conn.commit()

def view_list_filtered(filt):
    if filt == "T":
        filt = input("Type in the value you re seeking: ").strip()
        cur.execute('''SELECT * FROM tricks WHERE trick_type=?''', filt)
    else:
        filt = input("Type in the value you re seeking: ").strip()
        cur.execute('''SELECT * FROM tricks WHERE trick_difficulty=?''', filt)

    rows = cur.fetchall()
    for row in rows:
        print(row)

def view_list_unfiltered():
    cur.execute('''SELECT * FROM tricks''')
    rows = cur.fetchall()
    for row in rows:
        print(row)

while True:
    print(
        "Add trick: A\n" \
        "View tricks: V\n" \
        "Delete trick: D\n" \
        "Update trick: U\n" \
        "Close: C")
    choice = input("Type in your choice: ").upper().strip()

    if choice == "A":
        trick_name = input("Trick name: ").strip()
        trick_type = input("Trick type: ").strip()
        trick_difficulty = input("Trick difficulty: ").strip()
        add_trick(trick_name, trick_type, trick_difficulty)

    elif choice == "V":
        filters = input("Would you like to filter by type(T), difficulty(D) or nothing(N): ").upper().strip()
        if filters == "T" or filters == "D":
            view_list_filtered(filters)
        elif filters == "N":
            view_list_unfiltered()

    elif choice == "C":
        break

cur.close()
conn.close()