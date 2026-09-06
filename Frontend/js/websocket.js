const socket = io(
    "http://127.0.0.1:5000"
);


// ==================================
// CONNECTION EVENTS
// ==================================

socket.on(
    "connect",
    () => {

        console.log(
            "[NIDS] Connected to WebSocket server"
        );


        addFeedMessage(

            "SYSTEM",

            "Connected to real-time threat monitoring server"

        );

    }
);


socket.on(
    "disconnect",
    () => {

        console.log(
            "[NIDS] Disconnected from WebSocket server"
        );


        addFeedMessage(

            "SYSTEM",

            "Disconnected from threat monitoring server"

        );

    }
);


// ==================================
// RECEIVE NEW ALERT
// ==================================

socket.on(
    "new_alert",
    (alert) => {

        console.log(
            "[NIDS] New Alert:",
            alert
        );


        const message =

            `${alert.attack_type} detected from ` +
            `${alert.source_ip}`;


        addFeedMessage(
            "ALERT",
            message
        );


        if (
            typeof addAlertToTable ===
            "function"
        ) {

            addAlertToTable(
                alert
            );

        }


        if (
            typeof loadStats ===
            "function"
        ) {

            loadStats();

        }


        if (
            typeof loadChartData ===
            "function"
        ) {

            loadChartData();

        }

    }
);


// ==================================
// ADD LIVE FEED MESSAGE
// ==================================

function addFeedMessage(
    type,
    message
) {

    const feedContainer =
        document.getElementById(
            "live-feed"
        );


    if (!feedContainer) return;


    const time =
        new Date().toLocaleTimeString();


    const feedItem =
        document.createElement("div");


    feedItem.className =
        "feed-message";


    feedItem.innerHTML = `

        <span class="feed-time">

            [${time}]

        </span>

        <strong>

            ${type}:

        </strong>

        ${message}

    `;


    feedContainer.prepend(
        feedItem
    );


    while (
        feedContainer.children.length > 50
    ) {

        feedContainer.removeChild(
            feedContainer.lastChild
        );

    }
}