class Llantas():
    def __init__(self, rin):
        self.rin=rin;
    def mover(self):
        return "Las llantas estan girando"
    
class vehiculo():
    def __init__(self, placas, rin):
        self.placas=placas;
        self.llantas= Llantas(18);
    def mover(self):
        self.llantas.mover();
        return "El carro se esta moviendo"
    def verplaca(self):
        return self.placas
#aplicamos el patron de simplicidad ya que hacemos que el carro se mueva moviendo sus llantas, ademas de respetar la consistencia, tomando en cuenta que el problema a solucinar por el metodo mover es hacer andar el carro
    
class Red():
    def __init__(self):
        self.nombre='red de nylon'
    def lanzar(self):
        return 'se ha lanzado la red'
    def cortar(self):
        return 'se ha cortado la red'

class Spiderman():
    red=Red()
    nombre='petter'
    def init(self):pass
    #Bien
    def lanzarRed(self):
        return self.red.lanzar()
    #Mal
    def cortarRed(self):
        return self.red.lanzar()
    
#implementation
hero=Spiderman()
SpiderMovil= vehiculo("xya351", 18)

print("¿se lanzara la red?, ",hero.lanzarRed())
#Fallo en el principio del menor asombro
#print("¿se cortara la red?, ",hero.cortarRed())


print("las placas del vehiculo son: ", SpiderMovil.verplaca(),", ",  SpiderMovil.mover())
#una manera de rompe la lew demeter es de la siguiente forma, suponiendo que queremos mover el carro.
#print( SpiderMovil.llantas.mover())
