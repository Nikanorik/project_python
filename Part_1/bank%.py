import math
def main():
    square_area = float(input('Enter square area place: '))
    paint_price = float(input('Enter price paint 5l: '))
    amount_capacity(square_area)
    amount_work_hour(square_area)
    paint = price_color(square_area,paint_price)
    work_place = price_work(square_area)
    general_price_work = paint+work_place
    print(f'General price work and paint {general_price_work}')
def amount_capacity(square_area):
    capacity = math.ceil((square_area/10))
    print(f'Amount 5 litr capacity {capacity}')
def amount_work_hour(square_area):
    work_hour = square_area/10*8
    print(f'Amount work hour {work_hour}')
def price_color(square_area, paint_price):
    price = math.ceil(square_area/10)*paint_price
    print(f'General price paint in roubles: {price}')
    return price
def price_work(square_area):
    price = square_area/10*2000
    print(f'Price work {price}')
    return price
if __name__=='__main__':
    main()









