import tkinter as tk                
from tkinter import *                
from tkinter import font as tkfont  
from tkinter.messagebox import *
import time


current_balance = 1000

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        self.shared_data = {'Balance':tk.IntVar()}
        # self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, MenuPage, WithdrawPage, DepositPage, BalancePage,CardsPage,ApprovedPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        self.controller.title("X-ATM")
        # self.controller.state('zoomed')
        self.controller.geometry("760x870")
        self.controller.iconphoto(False,tk.PhotoImage(file='./img/atm (1).png'))

        heading_label = tk.Label(self,
                                 text='X-ATM',
                                 font=('orbitron',45,'bold'),
                                 foreground='white',
                                 background='#3d3d5c'
                                 )
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()

        # password
        password_label = tk.Label(self,
                                  text='Enter Your PIN',
                                  font=('orbitron',13),
                                  bg='#3d3d5c',
                                  foreground='white'
                                  )
        password_label.pack(pady=10)

        # password_entry
        my_password = tk.StringVar()
        password_entry_box = tk.Entry(self,
                                      textvariable=my_password,
                                      font=('orbitron',12),
                                      width=22
                                      )
        password_entry_box.focus_set()
        password_entry_box.pack(ipady=7)

        def handle_focus_in(_):
            password_entry_box.configure(foreground='black',show='*')

        password_entry_box.bind('<FocusIn>',handle_focus_in)

        # password_check
        def check_password():
            if my_password.get() == '123':
                my_password.set('')
                incorrect_password_label['text'] =''
                controller.show_frame('MenuPage')
            else:
                incorrect_password_label['text'] = 'Invalid password'
        enter_button = tk.Button(self,
                                 text='Enter',
                                 command=check_password,
                                 font=('orbitron',10),
                                 relief='raised',
                                 borderwidth=3,
                                 width=31,
                                 height=3
                                 )
        enter_button.pack(pady=10)

        incorrect_password_label = tk.Label(self,
                                             text='',
                                             font=('orbitron',13),
                                             foreground='white',
                                             background='#33334d',
                                             anchor='n'
                                             ) 
        incorrect_password_label.pack(fill='both',expand=True)

        #bottom frame    
        bottom_frame = tk.Frame(self,
                                 relief='raised',
                                 borderwidth=3
                                 )
        bottom_frame.pack(fill='x',side='bottom')

        # Cards_Photo
        visa_photo = tk.PhotoImage(file='./img/visa.png')
        visa_label = tk.Label(bottom_frame,
                              image=visa_photo
                              )
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='./img/mastercard.png')
        mastercard_label = tk.Label(bottom_frame,
                              image=mastercard_photo
                              )
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        meeza_photo = tk.PhotoImage(file='./img/meeza.png')
        meeza_label = tk.Label(bottom_frame,
                              image=meeza_photo
                              )
        meeza_label.pack(side='left')
        meeza_label.image = meeza_photo

        # time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()




class MenuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='X-ATM',
                                 font=('orbitron',45,'bold'),
                                 foreground='white',
                                 background='#3d3d5c'
                                 )
        heading_label.pack(pady=25)

        main_menu_label= tk.Label(self,
                                  text='Main Menu',
                                  font=('orbitron',13),
                                  foreground='white',
                                  background='#3d3d5c'
                                  )
        main_menu_label.pack()

        # #################################
        # selection BTNs
        selection_label = tk.Label(self,
                                      text='Please make a selection',
                                      font=('orbitron',13),
                                      fg='white',
                                      bg='#47476b',
                                      anchor='n'
                                      )
        selection_label.pack(fill='x',pady=15,anchor='n')

        button_frame = tk.Frame(self,
                                bg='#33334d'
                                )
        button_frame.pack(fill='both',expand=True)

        def withdraw():
            controller.show_frame('WithdrawPage')
        withdraw_button = tk.Button(button_frame,
                                    text="Withdraw",
                                    command=withdraw,
                                    relief='raised',
                                    borderwidth=3,
                                    width=29,
                                    height=3,
                                    font=('orbitron',13),
                                    )
        withdraw_button.pack(pady=15)

        def deposit():
            controller.show_frame('DepositPage')
        deposit_button = tk.Button(button_frame,
                                    text="Deposit",
                                    command=deposit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=29,
                                    height=3,
                                    font=('orbitron',13),
                                    )
        deposit_button.pack(pady=15)

        def balance():
            controller.show_frame('BalancePage')
        balance_button = tk.Button(button_frame,
                                    text="Balance",
                                    command=balance,
                                    relief='raised',
                                    borderwidth=3,
                                    width=29,
                                    height=3,
                                    font=('orbitron',13),
                                    )
        balance_button.pack(pady=15)

        def exit():
            controller.show_frame('StartPage')
        exit_button = tk.Button(button_frame,
                                    text="Exit",
                                    command=exit,
                                    relief='raised',
                                    borderwidth=3,
                                    width=29,
                                    height=3,
                                    font=('orbitron',13),
                                    )
        exit_button.pack(pady=15)

        # ###############################################
        #bottom frame    
        bottom_frame = tk.Frame(self,
                                 relief='raised',
                                 borderwidth=3
                                 )
        bottom_frame.pack(fill='x',side='bottom')

        # Cards_Photo
        visa_photo = tk.PhotoImage(file='./img/visa.png')
        visa_label = tk.Label(bottom_frame,
                              image=visa_photo
                              )
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='./img/mastercard.png')
        mastercard_label = tk.Label(bottom_frame,
                              image=mastercard_photo
                              )
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        meeza_photo = tk.PhotoImage(file='./img/meeza.png')
        meeza_label = tk.Label(bottom_frame,
                              image=meeza_photo
                              )
        meeza_label.pack(side='left')
        meeza_label.image = meeza_photo

        # time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()



class WithdrawPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='X-ATM',
                                 font=('orbitron',45,'bold'),
                                 foreground='white',
                                 background='#3d3d5c'
                                 )
        heading_label.pack(pady=25)

        choose_amount_label= tk.Label(self,
                                  text='Choose the amount you want to withdraw',
                                  font=('orbitron',13),
                                  foreground='white',
                                  background='#3d3d5c'
                                  )
        choose_amount_label.pack()

        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        def withdraw(amount):
            global current_balance
            current_balance -= amount
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')

        twenty_button = tk.Button(button_frame,
                                  text='20',
                                  command=lambda:withdraw(20),
                                  relief='raised',
                                  font=('orbitron',13),
                                  borderwidth=3,
                                  width=15,
                                  height=4
                                  )
        twenty_button.grid(row=0,column=0,pady=15,padx=25)

        forty_button = tk.Button(button_frame,
                                  text='40',
                                  command=lambda:withdraw(40),
                                  relief='raised',
                                  font=('orbitron',13),
                                  borderwidth=3,
                                  width=15,
                                  height=4
                                  )
        forty_button.grid(row=1,column=0,pady=15)

        sixty_button = tk.Button(button_frame,
                                  text='60',
                                  command=lambda:withdraw(60),
                                  relief='raised',
                                  font=('orbitron',13),
                                  borderwidth=3,
                                  width=15,
                                  height=4
                                  )
        sixty_button.grid(row=2,column=0,pady=15)
        eighty_button = tk.Button(button_frame,
                                  text='80',
                                  command=lambda:withdraw(80),
                                  relief='raised',
                                  font=('orbitron',13),
                                  borderwidth=3,
                                  width=15,
                                  height=4
                                  )
        eighty_button.grid(row=3,column=0,pady=15)

        one_hundred_button = tk.Button(button_frame,
                                          text='100',
                                          command=lambda:withdraw(100),
                                          relief='raised',
                                          borderwidth=3,
                                          font=('orbitron',13),
                                          width=15,
                                          height=4
                                          )
        one_hundred_button.grid(row=0,column=1,pady=15,padx=295)

        two_hundred_button = tk.Button(button_frame,
                                          text='200',
                                          command=lambda:withdraw(200),
                                          relief='raised',
                                          borderwidth=3,
                                          font=('orbitron',13),
                                          width=15,
                                          height=4
                                          )
        two_hundred_button.grid(row=1,column=1,pady=15)

        three_hundred_button = tk.Button(button_frame,
                                          text='300',
                                          command=lambda:withdraw(300),
                                          relief='raised',
                                          font=('orbitron',13),
                                          borderwidth=3,
                                          width=15,
                                          height=4
                                          )
        three_hundred_button.grid(row=2,column=1,pady=15)

        def card():
            controller.show_frame('CardsPage')
        card_button = tk.Button(button_frame,
                                    text="Other amount",
                                    command=card,
                                    font=('orbitron',13),
                                    relief='raised',
                                    borderwidth=3,
                                    width=15,
                                    height=3
                                    )
        card_button.grid(row=3,column=1,pady=15)

        # cash = tk.StringVar()
        # other_amount_entry = tk.Entry(button_frame,
        #                               textvariable=cash,
        #                               width=37,
        #                               justify='right')
        # other_amount_entry.grid(row=3,column=1,pady=15,ipady=30)

        # def other_amount(_):
        #     global current_balance
        #     current_balance -= int(cash.get())
        #     controller.shared_data['Balance'].set(current_balance)
        #     cash.set('')
        #     controller.show_frame('MenuPage')

        # other_amount_entry.bind('<Return>',other_amount)


        # back -------------------------------

        button_frame = tk.Frame(self,
                                 bg='#33334d',
                                #  relief='raised',
                                 )
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('MenuPage')

        image = PhotoImage(file='./img/back.png')
        menu_button = tk.Button(button_frame,
                                image=image,
                                command=menu,
                                bg='#666699',
                                relief='raised',
                                borderwidth=0,  
                                # highlightthickness=0,
                                )
        menu_button.image = image
        menu_button.pack(anchor='se',pady=7,padx=7)

        # #################################

        bottom_frame = tk.Frame(self,
                                 relief='raised',
                                 borderwidth=3
                                 )
        bottom_frame.pack(fill='x',side='bottom')

        # Cards_Photo
        visa_photo = tk.PhotoImage(file='./img/visa.png')
        visa_label = tk.Label(bottom_frame,
                              image=visa_photo
                              )
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='./img/mastercard.png')
        mastercard_label = tk.Label(bottom_frame,
                              image=mastercard_photo
                              )
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        meeza_photo = tk.PhotoImage(file='./img/meeza.png')
        meeza_label = tk.Label(bottom_frame,
                              image=meeza_photo
                              )
        meeza_label.pack(side='left')
        meeza_label.image = meeza_photo

        # time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()



class DepositPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='X-ATM',
                                 font=('orbitron',45,'bold'),
                                 foreground='white',
                                 background='#3d3d5c'
                                 )
        heading_label.pack(pady=25)

        space_label = tk.Label(self,height=4,bg='#3d3d5c')
        space_label.pack()

        # password
        enter_amount_label = tk.Label(self,
                                  text='Enter amount',
                                  font=('orbitron',13),
                                  bg='#3d3d5c',
                                  foreground='white'
                                  )
        enter_amount_label.pack(pady=10)

        cash = tk.StringVar()
        deposit_entry = tk.Entry(self,
                                  textvariable=cash,
                                  font=('orbitron',12),
                                  width=22
                                  )
        deposit_entry.pack(ipady=7)

        def deposit_cash():
            global current_balance
            current_balance += int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            controller.show_frame('MenuPage')
            cash.set('')

        enter_button = tk.Button(self,
                                  text='Enter',
                                  command=deposit_cash,
                                  relief='raised',
                                  borderwidth=3,
                                  width=23,
                                  height=2,
                                  font=('orbitron',13),
                                  )
        enter_button.pack(pady=15)

        two_tone_label = tk.Label(self,bg='#33334d')
        two_tone_label.pack(fill='both',expand=True)

        # back -------------------------------

        button_frame = tk.Frame(self,
                                 bg='#33334d',
                                #  relief='raised',
                                 )
        button_frame.pack(fill='both')

        def menu():
            controller.show_frame('MenuPage')

        image = PhotoImage(file='./img/back.png')
        menu_button = tk.Button(button_frame,
                                image=image,
                                command=menu,
                                bg='#666699',
                                relief='raised',
                                borderwidth=0,  
                                # highlightthickness=0,
                                )
        menu_button.image = image
        menu_button.pack(anchor='se',pady=7,padx=7)

        # button_frame = tk.Frame(self, bg='#33334d')
        # button_frame.pack(fill='both')

        # def menu():
        #     controller.show_frame('MenuPage')

        # menu_button = tk.Button(button_frame,
        #                         command=menu,
        #                         text='Menu',
        #                         relief='raised',
        #                         borderwidth=3,
        #                         width=20,
        #                         height=5,
        #                         )
        # menu_button.pack(anchor='se')



        # #################################

        bottom_frame = tk.Frame(self,
                                 relief='raised',
                                 borderwidth=3
                                 )
        bottom_frame.pack(fill='x',side='bottom')

        # Cards_Photo
        visa_photo = tk.PhotoImage(file='./img/visa.png')
        visa_label = tk.Label(bottom_frame,
                              image=visa_photo
                              )
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='./img/mastercard.png')
        mastercard_label = tk.Label(bottom_frame,
                              image=mastercard_photo
                              )
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        meeza_photo = tk.PhotoImage(file='./img/meeza.png')
        meeza_label = tk.Label(bottom_frame,
                              image=meeza_photo
                              )
        meeza_label.pack(side='left')
        meeza_label.image = meeza_photo

        # time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()


class BalancePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='X-ATM',
                                 font=('orbitron',45,'bold'),
                                 foreground='white',
                                 background='#3d3d5c'
                                 )
        heading_label.pack(pady=25)

        global current_balance
        controller.shared_data['Balance'].set(current_balance)
        balance_label = tk.Label(self,
                                  textvariable=controller.shared_data['Balance'],
                                  font=('orbitron',18),
                                  fg='white',
                                  bg='#47476b',
                                  anchor='n')
        balance_label.pack(fill='x',pady=25)

        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        def menu():
            controller.show_frame('MenuPage')

        # After modification -----------------
        menu_button = tk.Button(button_frame,
                                  command=menu,
                                  text='Menu',
                                  relief='raised',
                                  borderwidth=3,
                                  width=23,
                                  height=2,
                                  font=('orbitron',13),
                                  )
        menu_button.pack(pady=25)

        def exit():
            controller.show_frame('StartPage')

        # After modification -----------------
        exit_button = tk.Button(button_frame,
                                  text='Exit',
                                  command=exit,
                                  relief='raised',
                                  borderwidth=3,
                                  width=23,
                                  height=2,
                                  font=('orbitron',13),
                                  )
        exit_button.pack(pady=15)
        # #################################

        bottom_frame = tk.Frame(self,
                                 relief='raised',
                                 borderwidth=3
                                 )
        bottom_frame.pack(fill='x',side='bottom')

        # Cards_Photo
        visa_photo = tk.PhotoImage(file='./img/visa.png')
        visa_label = tk.Label(bottom_frame,
                              image=visa_photo
                              )
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='./img/mastercard.png')
        mastercard_label = tk.Label(bottom_frame,
                              image=mastercard_photo
                              )
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        meeza_photo = tk.PhotoImage(file='./img/meeza.png')
        meeza_label = tk.Label(bottom_frame,
                              image=meeza_photo
                              )
        meeza_label.pack(side='left')
        meeza_label.image = meeza_photo

        # time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()




class CardsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='X-ATM',
                                 font=('orbitron',45,'bold'),
                                 foreground='white',
                                 background='#3d3d5c'
                                 )
        heading_label.pack(pady=25)

# ################################################################


        choose_amount_label= tk.Label(self,
                                  text='Enter the amount you would like',
                                  font=('orbitron',13),
                                  foreground='white',
                                  background='#3d3d5c'
                                  )
        choose_amount_label.pack()

        button_frame = tk.Frame(self,bg='#33334d')
        button_frame.pack(fill='both',expand=True)

        # def withdraw(amount):
        #     global current_balance
        #     current_balance -= amount
        #     controller.shared_data['Balance'].set(current_balance)
        #     controller.show_frame('MenuPage')

        cash = tk.StringVar()
        other_amount_entry = tk.Entry(button_frame,
                                      textvariable=cash,
                                      font=('orbitron',13),
                                      width=25,
                                      justify='right'
                                      )
        other_amount_entry.pack(pady=35,ipady=30)

        def other_amount(_):
            global current_balance
            current_balance -= int(cash.get())
            controller.shared_data['Balance'].set(current_balance)
            cash.set('')
            controller.show_frame('ApprovedPage')

        other_amount_entry.bind('<Return>',other_amount)


        # back -------------------------------

        button_frame = tk.Frame(self,
                                 bg='#33334d',
                                #  relief='raised',
                                 )
        button_frame.pack(fill='both')

        def withdraw_back():
            controller.show_frame('WithdrawPage')
            cash.set('')

        image = PhotoImage(file='./img/back.png')
        menu_button = tk.Button(button_frame,
                                image=image,
                                command=withdraw_back,
                                bg='#666699',
                                relief='raised',
                                borderwidth=0,  
                                # highlightthickness=0,
                                )
        menu_button.image = image
        menu_button.pack(anchor='se',pady=7,padx=7)
        
