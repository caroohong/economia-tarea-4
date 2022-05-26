import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
class mercado:
    def __init__(self, DAPmax, COmin, d, s):
        self.DAPmax, self.COmin, self.d, self.s = DAPmax, COmin, d, s
        if DAPmax < COmin:
            raise ValueError('Demanda insuficiente.')

    def cantidad_equilibrio(self):
        "Cálculo cantidad de equilibrio"
        return  (self.DAPmax - self.COmin)/(self.d + self.s)

    def precio_equilibrio(self):
        "Cálculo cantidad de equilibrio"
        return  self.DAPmax - self.d * self.cantidad_equilibrio()

    def excedente_consumidor(self):
        "Cálculo excedente consumidor"
        return (self.DAPmax - self.precio_equilibrio())*self.cantidad_equilibrio()/2

    def excedente_productor(self):
        "Cálculo excedente productor"
        return (self.precio_equilibrio() - self.COmin) * self.cantidad_equilibrio() /2

    def excedente_total(self):
        "Cálculo excedente total"
        return self.excedente_productor() + self.excedente_consumidor()
    
    def demanda(self,x):
        "Función demanda"
        return self.DAPmax - self.d*x
        
    def oferta(self,x):
        "Función oferta"
        return self.COmin + self.s*x
#d= $(13.99-8.99)/1 suscripcion
#DAPmax, COmin, d, s
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0,16,0.1)
y19 = 1.05*x-1.793505
y21= 1.05*x-1.982295
#param_i = 15.49,0,0.76,1.05
#m = mercado(*param_i) 
param_i = 15.49,1.7081,0.76,1.05
m = mercado(*param_i) 

q_max = m.cantidad_equilibrio() * 2
q_grid = np.linspace(0.0, q_max, 100)
pd = m.demanda(q_grid)
ps = m.oferta(q_grid)

fig, ax = plt.subplots()
ax.plot(q_grid, pd, lw=2, alpha=0.6, label='demanda')
ax.plot(q_grid, ps, lw=2, alpha=0.6, label='oferta')
ax.plot(x,y19, label='oferta 19%')
ax.plot(x,y21, label='oferta 21%')
ax.set_xlabel('cantidad', fontsize=14)
ax.set_xlim(0, q_max)
ax.set_ylabel('precio', fontsize=14)
ax.legend(loc='lower right', frameon=False, fontsize=14)
ax.set(title='Oferta, Demanda y Equilibrio de mercados')
plt.show()

print("Excedente productor =",m.excedente_productor())
print("Excedente consumidor =",m.excedente_consumidor())
print("Excedente total =",m.excedente_total())
print("Cantidad de equilibrio =",m.cantidad_equilibrio())
print("Precio de equilibrio =",m.precio_equilibrio())
