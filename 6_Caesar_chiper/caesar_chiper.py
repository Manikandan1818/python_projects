import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# def encrypt(original_text, shift_amount):
#     cipher_text = "" #j    
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)  + shift_amount #7 -9        
#         shifted_position %= len(alphabet) #0-25
#         cipher_text += alphabet[shifted_position] #j    
#     print(f"Here is the encoded result: {cipher_text}")
# encrypt(original_text=text, shift_amount=shift)

# def decrypt(original_text, shift_amount):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amount
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the decoded result: {output_text}")
# decrypt(original_text=text, shift_amount=shift)


def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    if encode_or_decode == "decode":
        shift_amount *= -1               
               
    for letter in original_text:

        if letter not in alphabet:
            output_text += letter
        else:       
            shifted_position = alphabet.index(letter)  + shift_amount
            shifted_position %= len(alphabet) #0-25
            output_text += alphabet[shifted_position] #j    
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_Continue = True

while should_Continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_Continue = False
        print("Good Bye")