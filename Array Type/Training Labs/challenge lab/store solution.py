# Create a list of products in stock
products = ["sneakers", "jeans", "shirts"]

# Use indexing and slicing to access specific elements in the array and print them out
print("First product: ", products[0])
print("Second and Third products: ", products[1:3])

# Create a nested list of product bundles that can be made using the products in stock
bundles = [["sneaker and jeans bundle", "sneakers", "jeans"], ["shirt and jeans bundle", "shirts", "jeans"]]

# Use iterable unpacking to print out the name of the bundle and the products it requires
for bundle in bundles:
    print(f"{bundle[0]} requires {bundle[1]} and {bundle[2]}")

# Use the enumerate() function to print out the index and the name of each bundle
for index, bundle in enumerate(bundles):
    print(f"{index}: {bundle[0]}")

# Use the range() function to loop through the nested list and print out only the bundles that include a certain product (e.g. only bundles that include jeans)
product = "jeans"
for i in range(len(bundles)):
    if product in bundles[i][1:]:
        print(bundles[i][0])

# Use a list comprehension to create a new list of bundles that include at least one product from a certain category (e.g. all bundles that include sneakers)
category = "sneakers"
sneaker_bundles = [bundle for bundle in bundles if category in bundle[1:]]
print("Bundles that include sneakers: ", sneaker_bundles)

# Create a generator expression that generates the name of the bundle and the products it requires for all bundles that include a certain product
product = "jeans"
bundle_generator = ((bundle[0], bundle[1:]) for bundle in bundles if product in bundle[1:])
for bundle in bundle_generator:
    print(bundle)

