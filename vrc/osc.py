from pythonosc import dispatcher
from pythonosc import osc_server


class VRChatOSC:
    def __init__(self, host: str = "127.0.0.1", port: int = 9001):
        self.handlers = {}

        self.host = host
        self.port = port

        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.set_default_handler(self.handle_message)

        self.server = osc_server.ThreadingOSCUDPServer(
            (self.host, self.port),
            self.dispatcher,
        )

    def subscribe(self, parameter, data_type, handler):
        self.handlers[parameter] = {"type": data_type, "handler":handler}

    def handle_message(self, address, *args):
        parameter = address.removeprefix("/avatar/parameters/")

        if parameter not in self.handlers:
            # print(f"address: {address}")
            return

        subscription = self.handlers[parameter]

        if not isinstance(args[0], subscription["type"]):
            print(f"Invalid type for {parameter}, is {type(args[0])} but should be {subscription['type']}")
            return

        subscription["handler"](*args)

    def start(self):
        print(f"Listening for VRChat OSC on {self.host}:{self.port}")
        self.server.serve_forever()
