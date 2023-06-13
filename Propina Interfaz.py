import tkinter as tk

def calcular_propina():
    cantidad_factura = float(cantidad_entry.get())
    porcentaje_propina = float(porcentaje_entry.get())
    propina = cantidad_factura * (porcentaje_propina / 100)
    total = cantidad_factura + propina
    propina_label.config(text="Propina: $%.2f" % propina)
    total_label.config(text="Total a pagar (incluyendo propina): $%.2f" % total)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de propinas")

# Crear y posicionar los elementos de la interfaz
cantidad_label = tk.Label(ventana, text="Cantidad de la factura:")
cantidad_label.pack()
cantidad_entry = tk.Entry(ventana)
cantidad_entry.pack()

porcentaje_label = tk.Label(ventana, text="Porcentaje de propina:")
porcentaje_label.pack()
porcentaje_entry = tk.Entry(ventana)
porcentaje_entry.pack()

calcular_button = tk.Button(ventana, text="Calcular propina", command=calcular_propina)
calcular_button.pack()

propina_label = tk.Label(ventana, text="Propina: $0.00")
propina_label.pack()

total_label = tk.Label(ventana, text="Total a pagar (incluyendo propina): $0.00")
total_label.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
