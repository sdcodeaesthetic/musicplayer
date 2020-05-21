from tkinter import *
import os
import pygame

class MusicPlayer():
    def __init__(self, master):
        self.master = master
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()
        self.gui_interfaces()

    def gui_interfaces(self):
        #Label Frame
        upperframe = Frame(self.master, text = "Song Track", font = ("times new roman", 15, "bold"), bg = "grey", fg = "white", bd = 5, relief = GROOVE)
        upperframe.place(x = 0, y = 0, width = 600, height = 100)
        songtrack = Label(upperframe, textvariable = self.track, width = 20, font = ("times new roman", 24, "bold"), bg = "grey", fg = "gold")
        songtrack.grid(row = 0, column = 0, padx = 10, pady = 5)
        trackstatus = Label(upperframe, textvariable = self.status, font = ("times new roman", 24, "bold"), bg = "grey", fg = "gold")
        trackstatus.grid(row = 0, column = 1, padx = 10, pady = 5)
        #Button Frame
        bottomframe = Frame(self.master, text = "Control Panel", font = ("times new roman", 15, "bold"), bg = "grey", fg = "white", bd = 5, relief = GROOVE)
        bottomframe.place(x = 0, y = 100, width = 600, height=100)
        playbtn = Button(bottomframe, text = "PLAY", command = self.playsong, width = 6, height = 1, font = ("times new roman", 16, "bold"), fg = "navyblue", bg = "gold")
        playbtn.grid(row = 0, column = 0, padx = 10, pady = 5)
        pausebtn = Button(bottomframe, text = "PAUSE", command = self.pausesong, width = 8, height = 1, font = ("times new roman", 16, "bold"), fg = "navyblue", bg = "gold")
        pausebtn.grid(row = 0, column = 1, padx = 10, pady = 5)
        unpausebtn = Button(bottomframe, text = "UNPAUSE", command = self.unpausesong, width = 10, height = 1, font = ("times new roman", 16, "bold"), fg = "navyblue", bg = "gold")
        unpausebtn.grid(row = 0, column = 2, padx = 10, pady = 5)
        stopbtn = Button(bottomframe, text = "STOP", command = self.stopsong, width = 6, height = 1, font = ("times new roman", 16, "bold"), fg = "navyblue", bg = "gold")
        stopbtn.grid(row = 0, column = 3, padx = 10, pady = 5)
        #Playlist Frame
        songsframe = Frame(self.master, text = "Song Playlist", font = ("times new roman", 15, "bold"), bg = "grey", fg = "white", bd = 5, relief = GROOVE)
        songsframe.place(x = 600, y = 0, width = 400, height = 200)
        scrol_y = Scrollbar(songsframe, orient = VERTICAL)
        self.playlist = Listbox(songsframe, yscrollcommand = scrol_y.set, selectbackground = "gold", selectmode = SINGLE, font = ("times new roman", 12, "bold"), bg = "silver", fg = "navyblue", bd = 5, relief = GROOVE)
        scrol_y.pack(side = RIGHT, fill = Y)
        scrol_y.config(command = self.playlist.yview)
        self.playlist.pack(fill = BOTH)
        os.chdir("F:\Music\One Direction")
        songtracks = os.listdir()
        for track in songtracks:
            self.playlist.insert(END, track)

        def playsong(self):
            self.track.set(self.playlist.get(ACTIVE))
            self.status.set("-Playing")
            pygame.mixer.music.load(self.playlist.get(ACTIVE))
            pygame.mixer.music.play()

        def pausesong(self):
            self.status.set("-Paused")
            pygame.mixer.music.pause()

        def unpausesong(self)

if __name__ == '__main__':
    root = Tk()
    root.title("MP3 Music Player")
    player = MusicPlayer(root)
    root.mainloop()
