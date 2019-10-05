# getting started

* 설치

```bash
$ pip install EITRI
```

* import

```python
from EITRI.eitri import eitri

if __name__ == "__main__":
  # eitri 노드 연결정보 전달
  e = eitri(
    ip = "127.0.0.1",
    port = "3000",
    user = "user",
    password = "password"
  )

  last_block = e.block.get_last_block()
  print(last_block)

  block = e.block.get_block(0)
  print(block)

  node = e.node.get_info()
  print(node)

  txhash = e.transaction.get_transaction('0x123')
  print(txhash)

  validators = e.validator.get_validators()
  print(validators)
```