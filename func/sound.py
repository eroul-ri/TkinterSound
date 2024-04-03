import winsound

class Sound : 
    def __init__(self, volume):
        self.volume = volume

    def mute(self):
        self.volume.SetMute(0, None)

    def unmute(self): 
        self.volume.SetMute(1, None)

    def setVolmeMax(self):
        self.volume.SetMasterVolumeLevel(0.0, None)

    def soundPlay(self, filename):
        winsound.PlaySound(filename, winsound.SND_FILENAME)
    def soundPlay(self):
        winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)