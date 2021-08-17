//document.getElementById("button-name").addEventListener("click", ()=>{eel.get_random_name()}, false);
document.getElementById("button-product1").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product2").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product3").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product4").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product5").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product6").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product7").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product8").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product9").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product10").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product11").addEventListener("click", ()=>{eel.get_random_number()}, false);
document.getElementById("button-product12").addEventListener("click", ()=>{eel.get_random_number()}, false);

document.getElementById("button-coinInput").addEventListener("click", ()=>{eel.insertCoin()}, false);

//document.getElementById("button-date").addEventListener("click", ()=>{eel.get_date()}, false);
//document.getElementById("button-ip").addEventListener("click", ()=>{eel.get_ip()}, false);

eel.expose(prompt_alerts);
function prompt_alerts(description) {
  alert(description);
}

var total = 0;
eel.expose(insertCoin);
function insertCoin(coin = 10) {
    
    const btn1 = document.getElementById("button-product1");
    const btn2 = document.getElementById("button-product2");
    const btn3 = document.getElementById("button-product3");
    const btn4 = document.getElementById("button-product4");
    const btn5 = document.getElementById("button-product5");
    const btn6 = document.getElementById("button-product6");
    const btn7 = document.getElementById("button-product7");
    const btn8 = document.getElementById("button-product8");
    const btn9 = document.getElementById("button-product9");
    const btn10 = document.getElementById("button-product10");
    const btn11 = document.getElementById("button-product11");
    const btn12 = document.getElementById("button-product12");

    var products = {
        "products": [
            {
                "id": 1,
                "name": "Coca-Cola",
                "type": "Softdrink",
                "price": 140,
                "button": btn5,
                "image": "https://storage.googleapis.com/golden-wind/nextlevelweek/05-plantmanager/1.svg",
                "lane": ["1", "2"],
            },
        ]
    }

    
    
    const products1 = {
        "prices": [120, 160, 120, 120, 140, 160, 140, 130, 130, 160, 140, 130],
        "buttons": [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12],
    };

    const inventory = [
        {name: 'Coca', quantity: 2, price: 160},
        {name: 'Coffee', quantity: 0, price: 140},
        {name: 'Water', quantity: 5, price: 120}
    ];

    total += coin;
    document.getElementById("visorText").innerHTML = `${total}円`;

    if (total >= 120) { 
        btn1.classList.replace('redLed', 'greenLed');
        btn3.classList.replace('redLed', 'greenLed');
        btn4.classList.replace('redLed', 'greenLed');
    }

    if (total >= 130) { 
        btn8.classList.replace('redLed', 'greenLed');
        btn9.classList.replace('redLed', 'greenLed');
        btn12.classList.replace('redLed', 'greenLed');
    }

    if (total >= 140) { 
        btn5.classList.replace('redLed', 'greenLed');
        btn7.classList.replace('redLed', 'greenLed');
        btn11.classList.replace('redLed', 'greenLed');
    }

    if (total >= 160) { 
        btn2.classList.replace('redLed', 'greenLed');
        btn6.classList.replace('redLed', 'greenLed');
        btn10.classList.replace('redLed', 'greenLed');
    }

    products.forEach(product => {
        Object.entries(product).forEach(([key, value]) => {
            console.log(`${key} ${value}`);
            document.getElementById("visorText").innerHTML = `${value}`;
            if(total >= product.products["price"]) {
                product.products["button"].replace('redLed', 'greenLed');
            }
        });
    });
}


