suspects = [("Max Zorin", "Kills with guns", "Chip Tycoon"), ("Hugo Drax",), ("Jaws", "Bites people", "Mutant"),
            ("Nick Nack", "Really short"), ("Le Chiffre", "Good at poker", "Really evil"),
            ("Francisco Scaramanga", "Has a Golden Gun", "Probably will melt"),
            ("Mr Big", "Also the name of a rock band", "Dictator of San Monique")]

# write your program here
num = int(input('WHO DID IT HUGO!? '))
if num == 7:
    num = 0
cul = str(suspects[num][1:])
culprit = suspects[num][0]
print('It was ' + culprit)
print('Data: ' + cul)
