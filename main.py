from pkg.firewall_class import Firewall

from typing import Dict

def main(file_path: str) -> Dict[str, bool]:
    """main function to validate the input data"""

    try:
        firewall_instance = Firewall(file_path)
        result = firewall_instance.read_csv()
        return result
    except Exception as error:
        raise error


if __name__ == "__main__":

    main('input_file.csv')

    # miscillaneious use of accept_packet function
    print(firewall_instance.accept_packet("inbound", "tcp", 82, "192.168.1.1"))
    print(firewall_instance.accept_packet("inbound", "tcp", 34, "192.168.1.1-192.168.2.5"))

