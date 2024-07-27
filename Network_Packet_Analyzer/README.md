<h2>Explanation:</h2>

    Imports:
        sniff, IP, TCP, UDP, hexdump from the scapy library to handle packet capturing and analysis.

    packet_callback Function:
        This function is called whenever a packet is captured.
        It checks if the packet contains an IP layer.
        If an IP layer is present, it extracts the source and destination IP addresses and the protocol used.
        It determines whether the protocol is TCP (protocol number 6) or UDP (protocol number 17) or another type.
        It prints the source and destination IP addresses and the protocol type.
        If the packet has a TCP layer, it extracts and prints the source and destination ports, and uses hexdump to display the payload in a readable hex format.
        Similarly, if the packet has a UDP layer, it extracts and prints the source and destination ports, and uses hexdump to display the payload.
        If neither TCP nor UDP layers are present, it prints the IP payload using hexdump.
        It then prints a separator line for clarity.

    main Function:
        This function prompts the user to enter the network interface to sniff on (e.g., eth0 for Ethernet or wlan0 for Wi-Fi).
        It starts the packet sniffer on the specified interface, using the packet_callback function to process each packet.
        The sniff function captures packets on the specified interface and calls packet_callback for each packet.

    Running the Script:
        To run the script, you need to have root permissions because capturing network packets requires elevated privileges.
        You can run the script with root permissions using the sudo command in a terminal:

        sh

        sudo python3 Network_Packet_Analyze.py

        Enter the network interface you want to sniff on when prompted.

<h4>Additional Tools:</h4>
<h4>Using Wireshark:</h4>

If you prefer a graphical tool for detailed packet analysis, Wireshark is highly recommended. It provides extensive features for capturing and analyzing network traffic.

    Installing Wireshark:
        On Ubuntu:

        sudo apt-get install wireshark

        On Windows, download and install it from the official Wireshark website.

    Capturing Packets:
        Open Wireshark and select the network interface to capture packets from.
        Click "Start Capturing Packets."

    Analyzing Packets:
        Click on any captured packet to view detailed protocol information and payload data.

<h2>This enhanced script and the use of Wireshark will provide you with a comprehensive and readable analysis of network packets.</h2>
