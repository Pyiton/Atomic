from analyzer import keywordSearch


if __name__ == "__main__":
    ttt = keywordSearch.KeywordSearcher()
    ttt.names = keywordSearch.readFromFile("names.txt")
    ttt.secondNames = keywordSearch.readFromFile("secondNames.txt")
    ttt.thirdNames = keywordSearch.readFromFile("thirdNames.txt")
    ttt.invitationWords = keywordSearch.readFromFile("welcome.txt")
    ttt.endingWords = keywordSearch.readFromFile("ending.txt")
    intpr = keywordSearch.TextInterpreter("test2.txt", ttt)
    print(intpr.Interpret())
    intpr.writeInFile("result.txt")
    #ttt.names = keywordSearch.readFromFile("names.txt")
    #ttt.names = keywordSearch.readFromFile("names.txt")
