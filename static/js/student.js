/* ==========================================
   SMART HOSTEL CMS
   STUDENT JAVASCRIPT
========================================== */

"use strict";

document.addEventListener("DOMContentLoaded", () => {

    initializeCharacterCounter();
    initializeComplaintSearch();
    initializeDashboardCards();
    initializeProgressBars();
    initializeProfileAnimation();
    initializeFileUpload();
    initializeFormValidation();

});

/* ==========================================
   Character Counter
========================================== */

function initializeCharacterCounter(){

    const textarea=document.getElementById("description");
    const counter=document.getElementById("counter");

    if(!textarea || !counter) return;

    function update(){

        const length=textarea.value.length;

        counter.innerHTML=length+" / 500 Characters";

        if(length>450){

            counter.style.color="#ef4444";

        }else if(length>300){

            counter.style.color="#f59e0b";

        }else{

            counter.style.color="#10b981";

        }

    }

    textarea.addEventListener("input",update);

    update();

}

/* ==========================================
   Complaint Search
========================================== */

function initializeComplaintSearch(){

    const search=document.getElementById("searchComplaint");

    const table=document.getElementById("historyTable");

    if(!search || !table) return;

    search.addEventListener("keyup",()=>{

        const value=search.value.toLowerCase();

        table.querySelectorAll("tbody tr").forEach(row=>{

            row.style.display=row.innerText.toLowerCase().includes(value)
            ?"":"none";

        });

    });

}

/* ==========================================
   Dashboard Cards Animation
========================================== */

function initializeDashboardCards(){

    document.querySelectorAll(".student-card,.stat-card,.glass").forEach((card,index)=>{

        card.style.opacity="0";

        card.style.transform="translateY(30px)";

        setTimeout(()=>{

            card.style.transition=".6s";

            card.style.opacity="1";

            card.style.transform="translateY(0)";

        },index*120);

    });

}

/* ==========================================
   Progress Animation
========================================== */

function initializeProgressBars(){

    document.querySelectorAll(".progress-bar").forEach(bar=>{

        const width=bar.getAttribute("aria-valuenow") || 0;

        bar.style.width="0%";

        setTimeout(()=>{

            bar.style.transition="1s";

            bar.style.width=width+"%";

        },300);

    });

}

/* ==========================================
   Profile Image Hover
========================================== */

function initializeProfileAnimation(){

    const image=document.querySelector(".profile-card img");

    if(!image) return;

    image.addEventListener("mouseenter",()=>{

        image.style.transform="scale(1.08) rotate(3deg)";

        image.style.transition=".3s";

    });

    image.addEventListener("mouseleave",()=>{

        image.style.transform="scale(1) rotate(0deg)";

    });

}

/* ==========================================
   File Upload Preview
========================================== */

function initializeFileUpload(){

    const input=document.querySelector("input[type='file']");

    if(!input) return;

    input.addEventListener("change",()=>{

        if(input.files.length){

            if(typeof showToast==="function"){

                showToast(input.files[0].name+" selected");

            }

        }

    });

}

/* ==========================================
   Complaint Form Validation
========================================== */

function initializeFormValidation(){

    document.querySelectorAll("form").forEach(form=>{

        form.addEventListener("submit",(e)=>{

            const required=form.querySelectorAll("[required]");

            let valid=true;

            required.forEach(field=>{

                if(field.value.trim()===""){

                    field.style.borderColor="#ef4444";

                    valid=false;

                }else{

                    field.style.borderColor="#10b981";

                }

            });

            if(!valid){

                e.preventDefault();

                if(typeof showToast==="function"){

                    showToast("Please fill all required fields.","error");

                }

            }

        });

    });

}

/* ==========================================
   Complaint Card Hover
========================================== */

document.querySelectorAll(".complaint-card").forEach(card=>{

    card.addEventListener("mouseenter",()=>{

        card.style.transform="translateX(8px)";

        card.style.transition=".3s";

    });

    card.addEventListener("mouseleave",()=>{

        card.style.transform="translateX(0)";

    });

});

/* ==========================================
   Statistics Counter
========================================== */

document.querySelectorAll(".stat-value").forEach(counter=>{

    const target=parseInt(counter.innerText);

    if(isNaN(target)) return;

    let current=0;

    const increment=Math.max(1,Math.ceil(target/40));

    const timer=setInterval(()=>{

        current+=increment;

        if(current>=target){

            current=target;

            clearInterval(timer);

        }

        counter.innerText=current;

    },25);

});

/* ==========================================
   Scroll Reveal
========================================== */

const observer=new IntersectionObserver(entries=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.style.opacity="1";

            entry.target.style.transform="translateY(0)";

        }

    });

});

document.querySelectorAll(".glass,.student-card,.card").forEach(item=>{

    item.style.opacity="0";

    item.style.transform="translateY(25px)";

    item.style.transition=".6s";

    observer.observe(item);

});