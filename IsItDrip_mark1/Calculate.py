def drip(image_matrix):
  red_count = 0
  green_count = 0
  blue_count = 0
  pixel_number = 0
  #first half of outfit
  for i in range(len(image_matrix)//2):
        for j in range(int(0.25*len(image_matrix[i])), int(0.75*len(image_matrix[i]))):
          pixel = image_matrix[i][j]
          pixel_number+=1
          red_count+=pixel[0]
          green_count += pixel[1]
          blue_count += pixel[2]
  average = [int(red_count/pixel_number), int(green_count/pixel_number), (blue_count/pixel_number)]


  #second half of outfit
  #re-initializing
  red_count = 0
  green_count = 0
  blue_count = 0
  pixel_number = 0
  for i in range(len(image_matrix)//2, len(image_matrix)):
        for j in range(int(0.25*len(image_matrix[i])), int(0.75*len(image_matrix[i]))):
          pixel = image_matrix[i][j]
          pixel_number+=1
          red_count+=pixel[0]
          green_count += pixel[1]
          blue_count += pixel[2]
  average1 = [int(red_count/pixel_number), int(green_count/pixel_number), (blue_count/pixel_number)]
  difference = []
  for k in range(len(average)):
    #absolute value of the difference
    diff = abs(average[k]-average1[k])
    difference.append(diff)
  '''
  with fashion, the outfit is as stylish as it's weakest stylish colour difference/correlation
  so we need to find the max difference and categorize the get-up as one of the groups established by colour theory.
  In descending order of drip rating (how fashionable the get-up is):
  1)Monochromatic
  2)Analogous
  3)Tetradic
  4)Triadic
  5)Split Complementary
  6)Complementary
  A big caveat and limitation of our approach is that only the primary colours and their subsidiaries are being assesed.
  Black & White are essentially not considered here.
  '''
  check = min(difference)
  if check<20:
    return 10
  elif check<30:
    return 9
  elif check<40:
    return 8
  elif check<60:
    return 7
  elif check<70:
    return 6
  elif check<80:
    return 5
  elif check<85:
    return 4
  elif check<100:
    return 3
  elif check<120:
    return 2
  else:
    return 1

#very basic recommendation for RGB changes
def recommendation(image_matrix):
  red_count = 0
  green_count = 0
  blue_count = 0
  pixel_number = 0
  #first half of outfit
  for i in range(len(image_matrix)//2):
        for j in range(int(0.25*len(image_matrix[i])), int(0.75*len(image_matrix[i]))):
          pixel = image_matrix[i][j]
          pixel_number+=1
          red_count+=pixel[0]
          green_count += pixel[1]
          blue_count += pixel[2]
  average = [int(red_count/pixel_number), int(green_count/pixel_number), (blue_count/pixel_number)]


  #second half of outfit
  #re-initializing
  red_count = 0
  green_count = 0
  blue_count = 0
  pixel_number = 0
  for i in range(len(image_matrix)//2, len(image_matrix)):
        for j in range(int(0.25*len(image_matrix[i])), int(0.75*len(image_matrix[i]))):
          pixel = image_matrix[i][j]
          pixel_number+=1
          red_count+=pixel[0]
          green_count += pixel[1]
          blue_count += pixel[2]
  average1 = [int(red_count/pixel_number), int(green_count/pixel_number), (blue_count/pixel_number)]
  dominant = max(average)
  dominant1 = max(average1)
  colours = ["red", "green", "blue"]
  dominant_colours = []
  dominant_colours.append(colours[average.index(dominant)])
  dominant_colours.append(colours[average1.index(dominant1)])
  return dominant_colours



