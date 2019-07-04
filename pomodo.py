from datetime import timedelta
from datetime import datetime

class Pomodoro():
    """
    """

    #define timer types
    TIMER_NOME = 0
    TIMER_TASK = 1
    TIMER_SHORT_BREAK = 2
    TIMER_LONG_BREAK = 3

    def __init__(self):
        self.task_goal = 8
        self.task_count = 0
        self.long_break_goal = 4

        self.task_length = timedelta(minutes=25)


        self.short_break = timedelta(minutes=3)
        self.long_break = timedelta(minutes=15)

        self.timer_type = self.TIMER_NOME

    def start_task(self):


        self.timer_start = datetime.now()
        self.timer_end = self.timer_start + self.task_length
        self.timer_type = self.TIMER_TASK

        print('\n---- begin task {}----\n'.format(self.task_count + 1))

    def start_short_break(self):


        self.timer_start = datetime.now()
        self.hotimer_end = self.timer_start + self.short_break
        self.timer_type = self.TIMER_SHORT_BREAK

        print('\n---- begin short break ----\n')

    def complete_task(self):

        return self.task_count == self.task_goal

    def get_time_remainig(sefl):

        return self.timer_end - datetime.now()

    def format_timedelta(self, td):

        #find seconds    
        total_seconds = int(td.total_seconds())
        
        #3600 seconds in an hour
        hours, remainder = divmod(total_seconds, 3600)

        #60 seconds in a minute
        minutes, seconds = divmod(remainder,60)

        return ('{} mins {} secs'.format(minutes,seconds))

    def print_summary(self):


        task_name = 'none'

        #format timer output
        if self.timer_type == self.TIMER_TASK:
            task_name = 'task'
        elif self.timer_type == self.TIMER_SHORT_BREAK:
            task_name = 'short break'
        elif self.timer_type == self.TIMER_LONG_BREAK:
            task_name = 'long break'

        #format time remaiting output
        time_remainig = self.format_timedelta(self.get_time_remainig())

        print('{} | time remaiting: {}'.format(task_name, time_remainig))
