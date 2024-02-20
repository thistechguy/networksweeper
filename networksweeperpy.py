import os


# Function to print instructions
def instructions():
    print(f'Welcome to Network Sweeper! Please select and option below:')
    print('1. Check if host is up')
    # TODO - Add option to scan network subnet after creating logic
    # print('2. Scan subnet range for active/down hosts')
    print('2. Exit')

    command = input('Please select option: ')
    return command


def enter_cont():
    input('Press ENTER to continue...')


while True:
    user_input = instructions()
    if user_input == '1':
        host = input('Enter hostname: ')
        response = os.system(f'ping -c 1 {host}')

        if response == 0:
            print(f'{host} is UP!\n')
            enter_cont()
        else:
            print(f'{host} is DOWN!\n')
            enter_cont()

    # TODO: Add logic to ping subnet for active/inactive IPs

    else:
        print('You have exited NetworkSweeper. Thank you using this program!')
        break
