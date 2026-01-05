import numpy as np

def simulador_electronica_swipt():
    print("\n--- SIMULADOR DE ELECTRÓNICA DE POTENCIA Y SEÑAL (SWIPT) ---")
    print("Objetivo: Dimensionar Bias-T y Amplificador para señal de 3uA")
    
    # --- 1. DATOS DE ENTRADA (De tu simulación anterior) ---
    try:
        i_signal_ua = float(input("Ingrese la Corriente de Señal I_ph (uA) [ej. 3.0]: "))
        f_pwm = float(input("Ingrese la Frecuencia PWM (Hz) [ej. 5000]: "))
        v_panel_dc = 12.0 # Voltaje DC promedio del panel (Energía)
    except ValueError:
        print("Error: Ingrese números válidos.")
        return

    i_signal = i_signal_ua * 1e-6
    
    print("\n" + "="*60)
    print(f"ANÁLISIS DE IMPEDANCIAS PARA {f_pwm} Hz")
    print("="*60)

    # --- 2. DISEÑO DEL BIAS-T (Separador) ---
    # Criterio: La rama de datos debe tener BAJA impedancia a 5kHz
    #           La rama de energía debe tener ALTA impedancia a 5kHz
    
    # Valores comerciales propuestos para iterar
    l_bobina = 100e-3  # 100 mH (Milihenrios)
    c_acoplo = 100e-9  # 100 nF (Nanofaradios)
    
    # Reactancias: X_L = 2*pi*f*L  |  X_C = 1 / (2*pi*f*C)
    w = 2 * np.pi * f_pwm
    z_bobina = w * l_bobina
    z_capacitor = 1 / (w * c_acoplo)
    
    print(f"--- 1. Circuito Bias-T (Separación de Señal) ---")
    print(f"Componentes: Bobina {l_bobina*1000:.0f}mH | Capacitor {c_acoplo*1e9:.0f}nF")
    print(f"-> Impedancia Inductiva (Bloqueo AC): {z_bobina:.2f} Ohms")
    print(f"-> Impedancia Capacitiva (Paso AC):   {z_capacitor:.2f} Ohms")
    
    # Validación de Diseño
    if z_bobina > 1000 and z_capacitor < 500:
        print("✅ ESTADO: EXCELENTE. La bobina bloquea bien y el capacitor deja pasar la señal.")
    else:
        print("⚠️ ESTADO: REVISAR. Se recomienda aumentar L o C.")

    # --- 3. AMPLIFICADOR DE TRANSIMPEDANCIA (TIA) ---
    print(f"\n--- 2. Amplificador TIA (Conversión Corriente -> Voltaje) ---")
    
    # Buscamos un voltaje de salida legible para el Arduino (ej. > 1.0V)
    # V_out = I_in * R_feedback
    
    # Probamos con un valor comercial estándar: 470k Ohms
    r_feedback = 470000 
    v_out_teorico = i_signal * r_feedback
    
    print(f"Resistencia de Feedback (Rf): {r_feedback/1000} kOhms")
    print(f"Entrada: {i_signal_ua} uA  --->  Salida Estimada: {v_out_teorico:.4f} Volts")
    
    # --- 4. COMPARADOR (Digitalización) ---
    print(f"\n--- 3. Etapa de Comparación (ADC / Digital) ---")
    v_umbral = 0.5 # 0.5 Volts
    
    if v_out_teorico > v_umbral:
        margen = v_out_teorico - v_umbral
        print(f"Umbral del comparador: {v_umbral} V")
        print(f"✅ DETECCIÓN EXITOSA: La señal ({v_out_teorico:.2f}V) supera el umbral.")
        print(f"   Margen de seguridad: {margen*1000:.1f} mV")
    else:
        print(f"❌ FALLO: La señal amplificada ({v_out_teorico:.2f}V) es muy débil para el umbral.")
        print("   -> SUGERENCIA: Aumentar Rf a 1 MOhm.")

    print("\n" + "="*60)
    print("VALORES FINALES PARA PROTEUS:")
    print("="*60)
    print(f"1. Inductor (Serie Batería):  {l_bobina*1000:.0f} mH")
    print(f"2. Capacitor (Serie OpAmp):   {c_acoplo*1e9:.0f} nF")
    print(f"3. Resistencia TIA (Rf):      {r_feedback/1000:.0f} kOhms")
    print(f"4. Voltaje de Referencia (-): {v_umbral} V")
    print("="*60)

# Ejecutar simulador
simulador_electronica_swipt()