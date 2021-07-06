const myNumberTag = document.getElementById('myNumber');
const decreaseBtn = document.getElementById('decrease');
const increaseBtn = document.getElementById('increase');

let myNumber = +myNumberTag.textContent;

decreaseBtn.onclick = function() {
  myNumber--;
  myNumberTag.textContent = myNumber;
};

increaseBtn.onclick = function() {
  myNumber++;
  myNumberTag.textContent = myNumber
}

const coloreBtn = document.getElementsByClassName('color-btn');

for(let btn of coloreBtn) {
  btn.onclick = function() {
    myNumberTag.style.color = btn.dataset.color;
  }
}

const gradeBtn = document.querySelector('#grade');

gradeBtn.onclick = function() {
  alert('정답입니다!👏🏻');
}

//element.children 자식 요소 노드 - element의 자식요소 모음
//element.firstElementChild 자식 요소 노드 - element의 첫 번째 자식 요소 하나 
//element.lastElementChild 자식 요소 노드 - element의 마지막 자식 요소 하나
//element.parentElementChild 부모 요소 노드 - element의 부모 요소 하나
//element.previousElementSibling 형제 요소 노드 - element의 이전 혹은 좌측에 있는 요소 하나
//element.nextElementSibling 형제 요소 노드 - element의 우측 혹은 다음에 있는 요소 하나

//요소 노드 주요 프로퍼티
// innerHTML 내용을 추가 변경
// outerHTML
// textContext 단순히 텍스트만 다르기 때문에 특수문자도 텍스트화함 <li>