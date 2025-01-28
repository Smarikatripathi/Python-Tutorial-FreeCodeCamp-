def add_time(start, duration, starting_day=None):
    # Days of the week in order
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Parse the start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))
    
    # Convert start time to 24-hour format
    if period == "PM":
        start_hour += 12 if start_hour != 12 else 0
    elif period == "AM" and start_hour == 12:
        start_hour = 0

    # Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Add the hours and minutes
    total_minutes = start_minute + duration_minute
    total_hours = start_hour + duration_hour + (total_minutes // 60)
    total_minutes %= 60

    # Calculate the final period in 24-hour format
    final_hour = total_hours % 24
    days_later = total_hours // 24

    # Determine AM/PM for the final hour
    if final_hour >= 12:
        period = "PM"
        final_hour -= 12 if final_hour > 12 else 0
    else:
        period = "AM"
        final_hour = 12 if final_hour == 0 else final_hour

    # Calculate the new day of the week
    if starting_day:
        starting_day = starting_day.capitalize()
        start_day_index = days_of_week.index(starting_day)
        new_day_index = (start_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
    else:
        new_day = None

    # Build the result string
    result = f"{final_hour}:{total_minutes:02d} {period}"
    if new_day:
        result += f", {new_day}"
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result

# Examples
print(add_time('3:30 PM', '2:12'))  # '5:42 PM'
print(add_time('11:55 AM', '3:12'))  # '3:07 PM'
print(add_time('2:59 AM', '24:00'))  # '2:59 AM (next day)'
print(add_time('11:59 PM', '24:05'))  # '12:04 AM (2 days later)'
print(add_time('8:16 PM', '466:02'))  # '6:18 AM (20 days later)'
print(add_time('3:30 PM', '2:12', 'Monday'))  # '5:42 PM, Monday'
print(add_time('2:59 AM', '24:00', 'saturDay'))  # '2:59 AM, Sunday (next day)'
print(add_time('11:59 PM', '24:05', 'Wednesday'))  # '12:04 AM, Friday (2 days later)'
print(add_time('8:16 PM', '466:02', 'tuesday'))  # '6:18 AM, Monday (20 days later)'
