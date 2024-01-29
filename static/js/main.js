// const toggleBtn = document.querySelector(".navbar_toggleBtn")
// const menu = document.querySelector(".navbar_menu")
// const icons = document.querySelector(".navbar_icons")

// toggleBtn.addEventListener("click", () => {
//   menu.classList.toggle("nav_active")
//   icons.classList.toggle("nav_active")
// })

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

// 텍스트 애니메이션

var words = ['안녕하세요, jool 입니다 :)', 'SERVICE 1', 'SERVICE 2'],
  part,
  i = 0,
  offset = 0,
  len = words.length,
  forwards = true,
  skip_count = 0,
  skip_delay = 15,
  speed = 80;
var wordflick = function () {
  setInterval(function () {
    if (forwards) {
      if (offset >= words[i].length) {
        ++skip_count;
        if (skip_count == skip_delay) {
          forwards = false;
          skip_count = 0;
        }
      }
    } else {
      if (offset == 0) {
        forwards = true;
        i++;
        offset = 0;
        if (i >= len) {
          i = 0;
        }
      }
    }
    part = words[i].substr(0, offset);
    if (skip_count == 0) {
      if (forwards) {
        offset++;
      } else {
        offset--;
      }
    }
    $('.word').text(part);
  }, speed);
};

$(document).ready(function () {
  wordflick();
});

// Initialize Swiper

var swiper = new Swiper(".mySwiper", {
  rewind: true,
  autoplay: {
    delay:3000,
    disableOnInteraction: false,
  },
  speed: 600,
  parallax: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
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