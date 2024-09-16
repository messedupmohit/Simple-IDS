from ids.detector import start_sniffing
import logging

if __name__ == "__main__":
    logging.basicConfig(filename='logs/ids.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    print("[*] Starting IDS...")
    start_sniffing("eth0")
