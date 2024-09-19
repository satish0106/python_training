import sys
states=[]
capitals=[]
data=sys.argv
for i in range(1,len(data)):
    state_data= data[i].split()
    states.append(state_data[0])
    capitals.append(state_data[1])

print(states)
print(capitals)    
for i in range(0,len(states)):
    print(states[i],capitals[i])
    