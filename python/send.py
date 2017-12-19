#encoding:utf-8
#/usr/bin/env/python

import pika
import sys
 
message =  str(sys.argv[1 ])


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

channel = connection.channel()
 
channel.queue_declare(queue='rabbit_queue', durable=True)

 
channel.basic_publish(exchange = '',

					  routing_key ='rabbit_queue' ,
					  
					  body = message ,
					  properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))

print "[X] send message to rabbitmq %s from python"  % (message ,)
 
connection.close()
