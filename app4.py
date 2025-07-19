import streamlit as st
from datetime import datetime
import time

# ========================
# CONFIGURAÇÕES INICIAIS
# ========================

# Data base
DATA_INICIAL = datetime(2025, 1, 18, 21, 5, 0)

# Imagem de fundo (pode trocar por outra URL ou arquivo local com st.image)
IMAGEM_FUNDO = "https://raw.githubusercontent.com/JoaoCotaDevDS/app.py/main/casal.jpg"


# Estilização
def estilizar_app(imagem_fundo_url):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{imagem_fundo_url}");
            background-size: 100% auto;
            background-position: center center;
            background-repeat: no-repeat;
            height: 100vh;
            color: white;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: left;
            padding-top: 100px;
        }}
        .titulo {{
            font-size: 48px;
            font-weight: bold;
            text-shadow: 2px 2px 4px #000000;
        }}
        .datas {{
            font-size: 30px;
            font-weight: 600;
            text-shadow: 1px 1px 3px #000000;
            margin-top: 20px;
            line-height: 1.6;
        }}
        </style>
        """, unsafe_allow_html=True)

# ========================
# FUNÇÃO DE CÁLCULO
# ========================

def calcular_tempos(data_inicial, data_final):
    diferenca = data_final - data_inicial
    total_segundos = int(diferenca.total_seconds())

    # Médias confiáveis
    segundos_por_ano = 365.25 * 86400         # ≈ 31_557_600
    segundos_por_mes = 2592000  # ≈ 2_629_800
    segundos_por_dia = 86400
    segundos_por_hora = 3600
    segundos_por_minuto = 60

    total_anos = total_segundos // segundos_por_ano
    total_meses = total_segundos // segundos_por_mes
    total_dias = total_segundos // segundos_por_dia
    total_horas = total_segundos // segundos_por_hora
    total_minutos = total_segundos // segundos_por_minuto

    return {
        "anos": int(total_anos),
        "meses": int(total_meses),
        "dias": int(total_dias),
        "horas": int(total_horas),
        "minutos": int(total_minutos),
        "segundos": total_segundos
    }

# ========================
# APP PRINCIPAL
# ========================

def main():
    estilizar_app(IMAGEM_FUNDO)

    st.markdown(f'<div class="titulo">Estamos juntos há...</div>', unsafe_allow_html=True)

    agora = datetime.now()
    tempo = calcular_tempos(DATA_INICIAL, agora)

    st.markdown(f'''
        <div class="datas">
            Meses: {tempo["meses"]}<br>
            Dias: {tempo["dias"]}<br>
            Horas: {tempo["horas"]}<br>
            Minutos: {tempo["minutos"]}<br>
            Segundos: {tempo["segundos"]}
        </div>
    ''', unsafe_allow_html=True)

    # Atualiza a cada 5 minutos (300 segundos)
    time.sleep(300)
    st.experimental_rerun()

# ========================
# EXECUÇÃO
# ========================

if __name__ == "__main__":
    main()
