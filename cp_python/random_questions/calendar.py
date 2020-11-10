"""
For two calendars, find time periods to schedule a meeting. Each calendar is represented by a list of meetings,
hence during those periods no meeting can be scheduled. Also, every calendar comes with bounds telling us the earliest
and the latest we can schedule meetings.

sample input:
# calendar one, meetings and bounds
[['9:00', '10:00'], ['12:30', '13:00']]
['8:00', '20:00']

# calendar two, meetings and bounds
[['7:00', '9:00'], ['12:30', '13:00']]
['6:00', '17:00']
"""

from typing import List, Optional


class Time:
    def __init__(self, time_str: str):
        """Format or time_str assumed to be military: '15:30'."""
        self.time_str = time_str

    @property
    def hour(self):
        return int(self.time_str.split(':')[0])

    @property
    def minute(self):
        return int(self.time_str.split(':')[1])

    def __gt__(self, other):
        if self.hour > other.hour:
            return True
        elif self.hour == other.hour:
            return self.minute > other.minute
        elif self.hour < other.hour:
            return False

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def _to_hour_min(self):
        return [int(item) for item in self.time_str.split(':')]

    def __repr__(self):
        return f'Time({self.time_str})'


class Slot:
    def __init__(self, start: str, end: str):
        """Format of arguments assumed to be military: '15:30'."""
        self.start = Time(start)
        self.end = Time(end)

    def __repr__(self):
        return f'{self.__class__.__name__}(start={self.start}, end={self.end})'

    def find_overlap(self, other: 'Slot') -> Optional['Slot']:
        slot_ahead, slot_behind = sorted([self, other], key=lambda slot: slot.start)
        if slot_behind.start > slot_ahead.end:
            return None
        else:
            mutual_slot_start = slot_behind.start
            if slot_ahead.end > slot_behind.end:
                return Slot(mutual_slot_start, slot_behind.end)
            else:
                return Slot(mutual_slot_start, slot_ahead.end)


class Meeting(Slot):
    def __init__(self, start: str, end: str):
        super().__init__(start, end)


class Calendar:
    def __init__(self, meetings: List[Meeting] = None):
        self.meetings = meetings if meetings else []

    def free_slots(self, day_bounds: Slot):
        """Bounds represents start and end for possible meetings."""
        free_slots: List[Slot] = []
        time_ptr = day_bounds.start
        for meeting in self.meetings:
            if meeting.start > time_ptr:
                free_slots.append(Slot(time_ptr.time_str, meeting.start.time_str))
            time_ptr = meeting.end
        if day_bounds.end > time_ptr:
            free_slots.append(Slot(time_ptr.time_str, day_bounds.end.time_str))
        return free_slots


def find_mutual_slots(cal1: Calendar, cal2: Calendar, bounds1: Slot, bounds2: Slot) -> List[Slot]:
    slots1, slots2 = cal1.free_slots(bounds1), cal2.free_slots(bounds2)
    mutual_slots = []
    for slot1 in slots1:
        for slot2 in slots2:
            overlap = slot1.find_overlap(slot2)
            if overlap is not None:
                mutual_slots.append(overlap)
    return mutual_slots


if __name__ == '__main__':
    calendar_one = Calendar([Meeting('8:00', '9:30'),
                             Meeting('10:00', '14:00'),
                             Meeting('15:00', '15:30')])
    bounds_one = Slot("7:00", "17:30")
    calendar_two = Calendar([Meeting('9:00', '12:30')])
    bounds_two = Slot("7:00", "19:00")

    print(f'Calendar 1 meetings: {calendar_one.meetings}')
    print(f'Calendar 2 meetings: {calendar_two.meetings}')
    print('---')
    print(f'Calendar 1 free slots: {calendar_one.free_slots(day_bounds=bounds_one)}')
    print(f'Calendar 2 free slots: {calendar_two.free_slots(day_bounds=bounds_two)}')
    print('---')
    print(f'Mutual slots')
    for mutual_spot in find_mutual_slots(calendar_one, calendar_two, bounds1=bounds_one, bounds2=bounds_two):
        print('\n', mutual_spot)
