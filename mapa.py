freq = {}
filename = "./texto.txt"
for piece in open(filename).read().lower().split():
    word = "".join(c for c in piece if c.isalpha())
    if word:
        freq[word] = 1 + freq.get(word, 0)

maxWord = ""
maxCount = 0
for w, c in freq.items():
    if c > maxCount:
        maxWord = w
        maxCount = c

print("Palabra mas frecuente:", maxWord)
print("Numero de concurrencia:", maxCount)
