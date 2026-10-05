# Made By Ricky L.

dataList = []
dataHash = {}


def clear():
	dataList.clear()
	dataHash.clear()

def addEnd(value):
	dataList.append(value)
	if not value in dataHash:
		dataHash[value] = 1
	else:
		dataHash[value] += 1

def removeStart():
	if len(dataList) == 0:
		return None

	firstValue = dataList[0]
	if firstValue in dataHash:
		dataHash[firstValue] -= 1
		if dataHash[firstValue] == 0:
			del dataHash[firstValue]

	return dataList.pop(0)
	
def containsLinear(value):
	return value in dataList
	
def containsConstant(value):
	return True if value in dataHash and dataHash.get(value) > 0 else False
	
