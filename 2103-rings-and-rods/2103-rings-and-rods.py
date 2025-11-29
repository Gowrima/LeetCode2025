class Solution:
    def countPoints(self, rings: str) -> int:
        num_rods = 0
        color_to_rod = {}
        i = 0

        # rings = rings[::-1]   

        if len(rings) < 6:
            return 0

        while i < len(rings):
            color = rings[i]
            rod = rings[i + 1]

            if rod not in color_to_rod:
                color_to_rod[rod] = set()

            color_to_rod[rod].add(color)

            i += 2

        for rod in color_to_rod:
            if len(color_to_rod[rod]) == 3:
                num_rods += 1

        return num_rods
