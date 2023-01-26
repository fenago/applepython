import datetime
import calendar

class Event:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def event_summary(self):
        print("Event name: " + self.name)
        print("Event start date and time: " + str(self.start_date))
        print("Event end date and time: " + str(self.end_date))
        time_diff = self.end_date - self.start_date
        print("Event duration: " + str(time_diff))

    def generate_calendar(self, holidays=[]):
        # Create a calendar and set the start and end dates as bold
        cal = calendar.HTMLCalendar(calendar.SUNDAY)
        cal.setfirstweekday(calendar.SUNDAY)
        str = cal.formatmonth(self.start_date.year, self.start_date.month, withyear=True)
        str = str.replace('<td class="noday">&nbsp;</td>', "")
        str = str.replace('<td class="%s">' % (self.start_date.strftime("%A").lower()),
                           '<td class="%s" style="font-weight: bold">' % (self.start_date.strftime("%A").lower()))
        str = str.replace('<td>' + str(self.start_date.day) + '</td>',
                           '<td>' + str(self.start_date.day) + '</td>')
        str = str.replace('<td class="%s">' % (self.end_date.strftime("%A").lower()),
                           '<td class="%s" style="font-weight: bold">' % (self.end_date.strftime("%A").lower()))
        str = str.replace('<td>' + str(self.end_date.day) + '</td>',
                           '<td>' + str(self.end_date.day) + '</td>')
        # Highlight any holidays in the calendar
        for holiday in holidays:
            str = str.replace('<td class="%s">' % (holiday.strftime("%A").lower()),
                              '<td class="%s" style="color: red">' % (holiday.strftime("%A").lower()))
            str = str.replace('<td>' + str(holiday.day) + '</td>',
                              '<td>' + str(holiday.day) + '</td>')
        print(str)
event_name = input("Enter the name of the event: ")
event_start = input("Enter the start date and time of the event (MM/DD/YYYY HH:MM): ")
event_end = input("Enter the end date and time of the event (MM/DD/YYYY HH:MM): ")

start_date = datetime.datetime.strptime(event_start, "%m/%d/%Y %H:%M")
end_date = datetime.datetime.strptime(event_end, "%m/%d/%Y %H:%M")
my_event = Event(event_name, start_date, end_date)
my_event.event_summary()
my_event.generate_calendar()
