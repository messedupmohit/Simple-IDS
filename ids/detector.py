from scapy.all import sniff, IP, TCP
from .config import SUSPICIOUS_IPS, SUSPICIOUS_PORTS
import logging

def detect_intrusion(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        
        if ip_src in SUSPICIOUS_IPS or ip_dst in SUSPICIOUS_IPS:
            alert = f"[ALERT] Suspicious IP detected: {ip_src} -> {ip_dst}"
            print(alert)
            logging.info(alert)
        
        if packet.haslayer(TCP):
            port_src = packet[TCP].sport
            port_dst = packet[TCP].dport
            
            if port_src in SUSPICIOUS_PORTS or port_dst in SUSPICIOUS_PORTS:
                alert = f"[ALERT] Suspicious Port detected: {port_src} -> {port_dst} (Packet: {packet.summary()})"
                print(alert)
                logging.info(alert)

def start_sniffing(interface):
    print(f"[*] IDS running on {interface}")
    sniff(iface=interface, filter="ip", prn=detect_intrusion)
