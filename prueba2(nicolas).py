print("bienvenido a la clinica dental de oro")
opc=0
int(input("ingrese un servicio disponible"))
if opc == 0:
   brackets: 800.000
   implantes: 475.000
   carillas: 250.000
   
   print("\t\menu")
   print("-"*50)
   print ("cotizacion")
   print("-"*50)
   print("servicios disponibles:")
   print("carillas porcelana $250.000")
   print("implantes dentales $475.000")
   print("ortodoncia brackets $800.000")
   
   int(input("Eliga su tratamiento"))
   cont_tratamiento = 0
   brackets = int(input("Ingrese cantidad de brackets"))
   while brackets <= 1:
         brackets = int(input("ingrese digito valido"))
         if brackets >0:
            cont_brackets =(cont_brackets + brackets)
   implantes = int(input("¿cuantos implantes va a necesitar usted?"))
   while implantes <= 2:
         implantes = int(input("ingrese digito valido:"))
         if implantes >0:
            cont_implantes = (cont_implantes + implantes)
   carillas = int(input("ingrese numero de carillas"))
   while carillas <= 3:
          carillas = int(input("ingrese digito valido:"))
          if carillas >0:
             cont_carillas =(cont_carillas + carillas)
             


 

  

