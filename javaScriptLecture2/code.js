// fetch('https://jsonplaceholder.typecode.com/users')
//   .then((response) => response.text())
//   .then((result) => { const users = JSON.parse(result) });
// json.parse => json 객체를 자바스크립트 객체로 변환
// json.stringify => 자바스크립트 객체를 json 객체로 변환

//조회
const newMember = {
  name: 'Jerry', 
  email: 'jerry@codeitmail.kr',
  department: 'engineering',
};

fetch('https://learn.codeit.kr/api/members', {
  method: 'POST',
  body: JSON.stringify(newMember),
  
})
  .then((response) => response.text())
  .then((result) => { console.log(result) })

//수정
  const modifyMember = {
    name: 'Alice',
    email: 'alice@codeitmail.kr',
    department: 'marketing',
  };
  fetch('https://learn.codeit.kr/api/members/2', {
    method: 'PUT',
    body: JSON.stringify(modifyMember),
    
  })
    .then((response) => response.text())
    .then((result) => { console.log(result) })
  //삭제

  fetch('https://learn.codeit.kr/api/members/2', {
    method: 'DELETE',
  })
    .then((response) => response.text())
    .then((result) => { console.log(result) });

