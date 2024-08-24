import subprocess
import os
import time  # Importa o módulo time para medir o tempo

# Caminho do diretório do OSGeo4W
osgeo4w_bin_path = r"C:\OSGeo4W\bin"

# Adiciona o diretório do OSGeo4W ao PATH
os.environ["PATH"] += os.pathsep + osgeo4w_bin_path

# Lista de camadas a serem convertidas
layers = [
    "ARAT", "BAR", "BASE", "BAY", "BE", "CONJ", "CRVCRG", "CTAT", "CTMT",
    "EP", "EQCR", "EQME", "EQRE", "EQSE", "EQTRAT", "EQTRM", "EQTRMT",
    "PIP", "PNT", "PONNOT", "PT", "RAMLIG", "SEGCON", "SSDAT", "SSDBT",
    "SSDMT", "SUB", "UNCRAT", "UNCRBT", "UNCRMT", "UNREAT", "UNREMT",
    "UNSEAT", "UNSEBT", "UNSEMT", "UNTRMT", "UNTRAT", "UCAT_tab", "UCBT_tab",
    "UCMT_tab", "UGAT_tab", "UGBT_tab", "UGMT_tab"
]

# Configurações do banco de dados PostgreSQL
db_params = {
    "host": "localhost",
    "user": "iuri",
    "dbname": "bdgd",
    "password": "aa11bb22"
}

# Função para converter camadas
def convert_layer(layer_name):
    ogr2ogr_cmd = (
        f'ogr2ogr -f "PostgreSQL" '
        f'PG:"host={db_params["host"]} user={db_params["user"]} dbname={db_params["dbname"]} password={db_params["password"]}" '
        f'"C:\\Users\\Lucas\\Desktop\\ARQUIVOs_DE_TERCEIROS\\Energisa_MT_405_2022-12-31_V11_20230820-1800.gdb" '
        f'-nln {layer_name} -sql "SELECT * FROM {layer_name}"'
    )

    try:
        print(f"Convertendo layer {layer_name}...")
        result = subprocess.run(ogr2ogr_cmd, shell=True, text=True, capture_output=True)

        if result.returncode != 0:
            print(f"Erro ao converter a camada {layer_name}:")
            print(result.stderr)
        else:
            print(f"Camada {layer_name} convertida com sucesso.")
    except Exception as e:
        print(f"Erro ao executar o comando para a camada {layer_name}: {e}")


# Inicia a contagem do tempo
start_time = time.time()

# Converte todas as camadas
for layer in layers:
    convert_layer(layer)

# Termina a contagem do tempo
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Conversão de todas as camadas concluída em {elapsed_time:.2f} segundos.")
