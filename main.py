from data.fetcher import get_current_price, get_historical_data
import matplotlib.pyplot as plt

def main():
    coin = input("Enter Coin ID: ").lower().strip()

    current_price = get_current_price(coin)
    if current_price is not None:
        print(f"\nCurrent {coin.capitalize()} price (USD): {current_price}")
    else:
        print("Failed to fetch current price.")
        return

    historical_df = get_historical_data(coin)
    if historical_df.empty:
        print("Failed to fetch historical data.")
        return

    print("\nLast 5 Days' Prices:")
    print(historical_df.tail())

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(historical_df['date'], historical_df['price'], marker='o', linestyle='-')
    plt.title(f'{coin.capitalize()} Price Over Last 30 Days')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
