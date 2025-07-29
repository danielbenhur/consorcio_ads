from utils import read_csv, write_csv, log_info
from openai import OpenAI

# Inicializa cliente OpenAI
client = OpenAI()

def generate_variations(seed_terms, n=30):
    """
    Gera variações de palavras‑chave usando IA.
    """
    prompt = f"Gere {n} variações de busca para: {', '.join(seed_terms)}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )
    terms = response.choices[0].message.content.splitlines()
    return [t.strip() for t in terms if t.strip()]

def filter_keywords(input_csv, output_csv, max_cpc, min_volume):
    """
    Filtra palavras‑chave por CPC máximo e volume mínimo.
    """
    df = read_csv(input_csv)
    df_filtered = df[(df['AverageCpc'] <= max_cpc) & (df['SearchVolume'] >= min_volume)]
    write_csv(df_filtered, output_csv)
    log_info(f"{len(df_filtered)} palavras‑chave filtradas salvas em {output_csv}")

