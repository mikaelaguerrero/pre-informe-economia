# -*- coding: utf-8 -*-
"""Oferta, Demanda y Equilibrio de mercados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_99MP6QzJo4dGRBdX3fKhc7xFwcFjEMh
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

class mercado:
  def __init__(self, DAPmax, COmin, d, s):
    self.DAPmax, self.COmin, self.d, self.s = DAPmax, COmin, d, s
  
    if DAPmax < COmin:
      raise ValueError('Demanda insuficiente.')
    """
    Configura los parámetros del mercado. DAP￿￿￿ es la máxima disposición a
    pagar de cualquier consumider-el intercepto con el eje y de la función
    de demanda. COmin es el mínimo costo oportunidad de cualquier␣
    ↪productor-el
    intercepto con el eje y de la función de oferta. s es la pendiente de␣
    ↪la f
    unción de oferta. d es la pendiente de la función de demanda...
    """

  def cantidad_equilibrio(self):
    "Cálculo cantidad de equilibrio"
    return (self.DAPmax - self.COmin)/(self.d + self.s)

  def precio_equilibrio(self):
    "Cálculo cantidad de equilibrio"
    return self.DAPmax - self.d * self.cantidad_equilibrio()

  def excedente_consumidor(self):
    "Cálculo excedente consumidor"
    return (self.DAPmax - self.precio_equilibrio())*self.cantidad_equilibrio()/2

  def excedente_productor(self):
    "Cálculo excedente productor"
    return (self.precio_equilibrio() - self.COmin) * self.cantidad_equilibrio()/2

  def excedente_total(self):
    "Cálculo excedente total"
    return self.excedente_productor() + self.excedente_consumidor()

  def demanda(self,x):
    "Función demanda"
    return self.DAPmax - self.d*x

  def oferta(self,x):
    "Función oferta"
    return self.COmin + self.s*x
# Parámetros iniciales DAPmax, COmin, d, s
params_ini = 7,3,1,1
m = mercado(*params_ini)
q_max = m.cantidad_equilibrio() * 2
q_grid = np.linspace(0.0, q_max, 100)
pd = m.demanda(q_grid)
2
ps = m.oferta(q_grid)
fig, ax = plt.subplots()
ax.plot(q_grid, pd, lw=2, alpha=0.6, label='demanda')
ax.plot(q_grid, ps, lw=2, alpha=0.6, label='oferta')
ax.set_xlabel('cantidad', fontsize=14)
ax.set_xlim(0, q_max)
ax.set_ylabel('precio', fontsize=14)
ax.legend(loc='lower right', frameon=False, fontsize=14)
ax.set(title='Oferta, Demanda y Equilibrio de mercados')
plt.show()

# Baseline DAPmax, COmin, d, s
params_ini = 7,3,1,1
m = mercado(*params_ini)
print("Excedente productor =",m.excedente_productor())
print("Excedente consumidor =",m.excedente_consumidor())
print("Excedente total =",m.excedente_total())
3
print("Cantidad de equilibrio =",m.cantidad_equilibrio())
print("Precio de equilibrio =",m.precio_equilibrio())