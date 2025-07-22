import matplotlib.pyplot as plt

def plot_price_trends(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['price'], label='Price in USD')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Crypto Price Over Time')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
