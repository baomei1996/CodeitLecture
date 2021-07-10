try {
  console.log('에러 전');
  const codeit = '코드잇';
  codeit = 'codeit';//error
  const language = 'JavaScript';
  console.log(language);

} catch (e){
  console.log('에러 후');
}


function printMembers (members) {
  try {
    for (const member of members) {
      console.log(member)
    }
    
  } catch (error) {
    console.error(error);
    alert(`${error.name}가 발생했습니다. 콘솔창을 확인해 주세요.`)
  }
}

const teamA = ['상혜', '혜진', '지혜', '혜선'];
printMembers(teamA);

const codeit = { name: 'codeit' };
printMembers(codeit);

const teamB = ['영훈', '재훈', '종훈', '장훈'];
printMembers(teamB);