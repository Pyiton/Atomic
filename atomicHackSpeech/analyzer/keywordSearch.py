from enum import Enum


def readFromFile(filepath: str) -> dict[str]:
    result = {}
    with open(filepath, mode="r", encoding="utf-8") as fstream:
        keyw = fstream.read().strip().splitlines(keepends=False)
        for k in keyw:
            result[k] = ""
    return result


class KeywordSearcher:
    def __init__(self):
        self.keywords = {}
        self.names = {}
        self.secondNames = {}
        self.thirdNames = {}
        self.endingWords = {}
        self.beginningWords = {}
        self.invitationWords = {}


class TextInterpreterState(Enum):
    SEARCHING_FOR_BEGINNING = 1,
    SEARCHING_FOR_NAME = 2,
    READING_SPEAKER_TEXT = 3

def endsWithAnyOf(word: str, expr: list[str]) -> str:
    for w in expr:
        if word.endswith(w):
            return w
    return ""



class TextInterpreter:
    def __init__(self, filepath: str, searcher_: KeywordSearcher):
        self.searcher: KeywordSearcher = searcher_
        self.text = ""
        self.state = TextInterpreterState.SEARCHING_FOR_BEGINNING
        self.Read(filepath)
        self.lowerText = self.text.lower()

    def Read(self, filepath: str):
        with open(filepath, mode="r", encoding="utf-8") as fstream:
            self.text = fstream.read().strip()
        self.state = TextInterpreterState.SEARCHING_FOR_BEGINNING
    
    def writeInFile(self, filepath: str):
        f = open(filepath, mode="w", encoding="utf-8")
        f.write(self.Interpret())
        f.close()
    
    def Interpret(self) -> str:
        currentText = ""
        result = ""
        splitText = self.text.split()
        splitLowerText = self.text.split()
        skips = 0

        for i, word in enumerate(splitLowerText):
            if skips > 0:
                skips -= 1
                continue

            currentText += (" " + word) if (len(currentText)!=0) else word
            if self.state == TextInterpreterState.SEARCHING_FOR_BEGINNING and endsWithAnyOf(currentText, list(self.searcher.invitationWords.keys())):
                self.state = TextInterpreterState.SEARCHING_FOR_NAME
                currentText = ""

            elif self.state == TextInterpreterState.SEARCHING_FOR_NAME and word in self.searcher.names.keys():
                try:
                    if splitText[i-1] in self.searcher.secondNames.keys() and splitText[i+1] in self.searcher.thirdNames.keys():
                        currentText = "{} {} {}: \n".format(splitText[i-1], word, splitText[i+1])
                        skips += 1

                    elif splitText[i+2] in self.searcher.secondNames.keys() and splitText[i+1] in self.searcher.thirdNames.keys():
                        currentText = "{} {} {}: \n".format(splitText[i+2], word, splitText[i+1])
                        skips += 2

                    else:
                        currentText = "{}: \n".format(word)

                    result += currentText
                    currentText = ""
                    self.state = TextInterpreterState.READING_SPEAKER_TEXT

                except IndexError: pass

            elif self.state == TextInterpreterState.READING_SPEAKER_TEXT and endsWithAnyOf(currentText, list(self.searcher.endingWords.keys())):
                result += currentText + "\n"
                currentText = ""
                self.state = TextInterpreterState.SEARCHING_FOR_BEGINNING

        result += currentText

        return result

