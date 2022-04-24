def profit(info):
    lucro = ((info['sell_price'] * info['inventory']) - (info['cost_price'] * info['inventory']))
    lucro = round(lucro, 2)
    return lucro

print(profit({

    'cost_price' : 32.67,
    'sell_price': 45.00,
    'inventory' : 1200,

}))
