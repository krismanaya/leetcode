
def defangIPaddr(address:str) -> str:
        """
        this function takes 
        in a address "1.1.1.1" and
        returns a string "1[.]1[.]1[.]:
        :type address: str
        :rtype: str
        """
        addressArray = address.split('.')
        return "[.]".join(addressArray)

address = "255.100.50.0"
address2 = "1.1.1.1"
# easy cases
assert defangIPaddr(address=address) == "255[.]100[.]50[.]0"
assert defangIPaddr(address=address2) == "1[.]1[.]1[.]1"

