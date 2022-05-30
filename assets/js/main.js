(function ($) {
    "use strict";
    jQuery(document).on('ready', function () {

        // Partner Slides
        $('.partner-slides').owlCarousel({
            loop: true,
            nav: false,
            dots: false,
            rtl: true,
            autoplayHoverPause: true,
            autoplay: true,
            margin: 30,
            navText: [
                "<i class='flaticon-left-chevron'></i>",
                "<i class='flaticon-right-chevron'></i>"
            ],
            responsive: {
                0: {
                    items: 1,
                },
                576: {
                    items: 1,
                },
                768: {
                    items: 1,
                },
                1200: {
                    items: 1,
                }
            }
        });

    });
}(jQuery));

$(document).ready(function () {

    /* Centering the modal vertically */
    function alignModal() {
        var modalDialog = $(this).find(".modal-dialog");
        modalDialog.css("margin-top", Math.max(0,
            ($(window).height() - modalDialog.height()) / 2));
    }

    $(".modal").on("shown.bs.modal", alignModal);

    /* Resizing the modal according the screen size */
    $(window).on("resize", function () {
        $(".modal:visible").each(alignModal);
    });
});
$(document).ready(function () {
    $('#nav-icon').click(function () {
        $(this).toggleClass('open');
    });
    /* new codes */
$(".side-tab .text-body").click(function (event) {
        event.preventDefault();
        let dataTab = $(this).data("tab");
        $(".text-body span").css("background-color", "transparent")
        $(this).children('span').css("background-color", "#b6b6b6");
        $(".select-area").addClass("d-none");
        $("." + dataTab).removeClass("d-none");
    })
$("#returnDateHotel").persianDatepicker({
        altField: '#returnDateHotel',
        altFormat: "YYYY/MM/DD",
        observer: false,
        format: 'YYYY/MM/DD',
        initialValue: false,
        initialValueType: 'persian',
        autoClose: true,
    });
$("#goDateHotel").persianDatepicker({
        altField: '#goDateHotel',
        altFormat: "YYYY/MM/DD",
        observer: false,
        format: 'YYYY/MM/DD',
        initialValue: false,
        initialValueType: 'persian',
        autoClose: true,
    });
$("#hotelSrc").focus(function () {
        fetch('http://localhost/php/plane/cities.json')
            .then(res => res.json())
            .then(data => getDataFromJson(data))

        function getDataFromJson(data) {
            let dataCitie = data;
            let selectElemnt = document.getElementById("hotelSrc")
            dataCitie.forEach(function (value) {
                selectElemnt.innerHTML += "<option value='" + value['id'] + "'>" + value['title'] + "</option>";
            })
        }
    })
});

function openNav() {
    document.getElementById("mySidenav").style.width = "250px";
    document.querySelector('#mNav').style.backgroundColor = "#237c8c"
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0"
    document.querySelector('#mNav').style.backgroundColor = "#1DBBD8"
}

function rangeValFunc(rangeVal) {
    let rangeWidth1 = document.getElementById("Tooltiptext1").textContent = rangeVal + ":00";
    let mainMinutes = rangeVal * 60;
    $(".ticket").filter(function () {
        let time = $(this).data('time');
        time = time.split(':');
        let hours = time[0], minutes = time[1];
        if (hours[0].toString() === '0') {
            hours = hours[1];
        }
        minutes = parseInt(minutes) + (hours * 60)
        $(this).toggle(mainMinutes <= minutes)
    });
}

$(".airline_checkbox").on('change', function () {
    let airlines = [];
    $(".airline_checkbox:checked").each(function () {
        airlines.push($(this).val())
    });
    $(".ticket").filter(function () {
        let airline = $(this).data('airline');
        $(this).toggle(airlines.includes(airline.toString()))
    });
})

$(".datePicker").attr('readonly', true)

$(function () {
    $(".datePicker").each(function () {
        let id = $(this).attr('id');
        if (id) {
            $(`#${id}`).persianDatepicker({
                altField: `#${id}`,
                altFormat: "YYYY/MM/DD",
                observer: false,
                format: "YYYY/MM/DD",
                initialValue: false,
                initialValueType: 'persian',
                autoClose: true,
            });
        }
    })
})
const setDate = () => {
    $(".birthdate").persianDatepicker({
        altField: '.birthdate',
        altFormat: "MM/DD",
        observer: false,
        format: 'MM/DD',
        initialValue: false,
        initialValueType: 'persian',
        autoClose: true,
    });
}
setDate()


