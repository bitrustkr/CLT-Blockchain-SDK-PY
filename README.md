<img src="./docs/images/logo.png" width="100%" height="auto">

# CLT-Blockchain-SDK

* [usage](#usage)
* [development](#development)
* [interface](https://github.com/bitrustkr/CLT-Blockchain-SDK-PY/blob/master/docs/API.md)

## usage

```bash
$ pip install EITRI
```

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

## development

* test

test 코드를 실행하기 위해 `test.py` 실행

```bash
$ python test.py
```

* deploy

```bash
$ ./publish.sh
```

배포하기 위해 **`setup.py`**의 **`version`** 변경

[pip](https://pypi.org/project/EITRI) 배포