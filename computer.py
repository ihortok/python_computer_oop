class Computer:
    turned_on = False
    open_programs = []
    files = []
    logger = []

    def __init__(self, processor, ram, storage, display, keyboard, mouse):
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.display = display
        self.keyboard = keyboard
        self.mouse = mouse

    def start(self):
        if len(self.logger) > 0:
            for log in self.logger:
                print log + ';'
            return
        print 'No action has been added'

    def computer_on(self):
        if not self.turned_on:
            self.logger.append("Launching...")
            self.turned_on = True
            self.logger.append("Hello! Your computer has been turned on")

    def computer_off(self):
        if self.turned_on:
            self.logger.append("Turning off...")
            self.turned_on = False
            self.logger.append("Good buy!")

    def create_file(self, filename, file_size):
        if self.turned_on:
            self.logger.append("Creating a file '" + str(filename) + "'...")
            if self.storage.used_memory + file_size < self.storage.memory:
                if len(self.files) > 0:
                    for file in self.files:
                        if file['name'] == filename:
                            return self.logger.append("'" + filename + "' already exists on your computer")
                    self.save_file(filename, file_size)
                else:
                    self.save_file(filename, file_size)
            else:
                self.logger.append("Not enough memory. You can remove something to free some space")

    def save_file(self, filename, file_size):
        self.files.append({'name': filename, 'size': file_size})
        self.storage.used_memory += file_size
        free_space = self.storage.memory - self.storage.used_memory
        self.logger.append("New file '" + str(filename) + "' has been created")
        self.logger.append(str(file_size) + " MB of memory used. Free space: " + str(free_space) + " MB")
    
    def delete_file(self, filename):
        if self.turned_on:
            self.logger.append("Removing a file '" + str(filename) + "'...")
            if str(filename) in self.files:
                self.files.remove(str(filename))
                self.storage.used_memory -= file_size
                free_space = self.storage.memory - self.storage.used_memory
                self.logger.append("'" + str(filename) + "' has been removed from your computer")
                return
            self.logger.append("'" + filename + "' does not exist on your computer")
    
    def open_file(self, file_name):
        if self.turned_on:
            self.logger.append("'" + file_name + "' is opening. Please, wait")
            if file_name in files:
                self.open_programs.append(file_name)
                self.logger.append("'" + file_name + "' is open now")
                return
            self.logger.append("'" + file_name + "' does not exist on your computer")

    def close_file(self, file_name):
        if self.turned_on:
            self.logger.append("'" + file_name + "' is closing...")
            if file_name in open_programs:
                self.open_programs.remove(file_name)
                self.logger.append("'" + file_name + "' has been closed")
                return
            self.logger.append("'" + file_name + "' does not exist on your computer")
