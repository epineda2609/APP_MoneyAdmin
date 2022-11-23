import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
import dbMoney
import requests
from datetime import datetime
from dateutil.relativedelta import relativedelta

class TkMoney:
	def __init__(self):
#------------------------------ Database
		self.moneyaccount1 = dbMoney.Database()
#------------------------------ Ventana1
		self.prinWindow = tk.Tk()
		self.prinWindow.title("MoneyApp")
		self.notebook1 = ttk.Notebook(self.prinWindow)
#---------------------------------------------------------------- page1
		self.page1 = ttk.Frame(self.notebook1)
		self.notebook1.add(self.page1, text="Movimientos")
		self.label1 = ttk.Label(self.page1, text="Mes:")
		self.label1.grid(padx=5, pady=5, column=0, row=0)
		self.month1 = tk.StringVar() #Combobox3
		month = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
		self.combobox3 = ttk.Combobox(self.page1, width=10, textvariable=self.month1, values= month, state="readonly")
		self.combobox3.current(0)
		self.combobox3.grid(padx=5, pady=5, column=1, row=0)
		self.label5 = ttk.Label(self.page1, text="Año:")
		self.label5.grid(padx=5, pady=5, column=0, row=1)
		self.years1 = tk.StringVar() #Combobox4
		years = ("2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032")
		self.combobox4 = ttk.Combobox(self.page1, width=10, textvariable=self.years1, values= years, state="readonly")
		self.combobox4.current(0)
		self.combobox4.grid(padx=5, pady=5, column=1, row=1)
		# self.entry1 = ttk.Entry(self.page1)
		# self.entry1.grid(padx=5, pady=5, column=1 , row=0)
		self.label2 = ttk.Label(self.page1, text="Monto:")
		self.label2.grid(padx=5, pady=5, column=0, row=2)
		self.entry2 = ttk.Entry(self.page1)
		self.entry2.grid(padx=5, pady=5, column=1, row=2)
		self.label3 = ttk.Label(self.page1, text="Tablas:")
		self.label3.grid(padx=5, pady=5, column=0, row=4)
		self.table = tk.StringVar() #combobox1
		tables = ("movimientos", "ingresoJML","inversionBolsa", "ahorrosUSD", "ahorrosCripto", "inversionPF", "cuotas")
		self.combobox1 = ttk.Combobox(self.page1, width =20, textvariable=self.table, values=tables, state="readonly")
		self.combobox1.current(0)
		self.combobox1.grid(padx=5, pady=5, column=1 , row=4)
		self.button1 = ttk.Button(self.page1, text="Guardar", command=self.buttonFunction)
		self.button1.grid(padx=5, pady=5, column=3, row=0)
		self.label4 = ttk.Label(self.page1, text="Items:")
		self.label4.grid(padx=5, pady=5, column=0, row=3)
		self.items = tk.StringVar() #combobox2
		items = ("alquiler","seguroAuto","luz","agua","tramite","gas","telefono","ABL","internet","banco","cochera","cuotas","gym","farmacia","mercado","nafta","viajes","entretenimiento","expensa","hbo","netflix","googleDrive","youtube","spotify","bienes","gastos","ingresosAdicionales","ingresoInversiones","ingresoUSD","ingresoJML","ahorro","sobrante")
		self.combobox2 = ttk.Combobox(self.page1, width=20, textvariable=self.items, values=items, state="readonly")
		self.combobox2.current(0)
		self.combobox2.grid(padx=5, pady=5, column=1 , row=3)
		self.label8 = ttk.Label(self.page1, text="Gastos:")
		self.label8.grid(padx=5, pady=5, column=4, row=0)
		self.gastoAll = tk.DoubleVar()
		self.entry3 = ttk.Entry(self.page1, textvariable=self.gastoAll)
		self.entry3.grid(padx=5, pady=5, column=5, row=0)

