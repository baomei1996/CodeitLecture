const rank = ["효준", "유나", "민환", "재하"];

const [macbook, ipad, airpods, coupon] = rank;

console.log('macbook')
console.log('ipad')
console.log('airpods')
console.log('coupon')

let note = '유나'
let pen = '효준'

console.log('note')
console.log('pen')

[note, pen] = [pen, note];

console.log('note')
console.log('pen')

//구조 분해
const macbook = {
  title: '맥북 프로 16형',
  price: 3690000,
  memory: '16GB',
  storage: '1TB SSD 저장 장치',
  display: '16형 Retina 디스플레이',
};

// const title = macbook.title;
//const price = macbook.price

const { title: product, price, color = "silver" }  = macbook;

console.log(product);
console.log(price);