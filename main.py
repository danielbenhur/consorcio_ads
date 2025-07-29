import argparse
from config import config
from keyword_generator import generate_variations, filter_keywords
from ad_creator import create_ads_from_keywords

def main():
    """Interpreta comandos CLI e executa etapas do pipeline."""
    parser = argparse.ArgumentParser(description="Consórcio Ads Automator")
    parser.add_argument("command", choices=["generate_keywords","filter_keywords","create_campaign"])
    args = parser.parse_args()

    if args.command == "generate_keywords":
        seeds = config['seeds']
        terms = generate_variations(seeds)
        print("\n".join(terms))
    elif args.command == "filter_keywords":
        params = config['filter']
        filter_keywords(
            params['input_csv'],
            params['output_csv'],
            params['max_cpc'],
            params['min_volume']
        )
    elif args.command == "create_campaign":
        create_ads_from_keywords(config, config['filter']['output_csv'])

if __name__ == "__main__":
    main()

