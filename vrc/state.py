class VRChatState:
    def __init__(self):
        self.contact_active = False

    def handle_contact(self, value):
        self.contact_active = value
        print(f"Contact: {value}")

    def test_contact(self, value):
        self.contact_active = value
        print(f"TEST VALUE: {value}")
