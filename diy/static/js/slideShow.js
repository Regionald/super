//automated slide show
var slideIndex=0;
showSlide();

function showSlide(n){
var i;
const slides=document.getElementsByClassName('mySlide');
const dots=document.getElementsByClassName('dots');
for(i=0;i<slides.length;i++){
    slides[i].style.display="none";
}
slideIndex++;
if(slideIndex>slides.length){
    slideIndex=1;
}
for(i=0;i<dots.length;i++){
    dots[i].classList.remove("active");
}
if(slideIndex<1){
    slideIndex=slides.length;
}

slides[slideIndex-1].style.display="block";
dots[slideIndex-1].classList.add("active"); 
setTimeout(showSlide,6000)
}

// first websites pictutr slides
var slideIndex1=1;
showSlide1(slideIndex1);


function plusSlide1(n) {
    showSlide1(slideIndex1 += n);
  }

function currentSlide1(n){
    showSlide1(slideIndex1=n);
}


function showSlide1(n){
var i;
const slides=document.getElementsByClassName('mySlide1');
const dots=document.getElementsByClassName('dot1');
for(i=0;i<slides.length;i++){
    slides[i].style.display="none";
}
if(n>slides.length){
    slideIndex1=1;
}
if(n<1){
    slideIndex1=slides.length;
}

for(i=0;i<dots.length;i++){
    dots[i].classList.remove("active");
}


slides[slideIndex1-1].style.display="block";
dots[slideIndex1-1].classList.add("active"); 
}
// second websites pictutr slides
var slideIndex2=1;
showSlide2(slideIndex2);


function plusSlide2(n) {
    showSlide2(slideIndex2 += n);
  }

function currentSlide1(n){
    showSlide2(slideIndex2=n);
}


function showSlide2(n){
var i;
const slides=document.getElementsByClassName('mySlide2');
const dots=document.getElementsByClassName('dot2');
for(i=0;i<slides.length;i++){
    slides[i].style.display="none";
}
if(n>slides.length){
    slideIndex2=1;
}
if(n<1){
    slideIndex2=slides.length;
}

for(i=0;i<dots.length;i++){
    dots[i].classList.remove("active");
}


slides[slideIndex2-1].style.display="block";
dots[slideIndex2-1].classList.add("active"); 
}

// Third websites pictutr slides
var slideIndex3=1;
showSlide3(slideIndex3);


function plusSlide3(n) {
    showSlide3(slideIndex3 += n);
  }

function currentSlide3(n){
    showSlide3(slideIndex3=n);
}


function showSlide3(n){
var i;
const slides=document.getElementsByClassName('mySlide3');
const dots=document.getElementsByClassName('dot3');
for(i=0;i<slides.length;i++){
    slides[i].style.display="none";
}
if(n>slides.length){
    slideIndex3=1;
}
if(n<1){
    slideIndex3=slides.length;
}

for(i=0;i<dots.length;i++){
    dots[i].classList.remove("active");
}


slides[slideIndex3-1].style.display="block";
dots[slideIndex3-1].classList.add("active"); 
}
// forth websites pictutr slides
var slideIndex4=1;
showSlide4(slideIndex1);


function plusSlide4(n) {
    showSlide4(slideIndex4 += n);
  }

function currentSlide4(n){
    showSlide4(slideIndex4=n);
}


function showSlide4(n){
var i;
const slides=document.getElementsByClassName('mySlide4');
const dots=document.getElementsByClassName('dot4');
for(i=0;i<slides.length;i++){
    slides[i].style.display="none";
}
if(n>slides.length){
    slideIndex4=1;
}
if(n<1){
    slideIndex4=slides.length;
}

for(i=0;i<dots.length;i++){
    dots[i].classList.remove("active");
}


slides[slideIndex4-1].style.display="block";
dots[slideIndex4-1].classList.add("active"); 
}
