import sqlite3
import wx

app = wx.App(False)
frame = wx.Frame(None, title='A Films', size=(700, 600))
panel = wx.Panel(frame)

wx.StaticText(panel, label='Film Data', pos=(325, 10))
list_ctrl = wx.ListCtrl(panel, pos=(20,50), size=(650, 350), style=wx.LC_REPORT)

def display(event):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM afilms")
    data = cursor.fetchall()
    
    list_ctrl.ClearAll()
    list_ctrl.InsertColumn(0, 'ID', width=50)
    list_ctrl.InsertColumn(1, 'Title', width=200)
    list_ctrl.InsertColumn(2, 'release_year', width=80)
    list_ctrl.InsertColumn(3, 'language', width=80)
    list_ctrl.InsertColumn(4, 'rental_rate', width=80)
    list_ctrl.InsertColumn(5, 'length', width=80)
    list_ctrl.InsertColumn(6, 'rating', width=60)

    for row in data:
        list_ctrl.Append(row)

    conn.close()

def insert_film(event):
    
    frame_insert_film = wx.Frame(None, title='New Film', size=(480, 300))
    panel = wx.Panel(frame_insert_film)
    wx.StaticText(panel, label='Enter a New Film', pos=(180, 10))

    wx.StaticText(panel, label='Title', pos=(30, 50))
    title = wx.TextCtrl(panel, pos=(100, 50), size=(100, 22))

    wx.StaticText(panel, label='Release Year', pos=(30, 80))
    release_year = wx.TextCtrl(panel, pos=(100, 80), size=(100, 22))

    wx.StaticText(panel, label='Language', pos=(30, 110))
    language = wx.TextCtrl(panel, pos=(100, 110), size=(100, 22))

    wx.StaticText(panel, label='Rental Rate', pos=(250, 50))
    rental_rate = wx.TextCtrl(panel, pos=(320, 50), size=(100, 22))

    wx.StaticText(panel, label='Length', pos=(250, 80))
    length = wx.TextCtrl(panel, pos=(320, 80), size=(100, 22))

    wx.StaticText(panel, label='Rating', pos=(250, 110))
    rating = wx.TextCtrl(panel, pos=(320, 110), size=(100, 22))

    def insert_film_data(event):
        if title.GetValue() == '' or release_year.GetValue() == '' or language.GetValue() == '' or rental_rate.GetValue() == '' or length.GetValue() == '' or rating.GetValue() == '':
            wx.MessageBox('Please fill in all fields', 'Error')
            return

        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO afilms (title, release_year, language, rental_rate, length, rating) VALUES (?, ?, ?, ?, ?, ?)", 
        (title.GetValue(), release_year.GetValue(), language.GetValue(), rental_rate.GetValue(), length.GetValue(), rating.GetValue()))
        conn.commit()
        conn.close()
        frame_insert_film.Close()
        display(event)

    ok_button = wx.Button(panel, label='OK', pos=(190, 180))
    ok_button.Bind(wx.EVT_BUTTON, insert_film_data)

    frame_insert_film.Show()


def close(event):
    frame.Close()

display_button = wx.Button(panel, label='Display', pos=(100, 480))
display_button.Bind(wx.EVT_BUTTON, display)

insert_film_button = wx.Button(panel, label='Insert Film', pos=(300, 480))
insert_film_button.Bind(wx.EVT_BUTTON, insert_film)

close_button = wx.Button(panel, label='Close', pos=(500, 480))
close_button.Bind(wx.EVT_BUTTON, close)


frame.Show()
app.MainLoop()