import matplotlib.pyplot as plt

x_axis = []
y_axis = []


def tnpo(n, num_of_x_axis = 0):
    if n == 4:
        num_of_x_axis += 1
        x_axis.append(num_of_x_axis)
        y_axis.append(n)
        return False
    if n % 2 == 0:
        num_of_x_axis += 1
        x_axis.append(num_of_x_axis)
        y_axis.append(n)
        n = n/2
        return tnpo(n, num_of_x_axis)
    if n % 2 != 0:
        num_of_x_axis += 1
        x_axis.append(num_of_x_axis)
        y_axis.append(n)
        n = (3 * n) + 1
        return tnpo(n, num_of_x_axis)
    return tnpo(n)

n = input("Enter the number:")
tnpo(int(n))

plt.plot(x_axis, y_axis)
plt.xlabel("num of iteration")
plt.ylabel("nums")
plt.title("3n+1")
plt.show()