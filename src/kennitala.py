from ast import Str
from datetime import datetime
from xmlrpc.client import Boolean

class Kennitala(object):
    """Class that handles common 
    Args:
        object (object): Extends the Class Object 
    """

    def __init__(self) -> None:
        pass

    def filter(self, unfiltered_text) -> Str: 
        """filters out everything in the string that isn't a number

        Args:
            kennitala_string (Str): unfiltered string
        """ 
        return ''.join([str(x) if x.isdigit() else "" for x in unfiltered_text])
    
    def validate(self, kennitala) -> Boolean:
        """Validates the icelandic personal kennitala, does not work for company kennitala
        Args:
            kennitala (Str): string containing a kennitala

        Returns:
            Boolean: [description]
        """
        if len(kennitala) != 10: return False
        if not kennitala.isdigit(): return False
        # Makes sure that the first six digits is a valid 
        try:
            datetime.strptime(kennitala[:6], '%d%m%y')
        except ValueError as e:
            return False
        # useless to check if the two random digits are between 20-99 since there are exceptions
        # century check
        if(kennitala[-1] != "9" and kennitala[-1] != "0"): return False
        # checksum check

        csum = (3*int(kennitala[0]) + 
                2*int(kennitala[1]) + 
                7*int(kennitala[2]) +
                6*int(kennitala[3]) +
                5*int(kennitala[4]) +
                4*int(kennitala[5]) +
                3*int(kennitala[6]) +
                2*int(kennitala[7])
                ) % 11
        csum = csum if csum == 0 else 11 - csum
        if(int(kennitala[8]) != csum): return False
        return True


if __name__ == "__main__":
    k = Kennitala()
    print(k.validate("2411992159"))
    print(k.validate("4411992194"))
    print(k.validate("24AA992159"))
    print(k.validate("241199AA59"))