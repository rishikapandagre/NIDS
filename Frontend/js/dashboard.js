const API_BASE_URL = "http://127.0.0.1:5000";


// ==================================
// LOAD STATISTICS
// ==================================

async function loadStats() {

    try {

        const response = await fetch(
            `${API_BASE_URL}/api/stats`
        );

        const data = await response.json();


        document.getElementById(
            "total-alerts"
        ).textContent =
            data.total_alerts ?? 0;


        document.getElementById(
            "total-attacks"
        ).textContent =
            data.total_attacks ?? 0;


        document.getElementById(
            "active-threats"
        ).textContent =
            data.active_threats ?? 0;


        document.getElementById(
            "top-attacker"
        ).textContent =
            data.top_attacker ?? "--";

    }

    catch (error) {

        console.error(
            "Error loading statistics:",
            error
        );

    }
}


// ==================================
// LOAD ALERTS
// ==================================

async function loadAlerts() {

    try {

        const response = await fetch(
            `${API_BASE_URL}/api/alerts`
        );

        const alerts =
            await response.json();


        const tableBody =
            document.getElementById(
                "alert-table-body"
            );


        tableBody.innerHTML = "";


        if (!alerts || alerts.length === 0) {

            tableBody.innerHTML = `

                <tr>

                    <td
                        colspan="6"
                        class="no-data"
                    >

                        No Security Alerts Detected.

                    </td>

                </tr>

            `;

            return;
        }


        alerts.forEach(alert => {

            addAlertToTable(
                alert,
                false
            );

        });

    }

    catch (error) {

        console.error(
            "Error loading alerts:",
            error
        );

    }
}


// ==================================
// ADD ALERT TO TABLE
// ==================================

function addAlertToTable(
    alert,
    prepend = true
) {

    const tableBody =
        document.getElementById(
            "alert-table-body"
        );


    if (!tableBody) return;


    const noDataRow =
        tableBody.querySelector(
            ".no-data"
        );


    if (noDataRow) {

        noDataRow.parentElement.remove();

    }


    const row =
        document.createElement("tr");


    const severity =
        (alert.severity || "LOW")
        .toLowerCase();


    const status =
        (alert.status || "ACTIVE")
        .toLowerCase();


    row.innerHTML = `

        <td>
            ${alert.source_ip || "--"}
        </td>

        <td>
            ${alert.destination_ip || "--"}
        </td>

        <td>
            ${alert.attack_type || "--"}
        </td>

        <td>

            <span
                class="severity-${severity}"
            >

                ${alert.severity || "LOW"}

            </span>

        </td>

        <td>

            ${formatTimestamp(
                alert.timestamp
            )}

        </td>

        <td>

            <span
                class="status-${status}"
            >

                ${alert.status || "ACTIVE"}

            </span>

        </td>

    `;


    if (prepend) {

        tableBody.prepend(row);

    }

    else {

        tableBody.appendChild(row);

    }


    while (
        tableBody.children.length > 50
    ) {

        tableBody.removeChild(
            tableBody.lastChild
        );

    }
}


// ==================================
// FORMAT TIMESTAMP
// ==================================

function formatTimestamp(timestamp) {

    if (!timestamp) {

        return "--";

    }


    try {

        const date =
            new Date(timestamp);

        return date.toLocaleString();

    }

    catch {

        return timestamp;

    }
}


// ==================================
// INITIALIZE DASHBOARD
// ==================================

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadStats();

        loadAlerts();


        setInterval(
            loadStats,
            5000
        );


        setInterval(
            loadAlerts,
            5000
        );

    }
);