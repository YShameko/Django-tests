from datetime import datetime, timedelta

def booking_time_explore(trainer_schedule, bookings, duration, check_time_step = 15):
    # Input parameters:
    # trainer_schedule: list [start_datetime, end_datetime]
    # bookings: list of tuples [(booking1_start_datetime, booking1_end_datetime),
    #                           (booking2_start_datetime, booking2_end_datetime), ...]
    # duration: integer, in minutes
    # check_time_step: integer, in minutes, default = 15 min
    #
    # Function returns: free_timeslots_list - [free_timeslot1_start_datetime, free_timeslot2_start_datetime, ...]
    #    ordered chronologically
    # ------------------------------------------------------------------------------------------------------------
    free_timeslots_list = []
    start_time, end_time = trainer_schedule
    time_to_add = start_time

    while time_to_add + timedelta(minutes=duration) <= end_time:
        this_time_is_free = True
        for booking in bookings:
            if (time_to_add + timedelta(minutes=duration) > booking[0]) and (time_to_add < booking[1]):
                this_time_is_free = False
                break
        if this_time_is_free:
            free_timeslots_list.append(time_to_add)

        time_to_add += timedelta(minutes=check_time_step)

    return free_timeslots_list

#-------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    pass