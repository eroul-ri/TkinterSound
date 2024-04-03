from tkinter import *
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
from ctypes import cast, POINTER
from func.sound import Sound
import winsound
import psycopg2

class ibiNotiApp:
    # 생성
    def __init__(self, window, volume):
        self.window = window

        self.window.title("iBi Notification")
        self.window.geometry("620x340")
        self.window.resizable(False, False)

        self.volume = volume

        self.__main__()
    
    ## DB 생성
    def connection(self):
        conn = psycopg2.connect(
            host = "172.17.10.228", 
            database = "ibi",
            user = "postgres",
            password = "1234", 
            port = "5432",
            )

        c = conn.cursor()

        # Create a Table
        c.execute('''CREATE TABLE IF NOT EXISTS customers
        (first_name TEXT,
        last_name TEXT);
        ''')

        conn.commit()
        conn.close()
    
    def soundPlay(self):
        sound = Sound(self.volume)

        sound.mute()
        sound.setVolmeMax()
        sound.soundPlay()

    # main
    def __main__(self):
        notiBtn = Button(self.window, text="알림테스트1", command=self.soundPlay)
        notiBtn.pack()

        notiBtn2 = Button(self.window, text="DB커넥션테스트", command=self.connection)
        notiBtn2.pack()



if __name__ == '__main__':    
    window = Tk()

    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    ibiNotiApp(window, volume)

    window.mainloop()




