from prettytable import PrettyTable

class ProcessScheduling:
    @staticmethod
    def repeat_scheduling():
        processes = int(input("How many processes do you want: "))
        process_lst = []

        for proc in range(1, processes + 1):
            at = int(input("Arrival time of P{}: ".format(proc)))
            bt = int(input("Burst time of P{}: ".format(proc)))
            process_lst.append((at, bt))

        # Create a PrettyTable for displaying processes, arrival time, and burst time
        table = PrettyTable()
        table.field_names = ["Process", "Arrival Time", "Burst Time"]

        for i, (at, bt) in enumerate(process_lst, start=1):
            table.add_row([f"P{i}", at, bt])

        print("Processes, Arrival Time, Burst Time in Table Form:")
        print(table)

        print("1.FCFS\n2.SJF\n3.PRIORITY\n4.ROUND ROBIN")
        process = int(input("Enter your Process: "))

        # Call the function based on the user's choice
        if process == 1:
            ProcessScheduling.fcfs(process_lst, processes)
        elif process == 2:
            print("\n1.SJF PRIMITIVE\n2.SJF NON-PRIMITIVE")
            sjf_process = int(input("Enter your Process: "))
            if sjf_process == 1:
                ProcessScheduling.sjf_primitive(process_lst, processes)
            elif sjf_process == 2:
                ProcessScheduling.sjf_non_primitive(process_lst, processes)
            else:
                print("Invalid choice. Please enter a number between 1 or 2.")
        elif process == 3:
            ProcessScheduling.priority(process_lst, processes)
        elif process == 4:
            ProcessScheduling.round_robin(process_lst, processes)
        else:
            print("Invalid choice. Please enter a number between 1 or 4.")

    @staticmethod
    def fcfs(process_lst, processes):
        process_lst.sort(key=lambda x: x[0])
        completion_time = [0] * len(process_lst)
        turnaround_time = [0] * len(process_lst)
        waiting_time = [0] * len(process_lst)
        completion_time[0] = process_lst[0][1]

        # Calculate completion time, turnaround time, and waiting time
        for i in range(1, len(process_lst)):
            completion_time[i] = completion_time[i - 1] + process_lst[i][1]
        for i in range(len(process_lst)):
            turnaround_time[i] = completion_time[i] - process_lst[i][0]
            waiting_time[i] = turnaround_time[i] - process_lst[i][1]

        # Display results in a table
        table = PrettyTable()
        table.field_names = ["Processes", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"]
        for i, (at, bt) in enumerate(process_lst, start=1):
            table.add_row([f"P{i}", at, bt, completion_time[i - 1], turnaround_time[i - 1], waiting_time[i - 1]])

        print("\nFCFS Scheduling:")
        print(table)

        # Print average waiting time and average turnaround time
        total_wt = sum(waiting_time)
        total_tat = sum(turnaround_time)
        avg_wt = total_wt / processes
        avg_tat = total_tat / processes
        print("\nAverage Waiting Time:", round(avg_wt, 4))
        print("Average Turnaround Time:", round(avg_tat, 4))
        print("\n")

    @staticmethod
    def sjf_primitive(process_lst, processes):
        process_lst.sort(key=lambda x: x[1])  # Sort by burst time
        completion_time = [0] * len(process_lst)
        turnaround_time = [0] * len(process_lst)
        waiting_time = [0] * len(process_lst)
        current_time = 0

        for i in range(len(process_lst)):
            completion_time[i] = current_time + process_lst[i][1]
            current_time += process_lst[i][1]

        # Display results in a table
        table = PrettyTable()
        table.field_names = ["Processes", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time",
                             "Waiting Time"]
        for i, (at, bt) in enumerate(process_lst, start=1):
            table.add_row([f"P{i}", at, bt, completion_time[i - 1], turnaround_time[i - 1], waiting_time[i - 1]])

        print("\nSJF (Primitive) Scheduling:")
        print(table)

    @staticmethod
    def sjf_non_primitive(process_lst, processes):
        process_lst.sort(key=lambda x: (x[0], x[1]))  # Sort by arrival time and burst time

        completion_time = [0] * len(process_lst)
        turnaround_time = [0] * len(process_lst)
        waiting_time = [0] * len(process_lst)
        current_time = 0

        for i in range(len(process_lst)):
            completion_time[i] = current_time + process_lst[i][1]
            current_time += process_lst[i][1]

        # Display results in a table
        table = PrettyTable()
        table.field_names = ["Processes", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time",
                             "Waiting Time"]
        for i, (at, bt) in enumerate(process_lst, start=1):
            table.add_row([f"P{i}", at, bt, completion_time[i - 1], turnaround_time[i - 1], waiting_time[i - 1]])

        print("\nSJF (Non-Primitive) Scheduling:")
        print(table)

    @staticmethod
    def priority(process_lst, processes):
        for i in range(processes):
            priority = int(input("Priority of P{}: ".format(i + 1)))
            process_lst[i] += (priority,)
        process_lst.sort(key=lambda x: x[2])
        completion_time = [0] * len(process_lst)
        turnaround_time = [0] * len(process_lst)
        waiting_time = [0] * len(process_lst)
        completion_time[0] = process_lst[0][1]

        # Calculate completion time, turnaround time, and waiting time
        for i in range(1, len(process_lst)):
            completion_time[i] = completion_time[i - 1] + process_lst[i][1]
        for i in range(len(process_lst)):
            turnaround_time[i] = completion_time[i] - process_lst[i][0]
            waiting_time[i] = turnaround_time[i] - process_lst[i][1]

        # Display results in a table
        table = PrettyTable()
        table.field_names = ["Processes", "Arrival Time", "Burst Time", "Priority", "Completion Time",
                             "Turnaround Time", "Waiting Time"]
        for i, (at, bt, priority) in enumerate(process_lst, start=1):
            table.add_row(
                [f"P{i}", at, bt, priority, completion_time[i - 1], turnaround_time[i - 1], waiting_time[i - 1]])

        print("\nPriority Scheduling:")
        print(table)

        # Print average waiting time and average turnaround time
        total_wt = sum(waiting_time)
        total_tat = sum(turnaround_time)
        avg_wt = total_wt / processes
        avg_tat = total_tat / processes
        print("\nAverage Waiting Time:", round(avg_wt, 4))
        print("Average Turnaround Time:", round(avg_tat, 4))
        print("\n")

    @staticmethod
    def round_robin(process_lst, processes):
        time_quantum = int(input("Enter the time quantum for Round Robin: "))

        remaining_burst_time = [process[1] for process in process_lst]
        completion_time = [0] * len(process_lst)
        turnaround_time = [0] * len(process_lst)
        waiting_time = [0] * len(process_lst)
        current_time = 0


        for i in range(len(process_lst)):
            turnaround_time[i] = completion_time[i] - process_lst[i][0]
            waiting_time[i] = turnaround_time[i] - process_lst[i][1]


        # Display results in a table
        table = PrettyTable()
        table.field_names = ["Processes", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time",
                             "Waiting Time"]
        for i, (at, bt) in enumerate(process_lst, start=1):
            table.add_row([f"P{i}", at, bt, completion_time[i - 1], turnaround_time[i - 1], waiting_time[i - 1]])

        print("\nRound Robin Scheduling:")
        print(table)

        # Print average waiting time and average turnaround time
        total_wt = sum(waiting_time)
        total_tat = sum(turnaround_time)
        avg_wt = total_wt / processes
        avg_tat = total_tat / processes
        print("\nAverage Waiting Time:", round(avg_wt, 4))
        print("Average Turnaround Time:", round(avg_tat, 4))
        print("\n")

    @classmethod
    def Repeat(cls):
        while True:
            cls.repeat_scheduling()
            repeat = input("Do you want to schedule processes again? (Y/N): ")
            if repeat.upper() != 'Y':
                break


if __name__ == "__main__":
    ProcessScheduling().Repeat()