const appstate = 'on_lan_';
let config;
if (appstate === 'on_lan'){
    config = {
        busURL: "http://192.168.163.145:5001",
        user_employeeURL: "http://192.168.163.145:5002",
        databaseURL: "http://192.168.163.145:5003",
    };
}
else if (appstate === 'himachi'){
    config = {
        busURL: "http://25.24.45.37:5001",
        user_employeeURL: "http://25.24.45.37:5002",
        databaseURL: "http://25.24.45.37:5003",
    };
}
else{
    config = {
        busURL: "http://127.0.0.1:5001",
        user_employeeURL: "http://127.0.0.1:5002",
        databaseURL: "http://127.0.0.1:5003",
    };
}

console.log(config)