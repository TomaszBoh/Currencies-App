from datetime import datetime, timedelta

def generate_dates(start_date_str):
    #Konwersja string na objekt daty
    start_date = start_date_str #datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end_date = datetime.now().date()

    #Generowanie dat
    date_list = []
    current_date = start_date
    while current_date <= end_date:
        date_list.append( (current_date.year, current_date.month, current_date.day) )
        current_date += timedelta(days=1)

    return date_list