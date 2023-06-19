class alma:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

lista = []

def read():
    with open("xyz.txt","r") as z:
        z.strip().split()
        x = z[1]
        y = z[2]
        z = z[3]
        obj = alma(x,y,z)
        lista.append(obj)

#float
#bool
#str
#int

#math.
#sqrt
#pow
#floor loefelé kerekít

#round 
#lower (islower) True/False
#upper (isupper) True/False