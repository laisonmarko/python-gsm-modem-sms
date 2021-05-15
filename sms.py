import serial
import time
import sys


ser = serial.Serial('COM30', 115200, timeout=12)

def SendCommand(command):

    print(command)
    ser.write(command.encode())
    time.sleep(2)
    data = ''
    if getline:
        data=ReadLine()
        return(data) 

def ReadLine():
    data = ser.readline()
    print (data)
    return data 



def ReceiveSms():
    SendCommand('ATZ\r')
    SendCommand('AT+CMGF=1\r')
    ser.flushInput()
    ser.flushOutput()
    SendCommand('AT\r')


    command = 'AT+CMGL="REC UNREAD"\r'                  #gets sms that has not been read
    print (SendCommand(command))
    data = ser.readall()
    data=str(data)
    print(data)
    if "REC UNREAD" in data:
        numberIndex=data.find('+255')
        smsIndex=data.find('"\\r\\n')+5
        smsLastIndex=data.find('\\r\\n\\r\\nOK\\r\\n')
        phone=data[numberIndex:numberIndex+13]
        sms=data[smsIndex:smsLastIndex]
        print("Phone:"+phone)
        print("sms :" +sms)


def SendSms(message,to):
      SendCommand('ATZ\r')
      SendCommand('AT+CMGF=1\r')
      to='AT+CMGS='+'"'+to+'"'

      SendCommand('ATE0\r')

      SendCommand('AT\r')
      
      SendCommand('AT+CMGD="ALL"\r')

      SendCommand('AT+CMGF=1\r')

      SendCommand(to + "\r")

      SendCommand(message + "\r")

      SendCommand(chr(26))

      print ("disconnecting")
      ser.flush()
      #ser.close()


