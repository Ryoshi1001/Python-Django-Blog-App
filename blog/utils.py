from calendar import HTMLCalendar
from datetime import datetime

class Calendar: 
  def __init__(self, year=None, month=None):
    self.year = year if year else datetime.now().year
    self.month = month if month else datetime.now().month


  def formatmonth(self): 
    return HTMLCalendar().formatmonth(self.year, self.month)