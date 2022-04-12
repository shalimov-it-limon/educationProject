#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import imaplib
import email
import base64
import html2text

#Метод для перекодировки рускоязычных записей
def detect_charset_and_decode_string(text: str) -> str:
    if "=?utf-8?" in text:
        return base64.decodebytes(text.replace("=?utf-8?B?", '').encode('utf-8')).decode('utf-8')
    if "=?UTF-8?" in text:
        return base64.decodebytes(text.replace("=?UTF-8?B?", '').encode('utf-8')).decode('utf-8')
    if "=?UTF-8?" in text[0]:
        return base64.decodebytes(text[0].replace("=?UTF-8?B?", '').encode('utf-8')).decode('utf-8') + "," + str(text[1])
    if "=?windows-1251?B?" in text:
        return base64.decodebytes(text.replace("=?windows-1251?B?", '').encode('cp1251')).decode('cp1251')
    if "=?koi8-r?B?" in text:
        return base64.decodebytes(text.replace("=?koi8-r?B?", '').encode("koi8-r")).decode("koi8-r")
    else:
        try:
            if not text.__contains__("FW:"):
                res = base64.decodebytes(text.encode('utf-8')).decode('utf-8')
                res = html2text.html2text(res)
                return res
            else:
                return text.replace("FW:", '')
        except Exception as ex:
            return  text

mail = imaplib.IMAP4_SSL('imap.mail.ru')
mail.login('shalimov@it-limon.ru', 'всё вам скажи, да покажи, ага')

mail.list()
mail.select("inbox")

result, data = mail.search(None, "ALL")

ids = data[0]
id_list = ids.split()
latest_email_id = id_list[-1]

result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

print("Адресат: " + str(detect_charset_and_decode_string(detect_charset_and_decode_string(email.utils.parseaddr(email_message['To'])))))
print("Отправитель: " + detect_charset_and_decode_string(email.utils.parseaddr(email_message['From'])))
print("Дата отправки: " + detect_charset_and_decode_string(email_message['Date']))
print("Тема письма:" + detect_charset_and_decode_string(email_message['Subject']))
#print(detect_charset_and_decode_string(email_message['Message-Id']))

if email_message.is_multipart():
    for payload in email_message.get_payload():
        body = payload.get_payload(decode=True).decode('utf-8')
        body = detect_charset_and_decode_string(body)
        print(body)
else:
    body = email_message.get_payload(decode=True).decode('utf-8')
    body = detect_charset_and_decode_string(body)
    print(body)
