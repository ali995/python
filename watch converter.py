def h_to_m():
    print("enter hour: ")
    hour=int(input())
    min=str(hour*60)
    print(min+" minute")
    input()

def h_to_s():
    print("enter hour: ")
    hour=int(input())
    sec=str(hour*(60**2))
    print(sec+" minute")
    input()



def m_to_s():
    print("enter minute: ")
    min=int(input())
    sec=str(min*60)
    print(sec+" minute")
    input()




while True:
    print("choose... \n 1.hour to minutes \n 2.hour to seconds \n 3.minutes to seconds  " )
    choice=int(input())
    if choice==1:
        h_to_m()
    elif choice==2:
        h_to_s()
    elif choice==3:
        m_to_s()
    elif choice<1 or choice>4:
        print("wrong choice... ")

    

