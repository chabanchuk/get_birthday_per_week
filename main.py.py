from datetime import date, datetime


def get_birthdays_per_week(users):

    today_day = date.today()
    birthdays = {}
    for user in users:
        user_birthday = user['birthday'].replace(year=today_day.year)
        delta = (user_birthday - today_day).days
        if delta < 0:
            delta += 365
        if 0 <= delta < 7:
            day_week = user_birthday.strftime('%A')
            if day_week == 'Monday' or day_week == 'Saturday' or day_week == 'Sunday':
                if 'Monday' not in birthdays:
                    birthdays['Monday'] = []

                birthdays['Monday'].append(user['name'])
            else:
                if day_week not in birthdays:
                    birthdays[day_week] = []
                birthdays[day_week].append(user['name'])
    return birthdays

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
