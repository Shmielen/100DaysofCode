import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)
again = True

def caesar(text, shift, direction):
  new_str = ''
  if direction == 'decode':
    shift *= -1
  for char in text:
    if char not in alphabet:
      new_str += char
    else:
      new_str += alphabet[alphabet.index(char)+shift]
  print(f"Here's the {direction}d result: {new_str}")
    
while again == True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  caesar(text, shift, direction)
  result = input('Do you want to go again?')
  if result == 'no':
    again = False
