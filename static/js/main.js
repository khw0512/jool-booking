// const toggleBtn = document.querySelector(".navbar_toggleBtn")
// const menu = document.querySelector(".navbar_menu")
// const icons = document.querySelector(".navbar_icons")

// toggleBtn.addEventListener("click", () => {
//   menu.classList.toggle("nav_active")
//   icons.classList.toggle("nav_active")
// })

// tabmenu 구현
// 1. 탭 버튼과 탭 내용 부분들을 querySelectorAll을 사용해 변수에 담는다.
const tabItem = document.querySelectorAll(".tab__item");
const tabContent = document.querySelectorAll(".tab__content");

// 2. 탭 버튼들을 forEach 문을 통해 한번씩 순회한다.
// 이때 index도 같이 가져온다.
tabItem.forEach((item, index) => {
  // 3. 탭 버튼에 클릭 이벤트를 준다.
  item.addEventListener("click", (e) => {
    // 4. 버튼을 a 태그에 만들었기 때문에, 
    // 태그의 기본 동작(링크 연결) 방지를 위해 preventDefault를 추가한다.
    e.preventDefault(); // a 
    
    // 5. 탭 내용 부분들을 forEach 문을 통해 한번씩 순회한다.
    tabContent.forEach((content) => {
      // 6. 탭 내용 부분들 전부 active 클래스를 제거한다.
      content.classList.remove("active");
    });

    // 7. 탭 버튼들을 forEach 문을 통해 한번씩 순회한다.
    tabItem.forEach((content) => {
      // 8. 탭 버튼들 전부 active 클래스를 제거한다.
      content.classList.remove("active");
    });

    // 9. 탭 버튼과 탭 내용 영역의 index에 해당하는 부분에 active 클래스를 추가한다.
    // ex) 만약 첫번째 탭(index 0)을 클릭했다면, 같은 인덱스에 있는 첫번째 탭 내용 영역에
    // active 클래스가 추가된다.
    tabItem[index].classList.add("active");
    tabContent[index].classList.add("active");
  });
});


// 모바일 네비케이션 모달
const modalOpenButton = document.getElementById('modalOpenButton');
const modalCloseButton = document.getElementById('modalCloseButton');
const modal = document.getElementById('modalContainer');
const navbtn = document.getElementById("modalOpenButton");

modalOpenButton.addEventListener('click', () => {
  modal.classList.remove('hidden');
  navbtn.classList.add('hidden');
});

modalCloseButton.addEventListener('click', () => {
  modal.classList.add('hidden');
  navbtn.classList.remove('hidden');
});

// Date Picker

// 선언한 TextBox에 DateTimePicker 위젯을 적용한다.
$('#fromDate').datetimepicker({
  language : 'ko', // 화면에 출력될 언어를 한국어로 설정한다.
  pickTime : false, // 사용자로부터 시간 선택을 허용하려면 true를 설정하거나 pickTime 옵션을 생략한다.
  defalutDate : new Date() // 기본값으로 오늘 날짜를 입력한다. 기본값을 해제하려면 defaultDate 옵션을 생략한다.
});

$('#toDate').datetimepicker({
  language : 'ko',
  pickTime : false,
  defalutDate : new Date()
});


// tabs
$(document).ready(function(){
  $('ul.tabs li').click(function(){
    var tab_id = $(this).attr('data-tab');

    $('ul.tabs li').removeClass('current');
    $('.tab-content').removeClass('current');

    $(this).addClass('current');
    $("#"+tab_id).addClass('current');
  });
});

