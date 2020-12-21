class Printer:
    def __init__(self, ppm) -> None:
        super().__init__()
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self) -> None:
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self) -> bool:
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newTask) -> None:
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pagerate