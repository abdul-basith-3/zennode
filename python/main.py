import math


def cart_total():
    return product['Product A']*a+product['Product B']*b+product['Product C']*c


def flat_10_discount():
    discount_dict['flat_10_discount'] = 10


def bulk_5_discount():
    bulk_5_discount_for_a = 0
    bulk_5_discount_for_b = 0
    bulk_5_discount_for_c = 0
    if a > 10:
        bulk_5_discount_for_a = 0.05 * a * product['Product A']
    if b > 10:
        bulk_5_discount_for_b = 0.05 * b * product['Product B']
    if c > 10:
        bulk_5_discount_for_c = 0.05 * c * product['Product C']
    discount_dict['bulk_5_discount'] = bulk_5_discount_for_a + bulk_5_discount_for_b + bulk_5_discount_for_c


def bulk_10_discount():
    discount_dict['bulk_10_discount'] = cart_total_amount * 0.1


def tiered_50_discount():
    if a > 15:
        discount_dict['tiered_50_discount'] += (a-15) * product['Product A'] * 0.5
    if b > 15:
        discount_dict['tiered_50_discount'] += (b-15) * product['Product B'] * 0.5
    if c > 15:
        discount_dict['tiered_50_discount'] += (c-15) * product['Product C'] * 0.5


def find_max_discount():
    list = discount_dict.values()
    return max(list)


def find_discount_name(max_discount):
    key_list = list(discount_dict.keys())
    value_list = list(discount_dict.values())
    position = value_list.index(max_discount)
    return key_list[position]


def cal_wrap_amount():
    wrap_amount = 0
    if wrap_a:
        wrap_amount += a
    if wrap_b:
        wrap_amount += b
    if wrap_c:
        wrap_amount += c
    return wrap_amount


def cal_shipping_fee():
    return math.ceil(total_quantity/10)*5


if __name__ == '__main__':
    product = {
        'Product A': 20,
        'Product B': 40,
        'Product C': 50
    }
    discount_dict = {
        'flat_10_discount': 0,
        'bulk_5_discount': 0,
        'bulk_10_discount': 0,
        'tiered_50_discount': 0
    }
    wrap_a, wrap_b, wrap_c = 0, 0, 0
    a = int(input("Enter the unit of PRODUCT A($20) :"))
    if a:
         wrap_a = input("Do you want to wrap the product (y/n) :")
         if wrap_a=='y' or wrap_a=='Y':
             wrap_a=1
         elif wrap_a=='n' or wrap_a=='N':
             wrap_a=0
         else :
             print("wrong choice")
             exit()
    b = int(input("Enter the unit of PRODUCT B($40) :"))
    if b:
        wrap_b = input("Do you want to wrap the product (y/n) :")
        if wrap_b == 'y' or wrap_b == 'Y':
            wrap_b = 1
        elif wrap_b == 'n' or wrap_b == 'N':
            wrap_b = 0
        else:
            print("wrong choice")
            exit()
    c = int(input("Enter the unit of PRODUCT C($50) :"))
    if c:
        wrap_c = input("Do you want to wrap the product (y/n) :")
        if wrap_c == 'y' or wrap_c == 'Y':
            wrap_c = 1
        elif wrap_c == 'n' or wrap_c == 'N':
            wrap_c = 0
        else:
            print("wrong choice")
            exit()
    total_quantity = a+b+c
    cart_total_amount = cart_total()
    if cart_total_amount > 200:
        flat_10_discount()
    if a > 10 or b > 10 or c > 10:
        bulk_5_discount()
    if total_quantity > 20:
        bulk_10_discount()
    if total_quantity > 30 and (a > 15 or b > 15 or c > 15):
        tiered_50_discount()
    total_wrap_amount = cal_wrap_amount()
    shipping_fee = cal_shipping_fee()
    max_discount = find_max_discount()
    discount_name = find_discount_name(max_discount) if max_discount > 0 else "nill"
    total_amount = cart_total_amount - max_discount + total_wrap_amount + shipping_fee
    print()
    print()
    print("PRODUCT NAME         QUANTITY        TOTAL AMOUNT")
    if a:
        print("PRODUCT A            " + str(a) + "                  " + str(product['Product A'] * a))
    if b:
        print("PRODUCT B            " + str(b) + "                  " + str(product['Product B'] * b))
    if c:
        print("PRODUCT C            " + str(c) + "                  " + str(product['Product C'] * c))
    print()
    print(f"SUBTOTAL :${cart_total_amount}")
    print(f"DISCOUNT NAME :{discount_name}")
    print(f"DISCOUNT AMOUNT :${max_discount}")
    print(f"SHIPPING FEE :${shipping_fee}")
    print(f"GIFT WRAP FEE :${total_wrap_amount}")
    print()
    print(f"TOTAL :${total_amount}")
