from prettytable import PrettyTable

table = PrettyTable(["food", "price"])
table.add_row(["ham", "$2"])
table.add_row(["eggs", "$1"])
table.add_row(["spam", "$4"])
print(table)
