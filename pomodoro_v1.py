'''
Pomodoro
'''
import time
import datetime as dt

import tkinter
from tkinter import messagebox
import winsound

t_now = dt.datetime.now()                               # Current time for reference
t_pom = 25 * 60                                         # Pomodoro time
t_delta = dt.timedelta(0, t_pom)                        # Time delta in mins
t_fut = t_now + t_delta                                 # Future Time, ending Pomodoro
delta_sec = 5 * 60                                      # Break Time, after Pomodoro
t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)      # Final time (w/ 5 mins. break)


# GUI set pomodoro in motion!

# Hide tkinter1s main window. We only need the alert message box
root = tkinter.Tk()
root.withdraw()
# Show alert message - Started
messagebox.showinfo("Pomodoro Started!", "\nIt is now " + t_now.strftime("%H:%M") +
    " hrs. \nTimer set for 25 mins.")

# Initialize pomodoro counters
total_pomodoros = 0
breaks = 0

# Mains Scrpit
while True:
    # Pomodoro Time!
    if t_now < t_fut:
        print('pomodoro')
        
    #it is now post working pomodoro, within the break.
    elif t_fut <= t_now <= t_fin:
        # check if first time here, if so ring a bell
        print('in break')
        if breaks == 0:
            print('if break')
            # Annay!
            for i in range(5):
                # first parameter is Hz and second is durarion in miliseconds
                winsound.Beep((i + 100), 700)
            print('Break Time!')
            breaks += 1

    # Pomodoro and break finished. Check if ready for another pomodoro!
    else:
        print('finished')
        # Pomodoro Finished. Reset breaks
        breaks = 0
        # Annay -> let user know that break is over
        for i in range(10):
            winsound.Beep((i + 100), 500)
        # Ask if user wants to start again
        usr_ans = messagebox.askyesno("Pomodoro Finished!", "\nWould you like to start another pomodoro?")
        total_pomodoros += 1
        if usr_ans == True:
            # user wants another pomodoro! Update values to indicate new timeset.
            t_now = dt.datetime.now()
            t_fut = t_now + dt.timedelta(0, t_pom)
            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)
            continue
        elif usr_ans == False:
            # User is done, display achievements for now.
            messagebox.showinfo("Pomodoro Finished!", "\nYou completed" +
                str(total_pomodoros) + "pomodoros today!")
        break
# check every 20 seconds and update currente time
print('sleeping')
time.sleep(20)
timenow = t_now.strftime("%H:%M")
