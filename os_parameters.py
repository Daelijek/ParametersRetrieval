from tkinter import *  # Import the Tkinter module for GUI
from tkinter import messagebox  # Import the messagebox module for displaying messages

import time  # Add this import statement for the time module
import platform  # Import the platform module to retrieve system information
import psutil  # Import the psutil module for system monitoring
import os  # Import the os module for operating system-related functionality

# Function to retrieve the operating system name and version
def get_os_name_and_version():
    try:
        return platform.system(), platform.version()  # Retrieve and return OS name and version
    except Exception as e:
        return "Error", "Cannot retrieve OS name and version"  # Handle error by returning an error message

# Function to retrieve processor information
def get_processor_info():
    try:
        return platform.processor()  # Retrieve and return processor information
    except Exception as e:
        return "Error", "Cannot retrieve processor information"  # Handle error by returning an error message

# Function to retrieve memory information
def get_memory_info():
    try:
        return psutil.virtual_memory().total / (1024 ** 3)  # Convert bytes to GB and return memory information
    except Exception as e:
        return "Error", "Cannot retrieve memory information"  # Handle error by returning an error message

# Function to retrieve disk information
def get_disk_info():
    try:
        return psutil.disk_usage('/').free / (1024 ** 3)  # Convert bytes to GB and return disk information
    except Exception as e:
        return "Error", "Cannot retrieve disk information"  # Handle error by returning an error message

def get_ip_address():
    try:
        return psutil.net_if_addrs()['Ethernet'][0].address
    except Exception as e:
        return "Error", "Cannot retrieve IP address"

def get_system_uptime():
    try:
        return round(time.time() - psutil.boot_time()) / 3600
    except Exception as e:
        return "Error", "Cannot retrieve system uptime"

def get_cpu_usage():
    try:
        return psutil.cpu_percent(interval=1)
    except Exception as e:
        return "Error", "Cannot retrieve CPU usage"

