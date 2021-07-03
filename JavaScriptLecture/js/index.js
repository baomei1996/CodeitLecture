//객체 (Object)

let codeit = {
  name: 'Codeit',
  bornYear: 2017,
  isVeryNice: true,
  worstCourse: null,
  bestCourse: {
    tltle: 'Javascript Beginner',
    language: 'JavaScript'
  }
}

//수정
codeit.name ='Bomi';
console.log(codeit.name);

//추가 
codeit.bestCourse.teacher ='Bomi';
console.log(codeit.bestCourse.teacher);

//삭제 
console.log(codeit.worstCourse);
delete codeit.worstCourse;
console.log(codeit.worstCourse);

//property의 존재 여부를 확인하는 방법
console.log(codeit.name !== undefined);

//propertyName in object

console.log('name' in codeit);


let greetings = {
  sayHello: function(name) {
    console.log(`${name} Hello`)
  },

  sayBye: function(name) {
    console.log(`${name} Bye`)
  },
}

greetings.sayHello('bomi')
greetings.sayBye('bomi')

for (let k in codeit) {
  console.log(k);
  console.log(codeit[k]);
}

let myDate = new Date();

console.log(myDate) //현재 시간

//'YYYY-MM-DDThh:mm:ss'

let myDate1 = new Date('1996-07-14T21:30:05')
console.log(myDate1)

// YYYY, MM, DD, hh, mm, ss month는 0월 -> 1월 

let myDate2 = new Date(2017, 4, 18, 19, 11, 16)

//time stamp 

let timeDiff = myDate.getTime() - myDate1.getTime() ;

console.log(timeDiff + '밀리초')
console.log(timeDiff /1000 + '초')
console.log(timeDiff / 1000/ 60 + '분')
console.log(timeDiff /1000 / 60 / 60 + '시간')
console.log(myDate1.getFullYear())
console.log(myDate1.getMonth())
console.log(myDate1.getDate()) //일
console.log(myDate1.getDay()) //요일
console.log(myDate1.getHours())
console.log(myDate1.getMinutes())
console.log(myDate1.getSeconds())


//array

let courseRanking = [
  'A',
  'B',
  'C',
  'D',
  'E',
  'F'
]


for(let i = 0; i < courseRanking.length; i++) {
  console.log(courseRanking[i]);

}
 

console.log(courseRanking.length)
courseRanking[6] = 'G' //배열 추가 
console.log(courseRanking)
courseRanking[1] = 'AA'
console.log(courseRanking)
//delete 는 아예 사라지지 않고 값만 사라짐 emmpty
// a번 인덱스로부터 b개 삭제 c를 추가함 splice(a, b, c)
//추가 삭제 수정이 가능함 
courseRanking.splice(1, 2)
console.log(courseRanking)


// 배열의 첫 요소 삭제 
courseRanking.shift();

// 배열의 마지막 요소를 삭제 
courseRanking.pop()
                              
// 배열의 첫 요소로 값 추가
courseRanking.unshift('Nice')

// 배열의 마지막 요소로 값 추가 
courseRanking.push('Hi Codeit')

//for ...of 
//for(변수 of 배열)
//for in 문은 객체에 적합 배열에는 사용을 권장하지 않음

for (let element of courseRanking) {
  console.log(element)
}

// 다차원 배열 
let twoDemensional = [[1, 2], [3, 4]]

console.log(twoDemensional[0][0]) //1

//숫자형 메서드 

let myNumber = 0.3591;

//toFixed(0~100)
console.log(myNumber.toFixed(3)) //4번째 자리 반올림 하여 0.359
console.log(Number(myNumber.toFixed(7))) //0.3591000 --> string type number로 형 변환]


//toString 파라미터로 받은 숫자의 진법으로 숫자를 변환해줌
let myNumber2 = 255;

console.log(myNumber2.toString(10))
console.log(myNumber2.toString(2))
console.log(myNumber2.toString(8))
console.log(myNumber2.toString(16))



