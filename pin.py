import time

real_pin = "1726"

print("Starting PIN brute-force attack...\n")

for i in range(10000):  # 0000 to 9999
    guess = str(i).zfill(4)  # ensures 4 digits like 0001, 0023, etc.
    
    print(f"Trying PIN: {guess}")
    time.sleep(0)  # small delay so you can see it working
    
    if guess == real_pin:
        print("\n✅ PIN FOUND!")
        print(f"The PIN is {guess}")
        print(f"Attempts taken: {i + 1}")
        break