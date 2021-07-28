import tkinter as tk
import time

class ChatWindow(object):

    def __init__(self, socket_id):
        self.mw = tk.Tk()
        
        self.socket_id = socket_id
        
        ####################
        # Creating the widgets
        ####################
        # with wrap - doesn't make sense to scroll horizontally.
        # the code for horizontal scroll is commented
        self.frame_received = tk.Frame(master = self.mw)
        self.txt_received = tk.Text(master = self.frame_received, width = 40, height= 30, wrap = 'word', state = 'disabled')
        self.ybar_received = tk.Scrollbar(master = self.frame_received, orient = 'vertical', command = self.txt_received.yview)
        self.txt_received.configure(yscrollcommand = self.ybar_received.set)
        
        # tags - how some messages will be formated
        self.txt_received.tag_config("sentmsgsep", spacing1 = '0.1i', \
            spacing3 = 5, \
            font = '-*-helvetica-bold-r-normal--*-140-*', \
            underline = "yes")
         
        
        self.frame_send = tk.Frame(master = self.mw)
        self.txt_send = tk.Text(master = self.frame_send, width = 30, height = 10, wrap = 'word')
        #xbar = tk.Scrollbar(master = mw, orient = 'horizontal', command = txt.xview)
        self.ybar_send = tk.Scrollbar(master = self.frame_send, orient = 'vertical', command = self.txt_send.yview)
        self.txt_send.configure(yscrollcommand = self.ybar_send.set)
        #txt.configure(xscrollcommand = xbar.set)
        self.btn_send = tk.Button(master = self.frame_send, text = '>>', \
            command = lambda s = self.txt_send, r = self.txt_received, channel = self.socket_id:\
                self.send_msg(s, r, "sentmsgsep"))

        # binding press <Eneter> event to txt_send - causing to send msg when enter is pressed
        # e parameter of lambda is the event object that have to pe passed to lambda
        self.txt_send.bind('<Return>', lambda e, s = self.txt_send, r = self.txt_received, channel = self.socket_id:\
            self.send_msg(s, r, "sentmsgsep", channel))


        ####################
        # Displaying the widgets
        ####################
        #in frame
        self.txt_received.grid(row = 0, column = 0, sticky = 'nsew')
        self.ybar_received.grid(row = 0, column = 1, sticky = 'ns')
        # in the main window - mw
        self.frame_received.grid(row = 0, column = 0, sticky = 'nsew')

        #in frame
        self.txt_send.grid(row = 0, column = 0, sticky = 'nsew')
        self.ybar_send.grid(row = 0, column = 1, sticky = 'ns')

        self.btn_send.grid(row = 0, column = 2, sticky = 'w')
        #xbar.grid(row = 1, column = 0, sticky = 'ew')
        self.frame_send.grid(row = 1, column = 0, sticky = 'nsew')

        # resize setup
        # per main window
        self.mw.columnconfigure(0, weight = 1)
        self.mw.rowconfigure(0, weight = 1)
        self.mw.rowconfigure(1, weight = 1)

        #per frames
        self.frame_send.columnconfigure(0, weight = 1)
        self.frame_send.rowconfigure(0, weight = 1)
        self.frame_received.columnconfigure(0, weight = 1)
        self.frame_received.rowconfigure(0, weight = 2)



    ##########
    # widget actions
    ##########
    def update_txt_received(self, txt_widget, separator_format_tag, sent_received, msg):
        txt_widget['state'] = 'normal'
        #ts = time.ctime() # standard format: 'Mon Jul 26 23:32:50 2021'
        # formating the time as described in the format string: "%y ..."
        ts = time.strftime("%y-%m-%d %X %Z", time.localtime())       
        txt_widget.insert('end', sent_received + ': @' + ts + '\n', separator_format_tag)
        txt_widget.insert('end', msg)
        txt_widget.insert('end', '\n')
        txt_widget['state'] = 'disabled'
        
    def socket_send_receive(self, socket_id, msg):
        b_msg = msg.encode('ascii')
        #s.sendall(b'Hello, world')
        socket_id.sendall(b_msg)
        data = socket_id.recv(1024)
        
        return data.decode('ascii')
        
    
    def send_msg(self, from_source, to_destination, sep_frmt_tag, socket_id = "None"):
        msg = from_source.get('1.0', 'end -1 char').strip('\n')
        print("msg: ", msg)
        if msg == '':
            from_source.delete('1.0', 'end')
            return "break"
        
        # recording the sent message in the upper text box
        self.update_txt_received(to_destination, sep_frmt_tag, "> Sent", msg)
        
        # sent text box cleanup
        from_source.delete('1.0', 'end')
        
        # if socket_id provided - send the message to the server
        if socket_id != "None":
            data = self.socket_send_receive(socket_id, msg)                
            self.update_txt_received(to_destination, sep_frmt_tag, "< Received", data)
        
        return "break"

if __name__ == "__main__":
    # For testing purpose - this module can be executed itself.
    # Whatever is written in the lower text box is recorded in the upper one
    print("Running as main:")
    cw = ChatWindow(socket_id = "None")
    cw.mw.mainloop()
else:
    print("Loaded module txt_for_chat")
