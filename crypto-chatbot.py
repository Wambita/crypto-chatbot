# crypto_chatbot.py

print("Hey there, I’m CryptoBuddy — your friendly crypto sidekick! Let’s find the perfect coin for you.")
print("⚠️ Disclaimer: Crypto is risky — always do your own research before investing!")
print("Type 'exit' to end chat.\n")

# Predefined Crypto Data
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3/10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6/10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8/10
    }
}

# Chatbot Logic
def crypto_advice(user_query):
    user_query = user_query.lower()
    
    if "sustainable" in user_query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        return f" Go for {recommend}! It has a great sustainability score and low energy use."
    
    elif "trending" in user_query or "rising" in user_query:
        rising_coins = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
        return f" These coins are rising: {', '.join(rising_coins)}"
    
    elif "long-term" in user_query or "growth" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                return f" {coin} is great for long-term growth. It's rising and eco-friendly!"
        return " Hmm, not sure about long-term options right now. Try again later!"
    
    elif "advice" in user_query or "recommend" in user_query or "which crypto" in user_query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] == "high":
                return f" Try {coin}. It’s on the rise and has a strong market cap."
    
    else:
        return " I’m not sure what you mean. Try asking about trends, sustainability, or long-term growth."

# Chat Loop
while True:
    user_query = input("You: ")
    if user_query.lower() == "exit":
        print("CryptoBuddy: Bye!  Remember to DYOR (Do Your Own Research)!")
        break
    response = crypto_advice(user_query)
    print(f"CryptoBuddy: {response}")
