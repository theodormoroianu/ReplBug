import testcase.bug_list


def run_bugs(bugs: list[str]):
    """
    Runs the list of provided bugs
    """
    for bug in bugs:
        if not bug.startswith("bug"):
            bug = "bug" + bug
        if bug not in testcase.bug_list.bug_list:
            raise ValueError(f"Bug {bug} not found")
        testcase.bug_list.bug_list[bug]()

def test():
    pass