$(".my-tabs span").on('click', function () {
    let that = $(this);
    $(".my-tabs span").each(function () {
        $(this).removeClass('active');
        let target = $(this).data('target');
        $(`#${target}`).removeClass('show')
    })
    $(that).addClass('active')
    let target = $(that).data('target');
    $(`#${target}`).addClass('show')
})
setTimeout(() => {
    $(".my-tabs span:first-child").click()
}, 100)
if (document.getElementById('addNewPassenger')) {
    document.getElementById('addNewPassenger').onclick = function () {
        let content = document.getElementsByClassName('passenger_wrapper')[document.getElementsByClassName('passenger_wrapper').length - 1].cloneNode(true);
        document.getElementById('passengers').appendChild(content);
        console.log(document.getElementsByClassName('passenger_wrapper')[document.getElementsByClassName('passenger_wrapper').length - 1].reset())
        setDate();
    }
    document.getElementById('finalSubmit').onclick = async function () {
        let forms = document.getElementsByClassName('passenger_wrapper');
        let data = $(forms).serialize();
        data = data + "&mobile=" + document.getElementById('mobile').value;
        data = data + "&email=" + document.getElementById('email').value;
        const form = document.createElement('form');
        data = data.split("&");
        data.forEach((value) => {
            let input = document.createElement('input');
            input.setAttribute('type', 'hidden');
            let split = value.split('=');
            input.setAttribute('name', split[0].replace('%5B%5D', ''));
            input.value = split[1];
            form.appendChild(input);
        });
        let input = document.createElement('input');
        input.setAttribute('type', 'hidden');
        input.setAttribute('name', 'csrfmiddlewaretoken');
        input.value = document.getElementsByName('csrfmiddlewaretoken')[0].value;
        form.appendChild(input);
        form.setAttribute('method', 'post');
        form.setAttribute('style', 'display: none;');
        form.setAttribute('action', document.getElementById('finalSubmit').attributes['data-url'].value);
        // let result = await fetch('', {
        //     method: 'POST',
        //     data: data,
        // });

        document.getElementsByTagName('body')[0].appendChild(form);

        form.submit()

    }
}
if (document.getElementsByClassName('side-tab').length > 0) {
    setTimeout(() => {
        console.log($(".side-tab a:nth-child(1)").click())
    }, 1)
}
if (document.getElementById('travelSrc')) {
    setTimeout(() => {
        $.ajax({
            url: "/cities",
            type: "get",
            success: res => {
                const options = [];
                for (const item in res) {
                    if (res.hasOwnProperty(item)) {
                        options.push(`<option value="${item}">${res[item]}</option>`)
                    }
                }
                document.getElementById('travelSrc').innerHTML = options.join('');
                document.getElementById('travelGoal').innerHTML = options.join('');
                document.getElementById('destination').innerHTML = options.join('');
            }
        })
    }, 200)
}
$('.select2').select2({
    placeholder: 'لطفا یک مورد را انتخاب کنید',
    width: "100%",
});
$("#destination").select2({
    placeholder: 'لطفا یک مورد را انتخاب کنید',
    width: "100%",

})
$("#fly-area-submit").click(function (e) {
    e.preventDefault();
    let goDate = $("#goDate").val();
    // let returnDate = $("#returnDate").val();
    let infantNum = $("#infantNum").val();
    let childNum = $("#childNum").val();
    let adultsNum = $("#adultsNum").val();
    if (!goDate || goDate === '') {
        alert("لطفا تاریخ رفت را انتخاب کنید");
        return;
    }
    // if (!returnDate || returnDate === '') {
    //     alert("لطفا تاریخ برگشت را انتخاب کنید");
    //     return;
    // }
    if (!infantNum || infantNum === '') {
        alert("لطفا تعداد نوزاد ها را وارد کنید");
        return;
    }
    if (!childNum || childNum === '') {
        alert("لطفا تعداد کودکان را وارد کنید");
        return;
    }
    if (!adultsNum || adultsNum === '') {
        alert("لطفا تعداد بزرگسالان را وارد کنید");
        return;
    }
    $('#fly-area').submit()
})
$("#travelSrc").on('change', function () {
    let value = $(this).val();
    $("#travelGoal").select2('destroy')
    let options = "";
    $("#travelGoal option").each(function () {
        if ($(this).val() !== value) {
            options += `<option value="${$(this).val()}">${$(this).text()}</option>`
        }
    })
    $("#travelGoal").html(options)
    $("#travelGoal").select2({
        placeholder: 'لطفا یک مورد را انتخاب کنید',
        width: '40%',
    });
})

$("#travelGoal").on('change', function () {
    let value = $(this).val();
    $("#travelSrc").select2('destroy')
    let options = "";
    $("#travelSrc option").each(function () {
        if ($(this).val() !== value) {
            options += `<option value="${$(this).val()}">${$(this).text()}</option>`
        }
    })
    $("#travelSrc").html(options)
    $("#travelSrc").select2({
        placeholder: 'لطفا یک مورد را انتخاب کنید',
        width: '40%',
    });
})

//

let containerTypeTravel = document.getElementById('container-type-travel')
let typeTravel = 2

let flexRadioDefault1 = document.getElementById('flexRadioDefault1')
let flexRadioDefault2 = document.getElementById('flexRadioDefault2')

flexRadioDefault1.addEventListener('change', function (e) {
    typeTravel = 1
    toggletypeTravel(1)
})
flexRadioDefault2.addEventListener('change', function (e) {
    typeTravel = 2
    toggletypeTravel(2)
})

function toggletypeTravel(type) {
    containerTypeTravel.setAttribute('type-travel', type)
}


$(document).ready(function () {
    $(".panel-header").click(function () {
        $(this).next().children(".panel-display").slideToggle();
    })
    $("#jobs-scroller").click(function () {
        $([document.documentElement, document.body]).animate({
            scrollTop: $(".jobs-list-sec").offset().top
        }, 1000);
    })
})

$("#jobs-scroller").click(function () {
    $([document.documentElement, document.body]).animate({
        scrollTop: $(".jobs-list-sec").offset().top
    }, 1000);
})


$(document).ready(function () {
    $(".panel-header").click(function () {
        $(this).next().children(".panel-display").slideToggle();
    })
})
