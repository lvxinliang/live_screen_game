import serial
import time
import asyncio
import websockets
import json

ser = None
def burst_balloon():
    print('Bursting balloon')
    if ser.is_open:
        ser.write(b'G1 Y0 F6000\n')
        ser.write(b'G1 Y-10 F6000\n')
        ser.write(b'G1 Y0 F6000\n')
    else:
        print('Failed to open serial port')


def do_action(nickname, gift):
    # if (gift['name'] == '点亮粉丝团' and gift['count'] >= 1):
    if (gift['count'] >= 1):
        print(f'{nickname}送出了{gift["count"]}个{gift["name"]}')
        for i in range(gift['count']):
            burst_balloon()
            # time.sleep(0.1)

def process_msg(msg):
    try:
        json_obj = json.loads(msg)
        if (json_obj['type'] == 'gift'):
            gift = json_obj['gift']
            nickname = json_obj['nickname']
            do_action(nickname, gift)
    except json.JSONDecodeError as e:
        print(f'Error decoding JSON: {e}')

async def msg_callback(websocket, path):
    async for message in websocket:
        process_msg(message)

def websocket_server():
    print('WebSocket服务启动成功，可通过 ws://localhost:8765 进行访问')
    asyncio.get_event_loop().run_until_complete(websockets.serve(msg_callback, 'localhost', 8765))
    asyncio.get_event_loop().run_forever()

def serial_init():
    global ser
    ser = serial.Serial('COM4', baudrate=9600)
    if ser.is_open:
        print('Serial port opened')
    else:
        print('Failed to open serial port')
if __name__ == '__main__':
    serial_init()
    websocket_server()
