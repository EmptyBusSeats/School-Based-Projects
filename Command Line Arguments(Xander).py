import os
import webbrowser
import random

random_phrases = ["011101100011010101110110001001011100101100011101001100010011", "ERROR: INVALID ANSWER", "WRONG WRONG WRONG WRONG WRONG WRONG", "Feel the Breeze : Felellel THe Brzzeeezeee : Flafflfl THAHEEHHEHEEHEE BRZzzzZzzz : FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF", "WEE WOO WEE WOO WEE WOO WEE WOO WEE WOO WEE WOO WEE WOO", "CANNOT COMPUTE<<<<<>>>>>>>INVALIDINVALIDINVAlidINvlAid!:LAvidnAQ!invALIDDFFFFGgZf"]
breakIt = 0


def clearConsole():
  command = 'cls'
  os.system(command)

#1. Author
#2. Videogames
#3. Favorite Song
#4. Websites
#5 Exit
#6 No more options, go away

def Options():
  print("Hello!")
  print("\t1. Author")
  print("\t2. Videogames")
  print("\t3. Favorite Song")
  print("\t4. Websites")
  print("\t5. Exit")
  print("\t6. No more options, go away")

while True:
  Options()

  if breakIt == 0:
    answer = int(input("Pick one of the numbers, except for 6: "))
    clearConsole()

    if answer == 1:
      print("\nThis program was made by Keane Hoxie\n")

    elif answer == 2:
      print("\nSome of my favorite videogames are:")
      print("Rocket League")
      print("NBA 2K")
      print("Apex Legends")
      print("Red Dead Redemption\n")

    elif answer == 3:
      print("My favorite songs are: ")
      print("Sing About Me, I'm Dying of Thirst - Kendrick Lamar")
      print("Icarus - EDEN")
      print("Wicked Games - The Weeknd\n")
      
    elif answer == 4:
      print("My favorite webistes are: ")
      print("https://www.youtube.com/")
      print("https://www.roblox.com/")
      print("https://www.spotify.com/us/\n")
    
    elif answer == 5:
      exit()
    
    elif answer == 6:
      print("Why did you choose this?\n")

      random_number = random.randint(0, 100)

      if random_number < 1:
        random_number = random.randint(0, len(random_phrases) - 1)
        print(random_phrases[random_number], "\n")

      elif random_number >= 1 and random_number <= 2:
        webbrowser.open("https://www.youtube.com/watch?v=A5jnftBQw2U")

      else:
        print("Uh oh, you messed up.")
        breakIt = 1






  elif breakIt == 1:
    answer = int(input("Picka fffirt one thnfff the numbnssbersss:"))
    clearConsole()

    if answer == 1:
      print("\nThis program was made by " + "\u0336REDACTED\u0336 \n")

    elif answer == 2:
      print("\nSomeeease of my fsfafffagavorifafte videogaaassdfffffffffames air:")
      print("Rosadcket Ledsasaague")
      print("NB122334A 2K12215543322566212")
      print("Apex PREADTOR afdsf21211321 Lege1 nds")
      print("Re67hjhbd Deadsaaaaaxaxxxxx Redempxxxxx a2123tion\n")

    elif answer == 3:
      print("My gfa12452vorite ssaassaongassas are: ")
      print("Sing agAdfbosaasutssaaaasasaMe=============, I'm Dying of Thirst -ss Kfgggendrick Lamar")
      print("\n\n\nnnnnnnn\n\n\n")
      print("Icaassasasarus - EDEdfffasfsafsafsaaN")
      print("Wickesaaaaaaad xzgaGames - The We12231eknd\n")
      
    elif answer == 4:
      print("My favorite webistes afafafaff22134141441re: ")
      print("https://www.youtube.com/watch?v=DH0BQtwEAsM")
      print("https://www.roblox.comasfdfssszzx/")
      print("https://www.spotify.co1212156798998/us/\n")
    
    elif answer == 5:
      breakIt = 0
    

    

  