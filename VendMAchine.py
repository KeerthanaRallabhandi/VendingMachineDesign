'''
Assignment 2 -  Design of Vending MAchine using Python

steps for the design of vending machine
1. creating a tKinter master window for creating the gui
2. adding the buttons of the items for the user preference selection
3. creating an inventory stock csv acting as a database for items being displayed
4. creating an add to cart for multiple item selection
5. Displaying the out of stock message in case of the item is on short from the inventory
6. checkout of the cart using the Total bill button to display the total amount and accept the cash from the user
7. In case of Cash submit
    -- if exact total/extra amount  given by user then display of appropriate message with/without change to be returned
'''
'''
1. Necessary modules importing for creating the GUI 
2. reading the inventory stock list for the items through dataframe module
'''
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import pandas as pd

ADD_CART = 0
clear_widget_list = []  # Manitaining a list of all the Widgets that need to be cleared before drawing new widget

Inventory_Stock = pd.read_csv('InventoryStock.csv')  # acting as a simulation database because for ease purpose

class vend_machine:
    # creating tk master window
    # creating a frame of specific style and size inside the master window and creating the grid
    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(70 * blank_space + "Vending Machine")
        self.root.geometry("625x355+300+100")
        self.root.configure(bg='#DCDCDC')
        self.frame = Frame(self.root, border=10, width=500, height=500, relief=GROOVE)
        self.frame.grid()

        self.main_frame()
        self.inventory = update_inventory_vm()

    '''
    1. creating sideframes inside the frame with grid positions
    2. creating buttons for representing each item in the sideframes
    3. attaching a button listener to each button -- buttonClick function acting as a lisener to the button    
    '''

    def main_frame(self):
        # creating items icon button frame
        side_frame1 = Frame(self.frame, bg='#808080', bd=2, width=600, height=150, relief=FLAT)
        side_frame1.grid(row=0, column=0, padx=12)
        self.img_sideframe_top = ImageTk.PhotoImage(Image.open("cockie.JPG"))
        self.button = Button(side_frame1, width=80, height=70, state=NORMAL,
                             image=self.img_sideframe_top, command=lambda *args: self.buttonClick("Cockie")).grid(row=0, column=0, padx=2, pady=4)
        self.img_sideframe_top1 = ImageTk.PhotoImage(Image.open("dairymilk.JPG"))
        self.button1 = Button(side_frame1, width=80, height=70, relief=RAISED, state=NORMAL,
                              image=self.img_sideframe_top1, command=lambda *args: self.buttonClick("Dairymilk")).grid(row=0, column=1, padx=2, pady=4)
        self.img_sideframe_top2 = ImageTk.PhotoImage(Image.open("coke.JPG"))
        self.button2 = Button(side_frame1, width=80, height=70, state=NORMAL,
                              image=self.img_sideframe_top2, command=lambda *args: self.buttonClick("Coke")).grid(row=0, column=2, padx=2, pady=4)
        self.img_sideframe_top3 = ImageTk.PhotoImage(Image.open("gems.JPG"))
        self.button3 = Button(side_frame1, width=80, height=70, state=NORMAL,
                              image=self.img_sideframe_top3, command=lambda *args: self.buttonClick("Gems")).grid(row=0, column=3, padx=2, pady=4)
        self.img_sideframe_top4 = ImageTk.PhotoImage(Image.open("kitkat.JPG"))
        self.button4 = Button(side_frame1, text="Kitkat", width=80, height=70, state=NORMAL,
                              image=self.img_sideframe_top4, command=lambda *args: self.buttonClick("Kitkat")).grid(row=0, column=4, padx=2, pady=4)

        side_frame2 = Frame(self.frame, bg='#808080', bd=5, width=600, height=150, relief=FLAT)
        side_frame2.grid(row=2, column=0, padx=12)
        self.img_sideframe_bottom5 = ImageTk.PhotoImage(Image.open("lays.JPG"))
        self.button5 = Button(side_frame2, width=80, height=70, state=NORMAL,
                              image=self.img_sideframe_bottom5, command=lambda *args: self.buttonClick("Lays")).grid(row=2, column=0, padx=2, pady=4)
        self.img_sideframe_bottom6 = ImageTk.PhotoImage(Image.open("namkeen.JPG"))
        self.button6 = Button(side_frame2, width=80, height=70, state=NORMAL,
                              image=self.img_sideframe_bottom6, command=lambda *args: self.buttonClick("Namkeen")).grid(row=2, column=1, padx=2, pady=4)
        self.img_sideframe_bottom7 = ImageTk.PhotoImage(Image.open("shots.JPG"))
        self.button7 = Button(side_frame2, width=80, height=70, state=NORMAL,
                              image=self.img_sideframe_bottom7, command=lambda *args: self.buttonClick("Shots")).grid(row=2, column=2, padx=2, pady=4)
        self.img_sideframe_bottom8 = ImageTk.PhotoImage(Image.open("w.JPG"))
        self.button8 = Button(side_frame2, width=80, height=70, state=NORMAL,
                              image=self.img_sideframe_bottom8,
                              command=lambda *args: self.buttonClick("WaterBottle")).grid(row=2, column=3, padx=2, pady=4)
        self.img_sideframe_bottom9 = ImageTk.PhotoImage(Image.open("doritos.JPG"))
        self.button9 = Button(side_frame2, width=80, height=70, state=NORMAL,
                              image=self.img_sideframe_bottom9, command=lambda *args: self.buttonClick("Doritos")).grid(row=2, column=4, padx=2, pady=4)

        self.side_frame2_mid = Frame(self.frame, bd=5, width=600, height=150, relief=RIDGE)

        ''' Item listener, called on every click to the item displayed in the frame!!
        1. button click is a listener which is called every time when a button is clicked
        2. this allows the user to enter the quantity of the item being selected 
        3. clicking on the add button to add the item to the total cart price -- where the add_to_cart function is listener for the add button
        4. user can select multiple items and enter the quantity of each item being added to the cart 
        5. clicking total_bill button for checking and displaying the total price of the transaction -- tot_bill_window function is the listener for the tot_bill button

        '''

    def buttonClick(self, name="dummy"):
        print("Entered button listener...")
        for wid in clear_widget_list:
            self.clear_frame(wid)

        self.side_frame2_mid = Frame(self.frame, bd=5, width=600, height=150, relief=RIDGE)
        self.side_frame2_mid.grid(row=1, column=0, padx=2)
        clear_widget_list.append(self.side_frame2_mid)

        self.quantity = Label(self.side_frame2_mid, text="Quantity").place(x=40, y=60)
        self.quantity_area = Entry(self.side_frame2_mid)
        self.quantity_area.place(x=100, y=60)

        self.button10 = Button(self.side_frame2_mid, width=10, height=2, state=NORMAL, text="Add",
                               command=lambda *args: self.add_to_cart(name)).place(x=400, y=60)
        self.button11 = Button(self.side_frame2_mid, width=10, height=2, state=NORMAL, text="Tot Bill",
                               command=lambda *args: self.tot_bill_window(ADD_CART)).place(x=400, y=100)

        display_cart_value_label = Label(self.side_frame2_mid, text=ADD_CART, font=("Arial", 9))
        display_cart_value_label.place(x=150, y=100)
        display_cart_label = Label(self.side_frame2_mid, text="CART PRICE=", font=("Arial", 9))
        display_cart_label.place(x=40, y=100)
        clear_widget_list.append(display_cart_label)
        clear_widget_list.append(display_cart_value_label)

        '''
        1. checks wether the item is present in the inventory -- "InStock" tells the item count in the inventory
        2. If item present then adds the items price(Quantity * price of selected item) into the cart and deducts the Item quantity from the inventory stock
        3. else displays "OUT OF STOCK" message on the frame
        4. Displays the Price being added into the cart at the bottom of the Frame and updates the item count in the inventory stock      
        '''

    def add_to_cart(self,name="dummy"):
        global ADD_CART
        qty_area = int(self.quantity_area.get())
        item_price = 0

        for row, stock in Inventory_Stock.iterrows():
            if stock['Item'] == name:
                print("Found Item - ", name)
                tot_qty = stock["InStock"] - qty_area
                if tot_qty < 0:
                    widget = self.Display_popup(self.side_frame2_mid, "OUT OF STOCK")
                    clear_widget_list.append(widget)
                    self.inventory.inventory_update(name)
                    return
                else:
                    item_price = stock['Amount']
                    print("Item price...", item_price)
                    ADD_CART = ADD_CART + (qty_area * item_price)
                    print("Added to cart...", ADD_CART)
                    Inventory_Stock.loc[row, ["InStock"]] = tot_qty

        display_cart_value_label = Label(self.side_frame2_mid, text=ADD_CART, font=("Arial", 9))
        display_cart_value_label.place(x=150, y=100)
        display_cart_label = Label(self.side_frame2_mid, text="CART PRICE =", font=("Arial", 9))
        display_cart_label.place(x=40, y=100)
        clear_widget_list.append(display_cart_label)
        clear_widget_list.append(display_cart_value_label)
        print(Inventory_Stock)
        Inventory_Stock.to_csv(r'InventoryStock.csv')

    '''
    1. Displays the total amt to be paid by the customer 
    2. provides an input for the customer to submit the cash(simulation) 
    3. Submit button checks wether the customer has given the rite amount of cash -- accept_cash function is the button listener 
                                                                which checks the total amt against the amt provided by the customer 
    4. After submission press the clear button to clear the cart and selection --  clear function is the button listener   
    '''

    def tot_bill_window(self, tot_amt):
        print("Entered total bill window.......")
        print("Total amount is - ", tot_amt)

        for wid in clear_widget_list:
            self.clear_frame(wid)

        self.side_frame3_mid = Frame(self.frame, bd=5, width=600, height=150, relief=RIDGE)
        self.side_frame3_mid.grid(row=1, column=0, padx=2)

        self.total_amt_lab = Label(self.side_frame3_mid, text="Pay amount =", font=("Arial", 18)).place(x=40, y=20)
        self.total_amt = Label(self.side_frame3_mid, text=tot_amt, font=("Arial", 18)).place(x=250, y=18)
        self.cash = Label(self.side_frame3_mid, text="Enter Cash").place(x=40, y=60)
        self.cash_amt = Entry(self.side_frame3_mid)
        self.cash_amt.place(x=130, y=60)

        for wid in clear_widget_list:
            self.clear_frame(wid)

        self.button12 = Button(self.side_frame3_mid, width=10, height=2, state=NORMAL, text="Submit",
                               command=self.accept_cash).place(x=400, y=60)

        self.button13 = Button(self.side_frame3_mid, width=10, height=2, state=NORMAL, text="Clear",
                               command=self.clear).place(x=400, y=100)

    '''
    1. Checks the cash submitted by the customer against the total bill 
    2. if customer has provided the exact amt displays thank you message 
    3. else customer provides less than the billed amt displays "Please give exact amount or greater" 
    4. else in case of extra amt than the toal billed price then displays "Please collect change {0}!! Thank you!!!!"
    '''

    def accept_cash(self):
        print("Entered accept cash......")
        cash = int(self.cash_amt.get())
        print("Accepted cash - ", cash)

        return_amt_str = ""

        bal_amt = cash - ADD_CART
        if bal_amt == 0:
            return_amt_str = r"{0}!!".format("Thank you!")
        elif bal_amt < 0:
            return_amt_str = r"{0}!!".format("Please give exact amount or greater")
        else:
            return_amt_str = r"Please collect change {0}!! Thank you!!!!".format(bal_amt)

        for wid in clear_widget_list:
            self.clear_frame(wid)

        Payment_note = Label(self.side_frame3_mid, text=return_amt_str, font=("Arial", 15))
        Payment_note.place(x=40, y=100)
        clear_widget_list.append(Payment_note)

    '''Removes the widgets from the clear widgets list and destroys the widget'''

    def clear_frame(self, widget):
        clear_widget_list.remove(widget)
        if widget != None:
            widget.destroy()

    def Display_popup(self, frame, disp_text):
        print("Entered button listener...")
        label1 = Label(frame, text=disp_text, font=("Arial", 18))
        label1.pack()
        return label1

    '''Function called at the end to clear all the widgets and make the cart empty/zero'''

    def clear(self):
        global ADD_CART
        for widgets in self.frame.winfo_children():
            widgets.destroy()

        ADD_CART = 0
        clear_widget_list.clear()
        self.main_frame()  # calling in the main frame for fresh/new selection


'''Class representing the inventory stock for to have a check on the emptied items and refill the item '''


class update_inventory_vm:

    def inventory_update(self, item_name):
        global Inventory_Stock
        read_original_values_of_actual_file = pd.read_csv(r"InventoryStock_backup.csv")
        for row1, stock1 in read_original_values_of_actual_file.iterrows():
            if stock1['Item'] == item_name:
                Inventory_Stock.loc[row1, ["InStock"]] = stock1["InStock"]
        Inventory_Stock.to_csv(r"InventoryStock.csv")


if __name__ == '__main__':
    root = Tk()  # creating the object of the tkinter container box
    application = vend_machine(
        root)  # passing the object to the vending machine init function who is then defining the dimnesion of the window/container creating all the buttons
    root.mainloop()  # will draw it on the screen displaying the tk gui window
