import math
def number(x):
      try:
          val=complex(x)
          if val.imag==0:
              pass
          else:
              return val
      except:
          pass
      try:
          val=float(x)
          if math.modf(val)==0:
              pass
          return val
      except:
          pass
      try:
          val=str(x)
          if isinstance(x,str)==True:
              return val
      except:
          pass
i=1
while i==1:    
     try:
          a=input("Enter the first value:")
          a=number(a)
          if isinstance(a,str)==True:
              print("alphabets not allowed")
              continue
          i=i+1

     except:
          print("Oops!\nRun again")
i=1
while i==1:
     try:
          b=input("Enter the second value:")
          b=number(b)
          if isinstance(b,str)==True:
              print("alphabets not allowed")
              continue
          i=i+1
     except:
          print("Oops!\nRun again.") 
i=1
while i==1:
    j=1
    while j==1:
        try:
            print("1.Addition\n2.Subraction\n3.Division\n4.Multipication\n5.power")
            opt=float(input("Enter Your Choice :"))
            j+=1
        except:
            print("Oops!\nRun again.\n\n")
    opt=round(opt)
    if opt ==1:
            print("the Added value is: ",a+b)
            i+=1
    elif opt ==2:
            print("the subracted value is: ",a-b)
            i+=1
    elif opt ==3:
            if  b == 0 :
                print("invalid option")
            else:    
                print("The Divided value is: ",a/b)
                i+=1
    elif opt ==4:
            print("The multiplied value is",a*b)
            i+=1
    elif opt ==5:
            print(a,"power",b,"is: ",a**b)  
            i+=1
    else:
            print("Invalid option selected\nPlease choose again\n\n")
