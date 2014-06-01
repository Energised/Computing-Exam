# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
#
#----------------------------------------------------------------------------
#
# Daniel Woolsey
# Skeleton Code Append v1.0.1
#
# Points of Information
#   - List doesn't start as a , uses "None" to start as a 1st term 
#   - Original code uses log if statements for returning strings with numerical values for rank and suit
#   
#--------------------------------changelog-----------------------------------
# 1) Menu doesnt reset score after any key is pressed
# 2) Capitals accepted through entire code (finally)
# 3) Simplified version of the GetRank and GetSuit functions using dictionaries
# 4) Use of a bubble sort via temp variable for recent score system (by AQA's standards)
# 5) Clears screen in command line Python for pretty program
# 6) Additions allow for game to be played lower or higher - chosen as gameMode
# 7) Tests for length of users name being > 10 alphanumeric characters
# 8) No points given if cards are of the same rank
# 9) Added lives system - user starts with 3 before the game can end 
#----------------------------------------------------------------------------
import random, os, sys

NO_OF_RECENT_SCORES = 3

#----------------------------DECK PARAMETERS---------------------------------

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0

#------------------------------GLOBALS/CONSTANTS-----------------------------

Deck = [None]
RecentScores = [None]
highScores = [None]
Choice = ''
AceHigh = False
placeHS = 1
place = 1
maxNameLength = 10
tempScore = 0
gameHold = [None]

#-------------------------------CARD STRINGS---------------------------------

def GetRankNew(RankNo):
  if AceHigh == False:
    RankSpace = {"1":"Ace","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six"
               ,"7":"Seven","8":"Eight","9":"Nine","10":"Ten","11":"Jack"
               ,"12":"Queen","13":"King"}
  elif AceHigh == True:
    RankSpace = {"1":"Ace","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six"
                 ,"7":"Seven","8":"Eight","9":"Nine","10":"Ten","11":"Jack"
                 ,"12":"Queen","13":"King"}
  Rank = ""
  try:
    Rank = RankSpace[str(RankNo)]
  except:
    print("!")
  return Rank

def GetSuitNew(SuitNo):
  SuitSpace = {"1":"Clubs","2":"Diamonds","3":"Hearts","4":"Spades"}
  Suit = ""
  try:
    Suit = SuitSpace[str(SuitNo)]
  except:
    print("!")
  return Suit

#------------------------------------MENU------------------------------------

def DisplayMenu():
  print()
  print('---------------------MAIN MENU---------------------')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Set and Display Top 10 High Scores')
  print('6. Change Ace Value Setting (Currently set as Ace High being',AceHigh,")")
  print('7. Game description')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():  
  Choice = input()
  print()
  return Choice

def clear():
  try:
    if sys.platform == 'win32' or 'win64':
      os.system('cls')
    else:
      os.system('clear')
  except:
    print()

def game_desc():
  clear()
  print()
  print("~/changelog")
  print("1) Menu doesnt reset score after any key is pressed")
  print("2) Capitals accepted through entire code (finally)")
  print("3) Simplified version of the GetRank and GetSuit functions using dictionaries")
  print("4) Use of a bubble sort via temp variable for recent score system (by AQA's standards)")
  print("5) Clears screen in command line Python for pretty program")
  print("6) Additions allow for game to be played lower or higher - chosen as gameMode")
  print("7) Tests for length of users name being > 10 alphanumeric characters")
  print("8) No points given if cards are of the same rank")
  print("9) Added lives system - user starts with 3 before the game can end")
  print()
  input("Press the any key ")
  clear()
  
