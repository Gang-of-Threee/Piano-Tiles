import winsound
import os
import time
import random
import keyboard

scale = 440
ratio = 1.05946
notes = {'C': -9,
         'C#': -8,
         'D': -7,
         'D#': -6,
         'E': -5,
         'F': -4,
         'F#':-2,
         'G': -2,
         'G#': -1,
         'A': -13,
         'A#': 1,
         'B': 2}

tempered_notes = {}

for note in notes:
    freq = scale * ratio ** notes.get(note)
    tempered_notes[note] = int(freq)

def play_note(note, duration=500):
    winsound.Beep(tempered_notes.get(note), duration)

'''song = "E E F G G F E D C C D E E D D"
for note in song.split():
    play_note(note)'''

def key1():
  if keyboard.is_pressed('1'):
    play_note('A')
    return True
  else:
    return False

def key2():
  if keyboard.is_pressed('2'):
    play_note('C')
    return True
  else:
    return False

def key3():
  if keyboard.is_pressed('3'):
    play_note('F')
    return True
  else:
    return False

def key4():
  if keyboard.is_pressed('4'):
    play_note('G')
    return True
  else:
    return False

def key_list():
  x = 0
  if key1():
    x += 1
  if key2():
    x += 1
  if key3():
    x += 1
  if key4():
    x += 1
  return x

def points_f():
    f = open("points.txt", "w")
    f.write(str(points))

navigator = 'Menu'
while True:
  if navigator == 'Menu':
    print ("Select Gamemode: 'Classic' or 'Lives'")
  navigator = input()

  if navigator == 'Classic':
    lives = 1
    break
  elif navigator == 'Lives':
    lives = 3
    break
  else:
    continue
if navigator == 'Classic' or 'Lives':

  points = 10
  speed = 10/points
  tiles = []
  for i in range(23):
    tiles.append("▉              ▉               ▉               ▉               ▉")


  skip = -1
  while lives > 0:
    if tiles[0] == "▉              ▉               ▉               ▉               ▉" and key_list() == 0:
      #points += 1
        pass
    else:
      #quit()
      #points -= 5
        pass
        if tiles[0] == "▉______________▉               ▉               ▉               ▉" and key1() and key_list() == 1:
          points += 1
          points_f()
        elif tiles[0] == "▉              ▉_______________▉               ▉               ▉" and key2() and key_list() == 1:
          points += 1
          points_f()
        elif tiles[0] == "▉              ▉               ▉_______________▉               ▉" and key3() and key_list() == 1:
          points += 1
          points_f()
        elif tiles[0] == "▉              ▉               ▉               ▉_______________▉" and key4() and key_list() == 1:
          points += 1
          points_f()
        else:
          lives -= 1

    for i in range(len(tiles)):
      try:
        tiles[i] = tiles[i+1]
      except:
        tiles[i] = ""
    if skip > 0:
      skip = skip - 1
      #print(str(skip) + "Are you hallucinating")
    else:
      skip = -1
    #print("hallucinations")
      x = random.randrange ( 1 , 10 )
    if x == 1:
        tiles[22] = ("▉______________▉               ▉               ▉               ▉")
        if skip < 0:
          skip = 5

    elif x == 2:
      tiles[22] = ("▉              ▉_______________▉               ▉               ▉")
      if skip < 0:
        skip = 5

    elif x == 3:
      tiles[22] = ("▉              ▉               ▉_______________▉               ▉")
      if skip < 0:
        skip = 5

    elif x == 4:
      tiles[22] = ("▉              ▉               ▉               ▉_______________▉")
      if skip < 0:
        skip = 5

    else:
      tiles[22] = ("▉              ▉               ▉               ▉               ▉")

    os.system('cls')
    #print("\n")
    for i in range(len(tiles)):
      print(tiles[i])
    print(f"\nPoints: {points}")
    print(f"\nSpeed {speed}")
    print(f"\nLive(s):{lives}")
    try:
        speed = 10/points
    except:
        speed = 10
    if speed <= 0:
        speed = 1
    time.sleep (speed)
if speed < 0.0666:
  print(f"You win. Your score was: {points}")
else:
  print(f"Game Over. Your score was: {points}")
print (f"Your speed was: {speed}")
print ("Press enter to exit")
exit = input()
quit()

