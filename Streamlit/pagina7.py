#Pagina del flujo de fondos
import streamlit as st
import pandas as pd 
import numpy_financial as npf

st.title('Flujo de fondos')

#Carga de datasets
future_data = pd.read_csv('datasets/2. Depurados/TLC Aggregated Data/ML_TS_Output_Anualized.csv')
future_data = future_data[future_data['industry']=='FHV - High Volume']

future_data.rename(columns={
    'anual_income_per_vehicle': 'Income_per_Vehicle (USD)',
    'anual_distance_per_vehicle': 'Miles_per_Vehicle',
    'anual_total_co2_emission': 'Total_CO2_Emissions'
}, inplace=True)
future_data =  future_data[future_data['year']>=2025]

# Dataset de VE
df_autos = pd.read_csv('datasets/2. Depurados/ElectricCarData_Clean.csv')#"df_modelo.csv")
df_autos.rename(columns={
    'brand': 'Brand',
    'model': 'Model',
    'efficiency_whkm': 'Efficiency (Wh/km)'
}, inplace=True)

df_autos['Efficiency (kWh/mile)'] = df_autos['Efficiency (Wh/km)']/1000* 0.1688666667 
df_autos['Precio Dolar'] = df_autos['price_euro'] * 1.06

promedio_ingresos = round(future_data["Income_per_Vehicle (USD)"].mean(),2)
promedio_millas = round(future_data["Miles_per_Vehicle"].mean(),2)
#print(f'El promedio de ingresos anuales es: {promedio_ingresos}')
#print(f'El promedio de millas recorridas anualmente es : {promedio_millas}')

año = 2025
for _, row in future_data.iterrows():  # iterrows() en lugar de interrows()
    globals()[f'Ingresos_año_{año}'] = round(row["Income_per_Vehicle (USD)"],2)
    #print(f'Los ingresos para el año {año} son {globals()[f"Ingresos_año_{año}"]}')
    año += 1

ingresos_años = []
for _, row in future_data.iterrows():
    ingresos_años.append(round(row["Income_per_Vehicle (USD)"],2))
#print(ingresos_años)

año = 2025
for _, row in future_data.iterrows():
    globals()[f'Millas_Año_{año}'] = round(row["Miles_per_Vehicle"],2)
    #print(f'Las Millas recorridas en el año {año} son {globals()[f"Millas_Año_{año}"]}')
    año+=1

millas_años = []
for _, row in future_data.iterrows():
    millas_años.append(round(row["Miles_per_Vehicle"],2))
#print(millas_años)

#Creacion de clase AUTO

class Auto:
    def __init__(self,tasa_descuento, precio, iva, licencia_1, licencia_2, placa, inspeccion, seguro, recorrido_anual, 
                 ingresos_anuales):
        self.precio = precio
        self.iva = iva
        self.licencia_1 = licencia_1
        self.licencia_2 = licencia_2
        self.placa = placa
        self.inspeccion = inspeccion
        self.seguro = seguro
        self.recorrido_anual = recorrido_anual
        self.ingresos_anuales = ingresos_anuales
        self.tasa_descuento = tasa_descuento
    
    def inversion_inicial(self):
        raise NotImplementedError
    
    def costos_operativos(self):
        raise NotImplementedError
    
    def flujo_neto_anual(self):
        return self.ingresos_anuales - self.costos_operativos()
    
    def flujo_caja_proyectado(self, años=7):
        
        # Inversión inicial negativa porqué es el año 0
        inversion_inicial = -self.inversion_inicial()
        
        ingresos_año = [0]
        costos_año = [0]
        flujo_neto = [inversion_inicial]  # Año 0: 
        flujo_descuento = [inversion_inicial]  # Año 0 Inversión inicial negativa
        ingresos_descuento_año = [0]
        
        # Se calcula el flujo neto anual
        for año in range(1, años + 1):
            self.ingresos_anuales = ingresos_años[año-1]
            self.recorrido_anual = millas_años[año-1]
            flujo_neto_actual = self.flujo_neto_anual()
            flujo_neto.append(flujo_neto_actual)
            flujo_descuento_actual = flujo_neto_actual / (1 + self.tasa_descuento) ** año
            flujo_descuento.append(flujo_descuento_actual)
            ingresos_año.append(self.ingresos_anuales)
            ingresos_descuento_año.append(ingresos_años[año-1]  / (1 + self.tasa_descuento) ** año)
            costos_año.append(self.costos_operativos())
        
        # Se crea el DataFrame de resultados
        df_flujo_caja = pd.DataFrame({
            'Año': range(0, años + 1),
            'Ingresos': ingresos_año, 
            'Costos Operativos': costos_año,
            'Flujo Neto': flujo_neto,
            'Flujo Neto Descontado': flujo_descuento,
            'Ingresos Descontado': ingresos_descuento_año        
        })
        
        # Calculo el flujo total descontado para el ROI
        return df_flujo_caja

    def calcular_roi(self, flujo_total):
        roi = flujo_total/ self.inversion_inicial() *100
        roi_mensual_simple = roi/7/12
        #roi_mensual_compuesto = ((1+ flujo_total/ self.inversion_inicial())**(1/(7*12))-1)*100 #- self.inversion_inicial()
        return round(roi, 2),round(roi_mensual_simple, 2)#,round(roi_mensual_compuesto, 2)

    def calcular_ir(self, ingreso_total):
        ir = ingreso_total / abs(self.inversion_inicial())
        return round(ir, 2)

    def calcular_payback_period(self):
        flujo_acumulado = 0
        payback = 0
        for año in range(1, 8):
            flujo_anual = self.flujo_neto_anual()
            flujo_acumulado += flujo_anual
            if flujo_acumulado >= abs(self.inversion_inicial()):
                payback = año
                break
        return payback if payback > 0 else "No recuperado en 7 años"
    
