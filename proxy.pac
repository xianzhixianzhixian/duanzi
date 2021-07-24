function FindProxyForURL(url, host) {
  if (isInNet(host, '172.17.0.0', '255.255.0.0')) {
    return 'SOCKS5 127.0.0.1:8888'
  }
  if (isInNet(host, '172.22.0.0', '255.255.0.0')) {
    return 'SOCKS5 127.0.0.1:8888'
  }
  return 'DIRECT'
}
