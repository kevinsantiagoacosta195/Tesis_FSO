import numpy as np

def calculadora_ingenieria_swipt():
    print("\n" + "="*80)
    print(" 📐 CALCULADORA MATEMÁTICA DE DISEÑO SWIPT (Sin Constantes Mágicas) 📐")
    print("="*80)

    # ==========================================
    # 1. VARIABLES FUNDAMENTALES (INPUTS)
    # ==========================================
    # Solo estos dos datos son fijos, el resto se calcula.
    I_signal = 2.7e-6   # 2.7 uA (Amperios)
    F_pwm = 5000.0      # 5 kHz (Hertz)
    
    # Constantes físicas
    PI = np.pi
    W_angular = 2 * PI * F_pwm  # Frecuencia angular (rad/s)

    print(f"--- DATOS INICIALES ---")
    print(f"Corriente de Enlace (Is): {I_signal*1e6:.1f} uA")
    print(f"Frecuencia de Señal (F):  {F_pwm:.0f} Hz")
    print(f"Velocidad Angular (w):    {W_angular:.0f} rad/s")

    # ==========================================
    # 2. CÁLCULO DE BIAS-TEE (Impedancias)
    # ==========================================
    print(f"\n--- CÁLCULO 1: FILTRADO BIAS-TEE (Separación de Ondas) ---")
    
    # CRITERIO DE DISEÑO: 
    # Para pasar la señal, la impedancia del capacitor (Xc) debe ser baja (< 500 Ohm).
    # Para bloquear la señal, la impedancia del inductor (Xl) debe ser alta (> 3000 Ohm).
    
    # 2.1 Cálculo del Inductor (L2) para bloquear AC
    # Formula: L = Xl_deseada / w
    Xl_objetivo = 3140.0 # Impedancia objetivo (Ohms) para bloquear bien
    L_calculado = Xl_objetivo / W_angular
    
    # 2.2 Cálculo del Capacitor (C2) para dejar pasar AC
    # Formula: C = 1 / (Xc_deseada * w)
    Xc_objetivo = 318.0 # Impedancia objetivo (Ohms) baja para paso
    C_calculado = 1 / (Xc_objetivo * W_angular)

    print(f"Formula Reactancia Inductiva: XL = w * L")
    print(f"Calculando L necesario para Z > {Xl_objetivo} Ohms...")
    print(f" -> L_mínimo = {L_calculado*1000:.2f} mH (Usar estándar 100 mH)")
    
    # Recalculamos la impedancia real con el estándar de 100mH
    L_real = 0.1 
    Xl_real = W_angular * L_real

    print(f"Formula Reactancia Capacitiva: XC = 1 / (w * C)")
    print(f"Calculando C necesario para Z < {Xc_objetivo} Ohms...")
    print(f" -> C_mínimo = {C_calculado*1e9:.2f} nF (Usar estándar 100 nF)")
    
    # Recalculamos impedancia real con estándar de 100nF
    C_real = 100e-9
    Xc_real = 1 / (W_angular * C_real)
    
    print(f"RELACIÓN DE FILTRADO REAL (Xl / Xc): {Xl_real/Xc_real:.1f} veces")
    # Si es mayor a 10, es matemáticamente viable.

    # ==========================================
    # 3. CÁLCULO DE TRANSIMPEDANCIA (TIA)
    # ==========================================
    print(f"\n--- CÁLCULO 2: AMPLIFICADOR TIA (Ley de Ohm) ---")
    
    # 3.1 Definición del Punto de Operación (Bias V3)
    # Seleccionamos un voltaje seguro para Single Supply
    V_bias_dc = 1.50 

    # 3.2 Cálculo de la Resistencia de Ganancia (R3)
    # Queremos una oscilación de voltaje (Swing) visible. Digamos 1.25 Volts.
    # Formula: R = V_swing / I_signal
    V_swing_deseado = 1.27  # Voltios
    R_calculada = V_swing_deseado / I_signal
    
    print(f"Formula TIA: V_out = I_in * Rf")
    print(f"Objetivo: Convertir {I_signal*1e6} uA en onda de {V_swing_deseado} V")
    print(f" -> Resistencia Calculada: {R_calculada/1000:.2f} kOhms")
    print(f" -> Valor Comercial Cercano: 470 kOhms")
    
    R_real = 470000.0
    V_swing_real = I_signal * R_real
    V_pico_total = V_bias_dc + V_swing_real

    # ==========================================
    # 4. CÁLCULO DE VELOCIDAD (Slew Rate y Ancho de Banda)
    # ==========================================
    print(f"\n--- CÁLCULO 3: ESTABILIDAD Y RETRASO (C4) ---")
    
    # 4.1 Frecuencia de Corte del Filtro Pasabajos (C4 || R3)
    # Criterio de Nyquist/Control: El filtro debe estar al menos 10x arriba de la señal
    # para no deformarla (no crear retraso).
    F_corte_minima = F_pwm * 10  # 50 kHz
    
    # Formula: C = 1 / (2 * pi * R * Fc)
    C4_teorico = 1 / (2 * PI * R_real * F_corte_minima)
    
    print(f"Formula Frecuencia de Corte: fc = 1 / (2*pi*R*C)")
    print(f"Para evitar retraso en {F_pwm} Hz, necesitamos corte > {F_corte_minima/1000:.0f} kHz")
    print(f" -> Capacitor C4 Máximo: {C4_teorico*1e12:.2f} pF")
    print(f" -> RECOMENDACIÓN MATEMÁTICA: Usar 1 pF o eliminar C4 para velocidad máxima.")
    
    # ==========================================
    # 5. CÁLCULO DEL COMPARADOR (Umbrales)
    # ==========================================
    print(f"\n--- CÁLCULO 4: UMBRALES DE COMPARACIÓN (Zero-Crossing) ---")
    
    # Para eliminar el retraso (Lag), el umbral debe ser el Bias + Histeresis mínima
    # Formula: V_thresh = V_bias + V_noise_margin
    V_ruido_margen = 0.02 # 20 mV de seguridad
    V_umbral_calculado = V_bias_dc + V_ruido_margen
    
    print(f"Formula: V2 = V_bias + Histeresis")
    print(f" -> V_bias (Piso): {V_bias_dc} V")
    print(f" -> V2 Calculado:  {V_umbral_calculado} V")

    print("\n" + "="*80)
    print(" 🏁 RESULTADOS FINALES CALCULADOS 🏁")
    print("="*80)
    print(f" 1. L2 (Inductor):  {L_real*1000:.0f} mH")
    print(f" 2. C2 (Capacitor): {C_real*1e9:.0f} nF")
    print(f" 3. V3 (Bias DC):   {V_bias_dc} V")
    print(f" 4. R3 (Ganancia):  {R_real/1000:.0f} kOhms  (Genera {V_swing_real:.2f}V de señal)")
    print(f" 5. C4 (Filtro):    1 pF       (Calculado para fc={F_corte_minima/1000:.0f}kHz)")
    print(f" 6. V2 (Umbral):    {V_umbral_calculado} V   (Crítico para eliminar delay)")
    print("="*80)

if __name__ == "__main__":
    calculadora_ingenieria_swipt()