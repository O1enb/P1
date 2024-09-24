

def send_email(mes, rec, *, sen = 'university.help@gmail.com'):
    if '@' not in rec or '@' not in sen or not rec.endswith((".com",".ru",".net")) or not sen.endswith((".com",".ru",".net")):
        print(f"Невозможно отправить письмо с адреса {sen} на адрес {rec}.")
    elif sen == rec:
        print("Нельзя отправить письмо самому себе!")
    elif sen == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sen} на адрес {rec}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sen} на адрес {rec}.")


send_email("message", 'university.helpgmail.com')
send_email("message", 'university.help@gmail.com')
send_email("message", 'university@gmail.com')
send_email("message", 'universityp@gmail.com', sen = 'help@gmail.com')