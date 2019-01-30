class objeto():

    def __init__(self, name, apellido):
        self.array = [cartas(), cartas(), cartas(), cartas(), cartas()]
        
        self.name = name
        self.apellido = apellido
        
    def __str__(self):
        for i in self.array:
            self.array[i] = ""
            texto = self.array[i]
        return texto

class cartas():

    def __init__(self):
        self.color = "peon"
        
person = objeto("Josue", "Tavarez")
person_two = objeto("Dante", "Benefactor")
print (person, person_two)

print (person.array)
#chr and ord para usar codigo Ascii
#print (chr(74), ord("J"))

        
        
    
