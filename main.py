import streamlit as st
import math
import plotly.graph_objects as go

st.set_page_config(
    page_title="Calculadora Somatocarta",
    page_icon="📊",  # Puedes usar un emoji o ícono personalizado
    layout="wide"  # Configura el diseño para ocupar toda la anchura
)

def calcular_ectomorfia(HWR):
  if HWR >= 40.75: return 0.732*HWR - 28.58
  if HWR < 40.75 and HWR > 38.25: return 0.463*HWR - 17.63
  if HWR <= 38.25: return 0.1

pi = math.pi

endomorfia = ""
mesomorfia = ""
ectomorfia = ""
x = ""
y = ""

etnias = {"Asiatic@":-2., "Afro-American@":1.1, "Caucasic@ o Hispán@":0.}

# Título de la aplicación
st.title("Calculadora Somatocarta")

col1, col2 = st.columns(2)
# Entrada de medidas
with col1:

    with st.container():
        col01, col02, col03 = st.columns(3)
        with col01:
            altura_cm = st.number_input("Altura (cm):", value=0.0, step=0.1, format="%.2f")
            altura_m = altura_cm / 100. if altura_cm else ""
            peso = st.number_input("Peso (kg):", value=0.0, step=0.1, format="%.2f")
            etnia = st.selectbox("Etnia:", ["Asiatic@", "Afro-American@", "Caucasic@ o Hispán@"])
            etnia = etnias[etnia]
        with col02:
            sexo = st.selectbox("Sexo:", ["Mujer", "Hombre"])
            sexo = 0. if sexo == "Mujer" else 1.
            edad = st.number_input("Edad:", value=0, step=1)
        with col03:
            pass
        
    with st.container():
        st.markdown("Medidas de los pliegues (mm)")
        col11, col12, col13 = st.columns(3)
        with col11:
            pli_tricipital = st.number_input("Pliegue Tricipital:", value=0.0, step=0.1, format="%.2f")
            pli_subescapular = st.number_input("Pliegue Subescapular:", value=0.0, step=0.1, format="%.2f")
            pli_biceps = st.number_input("Pliegue Biceps:", value=0.0, step=0.1, format="%.2f")
        with col12:  
            pli_ileocrestal = st.number_input("Pliegue Ileocrestal:", value=0.0, step=0.1, format="%.2f")
            pli_supraespinal = st.number_input("Pliegue Supraespinal:", value=0.0, step=0.1, format="%.2f")
            pli_abddominal = st.number_input("Pliegue Abdominal:", value=0.0, step=0.1, format="%.2f")
        with col13:   
            pli_muslo = st.number_input("Pliegue Muslo:", value=0.0, step=0.1, format="%.2f")
            pli_gemelar = st.number_input("Pliegue Gemelar:", value=0.0, step=0.1, format="%.2f")
    
    with st.container():
        st.markdown("Medidas de los perimetros (cm)")
        col21, col22, col23 = st.columns(3)
        with col21:
            per_brazo_relaj = st.number_input("Perimetro Brazo relajado:", value=0.0, step=0.1, format="%.2f")
            per_brazo_contr = st.number_input("Perimetro Brazo contraído:", value=0.0, step=0.1, format="%.2f")
            per_cintura = st.number_input("Perimetro Cintura:", value=0.0, step=0.1, format="%.2f")
        with col22:   
            per_cadera = st.number_input("Perimetro Cadera:", value=0.0, step=0.1, format="%.2f")
            per_gemelo = st.number_input("Perimetro Gemelo:", value=0.0, step=0.1, format="%.2f")
            per_muslo = st.number_input("Perimetro Muslo:", value=0.0, step=0.1, format="%.2f")
        with col23:
            pass
        
    with st.container():
        st.markdown("Medidas de los diametros (cm)")
        col31, col32, col33 = st.columns(3)
        with col31:
            DH = st.number_input("Diametro óseo biepicondileo del húmero:", value=0.0, step=0.1, format="%.2f")
            DF = st.number_input("Diametro óseo biepicondileo del fémur:", value=0.0, step=0.1, format="%.2f")
            DM = st.number_input("Diametro muñeca:", value=0.0, step=0.1, format="%.2f")
        with col32:
            pass
        with col33:
            pass

  # Botón para calcular
if st.button("Calcular"):
    #comprobar_datos()
  
    PBC = per_brazo_relaj - pi*pli_tricipital/10
    PMC = per_muslo - pi*pli_muslo/10
    PGC = per_gemelo - pi*pli_gemelar/10

    MME = altura_m * (0.00744*(PBC**2) + 0.00088*(PMC**2) + 0.00441*(PGC**2)) + 2.4*sexo - 0.048*edad + etnia + 7.8

    masa_osea_kg = 3.02*((altura_m**2) * DM/100 * DF/100 * 400)
    
    X = (pli_tricipital + pli_subescapular + pli_supraespinal) * 170 / (altura_cm)
    endomorfia = -0.7182 + 0.1451*X - 0.00067*(X**2) + 0.0000014*(X**3)
    
    CAH = per_brazo_contr - pli_tricipital/10
    CCG = per_gemelo - (pli_gemelar/10.)
    mesomorfia = (0.858*DH + 0.601*DF + 0.188*CAH + 0.161*CCG) - (0.131*altura_cm) + 4.5
  
    HWR = (altura_cm)/peso**(1/3)

    ectomorfia = calcular_ectomorfia(HWR)
  
    x = ectomorfia - endomorfia
    y = 2*mesomorfia - (endomorfia + ectomorfia)

