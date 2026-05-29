class Action:
    name = "Unnamed Action"
    # If True, the action's result is shown in the status bar and the
    # editor contents are left unchanged. Use for read-only / metric
    # actions like Count Words, Count Characters, Sum All, etc.
    info = False

    def run(self, text: str) -> str:
        raise NotImplementedError
