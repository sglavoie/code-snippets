from multiprocessing import Process
import logging
import time

logger = logging.getLogger(__name__)


def my_func():
    process1 = Process(
        target=some_processing_func1,
        name="PB",
        args=("arg1", "arg2"),
    )
    process2 = Process(
        target=some_processing_func2,
        name="CSV",
        args=({"arg1": 1},),
    )

    process1.start()
    process2.start()

    # Loop to see whether the processes are still running. If any of them fails, kill
    # the other one to exit the automation immediately
    processes = {
        "name_process1": {
            "process": process1,
            "error": "Message to display on failure",
            "closed": False,
        },
        "name_process2": {
            "process": process2,
            "error": "Message to display on failure",
            "closed": False,
        },
    }
    num_processes = len(processes)
    processes_closed = 0
    while True:
        error = ""
        for process in processes.values():
            if process["closed"] or process["process"].is_alive():
                continue  # don't touch running or manually closed processes

            if process["process"].exitcode != 0:
                error = process["error"]
                break  # kill everything on failure, so stop checking

            # Process didn't fail and is not running anymore, so close it
            logger.debug(
                "Closing process '%s' to release its resources",
                process["process"].name,
            )
            process["process"].close()
            process["closed"] = True
            processes_closed += 1

        if error:
            for process in processes.values():
                if not process["closed"]:
                    process["process"].kill()
                    process["closed"] = True
            logger.error(error)
            raise RuntimeError(error)

        if processes_closed == num_processes:
            logger.debug("Processes finished successfully")
            break

        time.sleep(1)


def some_processing_func1(arg1: str, arg2: str):
    ...


def some_processing_func2(arg1: dict | None = None):
    ...
