import datetime
import pytz

def get_time_difference(departure_time, arrival_time):
    time_diff = arrival_time - departure_time
    return time_diff

def generate_trip_calendar(departure_date, arrival_date):
    current_date = departure_date
    while current_date <= arrival_date:
        if current_date == departure_date or current_date == arrival_date:
            print(f'{current_date.strftime("%B %d, %Y")} (Departure/Arrival)')
        else:
            print(current_date.strftime("%B %d, %Y"))
        current_date += timedelta(days=1)

def main():
    departure_location = input("Enter departure location: ")
    arrival_location = input("Enter arrival location: ")
    departure_date_str = input("Enter departure date (YYYY-MM-DD): ")
    departure_time_str = input("Enter departure time (HH:MM): ")
    arrival_date_str = input("Enter arrival date (YYYY-MM-DD): ")
    arrival_time_str = input("Enter arrival time (HH:MM): ")
    
    departure_datetime_str = f'{departure_date_str} {departure_time_str}'
    arrival_datetime_str = f'{arrival_date_str} {arrival_time_str}'
    
    departure_datetime = datetime.datetime.strptime(departure_datetime_str, '%Y-%m-%d %H:%M')
    arrival_datetime = datetime.datetime.strptime(arrival_datetime_str, '%Y-%m-%d %H:%M')
    
    departure_timezone = pytz.timezone(input("Enter departure timezone (e.g. America/New_York): "))
    arrival_timezone = pytz.timezone(input("Enter arrival timezone (e.g. America/New_York): "))
    
    departure_datetime = departure_timezone.localize(departure_datetime)
    arrival_datetime = arrival_timezone.localize(arrival_datetime)
    
    time_diff = get_time_difference(departure_datetime, arrival_datetime)
    print(f'Time difference between {departure_location} and {arrival_location}: {time_diff}')
    
    departure_date = departure_datetime.date()
    arrival_date = arrival_datetime.date()
    print(f'Trip dates: {departure_date} to {arrival_date}')
    
    generate_trip_calendar(departure_date, arrival_date)

if __name__ == '__main__':
    main()

