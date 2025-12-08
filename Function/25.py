#WAF to convert USD to INR

def converter(usd_val):
    inr_val = usd_val * 89
    print(f"{usd_val} USD is equal to {inr_val} INR")

converter(10)