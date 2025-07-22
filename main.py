from config import settings
from data.fetcher import fetch_crypto_data
from processing.cleaner import clean_data
from charts.plotter import plot_price_trends
from visualizations.dashboard import launch_dashboard

def main():
    raw_data = fetch_crypto_data(settings.DEFAULT_CRYPTO, settings.DEFAULT_PERIOD)
    cleaned_data = clean_data(raw_data)
    plot_price_trends(cleaned_data)
    launch_dashboard(cleaned_data)

if __name__ == "__main__":
    main()
