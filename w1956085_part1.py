#declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1956085
# IIT NO: 20220587
# Date: 09th december 2022


"""
References
    1.https://www.w3schools.com/python/python_intro.asp
    2.https://docs.python.org/3/tutorial/datastructures.html#dictionaries
    3.Lecture meterials & Tutorial meterials
"""


no_of_outcome = 0
progress = 0
trailer = 0
retriever = 0
exclude = 0

while True:
    
        while True:
                 
            while True:
                pass_credit = input("Please enter your credits at Pass : ")
                try:
                    pass_credit = int(pass_credit)
                    if pass_credit in range(0,121,20):
                        break
                    else:
                        print(" Out of range  \n")
                        print(" Please try again  \n")
                except ValueError:
                    print(" Integer Required.....")
                    print(" Please try again !!!!! \n")
        
        
            while True:
                defer_credit = input("Please enter your credits at Defer : ")
                try:
                    defer_credit = int(defer_credit)
                    if defer_credit in range(0,121,20):
                        break
                    else:
                        print(" Out of range  \n")
                        print(" Please try again !!!!!  \n")
                except ValueError:
                    print(" Integer Required..... \n")
                    print(" Please try again !!!!! \n")
            
            
            while True:
                fail_credit = input("Please enter your credits at Fail : ")
                try:
                    fail_credit = int(fail_credit)
                    if fail_credit in range(0,121,20):
                        break
                    else:
                        print(" Out of range  \n")
                        print(" Please try again !!!!! ")
                except ValueError:
                    print(" Integer Required.....  \n")
                    print(" Please try again !!!!! ")
            
            total = pass_credit + defer_credit + fail_credit 
            if total == 120:
                break 
            else:
                print("Total incorrect ! \n")
                print(" Please try again !!!!! \n")        
        
       
        if pass_credit == 120:
            result = 'Progress'
            
        elif pass_credit == 100:
            result = 'Progress(Module trailer)'
            
        elif pass_credit == 80 or pass_credit == 60:
            result = 'Module retriever'
            
        elif fail_credit >= 80:
            result = 'Exclude'
        else:
            result = 'Module retriever'
        print(result,'\n')
        
        if result == 'Progress':
            progress += 1
        elif result =='Progress(Module trailer)':
            trailer += 1 
        elif result == 'Module retriever':
            retriever += 1
        else: 
            exclude += 1
        
        no_of_outcome += 1
              
        
        Repeat = input("Would you like to process another time :  \nEnter 'y' for continue 'q' to quit and view results ")        
        Repeat= Repeat.lower()
        print('')
        if Repeat == 'q':
            break
        elif Repeat == 'y':
            continue
       

print("-" *50) 
print("Histogram  ") 
print(f'Progress   {progress} :',progress*'*')    
print(f'Trailer    {trailer} :',trailer*'*')
print(f'Retriever  {retriever} :',retriever*'*')
print(f'Exclude    {exclude} :',exclude* '*','\n')
print(no_of_outcome, " outcomes in total. ")
print('-'*50)

