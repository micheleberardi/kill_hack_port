import os
import psutil

def kill_processes_by_port(port):
    killed_any = False

    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        for conn in proc.info['connections']:
            if conn.laddr.port == port:
                try:
                    print(f"Found process with PID {proc.pid} and name {proc.info['name']}")

                    if proc.info['name'].startswith("docker"):
                        print("Found Docker. You might need to stop the container manually")

                    kill_process_and_children(proc)
                    killed_any = True

                except (PermissionError, psutil.AccessDenied) as e:
                    print(f"Unable to kill process {proc.pid}. The process might be running as another user or root. Try again with sudo")
                    print(str(e))

                except Exception as e:
                    print(f"Error killing process {proc.pid}: {str(e)}")

    return killed_any

def kill_process_and_children(proc):
    children = proc.children(recursive=True)
    for child in children:
        kill_process(child)

    kill_process(proc)

def kill_process(proc):
    print(f"Killing process with PID {proc.pid}")
    proc.kill()

# Example usage:
port_to_kill = 8080
if kill_processes_by_port(port_to_kill):
    print(f"Killed processes on port {port_to_kill}")
else:
    print(f"No processes found on port {port_to_kill}")
