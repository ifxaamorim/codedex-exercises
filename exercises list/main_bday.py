import datetime, bday_messages

today = datetime.date.today()

next_birthday = datetime.date(2025,9,8)

days_away =  next_birthday - today

if next_birthday == today:
    print(f"{bday_messages}")
else:
    print(f"Meu próximo aniversáio é em {days_away}")


