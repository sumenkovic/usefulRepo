def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
        item_total += v
    print("Total items: " + str(item_total))

def addToInventory(inventory, addItems):
        for i in range(len(addItems)):
            if addItems[i] in inventory.keys():
                inventory[addItems[i]] += 1
            else:
                inventory.setdefault(addItems[i], 1)
        return inventory


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'wooden planks':26}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

print("Before looting ")
displayInventory(stuff)
print()
print("After looting")
stuff = addToInventory(stuff, dragonLoot)
displayInventory(stuff)
