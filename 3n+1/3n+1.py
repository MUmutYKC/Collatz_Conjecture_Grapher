import matplotlib.pyplot as plt # importting matplotlib to plot the graph

x_axis = []
y_axis = []
# creating lists which will be used for specifying axes

def tnpo(n, num_of_x_axis = 0): # creating function
    if n == 4: 
        num_of_x_axis += 1 # adding one to the x-axis to show the num of iteration 
        x_axis.append(num_of_x_axis) # adding to the list
        y_axis.append(n) # adding output of the function to the y-axis
        return False # we have to stop the function because 4 puts it in a infinite loop
    if n % 2 == 0:
        num_of_x_axis += 1
        x_axis.append(num_of_x_axis)
        y_axis.append(n)
        n = n/2
        return tnpo(n, num_of_x_axis) # repeating the function to continue the algorithm
    if n % 2 != 0:
        num_of_x_axis += 1
        x_axis.append(num_of_x_axis)
        y_axis.append(n)
        n = (3 * n) + 1
        return tnpo(n, num_of_x_axis)

n = input("Enter the number:")
if n < 0 or n % 1:
    print("Number mus be a positive integer.") # function is defined only for positive integers
else:
    tnpo(int(n))
    plt.plot(x_axis, y_axis)
    plt.xlabel("num of iteration")
    plt.ylabel("nums")
    plt.title("3n+1")
    plt.show()
    
