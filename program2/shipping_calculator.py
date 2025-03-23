import wx

def calculate(event):
    if weight1.GetValue():
        weight_cost = 5
    elif weight2.GetValue():
        weight_cost = 8
    else:
        weight_cost = 12.25

    if speed1.GetValue():
        speed_cost = 2.75
    elif speed2.GetValue():
        speed_cost = 6.15
    elif speed3.GetValue():
        speed_cost = 10.70
    else:
        speed_cost = 15.50

    extra_cost = 0
    if extra_padding.GetValue():
        extra_cost = 4
    if gift_wrapping.GetValue():
        extra_cost = 6

    total_cost = round(weight_cost + speed_cost + extra_cost, 2)
    summary_label.SetLabel(f"{name.GetValue()}\n{address.GetValue()}\n{city_state_zip.GetValue()}\n${total_cost}")

def clear_form(event):
    name.SetValue('')
    address.SetValue('')
    city_state_zip.SetValue('')
    weight1.SetValue(True)
    speed1.SetValue(True)
    extra_padding.SetValue(False)
    gift_wrapping.SetValue(False)
    summary_label.SetLabel('')

app = wx.App(False)
frame = wx.Frame(None, title='Shipping Calculator', size=(400, 400))
panel = wx.Panel(frame)

wx.StaticText(panel, label='Name:', pos=(10, 10))
name = wx.TextCtrl(panel, pos=(120, 10), size=(220, 22))

wx.StaticText(panel, label='Address:', pos=(10, 40))
address = wx.TextCtrl(panel, pos=(120, 40), size=(220, 22))

wx.StaticText(panel, label='City, State, and ZIP:', pos=(10, 70))
city_state_zip = wx.TextCtrl(panel, pos=(120, 70), size=(220, 22))

wx.StaticText(panel, label='Weight', pos=(40, 110))
weight1 = wx.RadioButton(panel, label='0 - 1.9 lbs ($5.00)', pos=(10, 130), style=wx.RB_GROUP)
weight2 = wx.RadioButton(panel, label='2 - 4.9 lbs ($8.00)', pos=(10, 150))
weight3 = wx.RadioButton(panel, label='5 - 10 lbs ($12.25)', pos=(10, 170))

wx.StaticText(panel, label='Speed', pos=(160, 110))
speed1 = wx.RadioButton(panel, label='Overland ($2.75)', pos=(130, 130), style=wx.RB_GROUP)
speed2 = wx.RadioButton(panel, label='3-Day Air ($6.15)', pos=(130, 150))
speed3 = wx.RadioButton(panel, label='2-Day Air ($10.70)', pos=(130, 170))
speed4 = wx.RadioButton(panel, label='Overnight ($15.50)', pos=(130, 190))

wx.StaticText(panel, label='Options', pos=(290, 110))
extra_padding = wx.CheckBox(panel, label='Extra Padding ($4)', pos=(260, 130))
gift_wrapping = wx.CheckBox(panel, label='Gift Wrapping ($6)', pos=(260, 150))

calc_button = wx.Button(panel, label='Calculate Total', pos=(10, 230))
calc_button.Bind(wx.EVT_BUTTON, calculate)

clear_button = wx.Button(panel, label='Clear Form', pos=(10, 255))
clear_button.Bind(wx.EVT_BUTTON, clear_form)

wx.StaticText(panel, label='Shipping Summary', pos=(220, 230))
wx.StaticText(panel, label='----------------------------', pos=(200, 245))
summary_label = wx.StaticText(panel, label='', pos=(220, 260), size=(50, 50))

frame.Show()
app.MainLoop()