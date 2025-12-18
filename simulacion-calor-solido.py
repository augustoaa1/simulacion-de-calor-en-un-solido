Ce = 0.385 # J/(g * ºC) # calor especifico del cobre
m = 1000 # g
Ti = 50 # ºC
Tf = Ti # ºC
Q = m * Ce * (Tf - Ti)
while Q <= 100000:
    print("el calor es",Q, "J a una temperatura de", Tf, "ºC" )
    Tf = Tf + 10
    Q =  m * Ce * (Tf - Ti)