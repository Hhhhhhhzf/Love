const YEAR = 2017, MONTH = 8, DAY = 10;

function formatNum(num) {
    num = parseInt(num);
    if(num < 10)
        num = "0" + num;
    return num;
}

function clock() {
    const now = new Date();
    let ny = now.getFullYear();
    let nm = now.getMonth() + 1;
    let nd = now.getDate();
    let y, m, d;
    if(nm < MONTH || (nm == MONTH && nd < DAY)){
        y = ny - YEAR - 1;
    }
    else y = ny - YEAR;

    if(nm < MONTH){
        nm += 12;
    }
    m = nm - MONTH;
    if (nd < DAY){
        m -= 1;
        nd += 31;
    }
    d = nd - DAY;


    let h = now.getHours();
    let min = now.getMinutes();
    let s = now.getSeconds();
    let ms = parseInt("" + now.getMilliseconds()/10);


    document.getElementById("sum_day");
    document.getElementById("year").innerHTML = y;
    if (m < 10)
        m = '零' + m;
    document.getElementById("month").innerHTML = m;
    document.getElementById("day").innerHTML = formatNum(d);
    document.getElementById("hour").innerHTML = formatNum(h);
    document.getElementById("minute").innerHTML = formatNum(min);
    document.getElementById("second").innerHTML = formatNum(s);
    document.getElementById("ms").innerHTML = formatNum(ms);
}
function start(){
    setInterval(clock,10);
}

