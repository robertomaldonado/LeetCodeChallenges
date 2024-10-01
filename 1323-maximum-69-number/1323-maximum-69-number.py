class Solution:
    def maximum69Number (self, num: int) -> int:
        num_as_list = list(str(num))
        for i in range(len(num_as_list)):
            if num_as_list[i] == "6":
                num_as_list[i] = "9"
                break
        return int("".join(num_as_list))

        