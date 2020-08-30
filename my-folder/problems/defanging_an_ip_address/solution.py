class Solution:
    def defangIPaddr(self, address: str) -> str:
        ip = list(address)
        for i in range(len(ip)):
            if ip[i] == ".":
                ip[i] = "[.]"
        return ''.join(ip)