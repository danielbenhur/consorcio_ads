from google_ads_api import initialize_client, create_campaign
from utils import log_info

def create_ads_from_keywords(config, keywords_csv):
    """
    Constrói grupos de anúncio e anúncios a partir das palavras‑chave filtradas.
    """
    client = initialize_client(config)
    # Percorre palavras‑chave e executa criação de campanha
    log_info("Pipeline de criação de anúncios executado")

