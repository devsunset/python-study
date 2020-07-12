# $ pip install openpyxl

# https://matplotlib.org/gallery.html

from matplotlib import pyplot as plt
 
# case 1 (x-y line chart)
plt.plot([1,2,3], [110,130,120])
plt.show()

# case 2 (x-y line chart,  x-y label)
plt.plot(["Seoul","Paris","Seattle"], [30,25,55])
plt.xlabel('City')
plt.ylabel('Response')
plt.title('Experiment Result')
plt.show()

# case 3 (x-y line chart,  x-y label, line legend)
plt.plot([1,2,3], [1,4,9])
plt.plot([2,3,4],[5,6,7])
plt.xlabel('Sequence')
plt.ylabel('Time(secs)')
plt.title('Experiment Result')
plt.legend(['Mouse', 'Cat'])
plt.show()

# case 4 (x,y bar chart)
y = [5, 3, 7, 10, 9, 5, 3.5, 8]
x = range(len(y))
plt.bar(x, y, width=0.7, color="blue")
plt.show()