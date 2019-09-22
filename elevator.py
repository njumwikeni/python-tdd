
def elevator(left,right,call):
    if abs(call-right)<=abs(call - left):
        return "right"
    else:
        return "left"

print (elevator(0,1,0))
print (elevator(0,1,1))
print (elevator(0,1,2))
print (elevator(0,0,0))
print (elevator(0,2,1))
    
    
