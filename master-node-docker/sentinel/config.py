false, true = False, True
CONTRACT_ABI = [ { "constant": True, "inputs": [ { "name": "_addr", "type": "address" } ], "name": "getVpnUsage", "outputs": [ { "name": "", "type": "uint256", "value": "0" }, { "name": "", "type": "uint256", "value": "0" }, { "name": "", "type": "uint256", "value": "0" }, { "name": "", "type": "bool", "value": False } ], "payable": False, "stateMutability": "view", "type": "function" }, { "constant": True, "inputs": [], "name": "getBalance", "outputs": [ { "name": "", "type": "uint256", "value": "10000000000" } ], "payable": False, "stateMutability": "view", "type": "function" }, { "constant": True, "inputs": [], "name": "getDueAmount", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": False, "stateMutability": "view", "type": "function" }, { "constant": False, "inputs": [ { "name": "_to", "type": "address" }, { "name": "_amount", "type": "uint256" }, { "name": "_isVpnPayment", "type": "bool" } ], "name": "transferAmount", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function" }, { "constant": True, "inputs": [], "name": "getVpnAddrs", "outputs": [ { "name": "", "type": "address[]", "value": [] } ], "payable": False, "stateMutability": "view", "type": "function" }, { "constant": False, "inputs": [ { "name": "_addr", "type": "address" }, { "name": "_usedBytes", "type": "uint256" }, { "name": "_amount", "type": "uint256" }, { "name": "_timestamp", "type": "uint256" } ], "name": "addVpnUsage", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function" }, { "inputs": [ { "name": "initialSupply", "type": "uint256", "index": 0, "typeShort": "uint", "bits": "256", "displayName": "initial Supply", "template": "elements_input_uint", "value": "10000000000" } ], "payable": False, "stateMutability": "nonpayable", "type": "constructor" } ]
CONTRACT_ADDRESS = '0xBa03044D73f7AB55F0d09adA463A7a8Cc78f321F'
CONTRACT_NAME = 'Sentinel_test'
COINBASE_PASSWORD = 'sent123'
CONV_UNITS = 1e-06
