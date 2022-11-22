import sqlite3

class Database:
    def __init__(self):
        self.movimientos()
        self.ingresoJML()
        self.inversionBolsa()
        self.ahorrosUSD()
        self.ahorrosCripto()
        self.inversionPF()
        self.cuotas()
#---------------------------------------------------------------- Tabla Movimientos
    def movimientos(self):
        """Creacion de la tabla principal donde se registran 
        todos los gastos, inversiones y ahorros del mes"""
        self.conexion = sqlite3.connect("controlGasto.db")
        try:
            self.conexion.execute("""
                                    CREATE TABLE movimientos (
                                        "id" INTEGER PRIMARY KEY AUTOINCREMENT,
                                        "año" INTEGER,
                                        "mes" TEXT,
                                        "alquiler" REAL,
                                        "seguroAuto" REAL,
                                        "luz" REAL,
                                        "agua" REAL,
                                        "tramite" REAL,
                                        "gas" REAL,
                                        "telefono" REAL,
                                        "ABL" REAL,
                                        "internet" REAL,
                                        "banco" REAL,
                                        "cochera" REAL,
                                        "cuotas" REAL,
                                        "gym" REAL,
                                        "farmacia" REAL,
                                        "mercado" REAL,
                                        "nafta" REAL,
                                        "viajes" REAL,
                                        "entretenimiento" REAL,
                                        "expensa" REAL,
                                        "hbo" REAL,
                                        "netflix" REAL,
                                        "googleDrive" REAL,
                                        "youtube" REAL,
                                        "spotify" REAL,
                                        "bienes" REAL,
                                        "gastos" REAL,
                                        "ingresosAdicionales" REAL,
                                        "ingresoInversiones" REAL,
                                        "ingresoUSD" REAL,
                                        "ingresoJML" REAL,
                                        "valorUSD" REAL,
                                        "JML_USD" REAL
                                        "ahorro" REAL,
                                        "sobrante" REAL
                                    )""")
        except sqlite3.OperationalError:
            pass
        self.conexion.close()   

    def consultarExiste(self, busqueda, dataEx):
        """Esta funcion comprueba de acuerdo al año y el mes si el items ya esta cargado o si tiene valor null"""
        self.conexion = sqlite3.connect("controlGasto.db")
        self.busquedaEx = busqueda
        self.añoEx = str(dataEx[0])
        self.mesEx = dataEx[1]
        self.sentenciaEx = f"SELECT {self.busquedaEx} FROM movimientos WHERE año={self.añoEx} AND mes='{self.mesEx}'"
        self.cursor = self.conexion.execute(self.sentenciaEx)
        self.filaEx = self.cursor.fetchone()
        return self.filaEx[0]


    def insertarExistente(self, busqueda, monto, dataInsert):
        """Esta función se encarga de insertar informacion en los items que aparecen como null dentro de una fila de mes ya creada. SOLO PARA LA TABLA MOVIMIENTO"""
        self.item = busqueda
        self.monto = monto
        self.añoInsert = str(dataInsert[0])
        self.mesInsert = dataInsert[1]
        try: 
            self.sentenciaInsert = f"UPDATE movimientos SET {self.item} = {self.monto} WHERE año={self.añoInsert} AND mes='{self.mesInsert}'"
            self.conexion = sqlite3.connect("controlGasto.db")
            self.cursor = self.conexion.execute(self.sentenciaInsert)
            self.conexion.commit()
            self.conexion.close()
        except sqlite3.OperationalError:
            pass

    def movimientosIn(self, busqueda, data):
        """Esta función permite ingresar los distintos items de acuerdo al año y al mes, para ello hay que pasarle que items queremos insertar y la tupla con los datos"""
        self.conexion = sqlite3.connect("controlGasto.db")
        self.busquedaIn = busqueda
        self.sentencia = f"INSERT INTO movimientos (año, mes,{self.busquedaIn}) VALUES (?,?,?)"
        self.cursor= self.conexion.execute(self.sentencia, data)
        self.conexion.commit()
        self.conexion.close()

    def allColumns(self, data):
        """Esta funcion te devuelve todas las filas que se suman para la fila gastos"""
        self.conexion = sqlite3.connect("controlGasto.db")
        yearAll = str(data[0])
        monthAll = data[1]
        sentenciaAll = f"SELECT alquiler, seguroAuto, luz, agua, tramite, gas, telefono, ABL, internet, banco, cochera, cuotas, gym, farmacia, mercado, nafta, viajes, entretenimiento, expensa, hbo, netflix, googleDrive, youtube, spotify, bienes FROM movimientos WHERE  año={yearAll} AND mes='{monthAll}'"
        cursor = self.conexion.execute(sentenciaAll)
        filas = cursor.fetchall()
        return filas

#---------------------------------------------------------------- Tabla ingresoJML
    def ingresoJML(self):
        """Creacion de la tabla donde registro mi ingreso principal y
        lo convierto a dolares de acuerdo a la cotizacion del día"""
        self.conexion = sqlite3.connect("controlGasto.db")
        try:
            self.conexion.execute(""" 
                                    CREATE TABLE ingresosJML (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        año INTEGER,
                                        mes TEXT,
                                        valorUSD REAL,
                                        JML_USD REAL
                                        )""")
        except sqlite3.OperationalError:
            pass
        self.conexion.close()

    def consultarIngreJML(self, dataEx):
        """Esta funcion obtiene de acuerdo al año y el mes el ingresoJML"""
        self.conexion = sqlite3.connect("controlGasto.db")
        self.añoEx = str(dataEx[0])
        self.mesEx = dataEx[1]
        self.sentenciaEx = f"SELECT ingresoJML FROM movimientos WHERE año={self.añoEx} AND mes='{self.mesEx}'"
        self.cursor = self.conexion.execute(self.sentenciaEx)
        self.filaEx = self.cursor.fetchone()
        return self.filaEx[0]
    
    def inIngresosJML(self, data):
        """Esta función permite ingresar el sueldo en dolares y el valor del dolar al momento de registrar el sueldo"""
        self.conexion = sqlite3.connect("controlGasto.db")
        self.sentencia = "INSERT INTO ingresosJML (año, mes, valorUSD, JML_USD) VALUES (?,?,?,?)"
        self.cursor= self.conexion.execute(self.sentencia, data)
        self.conexion.commit()
        self.conexion.close()
