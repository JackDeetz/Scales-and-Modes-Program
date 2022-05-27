"""Program prompts user for a key, a scale, and a mode, and returns the scale.

Breaks scales down to their Whole-step, Half-step, 3Half-steps 'interval' patterns
and creates scales by taking a key 'root' note, and advancing the Chromatic Scale
to find the corrent notes. The Mode advances the beginning note in the pattern based on the scales 'intervals'. Can scale to accomidate all scales easily
"""

##########################################
# IMPORTS:
#   <list modules needed for program and their purpose>
##########################################
#<replace this line with import statement(s)>

MODES = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian'] # for pentetonic scale, not neccesarily same for every scale

#All the notes in Half-step intervals
CHROMATIC_SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

#Scales added with their intervals as their array content
MAJOR_PENTETONIC_SCALE = ['W', 'W', 'WH', 'W', 'WH']
MINOR_PENTETONIC_SCALE = ['WH', 'W', 'W','WH', 'W', ]
DIMINISHED_SCALE = ['H', 'W', 'H', 'W', 'H', 'W', 'H', 'W', 'H']
MAJOR_SCALE = ['W', 'W', 'H', 'W', 'W', 'W', 'H']
WHOLE_TONE_SCALE = ['W', 'W', 'W', 'W', 'W', 'W']

#Array of scales
SCALES = [MAJOR_PENTETONIC_SCALE, MINOR_PENTETONIC_SCALE, DIMINISHED_SCALE, MAJOR_SCALE, WHOLE_TONE_SCALE]
#Array of scale names, corresponding to SCALES indexes
SCALES_NAMES = ["Major Pentetonic", "Minor Pentetonic", "Diminished", "Major", "Whole Tone"]

#Intervals used
WHOLE_STEP = 'W'
HALF_STEP = 'H'
THREE_HALF_STEPS = 'WH'

##########################################
# FUNCTIONS:
##########################################
#<given a key, a scale from SCALES[] and a mode, function returns a str array of notes that make the correct scale>
def scale (key : CHROMATIC_SCALE, scaleParam : [], mode = 0) :
  #find the index of the parameter key in the CHROMATIC_SCALE
  keyIndex = (CHROMATIC_SCALE.index(key))
  #Adjust the beginning note to match the 'mode' in the parameter
  for i in range (0, mode)  :
    if scaleParam[i % len(scaleParam)] == WHOLE_STEP :
      keyIndex += 2
    elif scaleParam[i % len(scaleParam)] == HALF_STEP :
      keyIndex += 1
    elif scaleParam[i % len(scaleParam)] == THREE_HALF_STEPS :
      keyIndex += 3
  #return array variable, add the first note, % 12 so the scale loops as keyIndex increases
  returnScale = [CHROMATIC_SCALE[keyIndex % 12]]

  #find next note by advancing up the CHROMATIC_SCALE by the 'intervals' set by the parameter SCALE
  for i in range (0, len(scaleParam)) :
    if scaleParam[(i + mode) % len(scaleParam)] == WHOLE_STEP :
      keyIndex += 2
    elif scaleParam[(i + mode) % len(scaleParam)] == HALF_STEP :
      keyIndex += 1
    elif scaleParam[(i + mode) % len(scaleParam)] == THREE_HALF_STEPS :
      keyIndex += 3
    #add the located note to the return variable
    returnScale.append(CHROMATIC_SCALE[(keyIndex) % 12])
  return returnScale

#<Prints the available scale details available and prompts user to enter preferences, returns the key, scale index, and mode index>
def menu () :
  valid = False
  print(CHROMATIC_SCALE)
  while (valid != True) :
    key = (input("Select your key: ")).upper()
    if CHROMATIC_SCALE.count(key) == 0 :
      print("huh?")
      continue
    valid = True
    
  print(SCALES_NAMES)
  valid = False
  while valid == False :
    scale = input("Scale: ").upper()
    for char in scale :
      if char == " " :
        char = "_"
    for element in SCALES_NAMES :
      if scale == element.upper() :
        scale = SCALES[SCALES_NAMES.index(element)]
        valid = True 
        break
    print(scale)
    if valid : 
      break
    print("huh?")
        
  valid = False
  while valid == False :
    mode = int(input(f"Mode position (1 - {len(scale)}): ")) - 1
    if mode < 0 or mode > len(scale) - 1 :
      print("huh?")
      continue
    valid = True
  
  return key, scale, mode
  
##########################################
# MAIN PROGRAM:
##########################################
def main() :
  print("~~~~~Music Scales Program~~~~~") #fancy title
  while True :
    key, scalePass, mode = menu()
    print(f"\t{scale(key, scalePass, mode)} \n")

main()