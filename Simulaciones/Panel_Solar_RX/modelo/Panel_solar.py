import numpy as np

def simulador_receptor_fso_total():
    print("--- SIMULADOR INTEGRAL DEL RECEPTOR (PANEL SOLAR) ---")
    
    # Parámetros constantes de diseño (Tesis)
    sensibilidad_dbm = -30.0  # Umbral de diseño
    responsividad = 0.4       # A/W para silicio a 650nm
    r_carga = 1000            # Resistencia de carga (1k Ohm)
    bitrate_bps = 258000      # Tasa de bits objetivo
    f_pwm_hz = 5000           # Frecuencia de tu PWM (5 kHz)
    k_boltzmann = 1.38e-23    # Constante física
    temp_k = 300              # Temperatura ambiente (Kelvin)

    # Configuración de Hardware
    area_cm2 = float(input("Ingrese el tamaño del panel solar (cm2): "))
    
    # Modelado de Capacitancia y Velocidad
    c_juntura = area_cm2 * 1e-9  # Estimación: 1nF por cm2
    f_corte = 1 / (2 * np.pi * r_carga * c_juntura)
    t_rise = 0.35 / f_corte      # Tiempo de subida
    
    escenarios_receptor = []
    
    while True:
        print(f"\n[Panel: {area_cm2}cm2 | BW: {f_corte/1000:.2f} kHz | Tr: {t_rise*1e6:.2f} us]")
        print("1. Agregar resultado de simulación de canal (Margen)")
        print("2. Calcular y Comparar Respuesta Integral (Tabla)")
        print("3. Salir")
        op = input("Seleccione: ")
        
        if op == "3": break
        
        if op == "1":
            nombre = input("Nombre del escenario (ej. Despejado 1km): ")
            margen_db = float(input(f"Ingrese el Margen (dB) obtenido: "))
            
            # Cálculo de Potencia y Corriente
            p_rx_dbm = margen_db + sensibilidad_dbm
            p_rx_watts = 10**((p_rx_dbm - 30) / 10)
            i_ph = p_rx_watts * responsividad
            
            # Análisis de Ruido
            v_noise = np.sqrt(4 * k_boltzmann * temp_k * r_carga * f_corte)
            snr = 20 * np.log10(i_ph * r_carga / v_noise) if i_ph > 0 else 0
            
            escenarios_receptor.append({
                'nombre': nombre,
                'p_rx_dbm': p_rx_dbm,
                'i_ph_ua': i_ph * 1e6,
                'snr': snr
            })
            print(f"✅ Escenario '{nombre}' guardado.")

        if op == "2":
            print(f"\n{'ESCENARIO':<15} | {'P_REC(dBm)':<10} | {'I_PH(uA)':<10} | {'SNR(dB)':<8} | {'ESTADO'}")
            print("-" * 80)
            for res in escenarios_receptor:
                # Criterios de éxito
                es_detectable = res['p_rx_dbm'] >= sensibilidad_dbm
                es_rapido = f_corte >= bitrate_bps
                
                if not es_detectable: estado = "POTENCIA BAJA"
                elif not es_rapido: estado = "PANEL LENTO"
                else: estado = "OK"
                
                print(f"{res['nombre']:<15} | {res['p_rx_dbm']:<10.2f} | {res['i_ph_ua']:<10.4f} | {res['snr']:<8.2f} | {estado}")
            
            # Análisis de fidelidad para el PWM de 5kHz
            periodo_pwm_us = (1/f_pwm_hz) * 1e6
            fidelidad = "EXCELENTE" if t_rise < (1/f_pwm_hz)*0.1 else "REGULAR (Redondeado)"
            
            print(f"\n--- ANÁLISIS TÉCNICO PARA BITÁCORA ---")
            print(f"* Frecuencia PWM: {f_pwm_hz/1000} kHz (Periodo: {periodo_pwm_us:.2f} us)")
            print(f"* Tiempo de Subida del Panel (Tr): {t_rise*1e6:.2f} us")
            print(f"* Fidelidad de la señal PWM: {fidelidad}")
            print(f"* Ruido Térmico Estimado: {v_noise*1e6:.2f} uV")
            
            if f_corte < bitrate_bps:
                print(f"⚠️ AVISO: El panel limita los 258kbps, pero soporta el PWM de {f_pwm_hz/1000}kHz.")

simulador_receptor_fso_total()