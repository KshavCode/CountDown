import time 
from plyer import notification

def timer(hour:int, minute:int, seconds:int, messag:str) :
    if len(str(hour)) <= len(str(minute)) <= len(str(seconds)) <= 2 :
        if 0 <= hour <= 59 or 0 <= minute <= 59 or 0 <= seconds <= 59 :
            tim = [hour, minute, seconds]
            while not (tim[0] == 0 and tim[1] == tim[2] == 0) :
                time.sleep(1)
                if tim[2] != 0 :
                    tim[2] -= 1
                elif tim[2] == 0 :
                    if tim[1] != 0 :
                        tim[2] = 59
                        tim[1] -= 1
                    elif tim[1] == 0 :
                        if tim[0] != 0 :
                            tim[0] -= 1
                            tim[1] = 59
                            tim[2] = 59
                if len(str(tim[2])) == 1 :
                    sec = f"0{tim[2]}"
                else :
                    sec = tim[2]
                if len(str(tim[1])) == 1 :
                    mi = f"0{tim[1]}"
                else :
                    mi = tim[1]
                if len(str(tim[0])) == 1 :
                    h = f"0{tim[0]}"
                else :
                    h = tim[0]
                print(f"{h}:{mi}:{sec}", end="\r")
            notification.notify(title=f"Timer Alert ({messag})", message=f"Your time is up for {hour}H:{minute}M:{seconds}S")
            return f"Time's up! Message : {messag}"
        else : 
            return "Error. Time should contain number less than or equal to 59 and cannot be negative!"
    else : 
        return "Hour, minute and seconds should contain not more than 2 digits!"

try : 
    hour = int(input("Enter integer for hour : "))
    minu = int(input("Enter integer for minute : "))
    sec = int(input("Enter integer for seconds : "))
    mes = input("Any label or message? (Leave empty if unwanted) : ")
    mes = None if mes == "" else mes
    print(timer(hour, minu, sec, mes))
except : 
    print("Invalid Format, time is in integers only!")