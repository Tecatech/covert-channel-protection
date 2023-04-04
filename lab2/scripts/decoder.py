from math import ceil
from pcapng import FileScanner
from sys import argv

PACKET_ID = 102
TIME_INTERVAL = 1


def decode_message(dump_information):
    message = ""
    
    with open(dump_information, "rb") as fp:
        scanner = FileScanner(fp)
        blocks = list(scanner)
        
        for counter in range(PACKET_ID, len(blocks) - 1):
            try:
                difference = blocks[counter].timestamp - blocks[counter - 1].timestamp
                message += str(ceil(max(difference - TIME_INTERVAL, 0)))
            except AttributeError as e:
                pass
        
        fp.close()
    
    return bytes.fromhex(hex(int(message, 2))[2:]).decode("utf-8")


if __name__ == "__main__":
    message = decode_message(argv[1])
    print("message:", message)