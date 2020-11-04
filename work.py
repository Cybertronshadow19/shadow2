from tkinter import *
from datetime import datetime
from tkinter import messagebox
import os
import shutil
import fnmatch

#Configuring the interface
root=Tk()
root.title("LOGIN PAGE")
root.configure()
root.geometry("700x700")




#Declaring some valiables
d = datetime(1,1,1).now()
Formating_time=('{}:{:02d} {}/{}/{}'.format(d.hour,d.minute,d.month,d.day,d.year))
uname='shadow'
passwr='shadow'

#The Title part
Title=Label(text="LOGIN PAGE",font=('arial',80,'bold'),bd=1,fg='red',justify=CENTER)
Title.grid(row=0,column=0,columnspan=2)

#Defining function for our buttons
def login():
    global Password_entry
    Uname=Username_entry.get()
    Upass=Password_entry.get()
    if Uname==uname and Upass==passwr:
        messagebox.showinfo("SHADOW","LOGIN SUCCESFUL")
        window = Toplevel()
        Password_entry.delete(0,END)
        window.title("Shadow system")
        window.geometry("750x750")
        window_Title_label = Label(window, text="SHADOW SYSTEM", fg="red",font=("ariana", 53, "bold"), justify=CENTER)
        window_Title_label.grid(row=0, column=0,columnspan=3,pady=10,padx=10)
        window_enter_folder_label=Label(window,text="Input The Directory To Open",fg="blue",font=("ariana",20,"bold"),justify=CENTER)
        window_enter_folder_label.grid(row=1,column=1,pady=15,padx=15)
        window_example_label=Label(window,text="EXAMPLE:: /home/netshadow/Documents",fg="orange",font=("ariana",10),justify=CENTER)
        window_example_label.grid(row=2,column=1)
        window_folder_entry=Entry(window,width=45,justify=CENTER,bg="blue",bd=4,borderwidth=5)
        window_folder_entry.grid(row=3,column=1)
        window_enter_files_label=Label(window,text="Input File To Use",fg="blue",font=("ariana",20,"bold"),justify=CENTER)
        window_enter_files_label.grid(row=4,column=1,pady=15,padx=15)
        window_example_label = Label(window, text="EXAMPLE:: music", fg="orange",font=("ariana", 10), justify=CENTER)
        window_example_label.grid(row=5, column=1)
        window_file_entry = Entry(window, width=20, justify=CENTER, bg="blue", bd=4, borderwidth=5)
        window_file_entry.grid(row=6, column=1)
        window_destination_folder_label=Label(window,text="Input The Destination Directory",fg="blue",font=("ariana",20,"bold"),justify=CENTER)
        window_destination_folder_label.grid(row=7,column=1,pady=15,padx=15)
        window_destination_folder_entry = Entry(window, width=45, justify=CENTER, bg="blue", bd=4, borderwidth=5)
        window_destination_folder_entry.grid(row=8, column=1,pady=15,padx=15)

        window_display_text_area=Text(window, width = 46, height = 6, bg="white",fg="blue", bd=4,font=('arial',10,'italic'))
        window_display_text_area.grid(row=14,column=1)
        window_display_text_area.insert(END, "shadow tech ::                   eduhshadow@gmail.com")

        ###defining functions of buttons
        def submit_entry():
            global folder
            global user_file
            global destination_folder

            destination_folder=window_destination_folder_entry.get()
            folder=window_folder_entry.get()
            user_file=window_file_entry.get()
            user_input_dispaly=Label(window,text="Source directory:>>   " + folder + " " + "::           " + " Selected file >>" + user_file)
            user_input_dispaly.grid(row=9,column=1)
            user_input_dispaly.update()
            user_input_dispaly2 = Label(window, text="Destination directory:>>     " + destination_folder)
            user_input_dispaly2.grid(row=10, column=1)
            user_input_dispaly2.update()
            try:
                if folder== "" or destination_folder=="" or user_file=="":
                    error = Label(window,text=" Invalid selection of directory",bg="yellow",fg="red",justify=CENTER,font=("ariana",10,"bold"))
                    error.grid(row=12, column=1)
            except IOError:
                window.update()

        def move_action():
         try :
                working_directory=folder
                files=os.listdir(working_directory)
                destination_directory=destination_folder
                window_display_text_area.insert(END,"\nmoving        " + user_file + "        ###############")
                for f in files:
                    if user_file == "pictures":
                        if fnmatch.fnmatch(f, "*.png") or fnmatch.fnmatch(f, "*.gif") or fnmatch.fnmatch(f,"*.jpg") or fnmatch.fnmatch(f, "*.jpeg") or fnmatch.fnmatch(f, "*.com") or fnmatch.fnmatch(f, "*.icon"):
                            pics = os.path.join(working_directory, f)
                            shutil.move(pics, destination_directory)
                    elif user_file == "music":
                        if fnmatch.fnmatch(f, "*.mp3"):
                            mmusic = os.path.join(working_directory, f)
                            shutil.move(mmusic, destination_directory)
                    elif user_file == "videos":
                        if fnmatch.fnmatch(f,"*.mp4"):
                            video=os.path.join(working_directory, f)
                            shutil.move(video,destination_directory)
                    elif user_file == "documents":
                        if fnmatch.fnmatch(f, "*.odt") or fnmatch.fnmatch(f, "*.doc") or fnmatch.fnmatch(f,"*.txt") or fnmatch.fnmatch(f, "*.pdf") or fnmatch.fnmatch(f,"*.toc") or fnmatch.fnmatch(f,"*.spec") or fnmatch.fnmatch(f, "*.odp") or fnmatch.fnmatch(f, "*.pptx") or fnmatch.fnmatch(f, "*.docx"):
                            docs=os.path.join(working_directory, f)
                            shutil.move(docs, destination_directory)
                    elif user_file == "programs":
                        if fnmatch.fnmatch(f, "*.py") or fnmatch.fnmatch(f,"*.sqlite") or fnmatch.fnmatch(f, "*.html") or fnmatch.fnmatch(f, "*.pkt") or fnmatch.fnmatch(f, "*.js") or fnmatch.fnmatch(f, "*.json"):
                            prog=os.path.join(working_directory, f)
                            shutil.move(prog, destination_directory)
                    elif user_file == "application":
                        if fnmatch.fnmatch(f,"*.exe") or fnmatch.fnmatch(f,"*.debian.tar.tx") or fnmatch.fnmatch(f,"*.debian.tar.gz") or fnmatch.fnmatch(f,"*.tar") or fnmatch.fnmatch(f,"*.deb") or fnmatch.fnmatch(f,"*.zip") or fnmatch.fnmatch(f,"*.pkg") or fnmatch.fnmatch(f,"*.tar.tx") or fnmatch.fnmatch(f,"*.tar.gz") or fnmatch.fnmatch(f,"*.run") or fnmatch.fnmatch(f,"*.budle") or fnmatch.fnmatch(f,"*.msi") :
                            apps=os.path.join(working_directory, f)
                            shutil.move(apps,destination_directory)
                window_display_text_area.insert(END, "\nmoving        " + user_file + "        succesful")

         except IOError:
             error_label = Label(window,text="You have an error in your input:::\n for files(one at a time) :application:music:documents:programs:music:videos:pictures",bg="cadet blue",fg="red",font=("ariana",10),justify=CENTER)
             error_label.grid(row=13, column=1)
        def copy_action():

            try :
                working_directory = folder
                destination_directory = destination_folder
                files = os.listdir(working_directory)

                window_display_text_area.insert(END, "\ncopying        " + user_file+ "        ##############")
                for f in files:
                    if user_file == "pictures":
                        if fnmatch.fnmatch(f, "*.png") or fnmatch.fnmatch(f, "*.gif") or fnmatch.fnmatch(f, "*.jpg") or fnmatch.fnmatch(f, "*.jpeg"):
                            pics = os.path.join(working_directory, f)
                            shutil.copy(pics, destination_directory)
                    elif user_file == "music":
                        if fnmatch.fnmatch(f, "*.mp3"):
                            mmusic = os.path.join(working_directory, f)
                            shutil.copy(mmusic, destination_directory)
                    elif user_file == "videos":
                        if fnmatch.fnmatch(f,"*.mp4"):
                            video=os.path.join(working_directory, f)
                            shutil.copy(video,destination_directory)
                    elif user_file == "documents":
                        if fnmatch.fnmatch(f, "*.odt") or fnmatch.fnmatch(f, "*.doc") or fnmatch.fnmatch(f,"*.txt") or fnmatch.fnmatch(f, "*.pdf") or fnmatch.fnmatch(f,"*.toc") or fnmatch.fnmatch(f,"*.spec") or fnmatch.fnmatch(f, "*.odp") or fnmatch.fnmatch(f, "*.pptx") or fnmatch.fnmatch(f, "*.docx"):
                            docs=os.path.join(working_directory, f)
                            shutil.copy(docs, destination_directory)
                    elif user_file == "programs":
                        if fnmatch.fnmatch(f, "*.py") or fnmatch.fnmatch(f,"*.sqlite") or fnmatch.fnmatch(f, "*.html") or fnmatch.fnmatch(f, "*.pkt") or fnmatch.fnmatch(f, "*.js") or fnmatch.fnmatch(f, "*.json"):
                            prog=os.path.join(working_directory, f)
                            shutil.copy(prog, destination_directory)
                    elif user_file == "application":
                        if fnmatch.fnmatch(f,"*.exe") or fnmatch.fnmatch(f,"*.debian.tar.tx") or fnmatch.fnmatch(f,"*.debian.tar.gz") or fnmatch.fnmatch(f,"*.tar") or fnmatch.fnmatch(f,"*.deb") or fnmatch.fnmatch(f,"*.zip") or fnmatch.fnmatch(f,"*.pkg") or fnmatch.fnmatch(f,"*.tar.tx") or fnmatch.fnmatch(f,"*.tar.gz") or fnmatch.fnmatch(f,"*.run") or fnmatch.fnmatch(f,"*.budle") or fnmatch.fnmatch(f,"*.msi") :
                            apps=os.path.join(working_directory, f)
                            shutil.copy(apps,destination_directory)
                window_display_text_area.insert(END, "\ncopying        " + user_file + "        succesful")
            except IOError :
                error_label2 = Label(window,text="You have an error in your input:::\n for files(one at a time) :application:music:documents:programs:music:videos:pictures",bg="cadet blue", fg="red", font=("ariana", 10), justify=CENTER)
                error_label2.grid(row=15, column=2)
        def reset():
            window_destination_folder_entry.delete(0,END)
            window_folder_entry.delete(0,END)
            window_file_entry.delete(0,END)
            window_display_text_area.delete("1.0",END)


        #Creating window button
        window_submit_button=Button(window,fg="black",bg="green",width=4,text="Submit",padx=16, pady=14, bd=7,font=("ariana",10,"bold"), command=submit_entry)
        window_submit_button.grid(row=11,column=0)
        window_move_button = Button(window,fg="black", bg="green", width=4, text="Move",padx=16, pady=14, bd=7,font=("ariana",10,"bold"),command=move_action)
        window_move_button.grid(row=11, column=1)
        window_copy_button = Button(window, fg="black", bg="green", width=4, text="Copy", padx=16, pady=14, bd=7,font=("ariana", 10, "bold"), command=copy_action)
        window_copy_button.grid(row=11, column=2)
        window_reset_button = Button(window, fg="black", bg="yellow", width=4, text="reset", padx=16, pady=14, bd=7,font=("ariana", 10, "bold"),command=reset)
        window_reset_button.grid(row=15, column=2)


    else:
        messagebox.showwarning("shadow","Wrong credetials")
