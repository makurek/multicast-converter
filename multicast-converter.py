# This is the MAC address that we are going to convert into multicast IP addresses
# How to properly return a value from a function - is it a good practice to create an object within a function and return it?

test_mac_address = "01:00:5e:0b:01:02"

def multicast_mac_to_ip(mac_address):

    mac_bytes = mac_address.split(":")
    ip_mask = 0xe0000000
    ip_mask |= int(mac_bytes[3], 16) << 16
    ip_mask |= int(mac_bytes[4], 16) << 8
    ip_mask |= int(mac_bytes[5], 16)
    result = list()
#    print("{:x}".format(ip_mask))

    for i in range(0,31):
        temp_ip = ip_mask
        temp_ip |= i << 23
        o4 = (temp_ip & 0xff000000) >> 24
        o3 = (temp_ip & 0x00ff0000) >> 16
        o2 = (temp_ip & 0x0000ff00) >> 8
        o1 = (temp_ip & 0x000000ff)
        result.append(str(o4) + "." + str(o3) + "." + str(o2) + "." + str(o1))
    return result

print(multicast_mac_to_ip(test_mac_address))


