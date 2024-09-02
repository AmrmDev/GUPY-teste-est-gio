string_formato_padrao = "quero estagiar na Target!"

string_invertida = ""
for i in range(len(string_formato_padrao) -1, -1, -1):
    string_invertida += string_formato_padrao[i]

print("string original: ", string_formato_padrao)
print("string invertida: ", string_invertida)