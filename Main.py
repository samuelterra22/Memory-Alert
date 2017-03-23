#!/usr/bin/env python

## References

## https://docs.python.org/2/library/email-examples.html
## http://stackoverflow.com/questions/11615591/available-and-used-system-memory-in-python

import time
import psutil
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime


def leMemoria():
    while 1:
        percMemoriaUsada = psutil.virtual_memory()[2]
        print("Memoria usada: " + str(percMemoriaUsada) + "%")
        if float(percMemoriaUsada) > 70.0:
            ##  ("Memoria ultrapassou 70%. Enviar email.")  ##
            enviaEmail(percMemoriaUsada)
        time.sleep(5)


def enviaEmail(percAtiginda):
    """
        Function just send a email.
    """

    me = "samuelterra22@gmail.com"
    you = "samuelterra22@hotmail.com"

    # me == my email address
    # you == recipient's email address

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Alerta de uso da memoria RAM"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text1 = "Olá!\nO servidor está usando " + str(percAtiginda) + "% da memoria disponível.\n\n"
    text2 = "Hora do alerta: " + str(datetime.now())
    text = text1 + text2

    # Record the MIME types of both parts - text/plain and text/html.
    part = MIMEText(text, 'plain')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part)

    # Send the message via local SMTP server.
    s = smtplib.SMTP('localhost')
    # sendmail function takes 3 arguments: sender's address, recipient's address
    # and message to send - here it is sent as one string.

    s.sendmail(me, you, msg.as_string())

    s.quit()

    return

if __name__ == '__main__':
    leMemoria()
