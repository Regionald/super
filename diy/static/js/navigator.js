const homeElem = document.querySelector(".homebtn");
        const aboutElem = document.querySelector(".aboutbtn");
        const contactElem = document.querySelector(".contactbtn");
        const contactFooter=document.getElementById('contactFooter');
        const aboutFooter=document.getElementById('aboutFooter');

        const home = document.querySelector(".home");
        const about = document.querySelector(".about");
        const contact = document.querySelector(".contact");

        contact.classList.add("hide");
        about.classList.add("hide");
        homeElem.classList.add('active');


       aboutFooter.onclick=aboutSelector;
       contactFooter.onclick=contactSelector;

        function homeSelector() {

            about.classList.add("hide");
            contact.classList.add("hide");
            home.classList.remove("hide");
            //active button
            homeElem.classList.add('active');
            aboutElem.classList.remove('active');
            contactElem.classList.remove('active');
        };

        function aboutSelector() {

            home.classList.add("hide");
            contact.classList.add("hide");
            about.classList.remove("hide");
            //active button
            aboutElem.classList.add('active');
            homeElem.classList.remove('active');
            contactElem.classList.remove('active');


        };

        function contactSelector() {

            about.classList.add("hide");
            home.classList.add("hide");
            contact.classList.remove("hide");
            //active button
            contactElem.classList.add('active');
            aboutElem.classList.remove('active');
            homeElem.classList.remove('active');
        };

        homeElem.addEventListener('click', homeSelector);
        aboutElem.addEventListener('click', aboutSelector);
        contactElem.addEventListener('click', contactSelector);
