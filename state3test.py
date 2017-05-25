from Tkinter import *
import MySQLdb as sql

root=Tk()
root.title('State Population Analysis')
root.geometry('750x360')

wintwo=Toplevel(master=root)
wintwo.title('State Population Analysis Results')
wintwo.geometry('600x360')

db=sql.connect("localhost","root","mysql123","states") 
mycursor=db.cursor()

greet=Label(root,text="Hi, this program helps you find the population and % population share of every US state from 1900-2020")
greet.grid(row=0,column=3)

explain=Label(root,text="The % population share is the percentage of the total US population that the state held in that year")
explain.grid(row=1,column=3)

ask=Label(root,text="What US population data would you like to analyze?")
ask.grid(row=2,column=3)
         
var=StringVar(root)
var.set("Select state")

options=OptionMenu(root,var,"USA","Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","District of Colombia","Florida","Georgia","Hawaii","Idaho",
                   "Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississipi","Missouri","Montana",
                   "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
                   "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming")
options.grid(row=10,column=0)

yr=StringVar(root)
yr.set("Select year")

years=OptionMenu(root,yr,"1900","1910","1920","1930","1940","1950","1960","1970","1980","1990","2000","2010","2020")
years.grid(row=10,column=5)

def analyze(): 
    query = "SELECT states,p"+yr.get()+","+yr.get()+"share from states.states_analysis where states='%s';" %var.get()
    mycursor.execute(query)
    res=mycursor.fetchall()

    for r in res:
        if (yr.get()=="2020"):
            resLabel= Label(wintwo,text='The population and % share of ' + var.get() + ' in ' + yr.get() + ' will be ' + str(r[1]) + ' and ' + str(r[2])+'%')
            resLabel.pack(side=TOP)
        else:
            resLabel= Label(wintwo,text='The population and % share of ' + var.get() + ' in ' + yr.get() + ' were ' + str(r[1]) + ' and ' + str(r[2])+'%')
            resLabel.pack(side=TOP)               

def exitmain():
    root.destroy()

def exitsecond():
    wintwo.destroy()

analyzeBtn=Button(root,text="Analyze!",command=analyze)
analyzeBtn.grid(row=15,column=3)

returnBtn=Button(wintwo,text="Return to main menu")
returnBtn.pack(side=LEFT)

exitBtn=Button(root,text="Exit",command=exitmain)
exitBtn.grid(row=15,column=5)

exitBtn2=Button(wintwo,text="Exit",command=exitsecond)
exitBtn2.pack(side=RIGHT)

wintwo.mainloop()
mainloop()



