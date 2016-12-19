from tournament import *
def testPairings():
    """
    Test that pairings are generated properly both before and after match reporting.
    """
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")
    registerPlayer("Fluttershy")
    registerPlayer("Applejack")
    registerPlayer("Pinkie Pie")
    registerPlayer("Rarity")
    registerPlayer("Rainbow Dash")
    registerPlayer("Princess Celestia")
    registerPlayer("Princess Luna")
    standings = playerStandings()
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    print(id1, id2, id3, id4, id5, id6, id7,id8)
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    reportMatch(id5, id6)
    reportMatch(id7, id8)
    pairings = swissPairings()
    print(pairings[0][0],pairings[0][2])
    print(pairings[1][0],pairings[1][2])
    print(pairings[2][0],pairings[2][2])
    print(pairings[3][0],pairings[3][2])
    reportMatch(id1, id7)
    reportMatch(id2, id6)
    reportMatch(id4, id8)
    reportMatch(id5, id3)
    pairings = swissPairings()
    print(pairings[0][0],pairings[0][2])
    print(pairings[1][0],pairings[1][2])
    print(pairings[2][0],pairings[2][2])
    print(pairings[3][0],pairings[3][2])
    reportMatch(id1, id5)
    reportMatch(id2, id4)
    reportMatch(id3, id7)
    reportMatch(id6, id8)
    standings = playerStandings()
    [id1, id2, id3, id4, id5, id6, id7, id8] = [row[0] for row in standings]
    print(id1, id2, id3, id4, id5, id6, id7,id8)


if __name__ == '__main__':
    testPairings()
    print "Success!  All tests pass!"