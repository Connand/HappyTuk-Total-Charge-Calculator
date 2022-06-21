# 快樂玩遊戲(樂意)儲值總和計算機(下方附JavaScript版)
利用簡單的Python爬蟲取得所有儲值紀錄來計算儲值總額  
全部下載後放在同一個資料夾然後執行Sel.exe  
登入需要自己手動，而且reCAPTCHA驗證會搞你，需要有點耐心，只要10分鐘內登入即可  
# 注意
若有無法開啟的狀況，可能需要更新chromedriver.exe  
https://chromedriver.chromium.org/  
通常找`Latest stable release`那邊下載，然後放到跟程式同一個資料夾即可
# Known Bug
如果儲值紀錄只有一頁時，結果可能輸出0元
# 圖片
若網頁介面跟下圖不同，此程式可能無法使用  
![0](https://i.imgur.com/GWAzQ59.png)
# JavaScript版
1. 登入https://www.mangot5.com/Index/Billing/History?cPage=1
2. 按F12並點主控台(Console)
3. 貼上下方程式碼並按下Enter
```js
function getElementByXpath(path) {
    return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
}

let baseURL = "https://www.mangot5.com/Index/Billing/History?cPage="
let pageNum = 1
let totalAmount = 0;
let breakCtrl = false;

while(!breakCtrl){
    await new Promise((resolve, reject) => {
        setTimeout(function() {
            RES = $.post(baseURL + pageNum, function(data, status) {
                document.write(data);
                document.close();
                
                try{
                    table = getElementByXpath("//table[@class='table table-small-font table-striped']");
                    trlist = table.childNodes[3].getElementsByTagName("tr");
                    for(let item of trlist){
                        //console.log(item);
                        tdlist = item.getElementsByTagName('td');
                        txt = tdlist[1].innerHTML;
                        //console.log(txt.substr(0, txt.search(" TWD")));
                        totalAmount = totalAmount + parseInt(txt.substr(0, txt.search(" TWD")));
                    }
                    //console.log(totalAmount);
                } catch {
                    breakCtrl = true;
                }
            });
            pageNum = pageNum + 1;
            resolve();
        }, 2000);
    });
    if(pageNum >= 1000) break;
}
console.log(totalAmount);
alert('ㄋ總共課了 ' + totalAmount + ' 元')
```
