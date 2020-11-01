phrase = input('Enter phrase ')

phrase_len = len(phrase)

# calculating the number of the central element.
# The length of the user input can be even.
# in that case there will be two central elements, the program will consider the element with the highest number
# it is usually should be clarified by the product owner, but I'm to lazy to ask for it

central_elenent_no = int(phrase_len/2)

central_elenent = phrase[central_elenent_no]

print(central_elenent)

if central_elenent == phrase[0]:
    cut_phraze = phrase[1:-1:1]
    print(cut_phraze)