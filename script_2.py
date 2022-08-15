from datetime import datetime

while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    if current_time == "21:35:00":
        print("está na hora já")
        break
    else:
        print("ainda não está na hora")
