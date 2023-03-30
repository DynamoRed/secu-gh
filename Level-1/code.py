'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stucked then read the hint                   ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple

MAX_TOTAL = 1e7
MAX_AMOUNT = 1e5
MAX_QUANTITY = 1e2

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0
    
    for item in order.items:
        if item.type == 'payment':
            if item.amount < MAX_AMOUNT and item.amount > MAX_AMOUNT*-1:
                net += item.amount
        elif item.type == 'product':
            if item.quantity > 0 and item.quantity < MAX_QUANTITY and item.amount < MAX_AMOUNT and item.amount > 0:
                net -= item.amount * item.quantity
            if net < MAX_TOTAL*-1 or net > MAX_TOTAL:
                return("Max total excedeed")
        else:
            return("Invalid item type: %s" % item.type)
    
    if net != 0:
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
