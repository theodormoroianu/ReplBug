import socket, logging, os


def get_free_port():
    """
    Returns a free port.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def run_command(command: str) -> int:
    """
    Runs a command in the terminal.
    """
    print(f"Running command: {command}")
    logging.info(f"Running command: {command}")
    retcode = os.system(command)
    return retcode
