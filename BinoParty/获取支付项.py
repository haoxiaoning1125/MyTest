from model.model_payment import PurchaseItem
items = [x.row2dict() for x in PurchaseItem.query.filter(PurchaseItem.app_id == 1).all()]
itemid = 'com.elestorm.bingoadventure.new_themesale_10'
x = [item for item in items if item['identifier'] == itemid]


for item in items:
    x = item['identifier'].split('.')[-1]
    if re.match('new_themesale', x):
        print x

