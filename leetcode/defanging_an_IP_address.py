class Solution:
    def defang_IP_addr(self, address: str) -> str:
        index = 0
        for id in address:
            if id == ".":
                # address = f"{address[:index]}[.]{address[index + 1:]}"
                address = "[.]".join((address[:index], address[index + 1:]))
                index += 2
            index += 1
        return address

    def defang_IP_addr_extra_memory(self, address: str) -> str:
        ip_address = []
        for i in address:
            if i == ".":
                ip_address.append("[.]")
            else:
                ip_address.append(i)
        return "".join(ip_address)


address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

solution = Solution()
result = solution.defang_IP_addr(address)
print(result)
