class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {"blank": 0, "sign": 1, "digit": 2, "dot": 3},
            {"digit": 2, "dot": 3},
            {"digit": 2, "dot": 4, "e": 5, "blank": 8},
            {"digit": 4},
            {"digit": 4, "e": 5, "blank": 8},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7, "blank": 8},
            {"blank": 8},
        ]
        current_state = 0
        for char in s:
            if char.isdigit():
                char_type = "digit"
            elif char in ("-","+"):
                char_type = "sign"
            elif char in ("e", "E"):
                char_type = "e"
            elif char == ".":
                char_type = "dot"
            elif char == " ":
                char_type = "blank"
            else:
                return False
            if char_type not in states[current_state]:
                return False
            current_state = states[current_state][char_type]

        return current_state in (2,4,7,8)