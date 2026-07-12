/*==================================================
            IT Asset Management System
            script.js
==================================================*/

document.addEventListener("DOMContentLoaded", function () {

    /*==============================================
            SIDEBAR TOGGLE
    ==============================================*/
const menuBtn = document.getElementById("menu-btn");
const sidebar = document.getElementById("sidebar");
const main = document.querySelector(".main");

if (menuBtn && sidebar) {

    menuBtn.addEventListener("click", function () {

        sidebar.classList.toggle("close");

    });

}

    /*==============================================
            MOBILE SIDEBAR
    ==============================================*/

    if (window.innerWidth <= 768) {

        if (main) {

            main.style.marginLeft = "0px";

        }

        if (menuBtn && sidebar) {

            menuBtn.addEventListener("click", function () {

                sidebar.classList.toggle("show");

            });

        }

    }

    /*==============================================
            ACTIVE SIDEBAR LINK
    ==============================================*/

    const currentPage = window.location.pathname;

    document.querySelectorAll(".nav-links a").forEach(link => {

        if (link.getAttribute("href") === currentPage) {

            link.classList.add("active");

        }

    });

    /*==============================================
            COUNTER ANIMATION
    ==============================================*/

    const counters = document.querySelectorAll(".counter");

    counters.forEach(counter => {

        const target = parseInt(counter.innerText);

        let count = 0;

        const speed = Math.max(10, 200 / target);

        function updateCounter() {

            if (count < target) {

                count++;

                counter.innerText = count;

                setTimeout(updateCounter, speed);

            }

            else {

                counter.innerText = target;

            }

        }

        updateCounter();

    });


/*==============================================
            DARK MODE
==============================================*/

const themeToggle = document.getElementById("themeToggle");

if (themeToggle) {

    themeToggle.addEventListener("click", function () {

        document.body.classList.toggle("dark-mode");

        if (document.body.classList.contains("dark-mode")) {

            localStorage.setItem("theme", "dark");

            themeToggle.innerHTML = '<i class="bi bi-sun-fill"></i>';

        } else {

            localStorage.setItem("theme", "light");

            themeToggle.innerHTML = '<i class="bi bi-moon-fill"></i>';

        }

    });

    if (localStorage.getItem("theme") === "dark") {

        document.body.classList.add("dark-mode");

        themeToggle.innerHTML = '<i class="bi bi-sun-fill"></i>';

    }

}

    /*==============================================
            LIVE CLOCK
    ==============================================*/

    function updateClock() {

        const clock = document.getElementById("clock");

        if (!clock) return;

        const now = new Date();

        const options = {

            weekday: 'short',
            day: '2-digit',
            month: 'short',
            year: 'numeric',
            hour: '2-digit',
            minute: '2-digit',
            second: '2-digit'

        };

        clock.innerHTML = now.toLocaleString("en-IN", options);

    }

    updateClock();

    setInterval(updateClock, 1000);

    /*==============================================
            SEARCH FILTER
    ==============================================*/

    const searchInput = document.querySelector(".search-box input");

    if (searchInput) {

        searchInput.addEventListener("keyup", function () {

            let filter = this.value.toLowerCase();

            document.querySelectorAll("table tbody tr").forEach(row => {

                let text = row.innerText.toLowerCase();

                row.style.display = text.includes(filter) ? "" : "none";

            });

        });

    }

    /*==============================================
            TOOLTIP
    ==============================================*/

    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));

    tooltipTriggerList.map(function (tooltipTriggerEl) {

        return new bootstrap.Tooltip(tooltipTriggerEl);

    });

    /*==============================================
            CARD HOVER EFFECT
    ==============================================*/

    document.querySelectorAll(".card").forEach(card => {

        card.addEventListener("mouseenter", function () {

            card.style.transform = "translateY(-8px)";

        });

        card.addEventListener("mouseleave", function () {

            card.style.transform = "translateY(0px)";

        });

    });

    /*==============================================
            BUTTON RIPPLE EFFECT
    ==============================================*/

    document.querySelectorAll(".btn").forEach(button => {

        button.addEventListener("click", function (e) {

            const circle = document.createElement("span");

            const diameter = Math.max(button.clientWidth, button.clientHeight);

            circle.style.width = circle.style.height = `${diameter}px`;

            circle.style.left = `${e.clientX - button.offsetLeft - diameter / 2}px`;

            circle.style.top = `${e.clientY - button.offsetTop - diameter / 2}px`;

            circle.classList.add("ripple");

            const ripple = button.getElementsByClassName("ripple")[0];

            if (ripple) {

                ripple.remove();

            }

            button.appendChild(circle);

        });

    });

    /*==============================================
            PAGE LOADER
    ==============================================*/

    window.addEventListener("load", function () {

        const loader = document.querySelector(".loader");

        if (loader) {

            loader.style.display = "none";

        }

    });

});


// =========================
// Assets by Category (Bar)
// =========================
document.addEventListener("DOMContentLoaded", function () {

    const dashboardCanvas = document.getElementById("dashboardChart");

    if (dashboardCanvas) {

        const assetLabels = JSON.parse(dashboardCanvas.dataset.assetLabels || "[]");
        const assetValues = JSON.parse(dashboardCanvas.dataset.assetValues || "[]");

        new Chart(dashboardCanvas, {
            type: "bar",
            data: {
                labels: assetLabels,
                datasets: [{
                    label: "Assets by Category",
                    data: assetValues,
                    backgroundColor: [
                        "#0d6efd",
                        "#198754",
                        "#ffc107",
                        "#dc3545",
                        "#6f42c1",
                        "#20c997",
                        "#fd7e14"
                    ]
                }]
            }
        });

    }

    const pieCanvas = document.getElementById("pieChart");

    if (pieCanvas) {

        const complaintLabels = JSON.parse(pieCanvas.dataset.complaintLabels || "[]");
        const complaintValues = JSON.parse(pieCanvas.dataset.complaintValues || "[]");

        new Chart(pieCanvas, {
            type: "pie",
            data: {
                labels: complaintLabels,
                datasets: [{
                    data: complaintValues
                }]
            }
        });

    }

    const lineCanvas = document.getElementById("lineChart");

    if (lineCanvas) {

        const monthLabels = JSON.parse(lineCanvas.dataset.monthLabels || "[]");
        const monthValues = JSON.parse(lineCanvas.dataset.monthValues || "[]");

        new Chart(lineCanvas, {
            type: "line",
            data: {
                labels: monthLabels,
                datasets: [{
                    label: "Maintenance",
                    data: monthValues,
                    borderColor: "#0d6efd",
                    tension: 0.4
                }]
            }
        });

    }

});