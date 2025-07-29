import pandas as pd
import logging

# Configura logging básico
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

def read_csv(path):
    """Lê arquivo CSV em um DataFrame."""
    return pd.read_csv(path)

def write_csv(df, path):
    """Grava DataFrame em arquivo CSV."""
    df.to_csv(path, index=False)

def log_info(message):
    """Registra mensagem informativa no log."""
    logging.info(message)

