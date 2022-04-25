import tkinter
from tkinter import *
import pygame
import os
import sys

class audioPlayer():
    
    currentSongIndex = 0;
    currentSongName = ""
    allSongs = []
    supportedAudioExtensions = [".wav", ".mp3",".ogg"];
    musicIsPaused = True;
    audioInit = False;
    
    def __init__(self):
        #put all songs in dir into allSongs list
        audioPath = os.getcwd() + r"\Audio\\";
        listOfFiles = []
        for root, dirs, files in os.walk(audioPath):
            for file in files:
                listOfFiles.append(os.path.join(root, file))
        for name in listOfFiles:
            file = name[name.rfind("\\") + 1:]
            self.allSongs.append(audioPath + file)
        if not self.allSongs:
            print("No songs in the folder...")
            sys.exit()

        
        initAudioFile = self.allSongs[self.currentSongIndex];
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(initAudioFile)
        pygame.mixer.music.set_volume(0.5)
        self.currentSongName = initAudioFile;

 
    def playPauseAudio(self):
        
        if self.musicIsPaused:
            if self.audioInit:
                pygame.mixer.music.unpause()
                self.musicIsPaused = False;
                canvas.itemconfig(playPauseLabel, text="⏸")

            else:
                pygame.mixer.music.play()
                self.audioInit = True;
                self.musicIsPaused = False; 
                pygame.mixer.music.queue(self.allSongs[self.currentSongIndex+1])
                canvas.itemconfig(playPauseLabel, text="⏸")
                canvas.itemconfig(songTitle, text=self.currentSongName[0:self.currentSongName.rfind(".")][self.currentSongName.rfind("\\")+1:])

        else:
            pygame.mixer.music.pause();
            self.musicIsPaused = True
            canvas.itemconfig(playPauseLabel, text="▶")
            canvas.itemconfig(songTitle, text=self.currentSongName[0:self.currentSongName.rfind(".")][self.currentSongName.rfind("\\")+1:])

    
    def forward(self):

        if self.currentSongIndex != len(self.allSongs)-1:
            
            if self.musicIsPaused:
                self.currentSongIndex += 1;
                self.currentSongName = self.allSongs[self.currentSongIndex];
                pygame.mixer.music.unload();
                pygame.mixer.music.load(self.currentSongName)
                pygame.mixer.music.play();
                pygame.mixer.music.pause();
                canvas.itemconfig(songTitle, text=self.currentSongName[0:self.currentSongName.rfind(".")][self.currentSongName.rfind("\\")+1:])
            else:
                self.currentSongIndex += 1;
                self.currentSongName = self.allSongs[self.currentSongIndex];
                pygame.mixer.music.unload();
                pygame.mixer.music.load(self.currentSongName)
                pygame.mixer.music.play();
                canvas.itemconfig(songTitle, text=self.currentSongName[0:self.currentSongName.rfind(".")][self.currentSongName.rfind("\\")+1:])
            
        else:
            
            if self.musicIsPaused:
                self.currentSongIndex = 0;
                self.currentSongName = self.allSongs[self.currentSongIndex];
                pygame.mixer.music.unload();
                pygame.mixer.music.load(self.currentSongName)
                pygame.mixer.music.play();
                pygame.mixer.music.pause();
                canvas.itemconfig(songTitle, text=self.currentSongName[0:self.currentSongName.rfind(".")][self.currentSongName.rfind("\\")+1:])
            else:
                self.currentSongIndex = 0;
                self.currentSongName = self.allSongs[self.currentSongIndex];
                pygame.mixer.music.unload();
                pygame.mixer.music.load(self.currentSongName)
                pygame.mixer.music.play();
                canvas.itemconfig(songTitle, text=self.currentSongName[0:self.currentSongName.rfind(".")][self.currentSongName.rfind("\\")+1:])


    def previous(self):
        
        
        if self.currentSongIndex != 0:
            
            self.currentSongIndex -= 1;
            self.currentSongName = self.allSongs[self.currentSongIndex];
            pygame.mixer.music.unload();
            pygame.mixer.music.load(self.currentSongName)
            pygame.mixer.music.play();
            canvas.itemconfig(songTitle, text=self.currentSongName[0:self.currentSongName.rfind(".")][self.currentSongName.rfind("\\")+1:])
        else:
            
            self.currentSongIndex = len(self.allSongs)-1;
            self.currentSongName = self.allSongs[self.currentSongIndex]
            pygame.mixer.music.unload();
            pygame.mixer.music.load(self.currentSongName)
            pygame.mixer.music.play();
            canvas.itemconfig(songTitle, text=self.currentSongName[0:self.currentSongName.rfind(".")][self.currentSongName.rfind("\\")+1:])
        
        
    def getAllSongs(self):
        return self.allSongs;
       

    def playSongAtIndex(self):
        pass;


