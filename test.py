from EITRI.eitri import eitri

from EITRI import utils

if __name__ == "__main__":
  e = eitri(
    ip = "127.0.0.1",
    port = "3000",
    user = "user",
    password = "password"
  )

  last_block = e.block.get_last_block()
  print(last_block)
  print()

  block = e.block.get_block(0)
  print(block)
  print()

  node = e.node.get_info()
  print(node)
  print()

  txhash = e.transaction.get_transaction('0x123')
  print(txhash)
  print()

  validators = e.validator.get_validators()
  print(validators)
  print()

  print(utils.fromConvert(1))
  print(utils.toConvert(1))
  print(utils.unitMap())
  print(utils.isAddress(1))
  print(utils.isTxHash(1))
  print(utils.isBlockHash(1))