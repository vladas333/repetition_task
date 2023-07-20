from all_program import PcParts, CPU

while True:
    select = int(input("1: Show all computer parts \n"
                       "2: Show all CPU just names\n"
                       "3: Show full CPU list with spec \n"))
    if select == 1:
        print(PcParts.show_all_pc_parts())