def get_running_processes():
    try:
        processes = []
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=['pid', 'name', 'memory_percent'])
                processes.append(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return processes
    except Exception as e:
        return "Error", "Cannot retrieve running processes"

def get_disk_partitions():
    try:
        partitions = psutil.disk_partitions()
        return [{part.device: part.mountpoint} for part in partitions]
    except Exception as e:
        return "Error", "Cannot retrieve disk partitions"

def get_system_architecture():
    try:
        return platform.architecture()[0]
    except Exception as e:
        return "Error", "Cannot retrieve system architecture"

def get_environment_variables():
    try:
        return dict(os.environ)
    except Exception as e:
        return "Error", "Cannot retrieve environment variables"

# Function to retrieve the current user
def get_current_user():
    try:
        return os.getlogin()  # Retrieve and return the current user
    except Exception as e:
        return "Error", "Cannot retrieve current user"  # Handle error by returning an error message

# Function to retrieve all parameters
def get_all_parameters():
    os_name, os_version = get_os_name_and_version()  # Retrieve OS name and version
    processor_info = get_processor_info()  # Retrieve processor information
    memory_info = get_memory_info()  # Retrieve memory information
    disk_info = get_disk_info()  # Retrieve disk information
    ip_address = get_ip_address()  #Retrieve ip address
    system_uptime = get_system_uptime()  #Retrieve system uptime
    cpu_usage = get_cpu_usage()  # Retrieve cpu usage
    running_processes = get_running_processes()  # Retrieve running processes
    disk_partitions = get_disk_partitions()  # Retrieve disk partitions
    system_architecture = get_system_architecture()  # Retrieve system architecture
    enviroment_variables = get_environment_variables()  #R etrieve envirenment variables
    current_user = get_current_user()  # Retrieve current user
    return {
        "OS Name": os_name,
        "OS Version": os_version,
        "Processor Information": processor_info,
        "Memory (GB)": memory_info,
        "Available Disk Space (GB)": disk_info,
        "IP Address": ip_address,
        "System Uptime": system_uptime,
        "CPU Usage": cpu_usage,
        "Running Processes": running_processes,
        "Disk Partitions": disk_partitions,
        "System Architecture": system_architecture,
        "Enviroment variables": enviroment_variables,
        "Current User": current_user
    }  # Return a dictionary containing all parameters

# Function to retrieve and display a specific parameter
def retrieve_parameter(option):
    if option == 1:
        return get_os_name_and_version()  # Retrieve and return OS name and version
    elif option == 2:
        return get_processor_info()  # Retrieve and return processor information
    elif option == 3:
        return get_memory_info()  # Retrieve and return memory information
    elif option == 4:
        return get_disk_info()  # Retrieve and return disk information
    elif option == 5:
        return get_ip_address()  # Retrieve and return the current user
    elif option == 6:
        return get_system_uptime()  # Retrieve and return all parameters
    elif option == 7:
        return get_cpu_usage()  # Retrieve and return all parameters
    elif option == 8:
        return get_running_processes()  # Retrieve and return all parameters
    elif option == 9:
        return get_disk_partitions()  # Retrieve and return all parameters
    elif option == 10:
        return get_system_architecture()  # Retrieve and return all parameters
    elif option == 11:
        return get_environment_variables()  # Retrieve and return all parameters
    elif option == 12:
        return get_current_user()  # Retrieve and return all parameters
    elif option == 13:
        return get_all_parameters()  # Retrieve and return all parameters

# Function to display the result in a messagebox
def show_result(option):
    parameter_name = ""
    if option == 1:
        parameter_name = "OS Name and Version"
    elif option == 2:
        parameter_name = "Processor Information"
    elif option == 3:
        parameter_name = "Memory (GB)"
    elif option == 4:
        parameter_name = "Available Disk Space (GB)"
    elif option == 5:
        parameter_name = "IP Address"
    elif option == 6:
        parameter_name = "System Uptime"
    elif option == 7:
        parameter_name = "CPU Usage"
    elif option == 8:
        parameter_name = "Running Processes"
    elif option == 9:
        parameter_name = "Disk Partitions"
    elif option == 10:
        parameter_name = "System Architecture"
    elif option == 11:
        parameter_name = "Enviroment variables"
    elif option == 12:
        parameter_name = "Current User"
    elif option == 13:
        parameter_name = "All Parameters"
    
    result = retrieve_parameter(option)  # Retrieve the parameter based on the option
    messagebox.showinfo(parameter_name, "{}: {}".format(parameter_name, result))  # Display the result in a messagebox

# Main function
def main():
    root = Tk()  # Create a Tkinter window
    root.title('Daelijek Parameters Retrieval')  # Set the title of the window
    root.resizable(width=False, height=False)  # Disable window resizing
    root.geometry('330x660')  # Set the dimensions of the window

    background_color = "#f0f0f0"  # Define background color
    button_color = "#4CAF50"  # Define button color
    button_hover_color = "#45a049"  # Define button hover color
    text_color = "#333333"  # Define text color
    font_style = ("Arial", 12)  # Define font style

    root.config(bg=background_color)  # Set the background color of the window

    options = [  # Define options for parameter retrieval
        ("OS Name and Version", 1),
        ("Processor Information", 2),
        ("Memory (GB)", 3),
        ("Available Disk Space (GB)", 4),
        ("IP Address", 5),
        ("System Uptime", 6),
        ("CPU Usage", 7),
        ("Running Processes", 8),
        ("Disk Partitions", 9),
        ("System Architecture", 10),
        ("Enviroment variables", 11),
        ("Current User", 12),
        ("All Parameters", 13)
    ]

    for text, option in options:  # Create buttons for each option
        button = Button(root, text=text, command=lambda option=option: show_result(option), 
                        bg=button_color, fg=text_color, font=font_style, padx=10, pady=5,
                        activebackground=button_hover_color, activeforeground=text_color)
        button.pack(pady=5)  # Pack the button into the window with padding

    root.mainloop()  # Start the main event loop

if __name__ == "__main__":
    main()  # Call the main function when the script is executed
