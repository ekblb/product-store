from db import session

import tables

result = session.query(tables.Customer.customer_id).first()

print(result)
