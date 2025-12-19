class User:
    """
    Represents a bank user.
    Demonstrates encapsulation using private attributes.
    """

    def __init__(self, nic: str, name: str, contact: int):
        self.__nic = nic
        self.__name = name
        self.__contact = contact

    # NIC
    def get_nic(self) -> str:
        return self.__nic

    def set_nic(self, nic: str) -> None:
        self.__nic = nic

    # Name
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str) -> None:
        self.__name = name

    # Contact
    def get_contact(self) -> int:
        return self.__contact

    def set_contact(self, contact: int) -> None:
        self.__contact = contact
