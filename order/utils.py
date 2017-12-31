import uuid

def get_order_id():
	uid = uuid.uuid4()
	return "ORD" + str(uid)[:7].upper()
