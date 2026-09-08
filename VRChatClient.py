
from vrc.osc import VRChatOSC
from vrc.state import VRChatState

osc_client = VRChatOSC()
state = VRChatState()

osc_client.subscribe("Head_Contact", float, state.handle_contact)

osc_client.start()

