class Computer:
    turned_on = False
    open_apps = []
    files = []
    games = []
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

    def create_file(self, filename):
        if self.turned_on:
            self.logger.append("Creating a file '" + str(filename) + "'...")
            if str(filename) not in self.files:
                self.files.append(str(filename))
                self.logger.append("New file '" + str(filename) + "' has been created")
                return
            self.logger.append("'" + filename + "' already exists on your computer")

    def delete_file(self, filename):
        if self.turned_on:
            self.logger.append("Removing a file '" + str(filename) + "'...")
            if str(filename) in self.files:
                self.files.remove(str(filename))
                self.logger.append("'" + str(filename) + "' has been removed from your computer")
                return
            self.logger.append("'" + filename + "' does not exist on your computer")

    def install_game(self, game):
        if self.turned_on:
            self.logger.append("'" + str(game) + "' is installing. Please, wait")
            if str(game) not in self.games:
                self.games.append(str(game))
                self.logger.append("New game '" + str(game) + "' has been installed")
                return
            self.logger.append("'" + game + "' is already installed on your computer")

    def delete_game(self, game):
        if self.turned_on:
            self.logger.append("Removing a game '" + str(game) + "'...")
            if str(game) in self.games:
                self.games.remove(str(game))
                self.logger.append("'" + str(game) + "' has been removed from your computer")
                return
            self.logger.append("'" + game + "' does not exist on your computer")
    
    def open_application(self, app_name):
        if self.turned_on:
            self.logger.append("'" + app_name + "' is opening. Please, wait")
            if app_name in files or app_name in games:
                self.open_apps.append(app_name)
                self.logger.append("'" + app_name + "' is open now")
                return
            self.logger.append("'" + app_name + "' does not exist on your computer")

    def close_app(self, app_name):
        if self.turned_on:
            self.logger.append("'" + app_name + "' is closing...")
            if app_name in open_apps:
                self.open_apps.remove(app_name)
                self.logger.append("'" + app_name + "' has been closed")
                return
            self.logger.append("'" + app_name + "' does not exist on your computer")
