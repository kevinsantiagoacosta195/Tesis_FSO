import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# --- FUNCIÓN DE PROCESAMIENTO REUTILIZABLE ---
def procesar_fso(file_path, nombre_archivo):
    try:
        # Carga con manejo de errores
        df = pd.read_csv(file_path, sep=',', quotechar='"')
        df.columns = ['Time', 'Drain', 'Pin9']
        df['Time_us'] = (df['Time'] - df['Time'].iloc[0]) * 1e6
    except Exception as e:
        print(f"\n[!] Error al cargar {nombre_archivo}: {e}")
        return

    # --- LÓGICA DE CÁLCULO ---
    t = df['Time_us'].values
    v_in = df['Pin9'].values
    v_out = df['Drain'].values

    u_in = (v_in.max() + v_in.min()) / 2
    u_out = (v_out.max() + v_out.min()) / 2
    
    ctrl_high = (v_in > u_in).astype(int)
    pwr_on = (v_out < u_out).astype(int) 
    
    sub_in = np.where(np.diff(ctrl_high) == 1)[0]
    baj_in = np.where(np.diff(ctrl_high) == -1)[0]
    sub_out = np.where(np.diff(pwr_on) == 1)[0]
    baj_out = np.where(np.diff(pwr_on) == -1)[0]

    # Sincronización de flancos
    if len(sub_in) == 0 or len(sub_out) == 0:
        print(f"[!] No se detectaron pulsos en {nombre_archivo}")
        return

    if sub_in[0] > baj_in[0]: baj_in = baj_in[1:]
    m_in = min(len(sub_in), len(baj_in))
    sub_in, baj_in = sub_in[:m_in], baj_in[:m_in]

    if sub_out[0] > baj_out[0]: baj_out = baj_out[1:]
    m_out = min(len(sub_out), len(baj_out))
    sub_out, baj_out = sub_out[:m_out], baj_out[:m_out]

    # Cálculo de métricas
    periodos = np.diff(t[sub_in])
    t_per_prom = np.mean(periodos)
    f_khz = 1 / (t_per_prom / 1e3) if t_per_prom > 0 else 0
    
    t_on_ard = np.mean(t[baj_in] - t[sub_in])
    t_on_lar = np.mean(t[baj_out] - t[sub_out])
    
    dc_ard = (t_on_ard / t_per_prom) * 100
    dc_lar = (t_on_lar / t_per_prom) * 100

    # Rise Time con Interpolación
    idx_f = sub_out[0]
    t_centro = t[idx_f]
    mask = (t > t_centro - 2) & (t < t_centro + 2)
    t_v, v_v = t[mask], v_out[mask]
    
    v_max, v_min = v_out.max(), v_out.min()
    v_90 = v_min + (v_max - v_min) * 0.90
    v_10 = v_min + (v_max - v_min) * 0.10

    # Interpolación para precisión sub-muestreo
    t_c90 = np.interp(v_90, v_v[::-1], t_v[::-1])
    t_c10 = np.interp(v_10, v_v[::-1], t_v[::-1])
    tr = abs(t_c10 - t_c90)
    bw_kbps = (0.35 / tr) * 1000 if tr > 0 else 0

    # --- GENERACIÓN DE GRÁFICA ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 9), gridspec_kw={'height_ratios': [1, 1]})

    ax1.plot(df['Time_us'], df['Pin9'], color='red', alpha=0.6, label='Control Arduino')
    ax1.plot(df['Time_us'], df['Drain'], color='green', label='Salida Drain')
    ax1.set_xlim(0, 1000)
    ax1.set_title(f"ANÁLISIS FSO: {nombre_archivo}", fontsize=14, fontweight='bold')
    ax1.set_ylabel("Voltaje (V)")
    ax1.legend(loc='upper right')
    ax1.grid(True, linestyle=':', alpha=0.6)

    ax2.plot(t_v, v_v, 'g-o', markersize=4, label='Señal Drain (Muestras)')
    ax2.axhline(v_90, color='blue', linestyle='--', alpha=0.5, label='90%')
    ax2.axhline(v_10, color='red', linestyle='--', alpha=0.5, label='10%')
    ax2.set_title(f"Detalle Rise Time Interpolado: {tr:.4f} $\mu s$", fontsize=12)
    ax2.set_xlabel("Tiempo [$\mu s$]")
    ax2.set_ylabel("Voltaje [V]")
    ax2.legend()
    ax2.grid(True, which='both', alpha=0.3)

    reporte = (
        f"ARCHIVO: {nombre_archivo}\n"
        f"Frecuencia: {f_khz:.3f} kHz\n"
        f"Duty In:    {dc_ard:.2f} %\n"
        f"Duty Out:   {dc_lar:.2f} %\n"
        f"Error DC:   {abs(dc_ard - dc_lar):.4f} %\n"
        "---------------------------\n"
        f"Rise Time:  {tr:.4f} us\n"
        f"BW Est.:    {bw_kbps:.2f} Kbps"
    )

    fig.text(0.77, 0.5, reporte, fontsize=10, family='monospace', verticalalignment='center',
             bbox=dict(facecolor='white', alpha=0.8, edgecolor='black'))

    plt.subplots_adjust(right=0.75, hspace=0.35)
    
    print(f"[*] Mostrando {nombre_archivo}. Cierra la ventana para continuar...")
    plt.show()
    plt.close(fig) # Liberar memoria tras cerrar la ventana

# --- FLUJO PRINCIPAL ---
if __name__ == "__main__":
    base_path = r"C:\Users\kevin\Documents\DOCUMENTOS VIDA\Proyecto de vida\Universidad\Tesis FSO\Tesis_FSO\Simulaciones\Pwm_Laser\resultados\Datos"
    archivos = ["DATOS_25%.DAT", "DATOS_50%.DAT", "DATOS_75%.DAT"]

    try:
        for nombre in archivos:
            full_path = os.path.join(base_path, nombre)
            if os.path.exists(full_path):
                procesar_fso(full_path, nombre)
            else:
                print(f"[!] Archivo no encontrado: {nombre}")
        print("\n[+] Procesamiento de todos los archivos finalizado.")
    except KeyboardInterrupt:
        print("\n[!] Proceso detenido por el usuario.")