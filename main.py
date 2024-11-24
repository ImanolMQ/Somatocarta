import streamlit as st
import math

def calcular_ectomorfia(ectomorfia, HWR):
  if HWR >= 40.75: return 0.732*HWR - 28.58
  if HWR < 40.75 and HWR > 38.25: return 0.463*HWR-17.63
  if HWR <= 38.25: return ectomorfia = 0.1
  
  return "error"

pi = math.pi

endomorfia = ""
mesomorfia = ""
ectomorfia = ""

# Título de la aplicación
st.title("Calculadora Somatocarta")

col1, col2 = st.columns(2)
# Entrada de medidas
with col1:
  altura_cm = st.number_input("Altura (cm):", value=0.0, step=0.1, format="%.2f")
  altura_m = altura_cm / 100. if altura_cm else ""
  peso = st.number_input("Peso (kg):", value=0.0, step=0.1, format="%.2f")
  
  st.markdown("Medidas de los pliegues (mm)")
  pli_tricipital = st.number_input("Tricipital:", value=0.0, step=0.1, format="%.2f")
  pli_subescapular = st.number_input("Subescapular:", value=0.0, step=0.1, format="%.2f")
  pli_biceps = st.number_input("Biceps:", value=0.0, step=0.1, format="%.2f")
  pli_ileocrestal = st.number_input("Ileocrestal:", value=0.0, step=0.1, format="%.2f")
  pli_suprespinal = st.number_input("Suprespinal:", value=0.0, step=0.1, format="%.2f")
  pli_abddominal = st.number_input("Abdominal:", value=0.0, step=0.1, format="%.2f")
  pli_muslo = st.number_input("Muslo:", value=0.0, step=0.1, format="%.2f")
  pli_gemelar = st.number_input("Gemelar:", value=0.0, step=0.1, format="%.2f")
  
  st.markdown("Medidas de los perimetros (cm)")
  per_brazo_relaj = st.number_input("Braco relajado:", value=0.0, step=0.1, format="%.2f")
  per_brazo_contr = st.number_input("Brazo contraído:", value=0.0, step=0.1, format="%.2f")
  per_cintura = st.number_input("Cintura:", value=0.0, step=0.1, format="%.2f")
  per_cadera = st.number_input("Cadera:", value=0.0, step=0.1, format="%.2f")
  per_gemelo = st.number_input("Gemelo:", value=0.0, step=0.1, format="%.2f")
  per_muslo = st.number_input("Muslo:", value=0.0, step=0.1, format="%.2f")
  
  st.markdown("Medidas de los diametros (cm)")
  DH = st.number_input("Diametro óseo biepicondileo del húmero:", value=0.0, step=0.1, format="%.2f")
  DF = st.number_input("Diametro óseo biepicondileo del fémur:", value=0.0, step=0.1, format="%.2f")
  DM = st.number_input("Diametro muñeca:", value=0.0, step=0.1, format="%.2f")

  st.markdown("Datos adicionales:")
  etnia = st.selectbox("Etnia del paciente:", ["Asiatic@", "Afro-American@", "Caucasic@ o Hispán@"])
  sexo = st.selectbox("Sexo del paciente:", ["Mujer", "Hombre"])

  # Botón para calcular
if st.button("Calcular"):
    #comprobar_datos()
  
    PBC = per_brazo_relajado - pi*pli_triceps/10
    PMC = per_muslo - pi*pli_muslo/10
    PGC = per_gemelo - pi*pli_pierna/10

    MME = altura_m * (0.00744*PBC^2 + 0.00088*PMC^2 + 0.00441*PGC^2) + 2.4*sexo - 0.048*edad + etnia + 7.8

    masa_osea_kg = 3.02*(altura_m^2 * DM * DF * 400)
    
    X = (pli_triceps + pli_subescapular + pli_supraespinal) * 170 / (altura_cm)
    endomorfia <- -0.7182 + 0.1451*X - 0.00067*X^2 + 0.0000014*X^3
    
    CAH = per_brazo_contraido - pli_triceps/10
    CCG = per_gemelo - pli_pierna/10
    mesomorfia <- (0.858*DH + 0.601*DF*100 + 0.188*CAH + 0.161*CCG) - (0.131*altura_cm) + 4.5
  
    HWR = (altura_cm)/peso^(1/3)

    ectomorfia = calcular_ectomorfia(ectomorfia, HWR)
  
    x = ectomorfia - endomorfia
    y = 2*mesomorfia - (endomorfia + ectomorfia)

with col2:
  st.markdown("Endomorfia: ", endomorfia)
  st.markdown("Mesomorfia: ", mesomorfia)
  st.markdown("Ectomorfia: ", ectomorfia)

  st.markdown("X:", x, "   y:", y)