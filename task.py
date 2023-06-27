def hours2mins(hours):
    return hours * 60

def hours_or_mins(val):
    ans = input("Enter h for hours, m for minutes: ")
    if ans == "h":
        return val * 60
    elif ans == "m":
        return val/60
    
def count_letters(txt):
    return len(txt)


print(count_letters("among"))
print(hours_or_mins(200))