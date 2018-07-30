# -*- coding:utf-8 -*-

# ............................
# ............................
# ............................
# ............................
# ............................
# ............................
# .....@@@@@@@.....@..........
# ....@@.....@@....@..........
# ...@.........@...@..........
# ..@@.............@..........
# ..@..............@..........
# .@@..............@..........
# .@@..............@.....@@@..
# .@...............@...@@@....
# .@...............@@@@@......
# .@@..............@@@........
# ..@..............@..........
# ..@@.............@....@.....
# ...@@.......@@...@....@@....
# ....@@.....@@....@.....@@...
# ......@@@@@......@......@...
# ............................
# ............................
# ............................
# ............................
# ............................
# ............................
# ............................
# ck大法好

# import os
# import re
# import sys
# import getopt
# import logging

from uuid import uuid1
# from pprint import pprint
from dateutil.relativedelta import relativedelta
from datetime import date, datetime, time, timedelta
from icalendar import Calendar, Event, Alarm
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

class AddCalendar(object):
	"""docstring for AddCalendar"""
	def __init__(self):
		pass


	def createMemoryEv(self,summary):
		'''
		summary: 标题
			提醒复习，1，2，4，8，15，30
		'''
		_da = [1,2,4,8,15,30]
		cal = Calendar()
		cal['version'] = '2.0'
		cal['prodid'] = '-//Apple Inc.//Mac OS X 10.13.6//EN'
		events = []
		for da in _da:
			event = Event()
			alarm = Alarm()
			event.add('uid',str(uuid1()) + '@CQUT')
			event.add('summary',summary)
			event.add('dtstamp',datetime.now())
			year,month,day = datetime.now().timetuple()[0:3]
			event.add('dtstart',datetime(year,month,day,23,0,0) + relativedelta(days = da-1))
			event.add('dtend',datetime(year,month,day,23,30,0) + relativedelta(days = da-1))
			alarm.add('TRIGGER',datetime(year,month,day,22,57,0) + relativedelta(days = da-1))
			alarm.add('action','DISPLAY')
			event.add_component(alarm)
			cal.add_component(event)

		with open("记忆事件.ics","w+") as file:
			file.write(cal.to_ical().decode('utf-8'.replace('\r\n','\n').strip()))
			file.close()


	#用于测试的函数：

	def createAnIcs(self,title,starttime,endtime,place):
		'''
			title:日历的标题
			start:日历的开始时间
			endtime:日历持续的时间
			place:地点

		'''
		cal = Calendar()
		cal['version'] = '2.0'
		cal['prodid'] = '-//Apple Inc.//Mac OS X 10.13.6//EN'
		event = Event()
		alarm = Alarm()
		#ev_start_date = startdate
		#ev_start_datetime = datetime.combine(ev_start_date,starttime)
		ev_start_datetime = starttime
		#ev_last_relative_delta = relativedelta(lasttime[0],lasttime[1])
		#ev_end_datetime = ev_start_date + ev_last_relative_delta
		ev_end_datetime = endtime

		event.add('uid',str(uuid1()) + '@COUT')
		event.add('summary',title)
		event.add('dtstamp',datetime.now())
		event.add('dtstart',ev_start_datetime)
		event.add('dtend',ev_end_datetime)
		event.add('location',place)
		alarm.add('TRIGGER',ev_start_datetime)
		alarm.add('action','DISPLAY')
		event.add_component(alarm)
		'''
		BEGIN:VALARM
		TRIGGER:-PT15M
		ACTION:DISPLAY
		END:VALARM
		'''
		cal.add_component(event)
		with open("记忆事件.ics","w+") as file:
			file.write(cal.to_ical().decode('utf-8'.replace('\r\n','\n').strip()))
			file.close()


		
if __name__ == '__main__':
	ckc = AddCalendar()
	# _date = date(2018,7,31)
	# _timeSt = time(9,40)
	# _timeEn = time(10,0)
	# ckc.createAnIcs("一个事件",datetime(2018,7,30,9,40,0),datetime(2018,7,31,9,50,0),"where?")
	ckc.createMemoryEv("测试的记忆事件2")