import computer_builder

my_computer = computer_builder.ComputerBuilder().build()

my_computer.computer_on()
my_computer.create_file('new_file.txt')
my_computer.install_game('GTA 3')
my_computer.create_file('some_code.py')
my_computer.install_game('Mario Forever')
my_computer.delete_file('new_file.txt')
my_computer.delete_game('Mario Forever')
my_computer.delete_file('new_file_file.txt')
my_computer.delete_file('new_file.txt')
my_computer.install_game('Mario Forever')
my_computer.install_game('Mario Forever')
my_computer.computer_off()

my_computer.start()
