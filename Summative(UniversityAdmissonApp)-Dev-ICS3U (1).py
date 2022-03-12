"""
Author: Dev Jogalekar
Date of Last Update: 2022-01-28
Description: App that allows the user to choose a specific strand(out of 3) and enter thier grades,
and based on those grades the app can display what select univeresites you can(or can't) get into.

"""


# Import packages
import tkinter as tk
from tkinter import messagebox

#Declaring Strands for DropDown menu + subjects for those 3 strands
streams_options_list = ["Commerce", "Computer Science", "Engineering"]
cs_subject_list=["Adv Functions", "Calculus", "English","Subject4","Subject5","Subject6"]
bus_subject_list=["Adv Functions","English","Subject3","Subject4","Subject5","Subject6"]
engineering_subject_list=["English","Calculus","Chemistry","Physics","Adv Functions","Subject6"]


def show_subjects(choice):
     #Checking what choice from dropdown menu was and making labels accordingly(the label names come from the list relating to the strand)   
    if choice == "Commerce":
        ResultFrame.pack_forget()
        for i in range(6):
           eval('entry_sub'+str(i) + '.delete(0,tk.END)')
        for i in range(len(bus_subject_list)):
            eval('label_sub'+str(i)+'.config(text=bus_subject_list['+str(i)+'])')
    elif choice == "Computer Science":
        ResultFrame.pack_forget()
        for i in range(6):
           eval('entry_sub'+str(i) + '.delete(0,tk.END)')
        for i in range(len(cs_subject_list)):
            eval('label_sub'+str(i)+'.config(text=cs_subject_list['+str(i)+'])')         
    elif choice == "Engineering":
        ResultFrame.pack_forget()
        for i in range(6):
           eval('entry_sub'+str(i) + '.delete(0,tk.END)')
        for i in range(len(engineering_subject_list)):
            eval('label_sub'+str(i)+'.config(text=engineering_subject_list['+str(i)+'])')
    # show frame
    subFormFrame.pack()

# function to check the input of the user(from the stored entrybox value)

def validate_input():
    userinput = []
    for i in range(6):
        #.eval gets the value on the fly; ie instead of writing _value.get() for the 6 entries on 6 lines, I can write it on one
        userval =  eval('sub'+str(i) + '_value.get()')
        try:
            x = int(userval)
            if x >= 0 and x <= 100:
                userinput.append("true")
            else:
                userinput.append("false")
        except:
            userinput.append("false")
    #
    counter = userinput.count("true")
    if counter == 6:
        return True
    else:
        return False


