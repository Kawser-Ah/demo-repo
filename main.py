print('Hello github')

# Pull this in the local repository
import matplotlib.pyplot as plt
x=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
y=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
for i in range(len(x)):
    plt.figure()
    plt.plot(x[i],y[i])
    # Show/save figure as desired.
    #plt.show()
# Can show all four figures at once by calling plt.show() here, outside the loop.
plt.show()
