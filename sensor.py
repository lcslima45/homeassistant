import time
import random
import pika
a = True


count = 0 
while a:
    n = random.randint(0,20)
    print(n)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    if n==15:
        channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='FOGO!!!')
        print(" [x] Sent 'FOGO'")
        count = count + 1
        if count == 5:
            a = False
       
    else:
        channel.queue_declare(queue='hello')
        channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Nao tem FOGO!!!')
        print(" [x] Sent 'Nao tem FOGO'")

        
    time.sleep(5)