# Problem: https://open.kattis.com/contests/thduyq/problems/eventplanning

def main():
    participants, budget, hotels, weeks = list(map(lambda x: int(x), input().split(" ")))
    prices = []
    for i in range(hotels):
        price = int(input(" "))
        available_beds = [n for n in list(map(lambda x: int(x), input().split(" "))) if n >= participants]
        if available_beds:
            prices.append(price*participants)
    if prices:
        ans = min(prices)
        if ans <= budget:
            print(ans)
            return
    print("stay home")

main()