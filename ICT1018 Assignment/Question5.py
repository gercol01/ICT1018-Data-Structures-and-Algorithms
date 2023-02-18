arrayOp = ["+","-","*","/"] #array which stores all the possible operators

#algorithm to evaluate RPN expressions
def ADTstackAlgorithm(array):
    arrayE = [] #array used as a stack to evaluate
    for i in range(len(array)):#loop to traverse RPN expression
        flag = 0 #used to show that the value is an operator

        for j in range(len(arrayOp)): #loop to traverse operator array
            if array[i] == arrayOp[j]: #checking if the value is an operator or not
                flag = 1 #value is an operator
                break
        
        if flag == 1: #if the value is an operator
            a = arrayE.pop()
            b = arrayE.pop()

            if array[i] == '+':
                arrayE.append(b+a)

            if array[i] == '-':
                arrayE.append(b-a)
            
            if array[i] == '*':
                arrayE.append(b*a)
            
            if array[i] == '/':
                arrayE.append(b/a)
        else: #if the value is a number, push it onto the stack
            arrayE.append(array[i])
    
    print(arrayE) #printing the result

array1 = [5,3,"+",7,"*"] #array that stores an expression in RPN format
ADTstackAlgorithm(array1) #calling the algorithm to test