# #################################################################
        bottom_frame = tk.Frame(self,
                                 relief='raised',
                                 borderwidth=3
                                 )
        bottom_frame.pack(fill='x',side='bottom')

        # Cards_Photo
        visa_photo = tk.PhotoImage(file='./img/visa.png')
        visa_label = tk.Label(bottom_frame,
                              image=visa_photo
                              )
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='./img/mastercard.png')
        mastercard_label = tk.Label(bottom_frame,
                              image=mastercard_photo
                              )
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        meeza_photo = tk.PhotoImage(file='./img/meeza.png')
        meeza_label = tk.Label(bottom_frame,
                              image=meeza_photo
                              )
        meeza_label.pack(side='left')
        meeza_label.image = meeza_photo

        # time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()



class ApprovedPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,background='#3d3d5c')
        self.controller = controller

        heading_label = tk.Label(self,
                                 text='X-ATM',
                                 font=('orbitron',45,'bold'),
                                 foreground='white',
                                 background='#3d3d5c'
                                 )
        heading_label.pack(pady=25)


        approve_label= tk.Label(self,
                                  text='Transaction Approved',
                                  font=('orbitron',13),
                                  foreground='white',
                                  background='#3d3d5c'
                                  )
        approve_label.pack()

        button_frame = tk.Frame(self,
                                bg='#33334d'
                                )
        button_frame.pack(fill='both',expand=True)

        image = PhotoImage(file='./img/check.png')

        # Create a label and set the image
        image_label = tk.Label(button_frame, image=image,bg='#33334d')
        # Reference to prevent garbage collection
        image_label.image = image  
        # Place the label in the frame
        #  allows the label to expand to fill any extra space in the frame.
        image_label.pack(expand=True)
        #pack_propagate(False) prevents the frame from resizing to fit its contents, ensuring that the label remains centered
        image_label.pack_propagate(False)


        def continue_menu():
            controller.show_frame('MenuPage')
        continue_button = tk.Button(button_frame,
                                    text="Continue",
                                    command=continue_menu,
                                    relief='raised',
                                    borderwidth=3,
                                    background='#32df60',
                                    foreground='white',
                                    font=('orbitron',15),
                                    width=15,
                                    height=2,
                                    
                                    )
        continue_button.pack(side='right', padx=10, pady=15)

        def exit():
            controller.show_frame('StartPage')
        exit_button = tk.Button(button_frame,
                                    text="Exit",
                                    command=exit,
                                    relief='raised',
                                    borderwidth=3,
                                    bg='#f1426d',
                                    foreground='white',
                                    font=('orbitron',15),
                                    width=15,
                                    height=2,
                                    
                                    )
        exit_button.pack(side='left', padx=10, pady=15)




# #################################################################
        bottom_frame = tk.Frame(self,
                                 relief='raised',
                                 borderwidth=3
                                 )
        bottom_frame.pack(fill='x',side='bottom')

        # Cards_Photo
        visa_photo = tk.PhotoImage(file='./img/visa.png')
        visa_label = tk.Label(bottom_frame,
                              image=visa_photo
                              )
        visa_label.pack(side='left')
        visa_label.image = visa_photo

        mastercard_photo = tk.PhotoImage(file='./img/mastercard.png')
        mastercard_label = tk.Label(bottom_frame,
                              image=mastercard_photo
                              )
        mastercard_label.pack(side='left')
        mastercard_label.image = mastercard_photo

        meeza_photo = tk.PhotoImage(file='./img/meeza.png')
        meeza_label = tk.Label(bottom_frame,
                              image=meeza_photo
                              )
        meeza_label.pack(side='left')
        meeza_label.image = meeza_photo

        # time
        def tick():
            current_time = time.strftime('%I:%M %p').lstrip('0').replace(' 0',' ')
            time_label.config(text=current_time)
            time_label.after(200,tick)

        time_label = tk.Label(bottom_frame,font=('orbitron',12))
        time_label.pack(side='right')

        tick()


# ****************************************************************************************************************
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()