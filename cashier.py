def main():
	list = []

	while True:

		item = input("Item (enter \"done\" when finished): ")

		if item == "done":
			break

		price = int(input("Price: "))

		quantity = int(input("Quantity: "))

		list.append({"item": item, "price": price, "quantity": quantity})


	print(list)

	print ("-------------------------------------------------")
	print(" ")
	print("PANDA")
	print("Reciet")
	print(" ")
	print ("-------------------------------------------------")

	print("QTY || item || price")
	total = 0
	for items in list:
		print("%d %s %d $" %(items.get("quantity"),items.get("item"), items.get("quantity")*items.get("price") ))
		total = total + items.get("quantity")*items.get("price")
	print ("-------------------------------------------------")
	print("Total: %d $" %(total))


if __name__ == '__main__':
	main()
