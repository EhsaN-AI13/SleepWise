const sleepModeButton = document.getElementById("sleepMode");
const wakeModeButton = document.getElementById("wakeMode");

const timeInput = document.getElementById("timeInput");
const calculateButton = document.getElementById("calculateButton");

const result = document.getElementById("result");


let mode = "sleep";

sleepModeButton.classList.add("active");


sleepModeButton.addEventListener("click", function () {

    mode = "sleep";

    sleepModeButton.classList.add("active");
    wakeModeButton.classList.remove("active");

    result.innerHTML = "";

});


wakeModeButton.addEventListener("click", function () {

    mode = "wake";

    wakeModeButton.classList.add("active");
    sleepModeButton.classList.remove("active");

    result.innerHTML = "";

});


calculateButton.addEventListener("click", async function () {

    const time = timeInput.value;

    if (time === "") {

        result.innerHTML = "لطفاً زمان را وارد کنید.";

        return;
    }

let response;
let data;

try {

    response = await fetch(
        `/calculate?mode=${mode}&time=${time}`
    );
if (!response.ok) {
    throw new Error("Server error");
}

    data = await response.json();

}
catch (error) {

    result.innerHTML = "خطایی در ارتباط با سرور رخ داد.";

    return;
}

    if (data.error) {

        result.innerHTML = data.error;

        return;
    }


    if (mode === "sleep") {

        result.innerHTML = `
            <div class="result-card">
                <h3>پیشنهاد ۷ ساعته</h3>
                <p>${data.result_7}</p>
            </div>

            <div class="result-card">
                <h3>پیشنهاد ۸ ساعته</h3>
                <p>${data.result_8}</p>
            </div>
        `;

    }


    else if (mode === "wake") {

        let sleep7 = data.result_7;
        let sleep8 = data.result_8;

        let result7 = data.result_7_previous
            ? `${sleep7} (شب قبل)`
            : sleep7;

        let result8 = data.result_8_previous
            ? `${sleep8} (شب قبل)`
            : sleep8;


        result.innerHTML = `
            <div class="result-card">
                <h3>پیشنهاد ۷ ساعته</h3>
                <p>${result7}</p>
            </div>

            <div class="result-card">
                <h3>پیشنهاد ۸ ساعته</h3>
                <p>${result8}</p>
            </div>
        `;

    }

});