import streamlit as str

# Configuración de la pestaña del navegador
str.set_page_config(page_title="Mi App de Finanzas", page_icon="💰", layout="centered")

# --- PORTADA DE LA APLICACIÓN (Nueva sección visual) ---
str.markdown(
    """
    <div style="background-color:#2C3E50; padding:20px; border-radius:15px; text-align:center; margin-bottom:25px;">
        <h1 style="color:white; margin:0; font-size:28px;">💰 CONTROLADOR FINANCIERO PRO</h1>
        <p style="color:#BDC3C7; margin:10px 0 0 0; font-size:14px;">La forma más fácil y ordenada de proteger tus ingresos y calcular tus gastos mensuales.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

str.write("Bienvenido(a). Sigue los pasos hacia abajo para organizar las cuentas de este mes de forma automática.")
str.divider()

# --- SECCIÓN 1: CONFIGURACIÓN DE INGRESOS Y AHORRO ---
str.header("💵 1. Ingresos y Ahorro")

col1, col2 = str.columns(2)

with col1:
    # Corrección para que sea visualmente claro con separador de miles en el sistema
    ingresos = str.number_input(
        "Ingresa tus Ingresos Mensuales ($ COP):", 
        min_value=0, 
        value=2000000, 
        step=50000,
        format="%d"
    )

with col2:
    porcentaje_ahorro = str.slider(
        "Porcentaje de ahorro sugerido (%):", 
        min_value=0, 
        max_value=100, 
        value=10
    )

# Procedimientos matemáticos iniciales
monto_ahorro = ingresos * (porcentaje_ahorro / 100)
ingreso_disponible = ingresos - monto_ahorro

# Tarjetas informativas con los puntos de miles formateados para Colombia
str.info(f"**Ahorro Protegido:** ${monto_ahorro:,.0f} COP (Guardado automáticamente)")
str.success(f"**Presupuesto Neto para Gastos:** ${ingreso_disponible:,.0f} COP")
str.divider()

# --- SECCIÓN 2: REGISTRO DE GASTOS MENSUALES ---
str.header("📉 2. Registro de Gastos")
str.caption("Introduce el valor de cada gasto (utiliza los botones + / - o escribe el número directo):")

col_g1, col_g2 = str.columns(2)

with col_g1:
    g_arriendo = str.number_input("Valor de Arriendo ($):", min_value=0, value=600000, step=10000, format="%d")
    g_agua = str.number_input("Valor de Agua ($):", min_value=0, value=40000, step=5000, format="%d")
    g_luz = str.number_input("Valor de Luz ($):", min_value=0, value=70000, step=5000, format="%d")
    g_gas = str.number_input("Valor de Gas ($):", min_value=0, value=15000, step=2000, format="%d")

with col_g2:
    g_internet = str.number_input("Valor de Internet ($):", min_value=0, value=80000, step=5000, format="%d")
    g_mercado = str.number_input("Valor de Mercado ($):", min_value=0, value=400000, step=10000, format="%d")
    g_transporte = str.number_input("Valor de Transporte ($):", min_value=0, value=150000, step=5000, format="%d")

str.divider()

# --- SECCIÓN 3: PROCEDIMIENTOS FINALES Y DASHBOARD ---
str.header("📊 3. Dashboard de Resultados")

total_gastos = g_arriendo + g_agua + g_luz + g_gas + g_internet + g_mercado + g_transporte
saldo_final = ingreso_disponible - total_gastos

def calcular_pct(gasto):
    return (gasto / ingresos) * 100 if ingresos > 0 else 0

# Mostrar tarjetas visuales con los totales finales formateados con puntos
c_ing, c_gas, c_sal = str.columns(3)
c_ing.metric(label="Ingresos Totales", value=f"${ingresos:,.0f} COP")
c_gas.metric(label="Total Gastos del Mes", value=f"${total_gastos:,.0f} COP")

if saldo_final < 0:
    c_sal.metric(label="Saldo Libre Final", value=f"${saldo_final:,.0f} COP", delta="DÉFICIT", delta_color="inverse")
    str.error(f"⚠️ **¡Alerta de Deuda!** Has superado tu presupuesto disponible por ${abs(saldo_final):,.0f} COP.")
else:
    c_sal.metric(label="Saldo Libre Final", value=f"${saldo_final:,.0f} COP", delta="ESTABLE")
    str.balloons() # ¡Efecto visual de celebración si las cuentas van bien!
    str.success("✅ **¡Éxito!** Tus finanzas están bajo control. Cuentas pagas y ahorros asegurados.")

# Mostrar el desglose de impacto en la web
with str.expander("🔍 Ver impacto detallado de cada gasto en tus ingresos"):
    str.write(f"• **Arriendo:** ${g_arriendo:,.0f} COP ({calcular_pct(g_arriendo):.1f}%)")
    str.write(f"• **Mercado:** ${g_mercado:,.0f} COP ({calcular_pct(g_mercado):.1f}%)")
    str.write(f"• **Transporte:** ${g_transporte:,.0f} COP ({calcular_pct(g_transporte):.1f}%)")
    servicios_totales = g_agua + g_luz + g_gas + g_internet
    str.write(f"• **Servicios Públicos (Agua/Luz/Gas/Net):** ${servicios_totales:,.0f} COP ({calcular_pct(servicios_totales):.1f}%)")