#---------------------------------------------------------------- page2
		self.page2 = ttk.Frame(self.notebook1)
		self.notebook1.add(self.page2, text="IngresoJML")
		self.label6 = ttk.Label(self.page2, text="Mes:")
		self.label6.grid(padx=5, pady=5, column=0, row=0)
		self.month2 = tk.StringVar() #Combobox5
		month2 = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
		self.combobox5 = ttk.Combobox(self.page2, width=10, textvariable=self.month2, values= month2, state="readonly")
		self.combobox5.current(0)
		self.combobox5.grid(padx=5, pady=5, column=1, row=0)
		self.label7 = ttk.Label(self.page2, text="Año:")
		self.label7.grid(padx=5, pady=5, column=0, row=1)
		self.years2 = tk.StringVar() #Combobox6
		years2 = ("2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032")
		self.combobox6 = ttk.Combobox(self.page2, width=10, textvariable=self.years2, values= years2, state="readonly")
		self.combobox6.current(0)
		self.combobox6.grid(padx=5, pady=5, column=1, row=1)
		self.button2 = ttk.Button(self.page2, text="Registrar", command=self.registerUSD)
		self.button2.grid(padx=5, pady=5, column=1, row=2)

#---------------------------------------------------------------- page3
		self.page3 = ttk.Frame(self.notebook1)
		self.notebook1.add(self.page3, text="Inversion-IO")
#---------------------------------------------------------------- page4
		self.page4 = ttk.Frame(self.notebook1)
		self.notebook1.add(self.page4, text="Ahorros USD")
#---------------------------------------------------------------- page5
		self.page5 = ttk.Frame(self.notebook1)
		self.notebook1.add(self.page5, text="Ahorros Cripto")
#---------------------------------------------------------------- page6
		self.page6 = ttk.Frame(self.notebook1)
		self.notebook1.add(self.page6, text="Inversion PF")
#---------------------------------------------------------------- page7
		self.page7 = ttk.Frame(self.notebook1)
		self.notebook1.add(self.page7, text="Cuotas")
		self.label9 = ttk.Label(self.page7, text="Mes:")
		self.label9.grid(padx=5, pady=5, column=0, row=0)
		self.month7 = tk.StringVar() #Combobox7
		month7 = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")
		self.combobox7 = ttk.Combobox(self.page7, width=10, textvariable=self.month7, values= month7, state="readonly")
		self.combobox7.current(0)
		self.combobox7.grid(padx=5, pady=5, column=1, row=0)
		self.label10 = ttk.Label(self.page7, text="Año:")
		self.label10.grid(padx=5, pady=5, column=0, row=1)
		self.years7 = tk.StringVar() #Combobox8
		years7 = ("2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030", "2031", "2032")
		self.combobox8 = ttk.Combobox(self.page7, width=10, textvariable=self.years7, values= years7, state="readonly")
		self.combobox8.current(0)
		self.combobox8.grid(padx=5, pady=5, column=1, row=1)
		self.label11 = ttk.Label(self.page7, text="Cuotas:")
		self.label11.grid(padx=5, pady=5, column=3, row=0)
		self.cuotasVar = tk.IntVar()
		self.cuotas = (("3", 3),("6",6),("12",12),("18",18),("24",24))
		columna = 3
		for cuota in self.cuotas:
			self.radioButton = ttk.Radiobutton(self.page7, text=cuota[0], value=cuota[1], variable=self.cuotasVar)
			self.radioButton.grid(padx=5, pady=5, column=columna, row=1)	
			columna +=1
		self.label12 = ttk.Label(self.page7, text="Monto:")
		self.label12.grid(padx=5, pady=5,column=0, row=2)
		self.entry4 = ttk.Entry(self.page7)
		self.entry4.grid(padx=5, pady=5, column=1, row=2)
		self.label13 = ttk.Label(self.page7, text="Nombre:")
		self.label13.grid(padx=5, pady=5, column=0, row=3)
		self.entry5 = ttk.Entry(self.page7)
		self.entry5.grid(padx=5, pady=5, column=1, row=3)
		self.button3 = ttk.Button(self.page7, text="Guardar", command=self.cuotasIn)
		self.button3.grid(padx=5, pady=5, column= 2, row= 2, rowspan=2)
		
#---------------------------------------------------------------- Cierre de paginas y ventana
		self.notebook1.grid(column=0, row=0)
		self.prinWindow.mainloop()