with col2:
    if endomorfia == "" or mesomorfia == "" or ectomorfia == "" or x == "" or y == "":
        st.write("Endomorfia: NONE")
        st.write("Mesomorfia: NONE")
        st.write("Ectomorfia: NONE")
        st.write("Coordenadas Somatocarta: X = NONE, Y = NONE")
        
    else:
        st.write(f"Endomorfia: {endomorfia:.2f}")
        st.write(f"Mesomorfia: {mesomorfia:.2f}")
        st.write(f"Ectomorfia: {ectomorfia:.2f}")
        st.write(f"Coordenadas Somatocarta: X = {x:.2f}, Y = {y:.2f}")
    

    # Crear figura
    fig = go.Figure()
    
    # Configurar el layout para los ejes
    fig.update_layout(
        xaxis=dict(
            range=[-8, 8],       # Rango de -8 a 8
            tickmode='linear',   # Marcas de ticks en modo lineal
            tick0=-8,            # Primer tick en -8
            dtick=1,             # Intervalos de 1 en 1
            mirror=True,         # Eje se refleja arriba y abajo
            showline=True,       # Mostrar línea del eje
            linecolor='white',   # Color de la línea del eje
            linewidth=1          # Grosor de la línea
        ),
        yaxis=dict(
            range=[-8, 16],      # Rango de -8 a 16
            tickmode='linear',   # Marcas de ticks en modo lineal
            tick0=-8,            # Primer tick en -8
            dtick=1,             # Intervalos de 1 en 1
            mirror=True,         # Eje se refleja a la izquierda y derecha
            showline=True,       # Mostrar línea del eje
            linecolor='white',   # Color de la línea del eje
            linewidth=1          # Grosor de la línea
        ),
        plot_bgcolor='rgba(0,0,0,0)',    # Fondo transparente para el gráfico
    )
    
    if not (x == "" or y == ""):
        fig.add_trace(go.Scatter(
        x=[x, x], 
        y=[-8, 16],  # Desde el rango mínimo hasta el máximo en y
        mode='lines',
        line=dict(color='blue', dash='dash'),
        name=f'Línea vertical (x={x})'
        ))
        
        # Agregar línea horizontal en y = y_value
        fig.add_trace(go.Scatter(
            x=[-8, 8],  # Desde el rango mínimo hasta el máximo en x
            y=[y, y],
            mode='lines',
            line=dict(color='red', dash='dash'),
            name=f'Línea horizontal (y={y})'
        ))
        
        # Agregar punto en (x_value, y_value)
        fig.add_trace(go.Scatter(
            x=[x],
            y=[y],
            mode='markers',
            marker=dict(color='green', size=10),
            name=f'Punto ({x}, {y})'
        ))
        
    fig.add_trace(go.Scatter(
    x=[-1, -1], 
    y=[-8, 16],  # Desde el rango mínimo hasta el máximo en y
    mode='lines',
    line=dict(color='white', dash='dash'),
    name=f'Línea vertical (x={x})'
    ))
    
    fig.add_trace(go.Scatter(
    x=[1, 1], 
    y=[-8, 16],  # Desde el rango mínimo hasta el máximo en y
    mode='lines',
    line=dict(color='white', dash='dash'),
    name=f'Línea vertical (x={x})'
    ))
    
    x_values = [x for x in range(-8, 9)]
    y_values = [x + 1 for x in x_values]  # Para una línea a 45º, y = x + 1
    fig.add_trace(go.Scatter(
        x=x_values, 
        y=y_values, 
        mode='lines',
        line=dict(color='blue', width=2, dash='dash'),
        name="Línea a 45º desplazada +1"
    ))
    
    x_values = [x for x in range(-8, 9)]
    y_values = [x - 1 for x in x_values]
    fig.add_trace(go.Scatter(
        x=x_values, 
        y=y_values, 
        mode='lines',
        line=dict(color='blue', width=2, dash='dash'),
        name="Línea a 45º desplazada -1"
    ))
    
    # x_values = [x for x in range(8, -9, -1)]
    # y_values = [x + 1 for x in x_values]
    # fig.add_trace(go.Scatter(
    #     x=x_values, 
    #     y=y_values, 
    #     mode='lines',
    #     line=dict(color='blue', width=2, dash='dash'),
    #     name="Línea a 45º desplazada"
    # ))
    
    # x_values = [x for x in range(8, -9, -1)]
    # y_values = [x - 1 for x in x_values]  
    # fig.add_trace(go.Scatter(
    #     x=x_values, 
    #     y=y_values, 
    #     mode='lines',
    #     line=dict(color='blue', width=2, dash='dash'),
    #     name="Línea a 45º desplazada"
    # ))

    st.plotly_chart(fig)