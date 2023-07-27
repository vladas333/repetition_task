from all_program import PcParts, CPU, Cooler


separate_line = "* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * "


def selected_cpu_input(part_n) -> dict:
    cpu_name = str(input(f"Enter CPU name\n"))
    core_count = int(input(f"Enter Core count\n"))
    performance_speed = float(input(f"Enter performance speed (ex. 0.0)\n"))
    boost_speed = float(input(f"Enter boost speed (ex. 0.0)\n"))
    tdp = int(input(f"Enter thermal design power (TDP)\n"))
    return CPU(part_n).add_cpu(
        cpu_name, core_count, performance_speed, boost_speed, tdp
    )


while True:
    select = int(
        input(
            f"So, what you need? Just select what to show: \n"
            "1: Available computer parts \n"
            "2: Select CPU \n"
            "3: Select Cooler \n"
            "0: Exit \n"
        )
    )
    print(separate_line)
    if select == 1:
        print(PcParts().show_all_pc_parts())
        print(separate_line)
    elif select == 2:
        part_name = "GPU"
        set_part = CPU(part_name)
        cpu_select = int(
            input(
                f"1: All CPU just names\n"
                "2: Full CPU dict with spec \n"
                "3: CPU names with Cores count\n"
                "4: CPU names with Performace speed \n"
                "5: CPU names with Boost speed \n"
                "6: CPU names with thermal design power (TDP) \n"
                "7: Search CPU by part of the name \n"
                "8: Add CPU \n"
                "0: Back \n"
            )
        )
        print(separate_line)
        if cpu_select == 1:
            print(f"All available CPU:\n", set_part.cpu_names())
            print(separate_line)
        elif cpu_select == 2:
            print(f"All available CPU with spec:\n", set_part.cpu_names())
            print(separate_line)
        elif cpu_select == 3:
            print(f"CPU names with Cores count:\n", set_part.cpu_names())
            print(separate_line)
        elif cpu_select == 4:
            print(f"CPU names with Performace speed:\n", set_part.cpu_names())
            print(separate_line)
        elif cpu_select == 5:
            print(f"CPU names with Boost speed:\n", set_part.cpu_names())
            print(separate_line)
        elif cpu_select == 6:
            print(f"CPU names with thermal design power (TDP):\n", set_part.cpu_names())
            print(separate_line)
        elif cpu_select == 7:
            cpu_name = input(f"Write a part of CPU name \n")
            show_cpu = int(
                input(f"1: Show just name \n" "2: Show names with spec\n" "3: Back\n")
            )
            if show_cpu == 1:
                print(f"Finded CPU:\n", set_part.find_cpu_by_name_just_names(cpu_name))
                print(separate_line)
            elif show_cpu == 7:
                print(f"Finded CPU:\n", set_part.find_cpu_by_name_with_spec(cpu_name))
                print(separate_line)
            elif cpu_select == 3:
                print(separate_line)
                continue
        elif cpu_select == 8:
            print(f"Added CPU: \n", selected_cpu_input(part_name))
            print(separate_line)
        elif cpu_select == 0:
            print(separate_line)
            continue
    elif select == 3:
        print(f"All available CPU coolers:\n", Cooler("Cooler").full_cooler_dict())
        print(separate_line)
    elif select == 0:
        exit()