#------------------------------LOADING A DECK--------------------------------

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRankNew(ThisCard.Rank), 'of', GetSuitNew(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
  ThisCard.Rank = Deck[1].Rank
  ThisCard.Suit = Deck[1].Suit
  for Count in range(1, 52 - NoOfCardsTurnedOver):
    Deck[Count].Rank = Deck[Count + 1].Rank
    Deck[Count].Suit = Deck[Count + 1].Suit
  Deck[52 - NoOfCardsTurnedOver].Suit = 0
  Deck[52 - NoOfCardsTurnedOver].Rank = 0

#---------------------------HIGHER OR LOWER TESTS----------------------------

def IsNextCardHigher(LastCard, NextCard):
  Higher = False
  if NextCard.Rank > LastCard.Rank:
    Higher = True
  return Higher

def gameMode():
  gameHigh = True
  print()
  print("-----------------CHOOSE A GAMEMODE-----------------")
  print()
  print("1: Is the Card Higher?")
  print("2: Is the Card Lower")
  print()
  try:
    gameCheck = input()
    if gameCheck == '2':
      gameHigh = False
  except:
    print()
  clear()
  return gameHigh
  
def IsNextCardLower(LastCard, NextCard):
  Lower = False
  if NextCard.Rank < LastCard.Rank:
    Lower = True
  return Lower

def AreTheyTheSame(LastCard, NextCard):
  Same = False
  if NextCard.Rank == LastCard.Rank:
    Same = True
  return Same

#-----------------------------------CHOICES----------------------------------

def GetPlayerName(maxNameLength):
  print()
  PlayerName = ""
  while True:
    PlayerName = input('Please enter your name: ')
    if (PlayerName == '') or (len(PlayerName) > maxNameLength):
      print("Invalid name length of over 10 characters")
    else:
      break
  print()
  return PlayerName

def GetChoiceFromUser(gameHigh):
  if gameHigh == True:
    Choice = input('Do you think the next card will be higher than the last card (enter y or n)? ').lower()
  else:
    Choice = input("Do you think the next card will be lower than the last card (enter y or n)? ").lower()
  return Choice

#------------------------------SCORES FUNCTIONS------------------------------

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0

def DisplayRecentScores(RecentScores):
  print()
  print('-------------------RECENT SCORES-------------------')
  print()
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    if len(RecentScores[Count].Name) == 0:
      pass
    else:
      print(RecentScores[Count].Name, 'got a score of', RecentScores[Count].Score)
  print()
  print('Press the any key to return to the main menu')
  input()
  clear()
  print()

def recentScoreBubbleSort(RecentScores):
  Sorted = False
  while not Sorted:
    for mark in range(1,NO_OF_RECENT_SCORES):
      a = RecentScores[mark].Score
      b = RecentScores[mark+1].Score
      if a < b:
        temp = RecentScores[mark+1]
        RecentScores[mark+1] = RecentScores[mark]
        RecentScores[mark] = temp
    Sorted = True 

#--------------------------------HIGH SCORES---------------------------------

def highScoreBubbleSort(highScore):
  sort_check = False
  while not sort_check:
    for mark in range(1,20):
      a = highScores[mark].Score
      b = highScores[mark+1].Score
      if a > b:
        temp = highScore[mark+1]
        highScores[mark+1] = highScores[mark]
        highScores[mark] = temp
    Sorted = True

def displayHighScore():
  for count in range(1,10):
    enum = 1
    name = highScores[enum].Name
    score = highScores[enum].Score
    print(enum,".",name,"with the score",score,sep=' ',end='\n')
    enum += 1

#-------------------------------UPDATING SCORES------------------------------
  
def UpdateRecentScores(RecentScores, Score):
  PlayerName = GetPlayerName(maxNameLength)
  FoundSpace = False
  Count = 1
  while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
    if RecentScores[Count].Name == '':
      FoundSpace = True
    else:
      Count = Count + 1
  if not FoundSpace:
    for Count in range(1, NO_OF_RECENT_SCORES):
      RecentScores[Count].Name = RecentScores[Count + 1].Name
      RecentScores[Count].Score = RecentScores[Count + 1].Score
    Count = NO_OF_RECENT_SCORES
  RecentScores[Count].Name = PlayerName
  RecentScores[Count].Score = Score
  clear()

def update_high_scores(highScores, Score):
  player_name = GetPlayerName(maxNameLength)
  place = 1
  highScores[place].Name = PlayerName
  highScores[place].Score = Score
  place+=1
  clear()
  
#------------------------------PLAYING THE GAME------------------------------

def PlayGame(Deck, RecentScores, tempScore, gameHold):
  clear()
  gameHigh = gameMode()
  lives = 3
  clear()
  print("-------------------PLAY THE GAME-------------------")
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while (Choice != 'y') and (Choice != 'n'):
      Choice = GetChoiceFromUser(gameHigh)
      if Choice == 'q':
        sys.exit()
        gameHold = Deck
    DisplayCard(NextCard)
    NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
    if gameHigh == True:
      Higher = IsNextCardHigher(LastCard, NextCard)
      Lower = ''
    else:
      Lower = IsNextCardLower(LastCard, NextCard)
      Higher = ''
    Same = AreTheyTheSame(LastCard, NextCard) 
    if (Higher and Choice == ('y' or 'Y')) or (not Higher and Choice == ('n' or 'N')):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Suit
    elif (Lower and Choice == ('y' or 'Y')) or (not Lower and Choice == ('n' or 'N')):
      DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
      LastCard.Rank = NextCard.Rank
      LastCard.Suit = NextCard.Rank
    elif Same == True:
      print("Those cards were the same, no points are won")
      print()
    else:
      lives-=1
      print()
      print("You have",lives,"lives remaining",sep=' ')
      if lives == 0:
        GameOver = True
  if GameOver:
    high_score_check = input("Do you want your score to be added to the high score table? (y/n)")
    if high_score_check.lower == 'y':
      DisplayEndOfGameMessage(NoOfCardsTurnedOver-2)
      UpdateRecentScores(RecentScores,51)
      update_high_scores(highScores, Score)
    else:
      DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
      UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)
    update_high_scores(highScores, 51)

#-----------------------------THE MAIN PROTOCOL------------------------------

if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
  while Choice != ('q' or 'Q'):
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores, tempScore, gameHold)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores, tempScore, gameHold)
    elif Choice == '3':
      recentScoreBubbleSort(RecentScores)
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      highScoreBubbleSort(highScores)
      displayHighScore()
    elif Choice == '6':
      if AceHigh == False:
        AceHigh = True
      else:
        AceHigh = False
      clear()
    elif Choice == '7':
      game_desc()
    else:
      clear()
