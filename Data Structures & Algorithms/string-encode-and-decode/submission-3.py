class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for string in strs:
            encoded_string += f"{len(string)}#{string}"
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        length_string = ""

        index = 0
        decoded_list = []
        while index < len(s):
            while s[index].isnumeric():
                length_string += s[index]
                index += 1

            length = int(length_string)
            # stops at the # simple
            # 4#abcd, we want to get 2:6 => index + 1: index + length + 1

            length_string = ""
            decoded_list.append(s[index + 1: index + length + 1])
            index = index + length + 1

        return decoded_list
