from scapy.all import *

def print_dns_pkt(x):
  src = '[src: ' + x.payload.src + ']'
  sport = '[sport: ' + str(x.payload.sport) + ']'
  dst = '[dst: ' + x.payload.dst + ']'
  dport = '[dport: ' + str(x.payload.dport) + ']'
  direction = ' '.join([src, sport, dst, dport])
  return x.summary() + '\n' + direction

def main():
  show_interfaces()
  if_index_str = input('Please select the interface to sniff with if_index: ')
  if_index = int(if_index_str)
  iface = dev_from_index(if_index)
  sniff(iface=iface, filter='udp and port 53',prn=print_dns_pkt)


if __name__ == '__main__':
  main()