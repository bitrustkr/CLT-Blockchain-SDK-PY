# Interface

* [connection](https://github.com/bitrustkr/CLT-Blockchain-SDK-PY#usage)
* [account](#account)
* [transaction](#transaction)
* [block](#block)
* [validator](#validator)
* [node](#node)
* [network](#network)


## account


## transaction

* **`get_transaction`**

트랜잭션 정보조회

```python
txhash = e.transaction.get_transaction('0x123')

{'hash': '51D316323EC833DCEBF0BE0B05C4910FD3FBC2DD0990C027AD26351EE375317F', 'height': '11202', 'index': 0, 'nonce': '1', 'time': '2019-08-23T00:34:42.6221603Z', 'sender': '742B63B4AA18361B903E9F164E5B6873706239FB', 'receiver': 'D99E8939133DEB1475E03AE4B21657E46C8E594F', 'gas': '12345', 'action': 1, 'amount': '1', 'pub_key': '5C8854D05667EDE74458EF3DE0DA3F50647AF4049EC258AA01EAD1E6E2C91945', 'sig': 'BC86BC6BD1D0A0B7F8B33A0E3482AD9131FAD85DD080AC4A950BF78196FC17F5EF14BAF898796D3DEA67A5A71DF7946EC1B0A4876BCCE1E1578D20D4E7284109'}
```

조회대산 트랜잭션 해시 전달

## block

* **`get_last_block`**

최신 블록정보 조회

```python
last_block = e.block.get_last_block()
  
{'block': {'block_id': {'hash': 'DF9D3EE29714224D6059A2B4A78C229FC0BB06E73B4DE9EB675AB52D044239C4', 'parts': {'total': '1', 'hash': '1F4A3B0367008252A725B28CD2B4CF9F8F5BA7C94EFFF351381DEECD235C6561'}}, 'header': {'version': {'block': '10', 'app': '1'}, 'chain_id': 'logichain-dev', 'height': '11603', 'time': '2019-08-22T01:47:01.9879485Z', 'num_txs': '1', 'total_txs': '1', 'last_block_id': {'hash': 'D20617735CE97ADED7DE88AA50A1D60F183729BF3A926B3F073DEFCF87F3D993', 'parts': {'total': '1', 'hash': 'F2971BE97176B4782675D1A9AC331A76BB381100C0EBEAB3073D79ECDCED7DAE'}}, 'last_commit_hash': '1FC65E838A575523E8447F971B90110E2C740629FD450A0E639488930E40D6F0', 'data_hash': 'A010956BD83B8BE563CEF6B1B466C8F6E4BA20966D61631B7129A03E6274DD75', 'validators_hash': '38237AA5AFE05DD628F68D4BE719A0EAC031D4F2561CED086C305162D58C91EC', 'next_validators_hash': '38237AA5AFE05DD628F68D4BE719A0EAC031D4F2561CED086C305162D58C91EC', 'consensus_hash': '048091BC7DDC283F77BFBF91D73C44DA58C3DF8A9CBC867405D8B7F3DAADA22F', 'app_hash': 'C77EE3A4C2E781DECC93BA904B55BF3574003E074AA77341677DFD814C52F34A', 'last_results_hash': '', 'evidence_hash': '', 'proposer_address': '5860EA6D8D8BD810812D43D1F44157EEB89F5F57'}}, 'txs': ['1FF50FD83EA636979E7EB1DF6CC0399F22358950914A8D69D0DB13775F6923B5']}
```

* **`get_block`**

블록조회

```python
block = e.block.get_block(0)

{'block': {'block_id': {'hash': 'DF9D3EE29714224D6059A2B4A78C229FC0BB06E73B4DE9EB675AB52D044239C4', 'parts': {'total': '1', 'hash': '1F4A3B0367008252A725B28CD2B4CF9F8F5BA7C94EFFF351381DEECD235C6561'}}, 'header': {'version': {'block': '10', 'app': '1'}, 'chain_id': 'logichain-dev', 'height': '11603', 'time': '2019-08-22T01:47:01.9879485Z', 'num_txs': '1', 'total_txs': '1', 'last_block_id': {'hash': 'D20617735CE97ADED7DE88AA50A1D60F183729BF3A926B3F073DEFCF87F3D993', 'parts': {'total': '1', 'hash': 'F2971BE97176B4782675D1A9AC331A76BB381100C0EBEAB3073D79ECDCED7DAE'}}, 'last_commit_hash': '1FC65E838A575523E8447F971B90110E2C740629FD450A0E639488930E40D6F0', 'data_hash': 'A010956BD83B8BE563CEF6B1B466C8F6E4BA20966D61631B7129A03E6274DD75', 'validators_hash': '38237AA5AFE05DD628F68D4BE719A0EAC031D4F2561CED086C305162D58C91EC', 'next_validators_hash': '38237AA5AFE05DD628F68D4BE719A0EAC031D4F2561CED086C305162D58C91EC', 'consensus_hash': '048091BC7DDC283F77BFBF91D73C44DA58C3DF8A9CBC867405D8B7F3DAADA22F', 'app_hash': 'C77EE3A4C2E781DECC93BA904B55BF3574003E074AA77341677DFD814C52F34A', 'last_results_hash': '', 'evidence_hash': '', 'proposer_address': '5860EA6D8D8BD810812D43D1F44157EEB89F5F57'}}, 'txs': ['1FF50FD83EA636979E7EB1DF6CC0399F22358950914A8D69D0DB13775F6923B5']}
```

조회대상 블록번호 전달

## validator

* **`get_validators`**

validator 조회

```python
validators = e.validator.get_validators()

{'block_height': '13967', 'validators': [{'address': '5860EA6D8D8BD810812D43D1F44157EEB89F5F57', 'pub_key': 'A33519E2814109F0EF3189971E6C18A2BA05EDD91BB328DEBA2B930B8160656A', 'voting_power': '10', 'proposer_priority': '0'}]}
```

## node

* **`get_info`**

노드정보 조회

```python
node = e.node.get_info()

{'node_info': {'protocol_version': {'p2p': '7', 'block': '10', 'app': '1'}, 'id': '0213ec14f96f6d1d5084f65a4109ff5550d131b2', 'listen_addr': 'tcp://0.0.0.0:26656', 'network': 'logichain-dev', 'version': '0.32.1', 'channels': '4020212223303800', 'moniker': 'yongseokkwon-pc', 'other': {'tx_index': 'on', 'rpc_address': 'tcp://127.0.0.1:26657'}}, 'sync_info': {'latest_block_hash': '57C34CC87C731A2649B0201039FFB94A51B180CBF094FDC1FBBD1ABCA7AA8C81', 'latest_app_hash': '86416F5FFF6619489F9A42A0636E07438A86F1649A5983DD7B032AFC35FF310A', 'latest_block_height': '14977', 'latest_block_time': '2019-08-23T01:56:22.4903998Z', 'catching_up': False}, 'validator_info': {'address': '5860EA6D8D8BD810812D43D1F44157EEB89F5F57', 'pub_key': 'A33519E2814109F0EF3189971E6C18A2BA05EDD91BB328DEBA2B930B8160656A', 'voting_power': '10', 'proposer_priority': '0'}, 'net_info': {'listening': True, 'listeners': ['Listener(@)'], 'n_peers': '0', 'peers': []}}
```

## network