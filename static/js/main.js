/* ==========================================
   SMART HOSTEL CMS
   MAIN JAVASCRIPT
========================================== */

"use strict";

/* ------------------------------
   DOM Ready
------------------------------ */

document.addEventListener("DOMContentLoaded", function () {

    initLoader();

    initScrollTop();

    initNavbar();

    initCounters();

    initFadeAnimation();

    initPasswordToggle();

    initRippleEffect();

    initAlerts();

    initTooltips();

    initSearchInputs();

});

/* ------------------------------
   Page Loader
------------------------------ */

function initLoader() {

    const loader = document.getElementById("loader");

    if (!loader) return;

    window.addEventListener("load", function () {

        loader.style.opacity = "0";

        setTimeout(() => {

            loader.style.display = "none";

        }, 500);

    });

}

/* ------------------------------
   Scroll To Top
------------------------------ */

function initScrollTop() {

    const btn = document.createElement("button");

    btn.id = "scrollTop";

    btn.innerHTML = '<i class="fa-solid fa-arrow-up"></i>';

    btn.style.position = "fixed";
    btn.style.right = "25px";
    btn.style.bottom = "25px";
    btn.style.width = "50px";
    btn.style.height = "50px";
    btn.style.borderRadius = "50%";
    btn.style.border = "none";
    btn.style.background = "#2563eb";
    btn.style.color = "#fff";
    btn.style.cursor = "pointer";
    btn.style.display = "none";
    btn.style.zIndex = "999";

    document.body.appendChild(btn);

    window.addEventListener("scroll", function () {

        if (window.scrollY > 300)

            btn.style.display = "block";

        else

            btn.style.display = "none";

    });

    btn.onclick = () => {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    };

}

/* ------------------------------
   Navbar Effect
------------------------------ */

function initNavbar() {

    const nav = document.querySelector(".navbar");

    if (!nav) return;

    window.addEventListener("scroll", function () {

        if (window.scrollY > 40) {

            nav.style.background = "rgba(8,17,31,.95)";

            nav.style.backdropFilter = "blur(20px)";

        }

        else {

            nav.style.background = "";

            nav.style.backdropFilter = "";

        }

    });

}

/* ------------------------------
   Animated Counters
------------------------------ */

function initCounters() {

    document.querySelectorAll(".stat-value").forEach(counter => {

        const target = Number(counter.innerText);

        if (isNaN(target)) return;

        let value = 0;

        const step = Math.max(1, Math.ceil(target / 50));

        const timer = setInterval(() => {

            value += step;

            if (value >= target) {

                value = target;

                clearInterval(timer);

            }

            counter.innerText = value;

        }, 25);

    });

}

/* ------------------------------
   Fade Animation
------------------------------ */

function initFadeAnimation() {

    const items = document.querySelectorAll(".card,.glass,.stat-card");

    const observer = new IntersectionObserver(entries => {

        entries.forEach(entry => {

            if (entry.isIntersecting) {

                entry.target.style.opacity = "1";

                entry.target.style.transform = "translateY(0)";

            }

        });

    });

    items.forEach(item => {

        item.style.opacity = "0";

        item.style.transform = "translateY(30px)";

        item.style.transition = ".6s";

        observer.observe(item);

    });

}

/* ------------------------------
   Password Toggle
------------------------------ */

function initPasswordToggle() {

    document.querySelectorAll("[data-password]").forEach(button => {

        button.addEventListener("click", function () {

            const input = document.getElementById(this.dataset.password);

            if (!input) return;

            input.type =

                input.type === "password"

                ? "text"

                : "password";

        });

    });

}

/* ------------------------------
   Ripple Effect
------------------------------ */

function initRippleEffect() {

    document.querySelectorAll(".btn").forEach(button => {

        button.addEventListener("click", function (e) {

            const ripple = document.createElement("span");

            ripple.className = "ripple";

            ripple.style.left =

                e.offsetX + "px";

            ripple.style.top =

                e.offsetY + "px";

            this.appendChild(ripple);

            setTimeout(() => {

                ripple.remove();

            }, 600);

        });

    });

}

/* ------------------------------
   Alerts
------------------------------ */

function initAlerts() {

    document.querySelectorAll(".alert").forEach(alert => {

        setTimeout(() => {

            alert.style.transition = ".5s";

            alert.style.opacity = "0";

            setTimeout(() => {

                alert.remove();

            }, 500);

        }, 4000);

    });

}

/* ------------------------------
   Tooltips
------------------------------ */

function initTooltips() {

    if (typeof bootstrap !== "undefined") {

        document.querySelectorAll('[data-bs-toggle="tooltip"]')

            .forEach(el => {

                new bootstrap.Tooltip(el);

            });

    }

}

/* ------------------------------
   Search Inputs
------------------------------ */

function initSearchInputs() {

    document.querySelectorAll("input[type='search']").forEach(input => {

        input.addEventListener("focus", function () {

            this.style.borderColor = "#2563eb";

        });

        input.addEventListener("blur", function () {

            this.style.borderColor = "";

        });

    });

}

/* ------------------------------
   Toast Notification
------------------------------ */

function showToast(message, type = "success") {

    const toast = document.createElement("div");

    toast.className = "toast-box";

    toast.innerHTML = message;

    toast.style.position = "fixed";
    toast.style.right = "25px";
    toast.style.top = "25px";
    toast.style.padding = "15px 25px";
    toast.style.background =
        type === "success"
            ? "#10b981"
            : "#ef4444";

    toast.style.color = "#fff";
    toast.style.borderRadius = "10px";
    toast.style.zIndex = "9999";

    document.body.appendChild(toast);

    setTimeout(() => {

        toast.remove();

    }, 3000);

}

/* ------------------------------
   Confirm Delete
------------------------------ */

function confirmDelete(message = "Are you sure?") {

    return confirm(message);

}

/* ------------------------------
   Smooth Anchor Scroll
------------------------------ */

document.querySelectorAll("a[href^='#']").forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        const target = document.querySelector(this.getAttribute("href"));

        if (!target) return;

        e.preventDefault();

        target.scrollIntoView({

            behavior: "smooth"

        });

    });

});