def Exit():
    Exit = messagebox.askyesno("Exit?", "CONFIRM EXIT")
    if Exit > 0:
        root.destroy()
        return

def reset_password():
    reset_question = Label(text='Who is the owner',font=('verdana', 15, 'bold'),fg='red')
    reset_question.grid(row=13, column=0)
    reset_entry=Entry()
    reset_entry.grid(row=14, column=0)

    def sub():
        reset_answer=reset_entry.get()

        if reset_answer == "Shadow":

            creditials = Label(text='username=shadow :: password=shadow', font=('verdana', 15, 'bold'),
                     fg='red')
            creditials.grid(row=14,column=0)

    reset_button = Button(text="submit", fg="black", bg="green", command=sub)
    reset_button.grid(row=13, column=1)

def help_format():
    window2=Toplevel()
    window2.title("Shadow tech")
    window2.configure(background="black")
    window2.geometry("600x600")

    window2_help_label=Label(window2,text='THIS IS THE HELP PAGE OF USING THE PROGRAM \nAND WHAT THE PROGRM IS ABOUT', bg="yellow",fg='green', font=("arial",15,"italic"))
    window2_help_label.grid(row=0,column=0, sticky=W+E)
    window2_help_label2=Label(window2,bg="black",text='''This is a file allocation program..\nIts main idea is to help the user in allocating his/her files
     \nfrom a specific folder to a destinattion folder. \nLets say for an example you have some mp4 files located \nin the Downloads folder and you want to move them
     \nor copy them to a new folder named videos this program \n will give you easy and a fast way to move the program......
     ''')
    window2_help_label2.grid(row=1,column=0,rowspan=3)
    window2_help_label3 = Label(window2,font=("arial",15,"italic"),text="How to use the program",fg="yellow")
    window2_help_label3.grid(row=5,column=0)
    window2_help_label3 = Label(window2,bg="black", text='''First you have to authenticate in the login page\n if you forgot your username reset it by using the 
    name given during acquiring the program..\n In the main window enter the working directory this is where you files are \n Next enter the files to move or copy those are \n video for the mp4 files \n music for the mp3 file \n application this is for any application extensio \n programs for any code files like (.py,.html)
    \ndocuments for any document file for example(.docx) 
    
    
    Hopes the program will be of great importance to you 
    
    Follow me :
    youtube :::Cybertron shadow
    twitter:: Cybertron shadow
    eduhshadow@gmail.com
    ''')
    window2_help_label3.grid(row=6, column=0)


