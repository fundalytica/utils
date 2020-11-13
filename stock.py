import re
def valid_symbol(symbol):
    STOCK_SYMBOL_PATTERN = "[A-Z]{1,4}((\.){1}[A|B]{1}){0,1}$"
    pattern = re.compile(STOCK_SYMBOL_PATTERN)
    match = pattern.match(symbol)
    return match is not None

import pandas as pd
from pandas.tseries.holiday import AbstractHolidayCalendar, Holiday, nearest_workday, USMartinLutherKingJr, USPresidentsDay, USMemorialDay, USLaborDay, USThanksgivingDay, GoodFriday
def USTradingCalendar():
    class USTradingCalendar(AbstractHolidayCalendar):
        rules = [
            Holiday('NewYearsDay', month=1, day=1, observance=nearest_workday),
            Holiday('USIndependenceDay', month=7, day=4, observance=nearest_workday),
            Holiday('Christmas', month=12, day=25, observance=nearest_workday),
            USMartinLutherKingJr,
            USPresidentsDay,
            GoodFriday,
            USMemorialDay,
            USLaborDay,
            USThanksgivingDay
        ]
    return USTradingCalendar()
def USOtherNonTradingDates():
    # December 5, 2018: National Day of Mourning for George H.W. Bush
    return ['2018-12-05']