#Creación clase AUTO CONVENCIONAL

class AutoConvencional(Auto): #Licencia_1 = unico pago, licencia_2 = anual
    def __init__(self, tasa_descuento, precio=36200, iva=0.08875, licencia_1=550,licencia_2=100, placa = 300,
                 seguro=5000, inspeccion = 150,
                 eficiencia=25 , mantenimiento=0.15, recorrido_anual=promedio_millas, #eficiencia en MPG / mantenimiento = USD x Milla
                 ingresos_anuales=promedio_ingresos):
        super().__init__(tasa_descuento,precio, iva, licencia_1, licencia_2, placa, inspeccion,
                         seguro, recorrido_anual, ingresos_anuales) # Se usa el super constructor para evitar redundancia ya que es una clase hija
        self.eficiencia = eficiencia
        self.mantenimiento = mantenimiento
    
    def inversion_inicial(self):
        return self.precio * (1 + self.iva) + self.licencia_1
    
    def costos_operativos(self):
        precio_gasolina_galon = 3.06 #USD x galon
        costo_gasolina_anual = (self.recorrido_anual / self.eficiencia) * precio_gasolina_galon
        costo_mantenimiento = self.mantenimiento * self.recorrido_anual
        costo_anual_salario = 2342 * 20  # Precio medio de la hora de un conductor de autos convencionales.
        return costo_gasolina_anual + costo_mantenimiento + self.seguro + self.licencia_2 + self.placa + self.inspeccion + costo_anual_salario

#Creación Clase AUTO ELÉCTRICO

class AutoElectrico(Auto): #Descuento de 5% al 10% en licencia ; Exencion del impuesto de venta
    def __init__(self,tasa_descuento, precio, eficiencia, iva=0, licencia_1=495,licencia_2=100, placa = 300,
                 seguro=1500, inspeccion = 100, mantenimiento=0.03, wallbox=600, 
                 recambio_bateria=5000, #mantenimiento = USD x Milla
                 recorrido_anual=promedio_millas, ingresos_anuales=promedio_ingresos): 
        super().__init__(tasa_descuento, precio, iva, licencia_1, licencia_2, placa, inspeccion, seguro, recorrido_anual, 
                         ingresos_anuales)
        self.eficiencia = eficiencia
        self.mantenimiento = mantenimiento
        self.wallbox = wallbox
        self.recambio_bateria = recambio_bateria
        self.tasa_descuento = tasa_descuento
        self.licencia_1=licencia_1
    
    def inversion_inicial(self):
        return self.precio + self.licencia_1 + self.wallbox
    
    def costos_operativos(self):
        precio_electricidad_kWh = 0.13 #USD x kHw
        costo_electricidad_anual = (self.recorrido_anual * self.eficiencia) * precio_electricidad_kWh
        costo_mantenimiento = self.mantenimiento * self.recorrido_anual
        costo_anual_bateria = self.recambio_bateria / 12.5
        costo_anual_salario = 2342 * 22 # Promedio de horas de menejo de un conductor por año * Precio promedio de la hora de un chofer de taxis en NY para VE.
        return costo_electricidad_anual + costo_mantenimiento + costo_anual_bateria + self.seguro + self.licencia_2 + self.placa + self.inspeccion + costo_anual_salario

