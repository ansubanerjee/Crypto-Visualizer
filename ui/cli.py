import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Crypto Visualizer")
    parser.add_argument('--crypto', type=str, default='bitcoin', help='Cryptocurrency to track')
    parser.add_argument('--days', type=str, default='30', help='Number of days to fetch data for')
    return parser.parse_args()