#Function to show what universities you can go to
def show_results():
  if validate_input() == True:
        
    def check_results():
       #Creating Global Variables(the "Sum" of all the entries)
       global Cs_Total
       Cs_Total = 0
       global Bus_Total
       Bus_Total = 0
       global Eng_Total
       Eng_Total = 0
       
       #Creating subjects_list
       global subjects_list
       subjects_list = []
       
       #Creating Local Variables that are going to be used as "return" values
       All_Three = "All_Three"
       Bus_0 = "Bus_0"
       Bus_1 = "Bus_1"
       Bus_2 = "Bus_2"
       Bus_Math = "Bus_Math"
       Bus_All_Three = "Bus_All_Three"
       Eng_False = "Eng_False"
       Eng_True = "Eng_True"
           
       #Checking what option from drop down menu
       
       if option_value.get() == "Computer Science":
         
            for j in range(6):
                #Evaluting all the values from the entry values
                    test =  eval('sub'+str(j) + '_value.get()')
                    test = int(test)
                    Cs_Total+=test
                    subjects_list.append(test)
                    
                    #Once all the values have been appended to the list; check them to see if they're 0 or not
                    #return stuff from this function based on that
    
            if subjects_list[0] == 0 or subjects_list[1] == 0:
                return False
            elif subjects_list[2] == 0:
                return True
            else:
                return All_Three
            #
       elif option_value.get() == "Commerce":
            for j in range(6):
                test = eval('sub'+str(j) + '_value.get()')
                test = int(test)
                Bus_Total += test
                subjects_list.append(test)
                
            if subjects_list[0] == 0 or subjects_list[1] == 0:
                return Bus_0
            #Here's a special case where certain entries HAVE to be above 60, so checking for that here
            elif (0<subjects_list[0]<60 and 0<subjects_list[1]<60) or 0<subjects_list[1]<60:
                return Bus_1
            elif 0<subjects_list[0]<60:
                return Bus_Math
            else:
                return Bus_All_Three
            
       elif option_value.get() == "Engineering":
             for j in range(6):
                test = eval('sub'+str(j) + '_value.get()')
                test = int(test)
                Eng_Total += test
                subjects_list.append(test)
                
             if subjects_list[0] == 0 or subjects_list[1] == 0 or subjects_list[2] == 0 or subjects_list[3] == 0 or subjects_list[4] == 0:
                return Eng_False
             else:
                return Eng_True
 
    #Check what the above function returned and start making corresponding labels to it         
    if check_results() == False:
       lbl_1.config(text="You can not get into Carleton U, OttawaU, Waterloo because you did not take "+ cs_subject_list[0] + " or " + cs_subject_list[1])
       lbl_2.config(text="  ")
       lbl_3.config(text = "  ")
       
    elif check_results() == True:
        #Here, it checks the average of only 5 subjects because the user entered a 0 for English
        if Cs_Total//5 < 85:
            lbl_1.config(text="You can not get into to Carleton U, OttawaU, Waterloo!")
            lbl_2.config(text="Your Average: " + str(Cs_Total//5))
            lbl3.config(text="Required Average for CareltonU(85),OttawaU(87) and Waterloo(95)")
        elif Cs_Total//5 >= 85:
            lbl_1.config(text="You can get into Carelton U, but you can not get into Waterloo or OttawaU because you did not take "+ cs_subject_list[2])
            lbl_2.config(text="Your Average: " + str(Cs_Total//5))
            lbl_3.config(text="Required Average for CareltonU(85),OttawaU(87) and Waterloo(95)")
            
    elif check_results() == "All_Three":
        #Checks the average, and then tells you what universities you can go to
        Cs_Average = (Cs_Total)//6
        if Cs_Average < 85:
            lbl_1.config(text="You can not get into Carelton U, OttawaU, Waterloo")
            lbl_2.config(text="Your Average: " + str(Cs_Average))
            lbl_3.config(text="Required Average for CareltonU(85),OttawaU(87) and Waterloo(95)")
        elif Cs_Average >=85 and Cs_Average < 87:
            lbl_1.config(text="You can get into Carleton, but not Waterloo and OttawaU")
            lbl_2.config(text="Your Average: " + str(Cs_Average))
            lbl_3.config(text="Required Average for CareltonU(85),OttawaU(87) and Waterloo(95)")
        elif Cs_Average >=87 and Cs_Average < 95:
            lbl_1.config(text="You can get into Carleton and OttawaU, but not Waterloo")
            lbl_2.config(text="Your Average: " + str(Cs_Average))
            lbl_3.config(text="Required Average for CareltonU(85),OttawaU(87) and Waterloo(95)")
        elif Cs_Average >= 95:
            lbl_1.config(text="You can get into Carleton,OttawaU and Waterloo!")
            lbl_2.config(text="Your Average: " + str(Cs_Average))
            lbl_3.config(text="Required Average for CareltonU(85),OttawaU(87) and Waterloo(95)")
            
    #Same Concept as above        
    elif check_results() == "Bus_0":
        lbl_1.config(text="You can not get into TrentU,Ontario Tech and UoT because you did not take\n "+ bus_subject_list[0] + " and/or " + bus_subject_list[1])
        lbl_2.config(text="  ")
        lbl_3.config(text="   ")
    elif check_results() == "Bus_1":
        lbl_1.config(text="You can not get into Ontario Tech,TrentU or UoT because your mark in \n" + bus_subject_list[0] + " and/or " + bus_subject_list[1] + " is below a 60")
        lbl_2.config(text="  ")
        lbl_3.config(text="   ")   
    elif check_results() == "Bus_Math":
        #Checking Average
        Bus_Average = (Bus_Total)//6
        if Bus_Average < 70:
            lbl_1.config(text="You can not get into Trent,UoT or Ontario Tech")
            lbl_2.config(text="Your Average: " + str(Bus_Average))
            lbl_3.config(text="Required Average for Trent(70),Ontario Tech(82) and UoT(89)")
        if Bus_Average>= 70 and Bus_Average<89:
            lbl_1.config(text="You can get into to TrentU")
            lbl_2.config(text="Your Average: " + str(Bus_Average))
            lbl_3.config(text="Required Average for Trent(70) and UoT(89)")
        elif Bus_Average >= 89:
            lbl_1.config(text="You can get into Trent and UoT")
            lbl_2.config(text="Your average: " + str(Bus_Average))
            lbl_3.config(text="Required Average for Trent(70) and UoT(89)")

    elif check_results() == "Bus_All_Three":
         Bus_Average = (Bus_Total)//6
         if Bus_Average < 70:
            lbl_1.config(text="You can not get into Trent,Ontario Tech and UoT")
            lbl_2.config(text="Your Average: " + str(Bus_Average))
            lbl_3.config(text="Required Average for Trent(70),Ontario Tech(82) and UoT(89)")
         elif Bus_Average >= 70 and Bus_Average <82:
             lbl_1.config(text="You can get into Trent, but not Ontario Tech and UoT")
             lbl_2.config(text="Your Average: " + str(Bus_Average))
             lbl_3.config(text="Required Average for Trent(70),Ontario Tech(82) and UoT(89)")
         elif Bus_Average >= 82 and Bus_Average < 89:
             lbl_1.config(text="You can get into Trent and Ontario Tech,but not UoT")
             lbl_2.config(text="Your Average: " + str(Bus_Average))
             lbl_3.config(text="Required Average for Trent(70),Ontario Tech(82) and UoT(89)")
         else:
             lbl_1.config(text="You can get into Trent, Ontario Tech and UoT")
             lbl_2.config(text="Your Average: " + str(Bus_Average))
             lbl_3.config(text="Required Average for Trent(70),Ontario Tech(82) and UoT(89)")
        
    elif check_results() == "Eng_False":
        lbl_1.config(text="You can't get into any unis because you did not take one of " + engineering_subject_list[0] + " , " + engineering_subject_list[1] + "\n" + engineering_subject_list[2] + " , " + engineering_subject_list[3] + " or " + engineering_subject_list[4])
        lbl_2.config(text="")           
        lbl_3.config(text="")
    else:
        Eng_Average = Eng_Total//6
        if Eng_Average < 74:
            lbl_1.config(text="You can not get into Windsor,Ryerson or UoT")
            lbl_2.config(text="Your Average: " + str(Eng_Average))
            lbl_3.config(text="Required Average for Windsor(74),Ryerson(80) and UoT(86)")
        elif Eng_Average >= 74 and Eng_Average <80:
            lbl_1.config(text="You can get into Windsor, but not Ryerson or UoT")
            lbl_2.config(text="Your Average: " + str(Eng_Average))
            lbl_3.config(text="Required Average for Windsor(74),Ryerson(80) and UoT(86)")
        elif Eng_Average >= 80 and Eng_Average < 86:
            lbl_1.config(text="You can get into Windsor and Ryerson, but not UoT")
            lbl_2.config(text="Your Average: " + str(Eng_Average))
            lbl_3.config(text="Required Average for Windsor(74),Ryerson(80) and UoT(86)")
        elif Eng_Average >= 86:
            lbl_1.config(text="You can get into Windsor,UoT and Ryerson")
            lbl_2.config(text="Your Average: " + str(Eng_Average))
            lbl_3.config(text="Required Average for Windsor(74),Ryerson(80) and UoT(86)")
    #Unhiding frame and showing everything on the new Frame        
    ResultFrame.pack()
    
    
  else:
      #If entry value is not an integer, make an Error box + delete all entries
      tk.messagebox.showerror(title='Error',message='     Invalid data entry     ')
      for i in range(6):
           eval('entry_sub'+str(i) + '.delete(0,tk.END)')
      ResultFrame.pack_forget()
      lbl_1.config(text="")
      lbl_2.config(text="")
      lbl_3.config(text="")
          
    
#main window
window = tk.Tk()
window.title("Welcome to University app")

#Set Size of Window
scr_w = window.winfo_screenwidth()
scr_h = window.winfo_screenheight()
win_w = round(int(scr_w)/2)
win_h = round(int(scr_h)/2)
center_x = int(scr_w/2 - win_w/2)
center_y = int(scr_h/2 - win_h/2)

window.geometry(f'{win_w}x{win_h}+{center_x}+{center_y}')
#window.state('zoomed')

#Make a Frame, and put Labels and Pictures on it
topFrame = tk.Frame(window, borderwidth=3, relief = tk.RIDGE)
topFrame.pack(side = tk.TOP)

tk.Label(topFrame, text = 'Welcome to LDHSS!', font = ("Arial", 25)).pack()

logo = tk.PhotoImage(file = r"c:\Temp\LDHSS_TenthAnniversary-CircleWeb.png")
logo_cropped = logo.subsample(2,2)
tk.Label(topFrame, image = logo_cropped).pack() 

tk.Label(topFrame, text = "Select your application stream").pack(side = tk.LEFT)

#Creating a DropDown menu
option_value = tk.StringVar()
option_value.set("Select an option")
dropdown_list = tk.OptionMenu(topFrame, option_value, *streams_options_list, command=show_subjects)
dropdown_list.pack(side = tk.LEFT)

tk.Label(topFrame, text = "   ").pack(side = tk.LEFT)
tk.Button(topFrame, text = "Exit", command = window.destroy).pack(side=tk.RIGHT)

# Creating Form Frame
subFormFrame = tk.Frame (window, borderwidth=2, relief = tk.GROOVE)
subFormFrame.pack()

#Making Labels+Entry Boxes to put on this Frame
info_label = tk.Label(subFormFrame,text="Please enter a 0 if you have not taken 1 of the mandatory subjects").grid(row = 0, column = 0, columnspan = 5)

label_sub0 = tk.Label(subFormFrame, text = "subject1")
label_sub0.grid(column = 0, row = 1, ipadx = 5, ipady = 2, sticky= tk.E)
#Storing the Entry Value as a StringVar
sub0_value = tk.StringVar()
entry_sub0 = tk.Entry(subFormFrame, textvariable=sub0_value)
entry_sub0.grid(column = 1, row = 1, ipadx = 2, ipady = 2)


label_sub1 = tk.Label(subFormFrame, text = "subject2")
label_sub1.grid(column = 0, row = 2, ipadx = 5, ipady = 2, sticky = tk.E)
sub1_value = tk.StringVar()
entry_sub1 = tk.Entry(subFormFrame, textvariable=sub1_value)
entry_sub1.grid(column = 1, row = 2, ipadx = 2, ipady = 2)

label_sub2 = tk.Label(subFormFrame, text = "subject3")
label_sub2.grid(column = 0, row = 3, ipadx = 5, ipady = 2, sticky = tk.E)
sub2_value = tk.StringVar()
entry_sub2 = tk.Entry(subFormFrame, textvariable=sub2_value)
entry_sub2.grid(column = 1, row = 3, ipadx = 2, ipady = 2)

label_sub3 = tk.Label(subFormFrame, text = "subject 4")
label_sub3.grid(column = 3, row = 1, ipadx = 5, ipady = 2, sticky = tk.E)
sub3_value = tk.StringVar()
entry_sub3 = tk.Entry(subFormFrame, textvariable=sub3_value)
entry_sub3.grid(column = 4, row = 1, ipadx = 2, ipady = 2)

label_sub4 = tk.Label(subFormFrame, text = "subject 5")
label_sub4.grid(column = 3, row = 2, ipadx = 5, ipady = 2, sticky = tk.E)
sub4_value = tk.StringVar()
entry_sub4 = tk.Entry(subFormFrame, textvariable=sub4_value)
entry_sub4.grid(column = 4, row = 2, ipadx = 2, ipady = 2)

label_sub5 = tk.Label(subFormFrame, text = "subject 6")
label_sub5.grid(column = 3, row = 3, ipadx = 5, ipady = 2, sticky = tk.E)
sub5_value = tk.StringVar()
entry_sub5 = tk.Entry(subFormFrame, textvariable=sub5_value)
entry_sub5.grid(column = 4, row = 3, ipadx = 2, ipady = 2)

tk.Label(subFormFrame, text = "    ").grid(column = 2, row = 1, ipadx = 5)
tk.Label(subFormFrame, text = "    ").grid(column = 2, row = 2, ipadx = 5)
tk.Label(subFormFrame, text = "    ").grid(column = 2, row = 3, ipadx = 5)
#Making a Button on this frame that has cmd show_results()
tk.Button(subFormFrame, text = "Where can I apply?", command = show_results).grid(row = 4, column = 0, columnspan = 5)

# results output frame
ResultFrame = tk.Frame (window,borderwidth=2,relief=tk.RIDGE)
ResultFrame.pack()

lbl_1 = tk.Label(ResultFrame, text = "  ",font=("Arial",11))
lbl_1.pack()
lbl_2 = tk.Label(ResultFrame,text="  ",font=("Arial",11))
lbl_2.pack()
lbl_3 = tk.Label(ResultFrame,text="   ",font=("Arial",11))
lbl_3.pack()

#Hide both of the frames
subFormFrame.pack_forget()
ResultFrame.pack_forget()

#run app mainloop
window.mainloop()