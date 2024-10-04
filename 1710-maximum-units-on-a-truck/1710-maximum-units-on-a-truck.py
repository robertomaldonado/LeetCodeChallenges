"""
boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]
"""
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        def find_max_unit_box(boxTypes: List[List[int]]) -> int:
            max_unit_box_index = -1
            max_units = 0
            for i in range(len(boxTypes)):
                if boxTypes[i][1] > max_units:
                    max_units = boxTypes[i][1]
                    max_unit_box_index = i
            return max_unit_box_index

        unit_count = 0
        remaining_truck_size = truckSize
        while remaining_truck_size > 0:
            max_unit_box_index = find_max_unit_box(boxTypes)
            if max_unit_box_index == -1:
                break
            box_count = min(remaining_truck_size, boxTypes[max_unit_box_index][0])
            unit_count += box_count * boxTypes[max_unit_box_index][1]
            remaining_truck_size -= box_count
            boxTypes[max_unit_box_index][1] = -1
        return unit_count
