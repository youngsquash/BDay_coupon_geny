import datetime, random, csv, string
import pandas as pd

#  functions go here

def id_generator(size=7, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def tier_size():
    return int(input('Number of TH birthdays?')), int(input('Number of SB birthdays?')), int(input('Number of SMT birthdays?'))

def get_date():
    return input('Todays date?')

def pref():
    return str(input('th prefix?')), str(input('sb prefix?')), str(input('summit prefix?'))


if __name__ ==" __main__":
    main()

def main():

# get date range
    today = get_date()
    ts = pd.Timestamp(today)
    effective_start = ts - pd.DateOffset(weeks=2)
    effective_end = ts + pd.DateOffset(weeks=2)

# ask for resp. numb of birthdays
    th_prefix, sb_prefix, st_prefix = pref()
    th_size, sb_size, st_size = tier_size()

# codes generator per tier
    trail_codes = [th_prefix + id_generator() for i in range(th_size)]
    switch_codes = [sb_prefix + id_generator() for i in range(sb_size)]
    summit_codes = [st_prefix + id_generator() for i in range(st_size)]

# create df's for export
    trail_df = pd.DataFrame(trail_codes, columns = ['code'])
    trail_df.insert(1, 'offer_id', ['3' for i in range(len(trail_df))])

    switch_df = pd.DataFrame(switch_codes, columns = ['code'])
    switch_df.insert(1, 'offer_id', ['4' for i in range(len(switch_df))])

    summit_df = pd.DataFrame(summit_codes, columns = ['code'])
    summit_df.insert(1, 'offer_id', ['5' for i in range(len(summit_df))])

# df roll up
    birthday_df = pd.concat([trail_df, switch_df, summit_df])
    birthday_df.insert(2, 'effectivity_start', [str(effective_start) for i in range(len(birthday_df))])
    birthday_df.insert(3, 'effectivity_end', [str(effective_end) for i in range(len(birthday_df))])
    birthday_df.insert(4, 'effectivity_timezone', ['Etc/UTC' for i in range(len(birthday_df))])

    # birthday_df['effective_start'] = birthday_df['effective_start'].strftime('m%/d%/Y%')
    # birthday_df['effective_end'] = birthday_df['effective_end'].strftime('m%/d%/Y%')
    header = ['code', 'offer_id', 'effectivity_start', 'effectivity_end', 'effectivity_timezone']
    birthday_df.to_csv('birthday_import.csv', index=False, header=header)

main()
