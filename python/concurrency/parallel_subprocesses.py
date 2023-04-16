from multiprocessing import Process
import datetime as dt
import subprocess
import time


def run_processes_in_parallel(
    process_commands: list[list[str]], num_processes: int = 20
):
    processes = []

    for process_command in process_commands:
        process_exec = Process(target=run_subprocesses, args=process_command)
        process_exec.start()
        processes.append(process_exec)

        while len(processes) >= num_processes:
            processes_copy = set()
            for process_exec in processes:
                if not process_exec.is_alive():
                    processes_copy.add(process_exec)

            for process_copy in processes_copy:
                processes.remove(process_copy)
            time.sleep(1)


def run_subprocesses(*args):
    saved_args = locals()
    process_command = list(saved_args["args"])

    for command in process_command:
        with subprocess.Popen(
            command, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        ) as process_exec:
            std_out, std_err = process_exec.communicate()
            if process_exec.returncode != 0:
                err_msg = "%s. Code: %s" % (
                    std_err.strip(),
                    process_exec.returncode,
                )
                raise Exception(err_msg)
            if std_out:
                log_print(std_out.decode())
            process_exec.wait()


def log_print(msg: str):
    print(f"[{dt.datetime.now().isoformat()}] {msg}")


# example usage
if __name__ == "__main__":
    import shlex

    with open("dates.txt", "r") as f:
        dates = f.read().splitlines()

        process_commands = []
        for date in dates:
            date_command = []

            date_command.append(shlex.split(f"mkdir -p ..."))
            date_command.append(shlex.split(f"cp file1 file2"))
            date_command.append(shlex.split(f"pigz -d some_file.gz"))

            process_commands.append(date_command)

        # run each list of commands sequentially from process_commands in parallel as
        # subprocesses
        run_processes_in_parallel(process_commands)
