def process_transaction(tx):
  if tx['receipt_status'] == '1':
    # Do something with the transaction
    print("Transaction was successful")
  else:
    # Do something else
    print("Transaction was not successful")

# Example usage
tx = {'receipt_status': '1'}
process_transaction(tx)