#---------------------------------------------------------------- FUNCTIONS movimientos
	def guardarMov(self):
		"""Esta función guarda la informacion ingresada en la pagina movimientos. A su vez consulta si el dato es null, si la fila esta creada, y si no esta creada la crea"""
		self.monthG = self.combobox3.get()
		self.yearG = self.combobox4.get()
		self.amountG = self.entry2.get()
		self.itemG = self.combobox2.get()
		self.tableG = self.combobox1.get()
		dataEx = (self.yearG, self.monthG)
		dataT = (self.yearG, self.monthG, self.amountG)
		try:
			response= self.moneyaccount1.consultarExiste(self.itemG, dataEx)
			if response == None:
					self.moneyaccount1.insertarExistente(self.itemG, self.amountG, dataEx)
			else:
				r = mBox.askyesno(message="Ya existe un valor. Desea sumarlo",title="ADVERTENCIA")
				if r == True:
					amountSum = float(self.amountG) + float(response)
					self.moneyaccount1.insertarExistente(self.itemG, amountSum, dataEx)
				else:
					pass
			#Podria agregar un else para cuando ya hay un valor ingresado
		except TypeError:
			self.moneyaccount1.movimientosIn(self.itemG, dataT)
			
	def updateGasto(self):
		"""Esta funcion suma todas las filas que componen la columna gasto e introduce este dato en la columna gasto. La idea es que cada vez que se guarde un gasto este item se actualiza"""
		monthUG = self.combobox3.get()
		yearUG = self.combobox4.get()
		dataUD = (yearUG, monthUG)
		allGasto = self.moneyaccount1.allColumns(dataUD)
		acumulador = 0
		for item in allGasto[0]:
			if item != None:
				itemN = float(item)
				acumulador += itemN
		self.gastoAll.set(acumulador)

	def buttonFunction(self):
		"""Esta funcion es auxiliar: me permite que se ejecute la cantidad de funciones que yo ingrese acá con un solo boton"""
		self.guardarMov()
		self.updateGasto()

#---------------------------------------------------------------- FUNCTIONS IngresoJML
	def registerUSD(self):
		"""Esta función solicita el valor del dolar, busca en la tabla movimientos mi sueldo, luego guarda mi sueldo, lo pasa a dolares y lo guarda en la tabla ingresosJML"""
		r = requests.get("https://api-dolar-argentina.herokuapp.com/api/dolarblue")
		valorUsd = r.json()
		usdBlue = float(valorUsd["venta"])
		self.monthUSD = self.combobox5.get()
		self.yearUSD = str(self.combobox6.get())
		dataUSD = (self.yearUSD, self.monthUSD)
		try:
			sueldoJML = float(self.moneyaccount1.consultarIngreJML(dataUSD))
			sueldoUSD = sueldoJML/usdBlue
			dataRegister = (self.yearUSD, self.monthUSD, usdBlue, sueldoUSD)
			self.moneyaccount1.inIngresosJML(dataRegister)
		except TypeError:
			pass
#---------------------------------------------------------------- FUNCTIONS Cuotas
	def cuotasIn(self):
		"""Esta funcion arma la tabla cuotas de acuerdo a los datos ingresados. De acuerdo a la cantidad de cuotas se completa la cantidad de meses"""

		mesesCuota = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre","enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre","enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre")

		nCuotas = int(self.cuotasVar.get())
		mesActual = self.month7.get()
		#añoActual = self.years7.get()
		montoActual = float(self.entry4.get())
		itemCuota = self.entry5.get()
		inicio = mesesCuota.index(mesActual) + 1
		fin = inicio + nCuotas

		montoMensual = montoActual/nCuotas

		meslist = []
		añolist = []

		for x in range(inicio,fin):
			meslist.append(mesesCuota[x])

		for z in range(1,(nCuotas+1)):
			now = datetime.now()
			new_year = now + relativedelta(months=(z))
			format = new_year.strftime("%Y")
			añolist.append(format)

		self.moneyaccount1.columnAdd(itemCuota)

		for w in range(nCuotas):
			año = añolist[w]
			mes = meslist[w]
			dataCuota = (año, mes, montoMensual)
			self.moneyaccount1.inCuotas(itemCuota, dataCuota)	
		"""Falta hacer que se vayan sumando las cuotas y se actualice el total 
		"""

		

money1 = TkMoney()
