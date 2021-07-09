const toDoList = document.querySelector('#to-do-list');

// 1. updateToDo 함수를 완성해 주세요.
function updateToDo(event) {
  if(event.target.classList.contains('item')){
    event.target.classList.toggle('done');

  }

}

function addToDo(text) {
  const newToDo = document.createElement('li');
  newToDo.textContent = text;
  newToDo.classList.add('item');
  toDoList.append(newToDo);


}
// 2. 각 li 태그가 아니라 하나의 태그에만 이벤트 핸들러를 등록해 주세요.
toDoList.addEventListener('click', updateToDo);

// 테스트 코드
const newToDo = document.createElement('li');
newToDo.textContent = '가계부 정리하기';
newToDo.classList.add('item');
toDoList.append(newToDo);

addToDo('보들이 놀아주기');
addToDo('코드잇 강의듣기');



toDoList.children[2].addEventListener('click', function(e) {e.stopPropagation()});