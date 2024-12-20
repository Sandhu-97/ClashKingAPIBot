import sqlite3

conn = sqlite3.connect('players.db')


def createTable(clan_name):
    cursor = conn.cursor()
    query = f"CREATE TABLE IF NOT EXISTS {clan_name} (name text, tag text, attack_wins int, donations int)"
    cursor.execute(query)
    conn.commit()
    

def insertIntoTable(clan, name, tag, attack_wins, donations):
    cursor = conn.cursor()
    query = f"INSERT INTO {clan} VALUES ('{name}', '{tag}', '{attack_wins}', '{donations}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()


def clearTable(clan):
    cursor = conn.cursor()
    query = f"DELETE FROM {clan}"
    cursor.execute(query)
    conn.commit()
    cursor.close()


def getMinAttacksData(clan, min_attacks):
    cursor = conn.cursor()
    query = f"SELECT NAME, TAG, ATTACK_WINS FROM {clan} WHERE attack_wins<{min_attacks}"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data


def getMinDonationsData(clan, min_donation):
    cursor = conn.cursor()
    query = f"SELECT NAME, TAG, DONATIONS FROM {clan} WHERE donations<{min_donation}"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data

def insertLink(tag, id):
    cursor = conn.cursor()
    query = f"INSERT INTO LINKS VALUES ('{tag}', '{id}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()

def getLink(tag):
    cursor = conn.cursor()
    query = f"SELECT ID FROM LINKS WHERE TAG='{tag}'"
    cursor.execute(query)
    data = cursor.fetchone()
    cursor.close()
    return data

# print(getLink("#GQ09RUQC")[0])