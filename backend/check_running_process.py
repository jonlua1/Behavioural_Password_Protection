import psutil

"""check if there is any running process that contains 
the given process_name
Returns True if process is running
Returns False if no such process is running"""
def check_running_process(process_name):
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if process_name.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