#End of Audio Player Class

#Functions
def playPauseAudioEventCaller(event):
    TheAudioPlayer.playPauseAudio();
def forwardEventCaller(event):
    TheAudioPlayer.forward();
def previousEventCaller(event):
    TheAudioPlayer.previous();
def restartProgram():
    os.system("python musicPlayer.py")
    exit()
def changeVolume(event):
    pygame.mixer.music.set_volume(volumeSlider.get()/100) 
   
    

    

#Start of Tkinter UI

#Configuration of the Main Window
windowWidth = 800
windowHeight = 600
TheAudioPlayer = audioPlayer()
currDir = os.getcwd();
mainWindow = Tk()
mainWindow.title("Music Player")
mainWindow.geometry(str(windowWidth) + "x" + str(windowHeight))
mainWindow.resizable(False, False)


#Canvas
canvas = Canvas(mainWindow, width=windowWidth, height=windowHeight);
bg = PhotoImage(file = "D:\\Microsoft VS Code\\Code\\MusicPlayerApp\\Assets\\background.png")
canvas.create_image(0,0,image=bg)
songTitle = canvas.create_text(400,5, text="No Song Playing...", font=("tahoma",20),anchor="n")
playPauseLabel = canvas.create_text(400,450, text="▶", font=("tahoma",20),anchor="n",tags="playPauseLabel")
forwardLabel = canvas.create_text(700,450, text="⏭️", font=("tahoma",20),anchor="e",tags="forwardLabel")
previousLabel = canvas.create_text(100,450,text="⏮️", font=("tahoma",20),anchor="w",tags="previousLabel")
volumeLabel = canvas.create_text(730,300,text="Volume", font=("tahoma",20),anchor="e")


canvas.tag_bind("playPauseLabel",'<Button-1>',playPauseAudioEventCaller)
canvas.tag_bind("forwardLabel",'<Button-1>',forwardEventCaller)
canvas.tag_bind("previousLabel",'<Button-1>',previousEventCaller)

#Volume Slider
volumeSlider = Scale(
    mainWindow,
    from_ = 0,
    to = 100,
    orient = HORIZONTAL ,
    resolution = 1,
    width=15,
    length=180,
    sliderlength=30,
    troughcolor="white",
    command=changeVolume,
    bg="white"
)

volumeSlider.set(pygame.mixer.music.get_volume() * 100);

#Songs List
songs = TheAudioPlayer.getAllSongs();
songListBox = Listbox(mainWindow,font="tahoma", bg="white",highlightcolor="white",selectbackground="tomato", bd=2,width=25)

#Favicon
mainWindow.iconphoto(False, tkinter.PhotoImage(file=currDir + r"\Assets\favicon.png"))


for i in range(0, len(songs),1):
    songListBox.insert(i,songs[i][songs[i].rfind("\\")+1:])


# UI Element Packing
songListBox.pack();
volumeSlider.pack();
canvas.pack(fill="both", expand=True)


#UI Positioning
songListBox.place(relx=0.98, rely=0.2, anchor=E)
volumeSlider.place(relx=0.98, rely=0.6, anchor=E);


#Run the Tkinter Main Window
mainWindow.mainloop();

if __name__ == '__main__':
    main()    








