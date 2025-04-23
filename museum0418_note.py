import serial
import time
import sys
import cv2
import numpy as np
from unitree_sdk2py.go2.video.video_client import VideoClient
from unitree_sdk2py.core.channel import ChannelSubscriber, ChannelFactoryInitialize
from unitree_sdk2py.idl.default import unitree_go_msg_dds__SportModeState_
from unitree_sdk2py.idl.unitree_go.msg.dds_ import SportModeState_
from unitree_sdk2py.go2.sport.sport_client import (
    SportClient,
    PathPoint,
    SPORT_PATH_POINT_SIZE,
)
import math
from dataclasses import dataclass
from unitree_sdk2py.go2.vui.vui_client import VuiClient
from wireless_controller_315 import Custom
from arcade import load_sound,play_sound,stop_sound

#得到QRcode对应的数字
def qrcode(image): 
  # detect and decode
  data, vertices_array, binary_qrcode = cv2.QRCodeDetector().detectAndDecode(image)
  # if there is a QR code
  # return the data
  if vertices_array is not None:
    if data != '':
        print(f'QRcode data: {data}')

        return data
    
# 导入音频文件
sound1 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/C1.mp3")
sound2 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/E1.mp3")
sound3 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/C2.mp3")
sound4 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/E2.mp3")
sound5 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/C3.mp3")
sound6 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/E3.mp3")
sound7 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/OP.mp3")
sound8 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/OP_E.mp3")
sound9 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/ED.mp3")
sound10 = load_sound("/home/unitree/unitree_sdk2_python/audio_lib/audio_files/ED_E.mp3")
player1 = 0 #记录音频是否正在播放
player2 = 0 
player3 = 0
player4 = 0
player5 = 0
player6 = 0
player7 = 0
player8 = 0
player9 = 0
player10 = 0
sound_flag = 0

if __name__ == "__main__":
    #初始化
    if len(sys.argv)>1:
        ChannelFactoryInitialize(0, sys.argv[1])
    else:
        ChannelFactoryInitialize(0)

    
    custom = Custom() # 创建custom对象
    custom.Init()
    sport_client = SportClient()  # 创建sport client
    sport_client.SetTimeout(10.0)
    sport_client.Init()
    client = VideoClient()  # Create a video client
    client.SetTimeout(3.0)
    client.Init()
    code, data = client.GetImageSample()
    index=0
    
    while True:   
        time.sleep(1)
        print(f'key mode : {custom.remoteController.QRmode}')
        KEY_index = custom.remoteController.QRmode #获取按键


        # Request normal when code==0
        # while code == 0 and KEY_index!=0:
            # Get Image data from Go2 robot
        if KEY_index == 1: #当按上键时
            _, data = client.GetImageSample() #打开摄像头

            # Convert to numpy image
            image_data = np.frombuffer(bytes(data), dtype=np.uint8)
            image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
            index = 0
            # detect qrcode
            if qrcode(image):
                index = qrcode(image)
                index = int(index)
            print(f'playing index: {index}')
            
        
        # Display image
        #cv2.imshow("front_camera", image)      leading the QT thread bug. cannot be together with play_sound

        # # Press ESC to stop                         bug: ESC cannot interrupt the loop 
        # if cv2.waitKey(20) == 27 or index!=0:
        #     break
        if index!=0 and KEY_index ==1: #按过上键且扫过数字
            #cv2.destroyAllWindows()
                if index == 1: #扫到1则：
                    sport_client.Stretch() #伸懒腰
                    KEY_index = 0 #清空按键
                    player1 = play_sound(sound1) #播放对应音频
                    time_play = time.time() #获取当前时间
                    sound_flag = 1 #表示正在播放第一段音频
                    
                    
                elif index == 2:
                    sport_client.Stretch()
                    KEY_index = 0
                    player3 = play_sound(sound3)
                    time_play = time.time()
                    sound_flag = 2
                    
                elif index == 3:
                    sport_client.Stretch()
                    KEY_index = 0
                    player5 = play_sound(sound5)
                    time_play = time.time()
                    sound_flag = 3
                    
                elif index == 6:                   
                    # sport_client.Scrape()
                    KEY_index = 0  
                    player7 = play_sound(sound7)
                    time_play = time.time()
                    sound_flag = 4
                    
                elif index == 5:                   
                    sport_client.Stretch()
                    KEY_index = 0
                    player9 = play_sound(sound9)
                    time_play = time.time()
                    sound_flag = 5
                    
                else:
                    print('not in files')
                
        index =0 #储存QRcode的变量清零

        if KEY_index == 2: #如果按左键：
            if player1: #若在播放音频1
                stop_sound(player1) #停止音频1
                player1 = 0
                KEY_index = 0
            elif player2:
                stop_sound(player2)
                player2 = 0
                KEY_index = 0
            elif player3:
                stop_sound(player3)
                player3 = 0
                KEY_index = 0
            elif player4:
                stop_sound(player4)
                player4 = 0
                KEY_index = 0
            elif player5:
                stop_sound(player5)
                player5 = 0
                KEY_index = 0
            elif player6:
                stop_sound(player6)
                player6 = 0
                KEY_index = 0
            elif player7:
                stop_sound(player7)
                player7 = 0
                KEY_index = 0
            elif player8:
                stop_sound(player8)
                player8 = 0
                KEY_index = 0
            elif player9:
                stop_sound(player9)
                player9 = 0
                KEY_index = 0
            elif player10:
                stop_sound(player10)
                player10 = 0
                KEY_index = 0
            # sport_client.RiseSit()

        
        if sound_flag == 1:
            print('playing sound 1')
            if time.time()-time_play>118: #已经播完音频
                # sport_client.RiseSit()
                sound_flag = 0 #清空sound_flag表示已经播完音频
        elif sound_flag == 2:
            print('playing sound 2')
            if time.time()-time_play>208:
                # sport_client.RiseSit()
                sound_flag = 0
        elif sound_flag == 3:
            print('playing sound 3')
            if time.time()-time_play>212:
                # sport_client.RiseSit()
                sound_flag = 0
        elif sound_flag == 4:
            print('playing sound 4')
            if time.time()-time_play>212:
                # sport_client.RiseSit()
                sound_flag = 0
        elif sound_flag == 5:
            print('playing sound 5')
            if time.time()-time_play>30:
                # sport_client.RiseSit()
                sound_flag = 0