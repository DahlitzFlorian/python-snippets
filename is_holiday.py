from datetime import date

import holidays


today = date.today()
is_holiday = today in holidays.Germany()

print(is_holiday)
