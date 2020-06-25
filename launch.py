import computer_builder

my_computer = computer_builder.ComputerBuilder().build()

my_computer.computer_on()
my_computer.create_file('new_file_1.txt', 500)
my_computer.open_file('new_file_1.txt')
my_computer.create_file('new_file_2.txt', 1000)
my_computer.open_file('new_file_2.txt')
my_computer.delete_file('new_file_1.txt')
my_computer.close_file('new_file_1.txt')
my_computer.create_file('new_file_3.txt', 1500)
my_computer.computer_off()
my_computer.computer_on()
my_computer.delete_file('new_file_1.txt')
my_computer.create_file('new_file_4.txt', 5500)
my_computer.create_file('new_file_4.txt', 500)
my_computer.create_file('new_file_1.txt', 2000)
my_computer.close_file('new_file_4.txt')
my_computer.open_file('new_file_4.txt')
my_computer.delete_file('new_file_3.txt')
my_computer.computer_off()

my_computer.start()
