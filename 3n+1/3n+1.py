from tkinder import * #Importing tkinder to get the number.
import matplotlib.pyplot as plt #Importting matplotlib to plot the graph.

x_axis = []
y_axis = []
#Creating lists which will be used for specifying axes.

def tnpo(n, num_of_x_axis = 0): #Creating function.
    if n == 4: 
        num_of_x_axis += 1 #Adding one to the x-axis to show the num of iteration.
        x_axis.append(num_of_x_axis) #Adding it to the list.
        y_axis.append(n) #Adding output of the function to the y-axis.
        return False #We have to stop the function because 4 puts it in a infinite loop.
    if n % 2 == 0:
        num_of_x_axis += 1
        x_axis.append(num_of_x_axis)
        y_axis.append(n)
        n = n/2
        return tnpo(n, num_of_x_axis) #Repeating the function to continue the algorithm.
    if n % 2 != 0:
        num_of_x_axis += 1
        x_axis.append(num_of_x_axis)
        y_axis.append(n)
        n = (3 * n) + 1
        return tnpo(n, num_of_x_axis)

app = Tk() #Creating the application to enter the number.
app.geometry("300x200")

def get_value(): #Function that will get the number from our entry
    global n 
    n = float(E1.get())

L1 = Label(app, text="Enter the number: ")
L1.pack( side = TOP)
L2 = Label(app, text="First press the Submit then close the app.")
L2.place(x=25, y=100)
E1 = Entry(app, bd =5)
E1.pack(side = TOP)
B1 = Button(app, text="Submit", command= get_value)
B1.place(x=25, y=150)
B2 = Button(app, text="Close", command=app.destroy)
B2.place(x=230, y=150)

app.mainloop()

if n < 0 or n % 1:
    print("Number mus be a positive integer.") #Function is defined only for positive integers.
else:
    tnpo(int(n))
    plt.plot(x_axis, y_axis)
    plt.xlabel("num of iteration")
    plt.ylabel("nums")
    plt.title("3n+1")
    plt.show()
    
