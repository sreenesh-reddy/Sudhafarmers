let entities, name, aadhaar;

document.addEventListener("DOMContentLoaded", () => {
    // checkAuthentication();

    entities = Array.from(document.querySelectorAll(".entity"));
    document.querySelector("#EntitySelect").addEventListener("click", selectEntity);

    name = document.querySelector("#Name");
    aadhaar = document.querySelector("#Aadhar");

    document.querySelector("#Submit").addEventListener("click", signupUser);
});

function selectEntity(e) {
    if (!e.target.matches("button:not(.disabled)"))
        return;

    for (let i of entities)
        i.classList.remove("selected");
    e.target.classList.add("selected");
}

async function signupUser() {
    let data = validateInputs();
    if (!data)
        return;

    // Make an AJAX request to your Django view for user signup.
    try {
        const response = await fetch("/auth/add/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                // Add any other headers you may need
            },
            body: JSON.stringify({
                name: data.name,
                aadhaar: data.aadhaar,
                isFarmer: (data.entity == "farmer"),
                isWholesaler: (data.entity == "wholesaler"),
            }),
        });

        if (response.status == 200) {
            await checkAuthentication();
        } else {
            console.error(await response.json());
        }
    } catch (error) {
        console.error(error);
    }
}

function validateInputs() {
    let data = {};
    let isValid = true;

    data.entity = null;
    for (let i of entities)
        if (i.classList.contains("selected"))
            data.entity = i.dataset.value;
    if (!data.entity) {
        isValid = false;
        alert("Please select one entity");
        console.error("Please select one entity");
    }

    data.name = name.value;
    if (!isInputValid(name)) {
        isValid = false;
        alert("Please check the name");
        console.error("Please check the name");
    }

    data.aadhaar = aadhaar.value;
    if (!isInputValid(aadhaar)) {
        isValid = false;
        alert("Please check the aadhaar card number");
        console.error("Please check the aadhaar card number");
    }

    if (!isValid)
        return null;
    return data;
}