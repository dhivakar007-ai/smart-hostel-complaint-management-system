/* ==========================================
   SMART HOSTEL CMS
   ADMIN PANEL JAVASCRIPT
========================================== */

"use strict";

document.addEventListener("DOMContentLoaded", function () {

    initializeDashboardCards();
    initializeComplaintSearch();
    initializeStudentSearch();
    initializeStatusFilter();
    initializeCounters();
    initializeChartsAnimation();
    initializeDeleteConfirmation();
    initializeTableHover();
    initializeAutoRefresh();

});

/* ==========================================
   Dashboard Animation
========================================== */

function initializeDashboardCards(){

    document.querySelectorAll(".stat-card,.glass,.card").forEach((card,index)=>{

        card.style.opacity="0";
        card.style.transform="translateY(25px)";

        setTimeout(()=>{

            card.style.transition=".6s";
            card.style.opacity="1";
            card.style.transform="translateY(0)";

        },index*120);

    });

}

/* ==========================================
   Complaint Search
========================================== */

function initializeComplaintSearch(){

    const input=document.getElementById("searchComplaint");

    if(!input) return;

    input.addEventListener("keyup",function(){

        const keyword=this.value.toLowerCase();

        document.querySelectorAll("#complaintTable tbody tr").forEach(row=>{

            row.style.display=row.innerText.toLowerCase().includes(keyword)
            ?"":"none";

        });

    });

}

/* ==========================================
   Student Search
========================================== */

function initializeStudentSearch(){

    const input=document.getElementById("studentSearch");

    if(!input) return;

    input.addEventListener("keyup",function(){

        const keyword=this.value.toLowerCase();

        document.querySelectorAll("#studentTable tbody tr").forEach(row=>{

            row.style.display=row.innerText.toLowerCase().includes(keyword)
            ?"":"none";

        });

    });

}

/* ==========================================
   Status Filter
========================================== */

function initializeStatusFilter(){

    const filter=document.getElementById("statusFilter");

    if(!filter) return;

    filter.addEventListener("change",function(){

        const value=this.value.toLowerCase();

        document.querySelectorAll("#complaintTable tbody tr").forEach(row=>{

            if(value===""){

                row.style.display="";

                return;

            }

            row.style.display=row.innerText.toLowerCase().includes(value)
            ?"":"none";

        });

    });

}

/* ==========================================
   Counter Animation
========================================== */

function initializeCounters(){

    document.querySelectorAll(".stat-value").forEach(counter=>{

        const target=parseInt(counter.innerText);

        if(isNaN(target)) return;

        let current=0;

        const increment=Math.max(1,Math.ceil(target/50));

        const timer=setInterval(()=>{

            current+=increment;

            if(current>=target){

                current=target;

                clearInterval(timer);

            }

            counter.innerText=current;

        },25);

    });

}

/* ==========================================
   Chart Animation
========================================== */

function initializeChartsAnimation(){

    document.querySelectorAll("canvas").forEach(chart=>{

        chart.style.opacity="0";

        setTimeout(()=>{

            chart.style.transition=".8s";
            chart.style.opacity="1";

        },300);

    });

}

/* ==========================================
   Delete Confirmation
========================================== */

function initializeDeleteConfirmation(){

    document.querySelectorAll(".btn-outline-danger").forEach(button=>{

        button.addEventListener("click",function(e){

            if(!confirm("Delete this record permanently?")){

                e.preventDefault();

            }

        });

    });

}

/* ==========================================
   Table Hover
========================================== */

function initializeTableHover(){

    document.querySelectorAll("tbody tr").forEach(row=>{

        row.addEventListener("mouseenter",()=>{

            row.style.transition=".2s";
            row.style.transform="scale(1.01)";

        });

        row.addEventListener("mouseleave",()=>{

            row.style.transform="scale(1)";

        });

    });

}

/* ==========================================
   Auto Refresh Timer
========================================== */

function initializeAutoRefresh(){

    const badge=document.getElementById("refreshStatus");

    if(!badge) return;

    let seconds=60;

    setInterval(()=>{

        seconds--;

        badge.innerHTML="Refresh in "+seconds+"s";

        if(seconds<=0){

            location.reload();

        }

    },1000);

}

/* ==========================================
   Export Button
========================================== */

document.querySelectorAll(".btn-success").forEach(button=>{

    if(button.innerText.toLowerCase().includes("export")){

        button.addEventListener("click",function(){

            if(typeof showToast==="function"){

                showToast("Report exported successfully.");

            }

        });

    }

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

document.querySelectorAll(".glass,.card,.stat-card").forEach(item=>{

    item.style.opacity="0";
    item.style.transform="translateY(25px)";
    item.style.transition=".6s";

    observer.observe(item);

});