import logging
from part_dict import PC_PARTS_DICT
from typing import Union

logging.basicConfig(
    level=logging.DEBUG,
    filename="data.log",
    filemode="a",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d/%m/%Y %H:%M:%S",
)


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
            self.pc_parts[selected_dict]
            for key, value in self.pc_parts.items():
                if key == selected_dict:
                    selected_item_dict.update(value)
            return selected_item_dict
        except:
            logging.info("Something looking not excisting data")
            return PcParts().show_all_pc_parts()


class CPU(PcParts):
    def __init__(self, part_name: str) -> None:
        self.part_name = part_name

        self.cpu_full_dict: dict = PcParts().get_select_dict(self.part_name)

    def cpu_names(self) -> list:
        cpu_names_list = []
        try:
            for key, value in self.cpu_full_dict.items():
                cpu_names_list.append(key)
            return cpu_names_list
        except:
            logging.error("Something looking not excisting data")
            return f"Not found, you can select just:\n", self.cpu_full_dict

    def full_cpu_dict(self) -> dict:
        return self.cpu_full_dict

    def cpu_cores(self) -> dict:
        cpu_cores_dict = {}
        for key, value in self.cpu_full_dict.items():
            for key1, value1 in value.items():
                if key1 == "Core_count":
                    cpu_cores_dict[key] = value1
        return cpu_cores_dict

    def cpu_performance_speed(self) -> dict:
        cpu_perf_speed_dict = {}
        for key, value in self.cpu_full_dict.items():
            for key1, value1 in value.items():
                if key1 == "Performace_speed":
                    cpu_perf_speed_dict[key] = value1
        return cpu_perf_speed_dict

    def cpu_boost_speed(self) -> dict:
        cpu_boost_speed_dict = {}
        for key, value in self.cpu_full_dict.items():
            for key1, value1 in value.items():
                if key1 == "Boost_speed":
                    cpu_boost_speed_dict[key] = value1
        return cpu_boost_speed_dict

    def cpu_tdp(self) -> dict:
        cpu_tdp_dict = {}
        for key, value in self.cpu_full_dict.items():
            for key1, value1 in value.items():
                if key1 == "TDP":
                    cpu_tdp_dict[key] = value1
        return cpu_tdp_dict

    def add_cpu(
        self,
        cpu_name: str,
        core_count: int,
        performance_speed: float,
        boost_speed: float,
        tdp: int,
    ) -> dict:
        self.cpu_full_dict[cpu_name] = {
            "Core_count": core_count,
            "Performace_speed": performance_speed,
            "Boost_speed": boost_speed,
            "TDP": tdp,
        }
        return self.cpu_full_dict
    
    def find_cpu_by_name_with_spec(self, find_cpu_name: str) -> dict:
        search_cpu_spec = {}
        for key, value in self.cpu_full_dict.items():
            if find_cpu_name in key:
                search_cpu_spec[key] = value
        return search_cpu_spec
    

    def find_cpu_by_name_just_names(self, find_cpu_name: str) -> list:
        search_cpu_names = []
        for key, value in self.cpu_full_dict.items():
            if find_cpu_name in key:
                search_cpu_names.append(key)
        return search_cpu_names

# all_pc = PcParts()
# print(all_pc.show_all_pc_parts())
# print(all_pc.get_select_dict("CPU"))
cpu_cl = CPU("CPU")
# print(f"Just CPU names list: \n", cpu_cl.cpu_names())
# print(f"Full list with spec:\n", cpu_cl.full_cpu_dict())
# print(f"CPU names with Cores count:\n", cpu_cl.cpu_cores())
# print(f"CPU names with Performace speed:\n", cpu_cl.cpu_performance_speed())
# print(f"CPU names with Boost speed:\n", cpu_cl.cpu_boost_speed())
# print(f"CPU names with thermal design power (TDP):\n", cpu_cl.cpu_tdp())
# print(cpu_cl.add_cpu("Intel Core i7-12700K", 12, 3.6, 5, 125))
cpu_name = "Intel"
print(f"Search CPU-{cpu_name},, return with spec: \n", cpu_cl.find_cpu_by_name_with_spec(cpu_name))
print(f"Search CPU-{cpu_name}, return just list: \n", cpu_cl.find_cpu_by_name_just_names(cpu_name))
