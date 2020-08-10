# Numpy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1

elif dice > 2 and dice < 6 :
    step = step + 1
    
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice,step)
