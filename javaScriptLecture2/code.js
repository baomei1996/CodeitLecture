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




    function removeUnnecessaryInfo(users) {
      const processedUserList = users.map((user) => {
        const keys = Object.keys(user);
        const processedUser = {};
        keys.forEach((key) => {
          if (key === 'name' || key === 'email') {
            processedUser[key] = user[key];
          }
        });
        return processedUser;
      });
      const p = new Promise((resolve) => {
        setTimeout(() => { resolve(processedUserList); }, 1000); 
      });
      return p;
    }
    
    fetch('https://jsonplaceholder.typicode.com/users')
      .then((response) => response.json())
      .then((result) => removeUnnecessaryInfo(result))
      .then((result) => {
        console.log(result);
      })
      .catch((error) => {
        console.log(error);
      })
      .finally(() => {
        console.log('This job will be done by server soon!');
      });

