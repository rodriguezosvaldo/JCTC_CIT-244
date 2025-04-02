import wx
import sqlite3
import requests
import datetime
import os
from dotenv import load_dotenv

def display_data(event):
    conn = sqlite3.connect('tech_stocks.db')
    cursor = conn.cursor()
    cursor.execute("SELECT company, symbol, purchase_price, shares FROM dow_stocks")
    rows = cursor.fetchall()
    conn.close()
    
    load_dotenv()
    api_key = os.getenv('FINNHUB_API_KEY')
    os.environ.pop("FINNHUB_API_KEY", None)
    data = []
    for row in rows:
        company_info = {
            'company': row[0],
            'symbol': row[1],
            'purchase_price': row[2],
            'shares': row[3]
        }
        response = requests.get(f'https://finnhub.io/api/v1/quote?symbol={company_info['symbol']}&token={api_key}')
        finnhub_data = response.json()
        current_price = finnhub_data['c']
        gain_loss = round((company_info['shares'] * (current_price - company_info['purchase_price'])),2)
        company_info['gain_loss'] = gain_loss
        company_info['current_price'] = current_price
        data.append(company_info)
    
    list_ctrl.DeleteAllItems()
    for company in data:
        index = list_ctrl.InsertItem(list_ctrl.GetItemCount(), company['company'])
        list_ctrl.SetItem(index, 1, company['symbol'])
        list_ctrl.SetItem(index, 2, str(company['purchase_price']))
        list_ctrl.SetItem(index, 3, str(company['current_price']))
        list_ctrl.SetItem(index, 4, str(company['shares']))
        list_ctrl.SetItem(index, 5, str(company['gain_loss']))
    
    total_gain_loss = 0
    for company in data:
        total_gain_loss += company['gain_loss']
    total_label.SetLabel(f'Net gain/loss: $ {total_gain_loss}')
    current_date = datetime.datetime.now() 
    current_date = current_date.strftime("%A %B %d, %Y : %H:%M") 
    date_label.SetLabel(current_date)

def cancel(event):
    frame.Close()

app = wx.App(False)
frame = wx.Frame(None, title='read data', size=(630, 400))
panel = wx.Panel(frame)

vertical_box = wx.BoxSizer(wx.VERTICAL)

date_label = wx.StaticText(panel, label="Today's Date")
vertical_box.Add(date_label, flag=wx.ALIGN_CENTER | wx.TOP, border=5)
total_label = wx.StaticText(panel, label="Total")
vertical_box.Add(total_label, flag=wx.ALIGN_CENTER | wx.BOTTOM, border=5)

list_ctrl = wx.ListCtrl(panel, style=wx.LC_REPORT)
column_labels = ["Company", "Symbol", "Purchase Price", "Current Price", "Shares", "Gain/Loss"]
for col, label in enumerate(column_labels):
    list_ctrl.InsertColumn(col, label)
    list_ctrl.SetColumnWidth(col, 100)
vertical_box.Add(list_ctrl, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

horizontal_box = wx.BoxSizer(wx.HORIZONTAL)
display_data_btn = wx.Button(panel, label='Display Data')
cancel_btn = wx.Button(panel, label='Cancel')
horizontal_box.Add(display_data_btn, flag=wx.RIGHT, border=10)
horizontal_box.Add(cancel_btn)

vertical_box.Add(horizontal_box, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
panel.SetSizer(vertical_box)

display_data_btn.Bind(wx.EVT_BUTTON, display_data)
cancel_btn.Bind(wx.EVT_BUTTON, cancel)

frame.Show()
app.MainLoop()

