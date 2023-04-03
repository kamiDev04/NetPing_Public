import requests
from bs4 import BeautifulSoup
import time
import psycopg2
from psycopg2 import Error


chat_id = '-*chat id*'

def insert_base():
    try:
        connection = psycopg2.connect(user="*user*",
                                      password="*password*",
                                      host="*host*",
                                      port="5432",
                                      database="*database*")
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO sms (id, date, phone_numb, body_message)
                                                       VALUES (%s,%s,%s,%s)"""
        postgresql_select_query = "SELECT * FROM ( SELECT * FROM sms ORDER BY id DESC LIMIT 1) AS _ ORDER BY id ASC;"
        cursor.execute(postgresql_select_query)
        last_str = cursor.fetchmany()
        for row in last_str:
            last_id = row[0]
        id_current = last_id + 1
        record_to_insert = (id_current, message[0], message[1], message[2])
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        count = cursor.rowcount
    except (Exception, Error) as error:
        requests.get(f'https://api.telegram.org/*bot*/'
                     f'sendMessage?chat_id={chat_id}&text="Ошибка при записи сообщения в базу данных", {error}')
    finally:
        if connection:
            cursor.close()
            connection.close()

r = requests.get('http://*host*/default/en_US/tools.html?type=sms_inbox', auth=('*username*', '*password'))
r.encoding = 'utf8'
soup = BeautifulSoup(r.text, 'html.parser')
stringSoup = str(soup)
index = '\nsms_row_insert(l1_sms_store, sms, pos, 1)'
stringSoup = stringSoup.split(index)[0]
index = 'sms= '
stringSoup = stringSoup.split(index)[1]
index = '["'
stringSoup = stringSoup.split(index)[1]
index = '"];'
stringSoup = stringSoup.split(index)[0]
lSMS = stringSoup.split('","')
listSMS = []
for SMS in lSMS:
    SMS = SMS.split(sep=',', maxsplit=3)
    listSMS.append(SMS)
print(listSMS)


while True:
    time.sleep(10)
    r = requests.get('http://*host*/default/en_US/tools.html?type=sms_inbox', auth=('*username*', '*password*'))
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text, 'html.parser')
    stringSoup = str(soup)
    index = '\nsms_row_insert(l1_sms_store, sms, pos, 1)'
    stringSoup = stringSoup.split(index)[0]
    index = 'sms= '
    stringSoup = stringSoup.split(index)[1]
    index = '["'
    stringSoup = stringSoup.split(index)[1]
    index = '"];'
    stringSoup = stringSoup.split(index)[0]

    lSMS2 = stringSoup.split('","')
    listSMS2 = []
    for SMS2 in lSMS2:
        SMS2 = SMS2.split(sep=',', maxsplit=3)
        listSMS2.append(SMS2)


    if listSMS2[0] == listSMS[0]:
        continue
    else:
        message = listSMS2[0]
        if message[1] == '*phone number 1*' or message[1] == '*phone number 2*':
            message_text = f'{message[0]}: {message[2]}'
            requests.get(f'https://api.telegram.org/*bot*/'
                         f'sendMessage?chat_id={chat_id}&text={message_text}')
            insert_base()
            # bot.send_message(message.chat.id, listSMS2[0])
        else:


            if listSMS2[1] == listSMS[0]:
                listSMS = listSMS2
                continue
            else:
                message = listSMS2[1]
                if message[1] == '*phone number 1*' or message[1] == '*phone number 2*':
                    message_text = f'{message[0]}: {message[2]}'
                    requests.get(f'https://api.telegram.org/*bot*/'
                                f'sendMessage?chat_id={chat_id}&text={message_text}')
                    insert_base()
                    # bot.send_message(message.chat.id, listSMS2[1])
                else:



                    if listSMS2[2] == listSMS[0]:
                        listSMS = listSMS2
                        continue
                    else:
                        message = listSMS2[2]
                        if message[1] == '*phone number 1*' or message[1] == '*phone number 2*':
                            message_text = f'{message[0]}: {message[2]}'
                            requests.get(f'https://api.telegram.org/*bot*/'
                                        f'sendMessage?chat_id={chat_id}&text={message_text}')
                            insert_base()
                            # bot.send_message(message.chat.id, listSMS2[2])
                        else:


                            if listSMS2[3] == listSMS[0]:
                                listSMS = listSMS2
                                continue
                            else:
                                if message[1] == '*phone number 1*' or message[1] == '*phone number 2*':
                                    message = listSMS2[3]
                                    message_text = f'{message[0]}: {message[2]}'
                                    requests.get(f'https://api.telegram.org/*bot*/'
                                                f'sendMessage?chat_id={chat_id}&text={message_text}')
                                    insert_base()
                                    # bot.send_message(message.chat.id, listSMS2[3])
                                else:


                                    if listSMS2[4] == listSMS[0]:
                                        listSMS = listSMS2
                                        continue
                                    else:
                                        message = listSMS2[4]
                                        if message[1] == '*phone number 1*' or message[1] == '*phone number 2*':
                                            message_text = f'{message[0]}: {message[2]}'
                                            requests.get(f'https://api.telegram.org/*bot*/'
                                                        f'sendMessage?chat_id={chat_id}&text={message_text}')
                                            insert_base()
                                            # bot.send_message(message.chat.id, listSMS2[4])
                                        else:


                                            if listSMS2[5] == listSMS[0]:
                                                listSMS = listSMS2
                                                continue
                                            else:
                                                message = listSMS2[5]
                                                if message[1] == '*phone number 1*' or message[1] == '*phone number 2*':
                                                    message_text = f'{message[0]}: {message[2]}'
                                                    requests.get(f'https://api.telegram.org/*bot*/'
                                                                f'sendMessage?chat_id={chat_id}&text={message_text}')
                                                    insert_base()
                                                    # bot.send_message(message.chat.id, listSMS2[5])
                                                else:


                                                    if listSMS2[6] == listSMS[0]:
                                                        listSMS = listSMS2
                                                        continue
                                                    else:
                                                        message = listSMS2[6]
                                                        if message[1] == '*phone number 1*' or message[1] == '*phone number 2*':
                                                            message_text = f'{message[0]}: {message[2]}'
                                                            requests.get(
                                                                f'https://api.telegram.org/*bot*/'
                                                                f'sendMessage?chat_id={chat_id}&text={message_text}')
                                                            insert_base()
                                                            # bot.send_message(message.chat.id, listSMS2[6])
                                                            listSMS = listSMS2
                                                            continue

requests.get(f'https://api.telegram.org/*bot*/'
             f'sendMessage?chat_id={chat_id}&text=Ошибка на сервере. Не удалось прочитать информацию с GSM шлюза. Мониторинг остановлен.')

