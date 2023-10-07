async function checkAuthentication() {
    let path = await routePath();
    if (!path)
        return;

    if ((path + "/") !== window.location.pathname && path !== window.location.pathname)
        window.location.pathname = path;
}

async function routePath() {
    let r = await sendApiRequest("/auth/user");
    let data = await r.json();

    let path;
    if (r.status === 200) {
        if (data.isFarmer)
            path = "/farmer";
        else if (data.isWholesaler)
            path = "/wholesaler";
    } else if (r.status === 403) {
        path = "/";
    } else if (r.status === 404) {
        path = "/signup";
    }

    return path;
}

async function sendApiRequest(url, options = {}) {
    options = Object.assign({}, options);

    if (typeof options.body === "object") {
        if (!options.headers)
            options.headers = {};
        if (!options.headers["Content-Type"])
            options.headers["Content-Type"] = "application/json";

        options.body = JSON.stringify(options.body);
    }

    return fetch(url, options);
}

async function assertOK(response) {
    if (!response || !response.status || response.status !== 200)
        throw new Error("Assert OK failed");

    return response;
}

function isInputValid(input) {
    return new RegExp(input.pattern).test(input.value);
}

// Note: The following code assumes that you've integrated it properly within your Django templates.
// You may need to adjust the HTML structure and elements accordingly.

document.addEventListener("DOMContentLoaded", () => {
    checkAuthentication();

    // Add event listeners or perform other actions as needed for your Django template.
});

// Create elements in the DOM. This function can be used as needed within your Django templates.
function createElement(name, parent, options = {}) {
    let classList = name.split(".");
    let tagName = classList.shift();

    let id = tagName.split("#");
    if (id.length > 1) {
        tagName = id[0];
        id = id[1];
    } else {
        id = undefined;
    }

    let element = document.createElement(tagName);

    if (id)
        element.id = id;

    if (classList.length > 0)
        for (let c of classList)
            element.classList.add(c);

    for (let o in options)
        if (o in element)
            element[o] = options[o];
        else
            element.setAttribute(o, options[o]);

    if (parent)
        parent.appendChild(element);

    return element;
}

async function logout() {
    await sendApiRequest("/auth/logout").then(assertOK);
    checkAuthentication();
}