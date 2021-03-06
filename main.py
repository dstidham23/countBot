from twisted.internet import reactor, protocol
import countBot


def main():
    serv_ip = 'domain'
    serv_port = 6667

    f = protocol.ReconnectingClientFactory()
    f.protocol = countBot.countBot

    reactor.connectTCP(serv_ip, serv_port, f)
    reactor.run()

if __name__ == '__main__':
    main()