#---------------------------------------------------------------- Tabla inversion Bolsa
    def inversionBolsa(self):
        """Creacion de la tabla donde registro las inversiones en la bolsa. En esta 
        se registran la cantidad y el valor de compra, el total invertido en el mes y
        el total acumulado"""
        self.conexion = sqlite3.connect("controlGasto.db")
        try:
            self.conexion.execute("""
                                    CREATE TABLE inversionBolsa (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            año INTEGER,
                                            mes TEXT,
                                            cantAPPL NUMERIC,
                                            APPL REAL,
                                            cantKO NUMERIC,
                                            KO REAL,
                                            cantAMZN NUMERIC,
                                            AMZN REAL,
                                            cantVZ NUMERIC,
                                            VZ REAL,
                                            total REAL,
                                            totalAcumulado REAL)
                                            """)
        except sqlite3.OperationalError:
            pass
        self.conexion.close()
#----------------------------------------------------------------Tabla ahorrosUSD
    def ahorrosUSD(self):
        """Creacion de la tabla donde se registran los ahorros en dolares tanto virtuales,
        como fisicos. Tambien se registron las ventas de cualquiera de ellos
        """
        self.conexion = sqlite3.connect("controlGasto.db")
        try:
            self.conexion.execute("""
                                    CREATE TABLE ahorrosUSD (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        año INTEGER,
                                        mes TEXT,
                                        USDT REAL,
                                        USD REAL,
                                        gastoUSDT REAL,
                                        gastoUSD REAL,
                                        gastoARS REAL
                                    )""")
        except sqlite3.OperationalError:
            pass
        self.conexion.close()
    
    def ahorrosCripto(self):
        """Creacion de la tabla donde se registran la cantidad de cripto
        monedas"""
        self.conexion = sqlite3.connect("controlGasto.db")
        try:
            self.conexion.execute("""
                                    CREATE TABLE ahorrosCripto (
                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            año INTEGER,
                                            mes TEXT,
                                            btc numeric,
                                            eth numeric,
                                            ada numeric,
                                            bnb numeric
                                            )""")
        except sqlite3.OperationalError:
            pass
        self.conexion.close()

    def inversionPF(self):
        """Creacion de la tabla donde se registran los plazos fijos: monto invertido, interes,
        ganancia y el total"""
        self.conexion = sqlite3.connect("controlGasto.db")
        try:
            self.conexion.execute("""
                                    CREATE TABLE inversionPF (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        año INTEGER,
                                        mes TEXT,
                                        inversion REAL,
                                        interes NUMERIC,
                                        ganancia REAL,
                                        total REAL)""")
        except sqlite3.OperationalError:
            pass
        self.conexion.close()
#---------------------------------------------------------------- Tabla Cuotas
    def cuotas(self):
        """Creacion de la tabla donde se registran los bienes o productos en cuotas"""
        self.conexion = sqlite3.connect("controlGasto.db")
        try:
            self.conexion.execute("""
                                    CREATE TABLE cuotas (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        año INTEGER,
                                        mes TEXT,
                                        total REAL,
                                        filtro REAL,
                                        curso1 REAL,
                                        silla REAL,
                                        adaptador REAL,
                                        curso2 REAL,
                                        teclado REAL
                                        )""")
        except sqlite3.OperationalError:
            pass
        self.conexion.close()

    def columnAdd(self, item):
        """Esta funcion añade una columna con el nuevo item de cuotas"""
        self.conexion = sqlite3.connect("controlGasto.db")
        self.sentenciaCA = f"ALTER TABLE cuotas ADD COLUMN {item} REAL"
        self.cursor = self.conexion.execute(self.sentenciaCA)
        self.conexion.commit()
        self.conexion.close()

    def inCuotas(self, item, dataCuota):
        """Esta función permite ingresar las cuotas en los distintos meses de acuerdo a las cuotas seleccionadas"""
        self.conexion = sqlite3.connect("controlGasto.db")
        self.sentencia = f"INSERT INTO cuotas (año, mes, {item}) VALUES (?,?,?)"
        self.cursor= self.conexion.execute(self.sentencia, dataCuota)
        self.conexion.commit()
        self.conexion.close()

   
#---------------------------------------------------------------- PRUEBAS
# prueba1 = Database()
# prueba1.inversionBolsa()
# prueba1.movimientosIn("luz", (2022, "enero", 686))
# prueba1.movimientosIn("agua", (2022, "enero", 567))
# prueba1.movimientosIn("agua", (2022,"marzo",1666))

# hola= prueba1.consultarExiste("luz", (2022,"marzo"))
# print(type(hola))
# prueba1.insertarExistente("gas", 345, (2022, "marzo"))
# print(type(prueba1.consultarExiste("gas", (2022, "enero"))))

# lista = prueba1.allColumns((2022, "agosto"))

# print(lista) #Me devuelve una lista con una tupla
#[(30000.0, 10000.0, 800.0, 540.0, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None)]