const CHART_API_URL =
    "http://127.0.0.1:5000/api/chart-data";


let attacksOverTimeChart;

let attackTypesChart;

let topAttackersChart;


// ==================================
// LOAD CHART DATA
// ==================================

async function loadChartData() {

    try {

        const response =
            await fetch(CHART_API_URL);

        const data =
            await response.json();


        updateAttacksOverTime(
            data.attacks_over_time || {}
        );


        updateAttackType(
            data.attack_types || {}
        );


        updateTopAttackers(
            data.top_attackers || {}
        );

    }

    catch (error) {

        console.error(
            "Error loading chart data:",
            error
        );

    }
}


// ==================================
// ATTACKS OVER TIME
// ==================================

function updateAttacksOverTime(data) {

    const canvas =
        document.getElementById(
            "attacksOverTimeChart"
        );


    if (!canvas) return;


    if (attacksOverTimeChart) {

        attacksOverTimeChart.destroy();

    }


    attacksOverTimeChart =
        new Chart(canvas, {

            type: "line",

            data: {

                labels:
                    Object.keys(data),

                datasets: [{

                    label:
                        "Attacks",

                    data:
                        Object.values(data),

                    borderColor:
                        "#ff5555",

                    backgroundColor:
                        "rgba(255, 85, 85, 0.1)",

                    borderWidth: 2,

                    tension: 0.4,

                    fill: true

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {

                        labels: {

                            color:
                                "#e8f1f8"

                        }

                    }

                },

                scales: {

                    x: {

                        ticks: {

                            color:
                                "#8fa3b8"

                        }

                    },

                    y: {

                        beginAtZero: true,

                        ticks: {

                            color:
                                "#8fa3b8"

                        }

                    }

                }

            }

        });
}


// ==================================
// ATTACK TYPES
// ==================================

function updateAttackType(data) {

    const canvas =
        document.getElementById(
            "attackTypesChart"
        );


    if (!canvas) return;


    if (attackTypesChart) {

        attackTypesChart.destroy();

    }


    attackTypesChart =
        new Chart(canvas, {

            type: "doughnut",

            data: {

                labels:
                    Object.keys(data),

                datasets: [{

                    data:
                        Object.values(data),

                    backgroundColor: [

                        "#03ccef",
                        "#e80101",
                        "#ffbf00",
                        "#8b13fb",
                        "#00f84f"

                    ],

                    borderWidth: 0

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {

                        position: "bottom",

                        labels: {

                            color:
                                "#e8f1f8"

                        }

                    }

                }

            }

        });
}


// ==================================
// TOP ATTACKERS
// ==================================

function updateTopAttackers(data) {

    const canvas =
        document.getElementById(
            "topAttackersChart"
        );


    if (!canvas) return;


    if (topAttackersChart) {

        topAttackersChart.destroy();

    }


    topAttackersChart =
        new Chart(canvas, {

            type: "bar",

            data: {

                labels:
                    Object.keys(data),

                datasets: [{

                    label:
                        "Attack Count",

                    data:
                        Object.values(data),

                    backgroundColor:
                        "rgba(176, 96, 250, 0.7)",

                    borderColor:
                        "#911bff",

                    borderWidth: 1

                }]

            },

            options: {

                responsive: true,

                maintainAspectRatio: false,

                plugins: {

                    legend: {

                        labels: {

                            color:
                                "#e8f1f8"

                        }

                    }

                },

                scales: {

                    x: {

                        ticks: {

                            color:
                                "#8fa3b8"

                        },

                        grid: {

                            display: false

                        }

                    },

                    y: {

                        beginAtZero: true,

                        ticks: {

                            color:
                                "#8fa3b8"

                        }

                    }

                }

            }

        });
}


// ==================================
// INITIALIZE CHARTS
// ==================================

document.addEventListener(
    "DOMContentLoaded",
    () => {

        loadChartData();


        setInterval(
            loadChartData,
            10000
        );

    }
);