def calcular_metricas_flota(tasa_descuento, cantidad_ve, cantidad_conv):
    resultados = []
    flujo_neto_comb_lista = []
    for _, fila in df_autos.iterrows():
        # Se extraen los datos del Dataset
        marca = fila['Brand']
        modelo = fila['Model']
        precio_ve = fila['Precio Dolar']
        eficiencia_ve = fila['Efficiency (kWh/mile)']
        
        # Se instancian los autos segun su naturaleza (electrico o convencional)
        auto_electrico = AutoElectrico(tasa_descuento, precio=precio_ve, eficiencia=eficiencia_ve)
        auto_convencional = AutoConvencional(tasa_descuento)


        # Se calcula el flujo de caja proyectado para cada tipo de auto
        flujo_ve = auto_electrico.flujo_caja_proyectado()
        flujo_conv = auto_convencional.flujo_caja_proyectado()
        #print (flujo_ve)
        flujo_neto_comb_lista =  cantidad_ve * flujo_ve['Flujo Neto Descontado'] +  cantidad_conv  * flujo_conv['Flujo Neto Descontado']
        # Se combinar flujos de caja para la flota (teniendo en cuenta su respectiva cantidad)
        flujo_neto_comb = round(
            cantidad_ve * flujo_ve['Flujo Neto Descontado'].sum() +
            cantidad_conv * flujo_conv['Flujo Neto Descontado'].sum(), 2
        )
        
        ingreso_comb =  round(
            cantidad_ve * flujo_ve['Ingresos Descontado'].sum() +
            cantidad_conv * flujo_conv['Ingresos Descontado'].sum(), 2
        )

        # Se calcula  la inversión inicial combinada
        inversion_comb = round(
            cantidad_ve * auto_electrico.inversion_inicial() +
            cantidad_conv * auto_convencional.inversion_inicial(), 2
        )
        
        # Se calcular las métricas financieras combinadas
        roi_comb = flujo_neto_comb/ inversion_comb *100
        roi_mensual_simple = roi_comb/7/12
        ir_comb = ingreso_comb / abs(inversion_comb)
        tir_comb = round(npf.irr(flujo_neto_comb_lista)*100,2)

        # Calculo del payback period combinado (considerando la proporción)
        flujo_anual_comb = [
            cantidad_ve * flujo_ve['Flujo Neto'].iloc[año] +
            cantidad_conv * flujo_conv['Flujo Neto'].iloc[año]
            for año in range(1, 6)
        ]
        flujo_acumulado = 0
        payback_comb = 0
        for año, flujo in enumerate(flujo_anual_comb, start=1):
            flujo_acumulado += flujo
            if flujo_acumulado >= abs(inversion_comb):
                payback_comb = año
                break
        
        # Se almacenan los resultados para el modelo actual
        resultados.append({
            'Brand': marca,
            'Model': modelo,
            'Efficiency (kWh/mile)' : eficiencia_ve,
            'Inversión Inicial Total (USD)': inversion_comb,
            'VNA (USD)': round(flujo_neto_comb,1),
            'TIR (%)':tir_comb,
            'ROI (%)': roi_comb,
            'ROI Mensualizado(%)': roi_mensual_simple,
            'IR (USD)': ir_comb,
            'Payback Period (Años)': payback_comb if payback_comb > 0 else "No recuperado en 7 años"
        })


    # Se convertierten los resultados a tipo DataFrame para una mejor visualización
    df_resultados = pd.DataFrame(resultados)
    df_resultados = df_resultados.sort_values(by="ROI (%)", ascending=False).reset_index(drop=True) # Se ordena para tener el ranking 


    return df_resultados

tasa_descuento = 0.10 # Primer Parámetro : Cantidad VE; Segundo Parámetro : Cantidad Autos Convencional
# Crear un selector para la cantidad de autos
cantidad_ve = st.slider("Seleccione cantidad de autos eléctricos:",min_value=0, max_value=1500, step=1)
cantidad_conv = st.slider("Seleccione cantidad de autos convencionales:",min_value=0, max_value=1500, step=1)
resultados_flota = calcular_metricas_flota(tasa_descuento, cantidad_ve, cantidad_conv)
# Mostrar el DataFrame resultante
st.write("Tabla de Resultados:")
st.markdown(f"""
En esta tabla se muestran los 5 mejores modelos de vehículos eléctricos en función a su rentabilidad.
A su vez se calculan distintas métricas como Efficiency (kWh/mile), Inversión Inicial Total (USD), VNA(USD), TIR (%), ROI%, ROI% mensualizado, IR(USD) y Payback Period (Años) para la combinación de {cantidad_ve} vehículos eléctricos y {cantidad_conv} vehículos convencionales. 
            """)
# Mostrar el DataFrame resultante

df5 = resultados_flota.head(5)
df5['Inversión Inicial Total (USD)'] = df5['Inversión Inicial Total (USD)'].apply(lambda x: f'{x:,}'.replace(',', '.'))
df5['VNA (USD)'] = df5['VNA (USD)'].apply(lambda x: f'{x:,}'.replace(',', '.'))
df5['VNA (USD)'] = df5['VNA (USD)'].apply(lambda x: f'{x:,}'.replace(',', '.'))
df5['TIR (%)'] = df5['TIR (%)'].apply(lambda x: f'{x:,}'.replace(',', '.'))
df5['ROI (%)'] = df5['ROI (%)'].apply(lambda x: f'{x:,}'.replace(',', '.'))
df5['ROI Mensualizado(%)'] = df5['ROI Mensualizado(%)'].apply(lambda x: f'{x:,}'.replace(',', '.'))
df5['IR (USD)'] = df5['IR (USD)'].apply(lambda x: f'{x:,}'.replace(',', '.'))


st.dataframe(df5)

