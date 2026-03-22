from tkinter import *
import cv2
from detect_mood import detect
import webbrowser as wb


class GUI:
    def __init__(self):
        self.win = Tk()
        self.win.geometry("1400x700")
        self.win.title("Music recommendation on Mood")
        self.win.configure(background='#121212')

        # Title
        self.lbltit = Label(self.win,
                            text="MOOD DETECTION SYSTEM",
                            font=("Montserrat",20,"bold","underline"),
                            fg="white",
                            bg="#121212")

        self.lbltit.place(x=400,y=20,width=600,height=50)

        # Start Button
        self.startbt = Button(self.win,
                              text="START",
                              font=("Montserrat",16,"bold"),
                              bg="#00ffff",
                              fg="black",
                              command=self.open_camera)

        self.startbt.place(x=500,y=150,width=100,height=50)

        # Exit Button
        self.exitbt = Button(self.win,
                             text="Exit",
                             font=("Montserrat",16,"bold"),
                             bg="#00ffff",
                             fg="black",
                             command=self.win.destroy)

        self.exitbt.place(x=800,y=150,width=100,height=50)

        # Mood Label
        self.lblmood = Label(self.win,
                             text="Mood : Not Detected",
                             font=("Montserrat",18,"bold"),
                             fg="yellow",
                             bg="#121212")

        self.lblmood.place(x=550,y=250,width=300,height=50)

        self.lblnote=Label(self.win,text="Songs playing on Spotify",
                           font=("Montserrat",18,"bold","italic"),
                           fg="light yellow",
                           bg="#121212")
        self.lblnote.place(x=550,y=330,width=300,height=50)



        # 🎵 Playlist Dictionary
        self.playlists = {
            "Happy": ["1)Buddhu Sa Mann","2)Khulke Jeene Ka","3)Won Din","more..."],
            "Sad": ["1)Main Dhoondne Ko Zamaane", "2)Bekhayali","3)Ae dil Hai Mushkil","more.."],
            "Angry": ["1)Kar Har Maidaan Fateh", "2)Brothers Anthem","3)Saadda Haq","more..."],
            "Surprise": ["1)Kudi Nu Nachne De", "2)Pathaka Guddi","3)Nadaand parinde","more..."],
            "Neutral": ["1)Hawayein","2)Raabta","3)Dil Main Ho Tum","more..."],
            "Fear": ["Soft Song 1"],
            "Disgust": ["Chill Song 1"]
        }

        self.spotify_playlists = {
            "happy": "https://open.spotify.com/playlist/3kSi9gg8PI45fy4y0XyhJb",
            "sad": "https://open.spotify.com/playlist/7gXRobbR7oazZ4PHvWXW33",
            "angry": "https://open.spotify.com/playlist/0N7bTAuO8ejUjW2YkyZfRB",
            "surprise": "https://open.spotify.com/playlist/7vatYrf39uVaZ8G2cVtEik",
            "neutral": "https://open.spotify.com/playlist/6qSnPjL2v5E61S1AkxLKIG?si=Ws9BBljdRyS2KsNltnDu_g",
            "fear": "https://open.spotify.com/playlist/2OpHqmLyvZfiVuOcP2KZqn",
            "disgust": "https://open.spotify.com/playlist/4Z9uxR135TmwTaMwEixd4b"
        }

        # 🎧 Song Listbox
        self.songlist = Listbox(self.win,
                                font=("Montserrat",14),
                                bg="black",
                                fg="white")

        self.songlist.place(x=500,y=380,width=400,height=200)

        self.win.mainloop()


    def open_camera(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow("Camera - Press C to Capture", frame)
            key = cv2.waitKey(1)

            if key == ord('c'):
                cv2.imwrite("captured_face.jpg", frame)
                print("Image Captured")
                mood = detect()
                self.lblmood.config(text="Mood : " + mood)
                # 🎵 Playlist load
                self.load_playlist(mood)
                self.open_spotify(mood)
                break

            if key == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def load_playlist(self, mood):

        self.songlist.delete(0, END)

        if mood in self.playlists:

            for song in self.playlists[mood]:

                self.songlist.insert(END, song)

    def open_spotify(self, mood):

        mood = mood.lower()

        if mood in self.spotify_playlists:
            url = self.spotify_playlists[mood]
            wb.open(url)
