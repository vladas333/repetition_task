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
            logging.info(
                "Something looking not excisting data in: PcParts.get_select_dict"
            )
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
            logging.error("Something looking not excisting data in: CPU.cpu_names")
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

    def add_cpu(
        self,
        cpu_name: str,
        core_count: int,
        performance_speed: float,
        boost_speed: float,
        tdp: int,
    ) -> Union[dict, list]:
        try:
            self.cpu_full_dict[cpu_name] = {
                "Core_count": int(core_count),
                "Performace_speed": float(performance_speed),
                "Boost_speed": float(boost_speed),
                "TDP": int(tdp),
            }
            logging.info(f"New CPU was added")
            return self.cpu_full_dict
        except:
            logging.error("Couldn't add new CPU to database")
            return f"Something go wrong. CPU wasn't added\n"


class Cooler(PcParts):
    def __init__(self, part_name: str) -> None:
        self.part_name = part_name
        self.cpu_full_dict: dict = PcParts().get_select_dict(self.part_name)

    def full_cooler_dict(self) -> dict:
        return self.cpu_full_dict