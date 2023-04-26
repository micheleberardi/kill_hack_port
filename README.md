# Kill Processes by Port (Python)
This Python script uses the psutil library to find and kill processes listening on a specified port, along with their child processes. It is particularly useful when you need to free up a port occupied by a process that should no longer be running.

Requirements
Python 3.6+
psutil library
To install the psutil library, run the following command:

```
pip install psutil
````

# Usage
To use the script, first modify the port_to_kill variable to the desired port number you want to free up. Then, simply run the script:

```
Copy code
python kill_processes_by_port.py
```
The script will find and kill processes listening on the specified port and their child processes. It will also display information about the processes being killed, such as their process ID (PID) and name.


# Example
Copy code
```
port_to_kill = 8080
if kill_processes_by_port(port_to_kill):
    print(f"Killed processes on port {port_to_kill}")
else:
    print(f"No processes found on port {port_to_kill}")
This example will find and kill processes listening on port 8080.
```

# Note
Killing a process with this script might require administrative privileges, especially if the process is running as another user or root. If you encounter a permission error, try running the script with administrative privileges (e.g., using sudo on Linux).