#The main  part ...THis is the login part
space=Label()
space.grid(row=1,column=0)
Username=Label(text='USERNAME',width=15,font=('verdana',20,'bold'),fg='blue',justify=CENTER)
Username.grid(row=2,column=0)
space=Label()
space.grid(row=3,column=4,columnspan=11)
Username_entry=Entry(width=30, bg="blue", bd=4,borderwidth=5)
Username_entry.grid(row=4,column=0,pady=20)
Username_entry.insert(0, "Enter your username")
Username_entry.bind( ' <Return> ' , lambda bindin:login())
space=Label()
space.grid(row=5,column=0)
Password=Label(text='PASSWORD',width=15,font=('verdana',20,'bold'),bd=1,fg='blue',justify=CENTER)
Password.grid(row=6,column=0)
space=Label()
space.grid(row=7,column=0)
Password_entry=Entry(width=30, bg="blue", bd=4, borderwidth=5)
Password_entry.grid(row=8,column=0)
Password_entry.insert(0, "Enter your password")
Password_entry.bind( ' <Return> ' , lambda bindin:login() )
space=Label()
space.grid(row=9,column=0)
#button part
btnLogin=Button(text='LOGIN',padx=16, pady=14, bd=7, fg="black",font=('arial',16,'bold'), width=10,bg="green",command=login)
btnLogin.grid(row=2,column=1)
btnReset=Button(text='RESET\nPASSWORD',padx=35, pady=1, bd=7, fg="black",font=('arial',16,'bold'), width=7,bg="green",command=reset_password)
btnReset.grid(row=4,column=1)
btnExit =Button(padx=10, pady=14, bd=7, fg="black",font=('arial',16,'bold'), width=11, text="Exit",bg="green", command=Exit)
btnExit.grid(row=6,column=1)
btnhelp =Button(padx=10, pady=14, bd=7, fg="black",font=('arial',16,'bold'), width=11, text="help",bg="green", command=help_format)
btnhelp.grid(row=8,column=1)

#The lower part and the time section
Shadow=Label(text="*"*4 + 'Shadow Tech' + "*"*4,font=('verdana',10,'bold'),bd=1,fg='red',justify=CENTER ,relief=SUNKEN)
Shadow.grid(row=11,column=0,pady=10,columnspan=3,sticky=W+E)
time=Label(font=('arial',15, 'bold'),text=Formating_time,fg="red", bd=1,justify=CENTER,relief=SUNKEN)
time.grid(row=10,column=0,pady=10,columnspan=3,sticky=W+E)

mainloop()
