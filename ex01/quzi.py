import random
import datetime
st = datetime.datetime.now()
ed = datetime.datetime.now()
aa = 0
def main():
    shutudai()
    kaito()

def shutudai():
    listq = ["サザエの旦那の名前は？","カツオの妹の名前は？","クラオはカツオから見てどんな関係？"]
    listn = random.randint(0,2)
    print(listq[listn],listn)
    return listn
    

def kaito():
    s = input("答えるんだ：")
    listk = [["マスオ","ますお"],["ワカメ","わかめ"],["甥","おい","甥っ子","おいっこ"]]
    if s in listk[shutudai()]:
        print("正解!!!")
        return True
    else:
        print("出直してこい")
        return False
main()