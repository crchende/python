import tkinter as tk
import time

mw = tk.Tk()

####################
# Creating the widgets
####################
# with wrap - doesn't make sense to scroll horizontally.
# the code for horizontal scroll is commented
frame_received = tk.Frame(master = mw)
txt_received = tk.Text(master = frame_received, width = 40, height= 30, wrap = 'word', state = 'disabled')
ybar_received = tk.Scrollbar(master = frame_received, orient = 'vertical', command = txt_received.yview)
txt_received.configure(yscrollcommand = ybar_received.set)

# tags - how some messages will be formated
txt_received.tag_config("sentmsgsep", spacing1 = '0.1i', \
    spacing3 = 5, \
    font = '-*-helvetica-bold-r-normal--*-140-*', \
    underline = "yes")



frame_send = tk.Frame(master = mw)
txt_send = tk.Text(master = frame_send, width = 30, height = 10, wrap = 'word')
#xbar = tk.Scrollbar(master = mw, orient = 'horizontal', command = txt.xview)
ybar_send = tk.Scrollbar(master = frame_send, orient = 'vertical', command = txt_send.yview)
txt_send.configure(yscrollcommand = ybar_send.set)
#txt.configure(xscrollcommand = xbar.set)
btn_send = tk.Button(master = frame_send, text = '>>', command = lambda: send_msg(txt_send, txt_received, "sentmsgsep"))

# binding press <Eneter> event to txt_send - causing to send msg when enter is pressed
txt_send.bind('<Return>', lambda e: send_msg(txt_send, txt_received, "sentmsgsep"))


####################
# Displaying the widgets
####################
#in frame
txt_received.grid(row = 0, column = 0, sticky = 'nsew')
ybar_received.grid(row = 0, column = 1, sticky = 'ns')
# in the main window - mw
frame_received.grid(row = 0, column = 0, sticky = 'nsew')

#in frame
txt_send.grid(row = 0, column = 0, sticky = 'nsew')
ybar_send.grid(row = 0, column = 1, sticky = 'ns')

btn_send.grid(row = 0, column = 2, sticky = 'w')
#xbar.grid(row = 1, column = 0, sticky = 'ew')
frame_send.grid(row = 1, column = 0, sticky = 'nsew')

# resize setup
# per main window
mw.columnconfigure(0, weight = 1)
mw.rowconfigure(0, weight = 1)
mw.rowconfigure(1, weight = 1)

#per frames
frame_send.columnconfigure(0, weight = 1)
frame_send.rowconfigure(0, weight = 1)
frame_received.columnconfigure(0, weight = 1)
frame_received.rowconfigure(0, weight = 2)



##########
# widget actions
##########
def send_msg(from_source, to_destination, sep_frmt_tag):
    msg = from_source.get('1.0', 'end -1 char').strip('\n')
    print("msg: ", msg)
    if msg == '':
        from_source.delete('1.0', 'end')
        return "break"
    
    to_destination['state'] = 'normal'
    #ts = time.ctime() # standard format: 'Mon Jul 26 23:32:50 2021'
    # formating the time as described in the format string: "%y ..."
    ts = time.strftime("%y-%m-%d %X %Z", time.localtime())
    
    to_destination.insert('end', 'Sent: @' + ts + '\n', sep_frmt_tag)
    to_destination.insert('end', msg)
    to_destination.insert('end', '\n')
    to_destination['state'] = 'disabled'
    
    from_source.delete('1.0', 'end')
    return "break"

if __name__ == "__main__":
    print("Running as main:")
    mw.mainloop()
else:
    print("Loaded module text_widget")
