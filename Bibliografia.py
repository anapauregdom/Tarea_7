
import random, string
class Bibliografia:
    def __init__(self,auth_name,auth_last_name1,auth_last_name2,title, year, tipe):
        self.auth_name=auth_name
        self.auth_last_name1= auth_last_name1
        self.auth_last_name2= auth_last_name2
        self.title = title
        self.year=year
        self.tipe=tipe

    def __str__(self):
        to_string = ""
        to_string += "Nombre del autor: " + self.auth_name + '\n'
        to_string += "Apellidos: " + self.auth_last_name1 +" "+ self.auth_last_name2 + '\n'
        to_string += 'Titulo: ' + self.title + '\n'
        to_string += 'Fecha de publicacion: ' + str(self.year) + '\n'
        to_string += 'Tipo: ' + self.tipe +'\n'
        return to_string
    def get_title(self):
        return "Titulo: "+ self.title + "\n"
    def get_auth(self):
        return "Autor: " +self.auth_name + " " + self.auth_last_name1 + " " + self.auth_last_name2 + "\n"

    def create_random_list(self,n_items=10):
        random_list=[]
        for i in range(n_items):
            letters = string.ascii_lowercase
            auth_name=''.join(random.choice(letters) for j in range(5))
            auth_last_name1 = ''.join(random.choice(letters) for j in range(7))
            auth_last_name2 = ''.join(random.choice(letters) for j in range(7))
            title = ''.join(random.choice(letters) for j in range(8))
            year = int (random.random() * 10000)
            tipe = ''.join(random.choice(letters) for j in range(8))
            Bibliografia2 = Bibliografia(auth_name,auth_last_name1,auth_last_name2,title,year,tipe)
            random_list.append(Bibliografia2)
        return random_list
    def select_authors(self,lista):
        a_regresar=[]
        for bibliografia in lista:
            a_insertar= "Autor: " +bibliografia.auth_name + " " +bibliografia.auth_last_name1 + " " + bibliografia.auth_last_name2 + "\n"
            a_regresar.append(a_insertar)
        return a_regresar
    def select_titles(self, lista):
        a_regresar=[]
        for bibliografia in lista:
            a_insertar= "Titulo: " + bibliografia.title
            a_regresar.append(a_insertar)
        return a_regresar
#author es una lista con el nombre como primer elemento, apellido paterno como segundo y materno como tercero.
    def exists_author(self,lista,author):
        if len(author)!=3:
            return
        else:
            for i in lista:
                if (author[0]  == i.auth_name) and (author[1] == i.auth_last_name1) and (author[2] == i.auth_last_name2):
                    return True
            return False
#title es un string con el titulo
    def exists_title(self,lista,title):
        for i in lista:
            if title == i.title:
                return True
        return False
    def coincidencias(self, lista1,lista2):
        a_regresar=[]
        for elem1 in lista1:
            for elem2 in lista2:
                if (elem1.auth_name == elem2.auth_name) and (elem1.auth_last_name1 == elem2.auth_last_name1) and (elem1.auth_last_name2 == elem2.auth_last_name2):
                    a_insertar = elem1.auth_name + " " +elem1.auth_last_name1 + " " + elem1.auth_last_name2
                    a_regresar.append(a_insertar)
        return a_regresar
class BibliografiaLibro(Bibliografia):
    def __init__(self,auth_name,auth_last_name1,auth_last_name2,title, year, tipe, editorial, genre):
        super().__init__(auth_name,auth_last_name1,auth_last_name2,title, year, tipe)
        self.editorial = editorial
        self.genero = genre
    def __str__(self):
        to_string =super().__str__()
        to_string += "Editorial: " + self.editorial + '\n'
        to_string += "Genero: " + self.genero + '\n'
        return to_string
class BibliografiaArticuloInvestugacion(Bibliografia):
    def __init__(self,auth_name,auth_last_name1,auth_last_name2,title, year, tipe, institute, subject):
        super().__init__(auth_name,auth_last_name1,auth_last_name2,title, year, tipe)
        self.institute = institute
        self.subject = subject
        
    def __str__(self):
        to_string =super().__str__()
        to_string += "Instituto: " + self.institute + '\n'
        to_string += "Tema de investigacion: " + self.subject + '\n'
        return to_string

    def get_auth(self):
        return self.auth_last_name1 + " " + self.auth_last_name2 + ' ' +self.auth_name[0]+ "."

class BibliografiaLibroInfantil(BibliografiaLibro):
    def __init__(self,auth_name,auth_last_name1,auth_last_name2,title, year, tipe, editorial, genre,edad, dibujos):
        super().__init__(auth_name,auth_last_name1,auth_last_name2,title, year, tipe,editorial,genre)
        self.edad = edad
        self.dibujos  = dibujos
    def __str__(self):
        to_string =super().__str__()
        to_string += "Rango de edad: " + self.edad + '\n'
        to_string += "Dibujos: " + str(self.dibujos) + '\n'
        return to_string
if __name__=="__main__":
    Bibliografia1 = Bibliografia("Lev","Nikoláievich","Tolstói","La guerra y la paz", 1869,"Libro")
    print(Bibliografia1)
    print(Bibliografia1.get_title())
    print(Bibliografia1.get_auth())    

    randomList=Bibliografia1.create_random_list()
    randomList.append(Bibliografia1)
    
    randomList2 = Bibliografia1.create_random_list()
    randomList2.append(Bibliografia1)

  
    author1 = [randomList[0].auth_name,randomList[0].auth_last_name1,randomList[0].auth_last_name2]
    title1 = randomList[2].title
    
    BibliografiaLib = BibliografiaLibro("Lev","Nikoláievich","Tolstói","La guerra y la paz", 1869,"Libro", "Alfaguara","Novela histórica, novela romántica, novela bélica y novela filosófica ")
    print(BibliografiaLib)

    BibliografiaArt=BibliografiaArticuloInvestugacion("Lev","Nikoláievich","Tolstói","La guerra y la paz", 1869,"Articulo de investigacion",'UNAM',"Biologia" )
    print(BibliografiaArt)
    print(BibliografiaArt.get_auth())

    BibliografiaLibroInfantil = BibliografiaLibroInfantil("Lev","Nikoláievich","Tolstói","La guerra y la paz", 1869,"Libro", "Alfaguara","Novela histórica, novela romántica, novela bélica y novela filosófica ", "De 6 a 12" , True)

    print(BibliografiaLibroInfantil)
    
    print("Ejercicio 2.2.1 " + "\n")
    print(Bibliografia1.select_authors(randomList))
    print("\n")
    print("Ejercicio 2.2.2" + "\n")
    print(Bibliografia1.select_titles(randomList))
    print("\n")
    print("Ejercicio 2.3.1" + "\n" + "Verificando si existe un autor que sabemos que existe")
    print(Bibliografia1.exists_author(randomList,author1))
    print("\n" + "Verificando que existe el author = [zzzzzzz,zzz,z]")
    print(Bibliografia1.exists_author(randomList,["zzzzzzz","zzz","z"]))
    print("\nEjercicio 2.3.2" + "\n" + "Verificando si existe un titulo que sabemos que existe")
    print(Bibliografia1.exists_title(randomList,title1))
    print("\n" + "Verificando si existe el titulo The pit and the pendulum")
    print(Bibliografia1.exists_title(randomList,"The pit and the pendulum"))
    print("\nEjercicio 2.4\n")
    print("Estamos insertando a Tolstói en ambas listas asi que solo deberia salir el")
    print(Bibliografia1.coincidencias(randomList,randomList2 ))
