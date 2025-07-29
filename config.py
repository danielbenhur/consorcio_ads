import os
import yaml

# Caminho para o arquivo de configuração
CONFIG_PATH = os.getenv("CONFIG_PATH", "config.yaml")

def load_config():
    """Carrega configurações e credenciais do projeto."""
    with open(CONFIG_PATH, "r") as file:
        return yaml.safe_load(file)

config = load_config()

