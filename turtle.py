# turtle schedule!
# starts at 0:00 and ends at 23:59
# minutes in a day is 1440 


num_meals = int(input ("Enter how many meals you would like Garvin to have in a day! "))

feeding_interval = num_meals / 1440

list_meal_mins = [] 
for i in range(num_meals):
    list_meal_mins.append(i*feeding_interval)

def mins_to_time(mins):
    time_hour = int(mins/60)
    time_mins = (mins % 60)
    print str(time_hour) + ":" + str(time_mins)
    
for i in list_meal_mins:
    mins_to_time(i)
    
#create a list (num_naps) long from 1 and multiply the intervals and use helper to turn them into time 