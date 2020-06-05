def simple_implementation(arr):
  # loop from 1 to end of array
  for i in range(1, len(arr)):
    temp = arr[i]

    j = i

    while j > 0 and temp < arr[j-1]:
      # copy element to left 
      arr[j] = arr[j - 1]

      j -= 1

    arr[j] = temp

  return arr


  # Sorting Books!

  class Book:

    def __init__(self, author, title, genre):
      self.author = author
      self.title = title
      self.genre = genre

    def __str__(self):
      return f'{self.title} by {self.author} in {self.genre}'