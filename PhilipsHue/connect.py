from phue import Bridge

__all__ = ["Connect"]

class Connect:
    """
    Creates a connection to the Philips Hue bridge.
    Takes the IP of the bridge as argument.
    """
    def __init__(self, bridgeIP, *args, **kwargs):
        self.conn = Bridge(bridgeIP)
        self.conn.connect()
        self.api = self.conn.get_api()

if __name__ == "__main__":
    conn = Connect()
    print(conn.api)
