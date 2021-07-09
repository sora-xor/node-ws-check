from scalecodec.type_registry import load_type_registry_file
from substrateinterface import SubstrateInterface

substrate = SubstrateInterface(
    url='ws://ac22.sora2.soramitsu.co.jp:9944', #put WS endpoint here
    ss58_format=69,
    type_registry_preset='default',
    type_registry=load_type_registry_file('custom_types.json'),

)


rpc_result = substrate.rpc_request(
    method="system_chain",
    params = []
).get('result')
print(rpc_result)


