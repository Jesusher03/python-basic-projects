print("Text analyzer")
text = (input("Add a text \n"))
text = text.lower()

print ("I'm going to ask you for three letters")
letter = input("write three letters (put a ',' before each letter)")
letter = letter.lower()
list_l = letter.split(",")

for letter in list_l:
    number_letters = text.count(letter)#Here we count how many times each letter appears in the text
    print("The letter", letter, "appears", number_letters, "times")

    

total = len(text) #Here we know the number of caracters the text has


print("The total of caracters is", total) #give the total of caracters 
print("The first letter is " + text[0])  #give the first letter
print("The last letter is " + text[-1]) #give the last letter

union = "".join(text[::-1]) #reverse the text
print(union)

search = "".join(text)
control = "python" in search

print(control)  #This say to us if the word "python is in the text the user write"

