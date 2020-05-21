from tkinter import *
import os
import pygame

class MP3MusicPlayer():
    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x200+200+200")
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = 'None'
        self.gui_interfaces()

    def gui_interfaces(self):
        #Label Frame
        upperframe = LabelFrame(self.master, text = "Song Track", font = ("calibri", 15, "bold"), bg = "grey", fg = "white", bd = 5, relief = GROOVE)
        upperframe.place(x = 0, y = 0, width = 600, height = 100)
        songtrack = Label(upperframe, textvariable = self.track, width = 30, font = ("calibri", 20, "bold"), bg = "grey", fg = "gold")
        songtrack.grid(row = 0, padx = 10, pady = 5)
        #Button Frame
        bottomframe = LabelFrame(self.master, text = "Control Panel", font = ("calibri", 15, "bold"), bg = "grey", fg = "white", bd = 5, relief = GROOVE)
        bottomframe.place(x = 0, y = 100, width = 600, height=100)
        playbtn = Button(bottomframe, text = "PLAY", width = 6, height = 1, font = ("calibri", 16, "bold"), fg = "blue", bg = "gold", command = lambda: self.play_song())
        playbtn.grid(row = 0, column = 0, padx = 10, pady = 5)
        pausebtn = Button(bottomframe, text = "PAUSE", width = 8, height = 1, font = ("calibri", 16, "bold"), fg = "blue", bg = "gold", command = lambda: self.pause_song())
        pausebtn.grid(row = 0, column = 1, padx = 10, pady = 5)
        unpausebtn = Button(bottomframe, text = "UNPAUSE", width = 10, height = 1, font = ("calibri", 16, "bold"), fg = "blue", bg = "gold", command = lambda: self.unpause_song())
        unpausebtn.grid(row = 0, column = 2, padx = 10, pady = 5)
        stopbtn = Button(bottomframe, text = "STOP", width = 6, height = 1, font = ("calibri", 16, "bold"), fg = "blue", bg = "gold", command = lambda: self.stop_song())
        stopbtn.grid(row = 0, column = 3, padx = 10, pady = 5)
        shufflebtn = Button(bottomframe, text = "SHUFFLE", width = 10, height = 1, font = ("calibri", 16, "bold"), fg = "blue", bg = "gold", command = lambda: self.shuffle_song())
        shufflebtn.grid(row = 0, column = 4, padx = 10, pady = 5)
        #Playlist Frame
        songsframe = LabelFrame(self.master, text = "Song Playlist", font = ("calibri", 15, "bold"), bg = "grey", fg = "white", bd = 5, relief = GROOVE)
        songsframe.place(x = 600, y = 0, width = 400, height = 200)
        scrol_y = Scrollbar(songsframe, orient = VERTICAL)
        self.playlist = Listbox(songsframe, yscrollcommand = scrol_y.set, selectbackground = "gold", selectmode = SINGLE, font = ("calibri", 12, "bold"), bg = "white smoke", fg = "blue", bd = 5, relief = GROOVE)
        scrol_y.pack(side = RIGHT, fill = Y)
        scrol_y.config(command = self.playlist.yview)
        self.playlist.pack(fill = BOTH)
        os.chdir("F:\Music")
        track_directory = os.listdir()
        for directory in track_directory:
            os.chdir("F:\Music\{}".format(directory))
            songtracks = os.listdir()
            for track in songtracks:     
                self.playlist.insert(END, track)

    def play_song(self):
        self.status = 'Playing'
        self.track.set(self.playlist.get(ACTIVE))
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def pause_song(self):
        self.status = 'Paused'
        pygame.mixer.music.pause()

    def unpause_song(self):
        self.status = 'Playing'
        pygame.mixer.music.unpause()

    def stop_song(self):
        self.status = 'Stopped'
        pygame.mixer.music.stop()

    def shuffle_song(self):
        pass

if __name__ == '__main__':
    root = Tk()
    root.title("MP3 Music Player")
    MP3MusicPlayer(root)
    root.mainloop()
