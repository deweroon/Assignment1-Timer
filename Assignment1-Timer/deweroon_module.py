import time

#Local Time

def local_time_indicator():
    seconds=time.time()
    Local_Time=time.ctime(seconds)
    print("Local Time : ", Local_Time)

#CHRONOMETER

def chronometer():
    print("Chronometer started.")
    delay= int(input("Please enter the waiting time (in seconds) : "))
    time.sleep(delay)
    print("----------TİME-İS-UP----------")
    print("The amount of time you want the stopwatch to stop.")

def lap_counter():
    print("-"*10)
    #Timer Starts
    start_time=time.time()
    last_time=start_time
    lapnum=1
    value=""

    print("Press enter for each lap.Press q to stop")

    print("-"*10)

    while value.lower() !="q":
        #Input for the ENTER key press
        value=input()

        #The current lap time
        laptime=round((time.time() - last_time), 2)

        #Total time elapsed since the timer started
        total_time=round((time.time() - start_time), 2)

        #Printing the lap number, lap time, total time
        print("Lap No -> "+str(lapnum))
        print("Total Time : "+str(total_time))
        print("Lap Time : "+str(laptime))

        print("-"*20)

        #Updating the previous total time and lap number
        last_time=time.time()
        lapnum += 1

    print("COMPLETED")
    print("-"*10)
    local_time_indicator()
    print("-"*20)