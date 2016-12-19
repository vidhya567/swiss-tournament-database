#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

roundno=0
def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    roundno=0
    c=connect()
    cursor=c.cursor()
    query=("DELETE FROM results")
    cursor.execute(query)
    c.commit()
    c.close()
    c=connect()
    cursor=c.cursor()
    query1=("UPDATE playerinfo SET won=0,played=0")
    cursor.execute(query1)
    c.commit()
    c.close()


def deletePlayers():
    """Remove all the player records from the database."""
    roundn0=0
    c=connect()
    cursor=c.cursor()
    query=("DELETE FROM playerinfo") 
    cursor.execute(query)
    c.commit()
    c.close()
    
def countPlayers():
    """Returns the number of players currently registered."""
    c=connect()
    cursor=c.cursor()
    query=("SELECT COUNT(*) as players FROM playerinfo" )
    cursor.execute(query)
    counter=cursor.fetchone()
    #print("the count is ")
    #print(counter)
    c.close()
    return counter[0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    c=connect()
    cursor=c.cursor()
    cursor.execute("INSERT INTO playerinfo(pname,won,played) VALUES (%s,0,0)",(name,))
    c.commit()
    c.close()



def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    c=connect()
    cursor=c.cursor()
    query=("SELECT pid ,pname ,won , played FROM playerinfo ORDER BY won DESC")
    cursor.execute(query)
    results=cursor.fetchall()
    #results=((row[0],row[1],row[2],row[3])for row in cursor.fetchall())
    c.close()
    return results
    

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    
    c=connect()
    cursor=c.cursor()
    cursor.execute("INSERT INTO results VALUES(%s,%s,%s,%s)",(roundno,winner,loser,winner,));
    c.commit()
    c.close()

    c=connect()
    cursor=c.cursor()
    query1=("SELECT won,played  FROM playerinfo WHERE pid=%s")
    data=(winner,)
    cursor.execute(query1,data)
    results=cursor.fetchone()
    c.close()
    awins=results[0]+1
    amatches=results[1]+1

    c=connect()
    cursor=c.cursor()
    query2=("SELECT played as lostmatches FROM playerinfo WHERE pid=%s")
    stringy=(loser,)
    cursor.execute(query2,stringy)
    lostmatches=cursor.fetchone()
    c.close()
    bmatches=lostmatches[0]+1
    

    c=connect()
    cursor=c.cursor()
    query3=("UPDATE playerinfo SET won=%s,played=%s WHERE pid=%s")
    query4=("UPDATE playerinfo SET played=%s WHERE pid=%s")
    p1=(awins,amatches,winner,)
    
    p3=(bmatches,loser,)
    cursor.execute(query3,p1)
    cursor.execute(query4,p3)
    c.commit()
    c.close

   
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    playertable=playerStandings()
    length=len(playertable)
    results=[]
    i=0
    while(i<length):
        id1=playertable[i][0]
        id2=playertable[i+1][0]
        name1=playertable[i][1]
        name2=playertable[i+1][1]
        temp=(id1,name1,id2,name2)
        results.append(temp)
        i=i+2
    return results


