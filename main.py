from twilio.rest import Client
import random 
from tkinter import * 
from tkinter import messagebox

class otp_checker(Tk):
    def __init__(self): 
        super().__init__()
        self.geometry("600x500")
        self.resizable(False,False)
        self.n=random.randint(1000,9999)
        self.client=Client("","")
        self.client.messages.create(to=[""],
                                    from_="",
                                    body=self.n)

    def Labels(self):
        self.c = Canvas(self,bg="white",width=400,height=200)
        self.c.place(x=100,y=60)
        self.Login_Title=Label(self,text="OTP verification",font="bold,20",bg="white")      #login title on the top
        self.Login_Title.place(x=210,y=90)

    def Entry(self):
        self.user_name=Text(self,borderwidth=2,wrap='word',width=20,height=2)
        self.user_name.place(x=190,y=160)
    
    def Button(self):
        self.submitbuttonimage=PhotoImage(file="submit.png")
        self.submitbutton=Button(self,image=self.submitbuttonimage,command=self.checkOTP,border=0)
        self.submitbutton.place(x=208,y=240)

        self.resendimage=PhotoImage(file="resendotp.png")
        self.resendOTP=Button(self,image=self.resendimage,command=self.resendOTP,border=0)
        self.resendOTP.place(x=208,y=400)

    def checkOTP(self):
        try:
            self.userInput=int(self.user_name.get(1.0,"end-1c"))
            if self.userInput==self.n:
                messagebox.showinfo("showinfo","Login success")
                self.n="done"
            elif self.n=="done":
                messagebox.showinfo("showinfo","Already Login")
            else:
                messagebox.showinfo("showinfo","wrong OTP")
        except:
            messagebox.showinfo("showinfo","INVALID OTP")

    def resendOTP(self):
        self.n=random.randint(1000,9999)
        self.client=Client("","")
        self.client.messages.create(to=[""],
                                    from_="",
                                    body=self.n)        

auth_token  ="xxxxxxxxxxxxxx"
account_sid ="XXXXXXXXXXXX"

if __name__=="__main__":
    window=otp_checker()
    window.mainloop()