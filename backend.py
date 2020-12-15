######    KIMIA KAMIYAB
from scholarly import scholarly
import sqlite3
import json
n='none'
def connection():
    connection = sqlite3.connect("./database.db")
    cur = connection.cursor()
    q1 = """ 
    CREATE TABLE IF NOT EXISTS maindatabase ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    fullName TEXT, 
    affiliation TEXT, 
    interests TEXT,    
    cites_per_year TEXT,
    hindex TEXT)
    """
    q2 = """ 
    CREATE TABLE IF NOT EXISTS publication ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    publicationstitle TEXT, 
    publicationscites INTEGER , 
    publicationsyear INTEGER,
    userID INTEGER )
    """
    cur.execute(q1)
    cur.execute(q2)
    connection.commit()
    connection.close()
connection()

def insert(first_n,last_n):
    full_name=first_n+' '+last_n
    search_query = scholarly.search_author(full_name)
    try:
        n = next(search_query)
    except StopIteration:
        return "This user doesn't exists"

    n = n.fill(sections=['basics', 'counts', 'indices', 'publications'])
    connection = sqlite3.connect("./database.db")
    cur = connection.cursor()
    interests=','.join(n.interests)
    cites_per_year = json.dumps((n.cites_per_year))
    pub=n.publications
    q = ("""SELECT fullName FROM maindatabase """)
    cur.execute(q)
    ifexists = cur.fetchall()
    name=[]
    for i in range(len(ifexists)):
        name.append(ifexists[i][0])

    if full_name in name:
        return 'This user is already exists'
    else:
        q1 = "INSERT INTO maindatabase VALUES (NULL,?,?,?,?,?)"
        cur.execute(q1,(full_name,n.affiliation,interests,cites_per_year,n.hindex))
        connection.commit()
        q2 = ("""SELECT id FROM maindatabase WHERE fullName=? """ )
        cur.execute(q2, ([full_name]))
        userID = cur.fetchall()[0][0]
        for item in pub:
            q2 = "INSERT INTO publication VALUES (NULL,?,?,?,?)"
            if 'year' in item.bib.keys() :
                y=item.bib['year']
            else:
                y=0
            cur.execute(q2, (item.bib['title'], item.bib['cites'], y,userID))
            connection.commit()
        connection.commit()
        connection.close()
        return "Mission accomplished"

def search(firstName,lastName,option):
    connection = sqlite3.connect("./database.db")
    cur = connection.cursor()
    fullName = firstName + ' ' + lastName

    q = ("""SELECT fullName FROM maindatabase """)
    cur.execute(q)
    ifexists = cur.fetchall()
    name=[]
    for i in range(len(ifexists)):
        name.append(ifexists[i][0])
    if fullName in name:
        if option == 'intrests':
            q2 = ("""SELECT interests FROM maindatabase WHERE fullName=? """)
            cur.execute(q2, ([fullName]))
            out = cur.fetchall()[0][0].split(",")
        elif option == 'Articles':
            q2 = ("""SELECT id FROM maindatabase WHERE fullName=? """)
            cur.execute(q2, ([fullName]))
            userID = cur.fetchall()[0][0]
            q2 = ("""SELECT publicationstitle FROM publication WHERE userID=? """)
            cur.execute(q2, (str(userID)))
            out = cur.fetchall()
        elif option == 'affiliation':
            q2 = ("""SELECT affiliation FROM maindatabase WHERE fullName=? """)
            cur.execute(q2, ([fullName]))
            out = cur.fetchall()
        connection.commit()
        connection.close()
        return out
    else:
        return 'This user doesnt exists'



