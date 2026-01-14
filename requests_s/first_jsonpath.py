import jsonpath

info={
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}

#所有作者的名字
print('所有作者的名字:')
ans=jsonpath.jsonpath(info,'$..author')
print(ans)
print('++'*30)

#第一本书的标题
print('第一本书的标题:')
ans=jsonpath.jsonpath(info,'$.store.book[0].title')
print(ans)
print('++'*30)

#第2，3，4本书的标题
print('第2，3，4本书的标题:')
ans=jsonpath.jsonpath(info,'$.store.book[1,2,3].title')
print(ans)
print('++'*30)

#所有书的标题
print('所有书的标题:')
ans=jsonpath.jsonpath(info,'$..title')
print(ans)
print('++'*30)

#所有价格大于5的书
print('所有价格大于5的书')
ans=jsonpath.jsonpath(info,'$..book[?(@.price>5)]')
print(ans)
print('++'*30)
