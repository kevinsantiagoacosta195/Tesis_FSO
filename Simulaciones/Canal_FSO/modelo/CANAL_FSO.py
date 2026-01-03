import numpy as np
import matplotlib.pyplot as plt

def simulador_tesis_pro():
    # --- ESPECIFICACIONES FIJAS ---
    P_tx_mw = 5.0
    P_tx_dbm = 10 * np.log10(P_tx_mw) # 5mW -> 6.99 dBm
    sensibilidad_dbm = -30.0          # Potencia mínima requerida
    longitud_onda_nm = 650            # Láser rojo
    div_mrad = 1.5                    # Divergencia del haz
    area_rx_cm2 = 4.0                 # Prototipo Panel Solar
    
    configuraciones = []

    while True:
        print("\n" + "="*40)
        print("   MENÚ DE SIMULACIÓN FSO (UIT-R)")
        print("="*40)
        print("1. Configurar nuevo escenario")
        print("2. Ver resultados y Graficar")
        print("3. Salir")
        op = input("Seleccione: ")

        if op == "3": break
        
        if op == "2":
            if not configuraciones:
                print("⚠️ Primero configure al menos un escenario.")
                continue
            
            dist_m = float(input("Distancia para reporte detallado (metros): "))
            d_range = np.linspace(0.1, dist_m * 1.2, 500)
            
            plt.figure(figsize=(10, 6))
            print(f"\n{'ESCENARIO':<18} | {'A_GEO':<7} | {'A_ATM':<7} | {'A_SCINT':<7} | {'MARGEN':<7}")
            print("-" * 65)
            
            for conf in configuraciones:
                # 1. Atenuación Geométrica (Ageo)
                r_h = d_range * np.tan(div_mrad/1000)
                a_h = np.pi * (r_h*100)**2 # Área en cm2
                a_geo_r = np.where(a_h > area_rx_cm2, 10*np.log10(a_h/area_rx_cm2), 0)
                
                # 2. Centelleo (Ascint)
                k = (2*np.pi)/(longitud_onda_nm * 1e-9)
                sig = 0.31 * conf['cn2'] * (k**(7/6)) * (d_range**(11/6))
                a_sci_r = 10 * np.log10(1 + np.sqrt(sig))
                
                # 3. Margen de Enlace (M)
                a_atm_r = conf['gamma'] * d_range
                m_r = P_tx_dbm - sensibilidad_dbm - a_geo_r - a_atm_r - a_sci_r - conf['asys']
                
                plt.plot(d_range, m_r, label=f"{conf['nombre']} (Cn2={conf['cn2']})")
                
                # Reporte en consola
                idx = (np.abs(d_range - dist_m)).argmin()
                print(f"{conf['nombre']:<18} | {a_geo_r[idx]:.2f} | {a_atm_r[idx]:.2f} | {a_sci_r[idx]:.2f} | {m_r[idx]:.2f} dB")

            plt.axhline(0, color='red', ls='--', label="Umbral Sensibilidad")
            plt.title(f"Comparativa de Margen de Enlace (Láser {longitud_onda_nm}nm)")
            plt.xlabel("Distancia (m)")
            plt.ylabel("Margen de Enlace (dB)")
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.show()
            continue

        if op == "1":
            # --- CONFIGURACIÓN DE ESCENARIO ---
            nombre = input("Nombre del escenario (ej. Niebla densa): ")
            
            # A. Clima (Gamma)
            print("Clima: 1.Despejado | 2.Niebla | 3.Lluvia | 4.Nieve")
            cl = input("Seleccione: ")
            gamma_m = 0
            if cl == "1": 
                gamma_m = 0.43 / 1000
            elif cl == "2":
                v = float(input("Visibilidad (km): "))
                q = 1.6 if v > 50 else (1.3 if v > 6 else 0.585 * (v**(1/3)))
                gamma_m = ((3.91 / v) * ((longitud_onda_nm / 550)**-q)) / 1000
            elif cl == "3":
                R = float(input("Intensidad lluvia (mm/h): "))
                gamma_m = (1.076 * (R**0.67)) / 1000
            elif cl == "4":
                S = float(input("Intensidad nevada (mm/h): "))
                tipo = input("1.Seca | 2.Húmeda: ")
                a, b = (0.065, 1.12) if tipo == "1" else (0.003, 1.38)
                gamma_m = (a * (S**b)) / 1000

            # B. Turbulencia (Cn2)
            print("Turbulencia: 1.Débil (1e-16) | 2.Media (1e-14) | 3.Fuerte (1e-13)")
            t_op = input("Seleccione: ")
            cn2 = 1e-16 if t_op=="1" else (1e-14 if t_op=="2" else 1e-13)

            # C. Pérdidas del sistema (Asys)
            asys = float(input("Pérdidas fijas (dB) [Desalineación + Lentes + Ventanas]: "))

            configuraciones.appeñnd({
                'nombre': nombre, 'gamma': gamma_m, 
                'cn2': cn2, 'asys': asys
            })
            print(f"✅ Escenario '{nombre}' guardado.")

simulador_tesis_pro()