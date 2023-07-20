import logging
from part_dict import PC_PARTS_DICT
from typing import Union

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

class PcParts:
    def __init__(self) -> None:
        self.pc_parts = PC_PARTS_DICT

    def show_all_pc_parts(self) -> list:
        part_list = []
        for key, val in self.pc_parts.items():
            part_list.append(key)
        return part_list
    
    def get_select_dict(self, selected_dict: str) -> Union[dict, list]:
        selected_item_dict: dict = {}
        try:
            for key, value in self.pc_parts.items():
                if selected_dict in key:
                    selected_item_dict.update(value)
            selected_item_dict.pop()
            return selected_item_dict
        except:
            logging.info("Something looking not excisting data")
            return PcParts().show_all_pc_parts()
    
class CPU(PcParts):
    def __init__(self, part_name : str) -> None:  
        self.part_name = part_name

        self.cpu_list = PcParts().get_select_dict(self.part_name)

    def cpu_names(self) -> list:
        cpu_names_list = []
        try:
            for key, value in self.cpu_list.items():
                cpu_names_list.append(key)
            return f"Just CPU name list:\n", cpu_names_list
        except:
            logging.error("Something looking not excisting data")
            return f"Not found, can select just:\n", self.cpu_list

    
    def full_cpu_list(self) -> list:
        cpu_list = []
        for key, value in self.pc_parts.items():
            if self.part_name in key:
                cpu_list.append(value)
        return cpu_list


    def cpu_cores(self) -> dict:
        cpu_cores_dict = {}
        for key, value in self.cpu_list.items():
            for key1, value1 in value.items():
                if key1 == "Core_count":
                    cpu_cores_dict[key]= value1
        return cpu_cores_dict

    def cpu_performance_speed() -> list:
        pass

    def cpu_boost_speed() -> list:
        pass

    def cpu_tdp() -> list:
        pass

all_pc = PcParts()
# print(all_pc.show_all_pc_parts())
# print(all_pc.get_select_dict("SMTH"))
cpu_cl = CPU("CPU")
print(cpu_cl.cpu_names())
# print(f"Full list with spec:\n", cpu_cl.full_cpu_list())
# print(f"CPU names with Cores count:\n", cpu_cl.cpu_cores())