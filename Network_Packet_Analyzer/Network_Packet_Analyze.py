from scapy.all import sniff, IP, TCP, UDP, hexdump

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        if protocol == 6:
            proto_name = "TCP"
        elif protocol == 17:
            proto_name = "UDP"
        else:
            proto_name = "Other"

        print(f"Source IP: {ip_src}")
        print(f"Destination IP: {ip_dst}")
        print(f"Protocol: {proto_name}")

        if packet.haslayer(TCP):
            tcp_layer = packet.getlayer(TCP)
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
            print("TCP Payload:")
            hexdump(tcp_layer.payload)
        elif packet.haslayer(UDP):
            udp_layer = packet.getlayer(UDP)
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
            print("UDP Payload:")
            hexdump(udp_layer.payload)
        else:
            print("IP Payload:")
            hexdump(packet[IP].payload)

        print("-" * 50)

def main():
    interface = input("Enter the interface you want to sniff on (e.g., eth0, wlan0): ")
    print(f"Starting packet sniffer on {interface}...")
    sniff(iface=interface, prn=packet_callback, store=0)

if __name__ == "__main__":
    main()
