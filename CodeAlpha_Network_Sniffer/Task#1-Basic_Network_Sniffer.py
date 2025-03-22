from scapy.all import sniff, hexdump

def packet_callback(packet):
     print(packet.show())  # Show detailed packet information
     print(hexdump(packet))  # Display raw packet data in hex format

print("Sniffer running...")
sniff(prn=packet_callback, store=False)