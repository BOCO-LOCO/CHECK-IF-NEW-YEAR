import datetime
#get the date informations
istoday = datetime.datetime.today()
newyear = datetime.date(2026, 1, 1 )

# simple check with if conditions for the specified date
def check_new_year():
    if istoday == newyear:
        print("\n-----Happy New Year-----\nouuuuuuuuuuuuuuuiiiiiiii\n".upper())
    else:
        print("\n-----You Still in The 2025, Mother fucker-----\n".upper())
        
check_new_year()
        
