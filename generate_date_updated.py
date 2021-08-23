from networkdays import networkdays
import datetime as dt
from datetime import datetime, timedelta
import holidays, pyperclip, os


# getting US holidays dates
holidays_dates = holidays.UnitedStates(
    years=datetime.now().year).get_named('day')

# start & end date
start_date = dt.date.today()
end_date = dt.date.today() + timedelta(days=100)

HOLIDAYS = holidays_dates  # define a Holidays list

#  return a list os workdays
days = networkdays.Networkdays(
    start_date,  # start date
    end_date,  # end date
    HOLIDAYS  # list of Holidays
)
#  return one day and autocopy it to clipboard
pyperclip.copy(str(days.networkdays()))

day_list = days.networkdays()
counter = 0 
for day in day_list:
    counter += 1
    #  return one day and autocopy it to clipboard
    formated_day = day.strftime('%m/%d/%Y')
    pyperclip.copy(str(formated_day))
    msg = pyperclip.paste()
    print('your date is : ', msg)
    if counter == 11:
        print('that was the last day !')
        os.system("pause")
        break
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y' :
        continue
    else:
        print("Goodbye")
        break





    

